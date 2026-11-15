---
title: Diagnosing and Fixing Linux Desktop Freezes Caused by ZRAM Swap Exhaustion and Baloo
created: '2026-11-14T20:38:49.114381-08:00'
date: '2026-11-14T20:40:49-08:00'
authors:
  - bendu
label: diagnosing-and-fixing-linux-desktop-freezes-caused-by-zram-swap-exhaustion-and-baloo
license: CC-BY-4.0
tags:
  - Linux
  - KDE
  - Plasma
  - Fedora
  - Aurora
  - Universal Blue
  - Baloo
  - zram
  - swap
  - OOM
  - systemd
  - systemd-oomd
  - journalctl
  - sysstat
  - sar
  - sysrq
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

When a Linux desktop workstation freezes completely—unresponsive mouse cursor, frozen clock, dead keyboard shortcuts, and no SSH response—it is easy to blame the GPU driver, the Wayland compositor, or a kernel panic. However, many multi-hour desktop lockups on modern Linux distributions are actually **executable page-cache thrashing livelocks** caused by full `zram` swap and an unconfigured swap OOM policy.

This post walks through a real-world post-mortem on an [Aurora](https://getaurora.dev/) (Universal Blue / Fedora Kinoite 44) workstation running KDE Plasma Wayland, showing how to diagnose system freezes using `journalctl` and `sysstat` (`sar`), identify the root causes (`kde-baloo` and `systemd-oomd` configuration gaps), and permanently fix the issue.

______________________________________________________________________

## 1. Symptoms of the Freezes

The workstation hardware and software environment:

- **OS**: Aurora (Fedora Kinoite 44 Atomic Desktop, KDE Plasma 6 on Wayland)
- **Hardware**: 62 GiB physical RAM, 8 GiB `zram0` compressed in-RAM swap, NVIDIA RTX 3070 GPU

Over two consecutive days, the system experienced two severe freezes:

1. **Freeze #1 (Self-Recovered After >1 Hour)**:
   Triggered immediately after pressing `Alt+F3` (the KWin window operations menu shortcut) inside a Chromium-based browser. The entire GUI locked up for over an hour before spontaneously recovering on its own.
1. **Freeze #2 (Hard Reboot After ~2.5 Hours)**:
   Occurred the following afternoon during normal desktop usage. The system remained completely unresponsive for roughly 2.5 hours until forced off via the hardware power button.

______________________________________________________________________

## 2. Diagnosing System Freezes with `journalctl` and `sar`

When investigating a freeze after a reboot, two tools provide complementary visibility:

- **`journalctl`**: Captures kernel and userspace daemon warnings leading up to and recovering from the freeze.
- **`sysstat` (`sar`)**: Records periodic system activity counters (`/var/log/sa/sa<DD>`) for memory, swap, and paging every 10 minutes.

### Step 1: Locate the Previous Boot in `journalctl`

List recorded boots to find the boot index of the frozen session (`-1` is the immediately preceding boot):

```bash
journalctl --list-boots
journalctl -b -1
```

First, check kernel logs for hardware faults, GPU hangs (`NVRM` / `Xid`), kernel panics, or kernel OOM killer invocations:

```bash
journalctl -b -1 -k
```

Surprisingly, **none occurred**—there were no kernel panics, no NVIDIA GPU hangs, and **not a single kernel or `systemd-oomd` OOM kill** during either freeze.

### Step 2: Recognize Userspace Thrashing Signatures in `journalctl`

Inspecting the full system journal around the freeze window revealed classic symptoms of severe memory thrashing and CPU/IO scheduling starvation:

```text
rtkit-daemon[...]: The canary thread is apparently starving. Taking action.
rtkit-daemon[...]: Demoting known real-time threads.
kwin_wayland[...]: The main thread was hanging temporarily!
chronyd[...]: Forward time jump detected!
systemd-udevd[...]: ... Worker [...] processing SEQNUM=... is taking a long time
systemd-udevd[...]: ... Worker [...] processing SEQNUM=... killed
at-spi2-registryd[...]: Disabling unresponsive app with pid ...
```

Key observations from the journal timeline:

- **Complete Logging Gap**: For the duration of the freeze (over 1 hour in Freeze #1 and 2.5 hours in Freeze #2), not a single log line was written to disk—even `sysstat`'s background timer could not get scheduled.
- **How Freeze #1 Recovered**: At the exact moment Freeze #1 ended, a Flatpak Chrome instance logged:
  ```text
  GPU process exited unexpectedly: exit_code=512
  ```
  When that single browser process finally crashed, it released enough anonymous memory to break the paging livelock, allowing `kwin_wayland`, `chronyd` (which noticed a massive forward wall-clock jump), and user input to resume immediately.

### Step 3: Reconstruct Memory, Swap, and Paging Activity with `sar`

Use `sar` against the daily `sysstat` data file (`/var/log/sa/sa<DD>`, where `<DD>` is the two-digit day of the month) to inspect memory (`-r`), swap (`-S`), and paging (`-B`) metrics:

```bash
# Memory utilization (-r), swap utilization (-S), and paging statistics (-B)
sar -f /var/log/sa/sa14 -r
sar -f /var/log/sa/sa14 -S
sar -f /var/log/sa/sa14 -B
```

The `sar` output exposed the exact mechanism of the freeze:

1. **RAM and ZRAM Swap Saturation (`sar -r` and `sar -S`)**:

   - Physical memory (`%memused`) climbed above **96%**.
   - The 8 GiB `zram0` swap device was **100.0% full** (`kbswpfree = 0`) for hours leading up to the freeze.

1. **Catastrophic Page-Cache Thrashing (`sar -B`)**:
   Right as the freeze began (and upon recovery when `sadc` could finally flush its sample), paging counters spiked to extreme levels:

   - `pgpgin/s`: **~596,850 KB/s**
   - `pgscank/s`: **~1,655,982 pages/s** (kswapd scanning over 1.65 million pages per second!)
   - `majflt/s`: **~424 major page faults/s**

#### Why Does Full Swap Cause a Complete Livelock Without Triggering OOM?

When anonymous memory (heap/stack allocations) fills almost all 62 GiB of RAM and 100% of the 8 GiB `zram` swap:

1. The kernel can no longer swap out anonymous pages because `kbswpfree = 0`.
1. To satisfy any memory allocation or page fault (such as pressing `Alt+F3` in KWin to render a popup menu), the kernel's only remaining reclaimable memory is **file-backed page cache**—including the **executable code pages** (`mmap`-ed binaries and shared libraries like `libc.so`, `libQt6*.so`, `kwin_wayland`, and Chrome).
1. The kernel evicts executable code pages that are actively in use. Less than a millisecond later, the CPU tries to execute the next instruction in that process, triggering a **major page fault (`majflt/s`)** to read the binary page back from the NVMe SSD (`pgpgin/s`), which immediately evicts another process's active code page.
1. Because file-backed pages are technically still being reclaimed, the kernel's in-kernel OOM killer believes memory reclaim is "making progress" and never fires, leaving the machine in a multi-hour livelock.

______________________________________________________________________

## 3. Root Causes Identified

### Culprit #1: KDE Baloo File Indexer (`baloo_file` / `baloo_file_extractor`)

Inspecting cgroup memory and swap usage on a fresh boot revealed an unexpected memory hog: `kde-baloo.service` (KDE's file and content indexing daemon).

- The workstation's `$HOME` directory contained **~600,000 files**, including source code repositories, compiled HTML documentation builds, Jupyter notebooks, and data archives.
- Because Baloo indexes both filenames and **full file contents** by default, its LMDB database at `~/.local/share/baloo/index` had ballooned to **26.75 GiB**.
- Within just **1 hour 40 minutes** of a fresh boot, `kde-baloo.service` had consumed:
  - **15.6 GiB of physical RAM** (throttled right against its systemd cgroup `MemoryHigh` limit), plus
  - **6.1 GiB of the 8 GiB `zram` swap** (with a peak swap consumption of **7.9 GiB**!).

In short, `baloo_file` single-handedly consumed nearly 100% of the system's `zram` swap and a quarter of physical RAM while constantly thrashing against its `MemoryHigh` boundary.

### Culprit #2: Multiple Flatpak Chrome / Chromium Instances

Alongside Baloo, multiple long-running Flatpak Chrome and Chromium browser instances accumulated **8–35 GiB of RSS** across dozens of tabs, renderer processes, and GPU buffers. Combined with Baloo's 22+ GiB footprint, total memory demand exceeded physical RAM + swap.

### Culprit #3: Why `systemd-oomd` Never Intervened

Modern Fedora distributions ship `systemd-oomd` to prevent userspace thrashing before a kernel livelock occurs. Running `oomctl` revealed why `systemd-oomd` stood by idly:

```bash
oomctl
```

```text
Dry Run: no
Swap Used Limit: 90.00%
Default Memory Pressure Limit: 60.00%
Default Memory Pressure Duration: 20s
System Context:
        Memory: Used: ...
        Swap: Used: 6.1G Total: 8.0G
Swap Monitored CGroups:
Memory Pressure Monitored CGroups:
        Path: /user.slice/user-1000.slice/user@1000.service
                Memory Pressure Limit: 80.00%
        Path: /system.slice
                Memory Pressure Limit: 80.00%
```

Notice the critical gap: **`Swap Monitored CGroups:` was completely empty!**

Even though `Swap Used Limit: 90.00%` was configured globally in `oomd.conf`, no slice had `ManagedOOMSwap=kill` enabled. Only `ManagedOOMMemoryPressure=kill` (at an 80% PSI threshold over 20s) was active on user and system slices. When `zram` hit 100%, `systemd-oomd` was not monitoring swap exhaustion on any cgroup.

______________________________________________________________________

## 4. Solutions and Mitigations

Fixing the workstation permanently requires three layers of defense:

1. **Eliminate the runaway memory/swap consumer** (`kde-baloo`).
1. **Enable proactive swap-based OOM killing** in `systemd-oomd` (`ManagedOOMSwap=kill`).
1. **Enable Magic SysRq keys** (`kernel.sysrq = 244`) as a manual hardware-level escape hatch.

### Solution 1: Disable and Purge the KDE Baloo File Indexer

#### What Does Baloo Do (and What Happens When You Disable It)?

Baloo (`baloo_file` and `baloo_file_extractor`) maintains an inverted index of filenames and file contents so that Dolphin and KRunner can perform instant full-text searches inside documents.

Disabling Baloo **does NOT break**:

- Launching applications in KDE Application Launcher or KRunner (`Alt+Space`)
- KRunner plugins (calculator, window switching, system settings, unit conversion, recent documents)
- Basic filename search in Dolphin (Dolphin automatically falls back to standard directory traversal when Baloo is disabled, or you can use fast CLI tools like `fd` and `rg`)

For developer workstations with hundreds of thousands of source, build, and virtual-environment files in `$HOME`, Baloo's content indexer is notorious for runaway LMDB growth and swap exhaustion.

#### Commands to Disable and Purge Baloo

```bash
# 1. Disable Baloo in KDE configuration
balooctl6 disable

# 2. Stop the systemd user service directly
# (Required if baloo_file is stuck thrashing and 'balooctl6 purge' hangs or times out)
systemctl --user stop kde-baloo.service

# 3. Purge the multi-gigabyte index database (~/.local/share/baloo/index)
balooctl6 purge

# 4. Verify Baloo is disabled and stopped
balooctl6 status
```

On our workstation, stopping `kde-baloo.service` and purging the index immediately freed **26.75 GiB of disk space**, reclaimed **15.6 GiB of RAM**, and dropped system swap usage from **6.1 GiB down to 0 B**.

*(Tip: If you ever want filename-only indexing without content indexing, you can configure **System Settings → Search → File Search**, uncheck **Also index file content**, and add heavy developer directories like `~/archives`, `~/.cache`, and `.venv` to the exclusion list.)*

### Solution 2: Enable Swap-Based OOM Killing in `systemd-oomd`

To ensure `systemd-oomd` kills the largest swap consumer whenever total swap usage exceeds 90%—before the kernel runs out of swap and livelocks on executable pages—enable `ManagedOOMSwap=kill` on the root cgroup slice (`-.slice`).

#### Why Is the Root Slice Named `-.slice`?

In systemd unit naming conventions, filesystem paths are converted into unit names by replacing `/` with `-`. Therefore, the root cgroup path `/` corresponds to the unit name `-.slice`, and its drop-in configuration directory is `/etc/systemd/system/-.slice.d/`.

> **CLI Tip**: Because `-.slice` starts with a hyphen (`-`), standard CLI tools interpret it as a command-line flag unless you pass `--` (end of options) first:
>
> ```bash
> systemctl status -- -.slice
> ls -la -- /etc/systemd/system/-.slice.d
> ```

#### Configure `ManagedOOMSwap=kill` on `-.slice`

Create the drop-in file `/etc/systemd/system/-.slice.d/10-oomd-root-slice-defaults.conf`:

```bash
sudo mkdir -p -- /etc/systemd/system/-.slice.d
sudo tee /etc/systemd/system/-.slice.d/10-oomd-root-slice-defaults.conf > /dev/null <<'EOF'
[Slice]
ManagedOOMSwap=kill
EOF
```

Reload `systemd` and restart `systemd-oomd`:

```bash
sudo systemctl daemon-reload
sudo systemctl restart systemd-oomd
```

Verify with `oomctl` that the root cgroup `/` is now actively monitored under `Swap Monitored CGroups:`:

```bash
oomctl
```

```text
Dry Run: no
Swap Used Limit: 90.00%
Default Memory Pressure Limit: 60.00%
Default Memory Pressure Duration: 20s
System Context:
        Memory: Used: 14.2G Total: 62.5G
        Swap: Used: 0B Total: 8.0G
Swap Monitored CGroups:
        Path: /
                Swap Usage: (see System Context)
Memory Pressure Monitored CGroups:
        Path: /user.slice/user-1000.slice/user@1000.service
                Memory Pressure Limit: 80.00%
        Path: /system.slice
                Memory Pressure Limit: 80.00%
```

With this configuration in place, if swap ever reaches 90% (7.2 GiB of 8 GiB), `systemd-oomd` will automatically terminate the offending cgroup (such as a runaway browser tab or background indexer) instead of allowing the entire desktop to freeze.

### Solution 3: Enable Magic SysRq Keys (`kernel.sysrq = 244`) as a Manual Last Resort

During Freeze #2, pressing `Alt+SysRq` combinations failed to work, and the kernel journal logged:

```text
kernel: sysrq: This sysrq operation is disabled.
```

By default, Fedora sets `kernel.sysrq = 16`, which only allows the `S` (Emergency Sync) command and disables both manual OOM invocation (`F`) and safe rebooting.

#### Understanding the `kernel.sysrq = 244` Bitmask

Setting `kernel.sysrq = 244` (`4 + 16 + 32 + 64 + 128`) enables all recovery, signaling, and filesystem-safety keys while keeping potentially sensitive kernel memory/register dumps disabled:

```{list-table} Magic SysRq Bitmask Breakdown for 244
---
header-rows: 1
---
- - Bit Value
  - Capability Enabled
  - SysRq Keys Unlocked
- - `4`
  - Control of keyboard / console logging
  - `R` (take keyboard back from Wayland/X11 into raw/XLATE mode)
- - `16`
  - Sync mounted filesystems
  - `S` (flush dirty buffers to disk)
- - `32`
  - Remount filesystems read-only
  - `U` (remount read-only to prevent filesystem corruption)
- - `64`
  - Process signaling (term, kill, oom-kill)
  - `E` (`SIGTERM`), `I` (`SIGKILL`), **`F` (invoke kernel OOM killer)**
- - `128`
  - Reboot / poweroff
  - `B` (immediate reboot), `O` (poweroff)
```

#### Persist `kernel.sysrq = 244` Across Reboots

Create `/etc/sysctl.d/90-sysrq.conf` and apply it immediately:

```bash
echo "kernel.sysrq = 244" | sudo tee /etc/sysctl.d/90-sysrq.conf
sudo sysctl -p /etc/sysctl.d/90-sysrq.conf
```

#### How to Use Magic SysRq During a Freeze

Because the Magic SysRq handler executes directly inside the Linux kernel interrupt context, it works even when Wayland, `kwin_wayland`, and userspace daemons are completely frozen:

1. **First Choice — Trigger a Manual OOM Kill (`Alt + SysRq + F`)**:
   Hold `Alt + SysRq` (often labeled `PrintScreen` / `PrtSc`) and press **`F`**.
   The kernel immediately invokes the in-kernel OOM killer to terminate the single largest memory-consuming process, freeing gigabytes of RAM and unfreezing your desktop within seconds without losing your session.
1. **Last Resort — Safe Reboot (`R -> E -> I -> S -> U -> B`)**:
   If the system still does not recover, hold `Alt + SysRq` and slowly press **`R`**, **`E`**, **`I`**, **`S`**, **`U`**, **`B`** (pausing ~1–2 seconds between keys) to cleanly terminate processes, flush caches, remount disks read-only, and reboot without risking filesystem corruption.

______________________________________________________________________

## 5. Summary Checklist

If your Fedora / Universal Blue KDE Plasma workstation suffers from inexplicable freezes:

1. Check previous boot logs with `journalctl -b -1` and paging stats with `sar -f /var/log/sa/sa<DD> -r -S -B`.
1. Check whether `kde-baloo.service` has bloated `~/.local/share/baloo/index` and exhausted `zram` swap; disable and purge it with `balooctl6 disable && systemctl --user stop kde-baloo.service && balooctl6 purge`.
1. Verify `oomctl` shows `/` under `Swap Monitored CGroups:` by setting `ManagedOOMSwap=kill` in `/etc/systemd/system/-.slice.d/10-oomd-root-slice-defaults.conf`.
1. Set `kernel.sysrq = 244` in `/etc/sysctl.d/90-sysrq.conf` so `Alt+SysRq+F` is always available to slay a runaway memory hog on demand.

______________________________________________________________________

## References

- [](#rescue-linux-from-gui-freezing)
- [](#universal-blue-atomic-linux-distributions)
- [](#atomic-linux-distributions)
- [](#managing-fedora-atomic-core-system-using-rpm-ostree)
- [](#configure-fcitx5-for-kde-plasma)
- [systemd-oomd.service(8) Manual Page](https://www.freedesktop.org/software/systemd/man/latest/systemd-oomd.service.html)
- [Linux Magic System Request Key Hacks — Kernel Documentation](https://docs.kernel.org/admin-guide/sysrq.html)
