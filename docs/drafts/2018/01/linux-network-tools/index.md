---
title: Linux Network Tools
created: '2018-01-10T10:24:23-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: linux-network-tools
license: CC-BY-4.0
tags:
  - software
  - Linux
  - network
  - tool
  - download
  - VPN
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Monitor Network

[WireShark](https://www.wireshark.org/)
[iStatMenus](https://bjango.com/mac/istatmenus/)
tcpdump

[9 Best Bandwidth Monitor and Network Usage Monitoring Tools](https://www.dnsstuff.com/bandwidth-monitor)

[Best Bandwidth Monitoring Software for Tracking Network Traffic Usage](https://www.netadmintools.com/bandwidth-monitor/)

## Network Admin

1. [arp-scan](tips-on-arp-scan)

1. [RustNet](https://github.com/domcyrus/rustnet)

1. ping

1. netstat

1. proxychains

1. sshuttle

1. ip addr

   ```
    ip addr show dev eth0
    ip addr show dev eth0 | grep -i --color=auto inet | cut -d / -f 1 | cut -d ' ' -f 6
   ```

1. nslookup

   ```
    nslookup ip_address
   ```

## Remote Tools

1. OpenSSH, keychain (keyring for OpenSSH)
1. Teamviewer
1. NoMachine, FreeNX
1. VNC
1. SSHFS
1. Remmina
1. YuuGuu (Web Conference)
1. LogMeIn (Windows and Mac only)

## VPN

1. [WireGuard](https://www.wireguard.com/) is a better alternative to OpenVPN.

1. [tailscale](https://tailscale.com/)
   is an easy-to-use and secure VPN that network that just works.
   It is based on WireGuard.

1. [LogMeIn Hamachi](https://www.vpn.net/)
   [LogMeIn Hamachi](https://www.vpn.net/)
   is a on-demand virtual networking service
   that enables secure remote access to your business network
   anywhere there is an Internet connection.
   It is extremely easy to set up.

1. ExpressVPN

1. PrivateInternetAccess

## Anonymous Tools

1. VPN
1. Proxy
1. Anomos
1. Tor
1. proxychains

## [Downloading Tools](downloading-tools)
