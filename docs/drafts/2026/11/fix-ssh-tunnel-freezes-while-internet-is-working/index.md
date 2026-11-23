---
title: Fix SSH Tunnel Freezes While Internet Is Working
created: '2026-11-22T17:26:05.663530-08:00'
date: '2026-11-22T17:26:05.663538-08:00'
authors:
  - bendu
label: fix-ssh-tunnel-freezes-while-internet-is-working
license: CC-BY-4.0
tags:
  - computer science
  - SSH
  - SSH tunnel
  - freeze
  - ControlMaster
  - keepalive
  - MTU
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

When your internet connection is working
but an SSH session or tunnel freezes,
the cause is typically one of the following:

- NAT/firewall state timeouts
- MTU/packet fragmentation blackholes
- a multiplexing (ControlMaster) master connection stuck on a dead TCP connection
  after sleep or a network switch

For general usage of SSH tunnels,
please refer to [](#ssh-tunnel) and [](#tips-on-ssh).

## Quick Escape: Kill a Frozen SSH Session

If your terminal is completely unresponsive and ignores `Ctrl+C`:

1. Press `Enter`.

1. Type `~.` (tilde followed by a period).
   The escape sequence is only recognized at the start of a line
   (which is why you press `Enter` first)
   and is disabled if `EscapeChar none` is set.
   In nested SSH sessions,
   `~~.` closes the inner session.

1. If you use a multiplexed connection or a background tunnel,
   terminate it from another terminal.

   ```bash
   ssh -O exit <remote-host>
   # or check matching processes first and then kill them
   pgrep -af "ssh .*<remote-host>"
   pkill -f "ssh .*<remote-host>"
   ```

## Diagnosis

```{list-table}
:header-rows: 1

* - When does it freeze?
  - Likely cause
  - Fix
* - After being idle for a few minutes
  - NAT / firewall state timeout
  - `ServerAliveInterval` in `~/.ssh/config`
* - Immediately when transferring data or printing large output
  - MTU / PMTU blackhole
  - Lower the MTU or enable MTU probing
* - After the laptop sleeps, locks, or changes networks
  - ControlMaster stuck on a dead connection
  - Keepalives + `ssh -O exit <remote-host>`
```

## 1. Freezes When Idle (NAT / Firewall State Timeout)

Home routers, mobile hotspots and intermediate firewalls
maintain state tables for TCP connections.
If a connection sends no traffic for a while (often a few minutes),
the router might silently drop the connection tracking entry
without sending a `FIN` or `RST`.
When you type again,
packets are discarded and SSH hangs indefinitely.

The fix is to enable client keepalives in `~/.ssh/config`
(or pass `-o ServerAliveInterval=15` on the command line).

```
Host *
    ServerAliveInterval 15
    ServerAliveCountMax 3
```

- `ServerAliveInterval 15`: sends a keepalive message through the encrypted channel every 15 seconds
  to keep NAT/firewall entries active.
- `ServerAliveCountMax 3`: if 3 consecutive keepalives go unanswered,
  SSH terminates the connection instead of hanging forever.

## 2. Freezes During Data Transfer or Large Output (MTU / PMTU Blackhole)

If small commands (e.g., `date`, `pwd`) work fine
but commands with large output (e.g., `cat file`, `git push`)
or high-bandwidth port forwarding freeze the tunnel instantly,
the cause is likely a path MTU blackhole.

- Path MTU Discovery (PMTUD) fails because an intermediate router drops large packets
  while blocking the ICMP "Fragmentation Needed" (Type 3, Code 4) replies.
- VPNs, overlays and other tunneled connections reduce the effective MTU below the standard 1500 bytes.

You can confirm the issue by sending non-fragmentable pings of different sizes.
`-s 1372` is the payload size,
which results in a 1400-byte packet after adding the 28-byte IP and ICMP headers.
Lower `-s` until pings go through to find the path MTU.

```bash
# Linux
ping -M do -s 1372 <host>
# macOS
ping -D -s 1372 <host>
```

Fixes:

- Lower the MTU of your local network interface (e.g., to 1380 or 1400).
  Notice that this change does not persist across reboots or reconnections.

  ```bash
  # Linux
  sudo ip link set dev <interface_name> mtu 1380
  # macOS
  sudo ifconfig <interface_name> mtu 1380
  ```

- On Linux,
  enable TCP MTU probing,
  which lets TCP detect blackholes without changing the MTU.

  ```bash
  sudo sysctl -w net.ipv4.tcp_mtu_probing=1
  ```

## 3. Freezes After Sleep / Lock / Network Switch (ControlMaster)

If you use SSH connection multiplexing (`ControlMaster auto`),
the master process might still be alive after the machine sleeps
or switches networks (e.g., from Wi-Fi to Ethernet),
while its underlying TCP connection is dead.
Subsequent SSH commands and forwarded ports are multiplexed onto the dead connection and hang.

Fixes:

- Enable keepalives (`ServerAliveInterval` and `ServerAliveCountMax` as shown above)
  so that the master detects the dead connection and exits.

- Terminate the master connection manually.

  ```bash
  ssh -O exit <remote-host>
  ```

- Optionally,
  set `ControlPersist` to limit how long an idle master lingers
  (this does not fix a dead connection by itself).
  It is suggested that you scope multiplexing to specific hosts rather than `Host *`.
  Use `%C` (a hash of the connection parameters) in `ControlPath`
  to avoid UNIX socket path length limits.

  ```
  Host <remote-host>
      ControlMaster auto
      ControlPath ~/.ssh/sockets/%C
      ControlPersist 10m
  ```

  The socket directory must exist.

  ```bash
  mkdir -p -m 700 ~/.ssh/sockets
  ```

## 4. Make Sessions and Tunnels Survive Network Drops

- Run persistent sessions on the remote host via terminal multiplexers such as `tmux` or `shpool`
  so that you can reattach after a disconnection.
- Use [mosh](https://mosh.org/), a UDP-based remote shell
  which survives IP changes, sleeps and network interruptions.
  Notice that mosh only helps interactive shells
  and does not support port forwarding.
- For tunnels,
  use [autossh](https://www.harding.motd.ca/autossh/) (e.g., `autossh -M 0` with the `ServerAlive*` options)
  or a systemd service with `Restart=always`
  to re-establish dropped tunnels automatically.
  Set `ExitOnForwardFailure yes`
  so that SSH exits (and gets restarted) if port forwarding cannot be set up.

## 5. Other Causes

- Expired credentials (e.g., short-lived SSH certificates or SSO sessions)
  can cause connections to drop.
  Re-authenticate if your environment uses them.
- Some routers mishandle packets with specific DSCP marks.
  Try `IPQoS none` in `~/.ssh/config`.
  (The legacy ToS keywords `lowdelay` and `throughput` are deprecated in recent OpenSSH versions.)
