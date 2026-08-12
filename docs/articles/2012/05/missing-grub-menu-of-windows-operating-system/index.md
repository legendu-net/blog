---
title: Missing GRUB Menu of Windows Operating System
created: '2012-05-03T19:10:47-07:00'
date: '2026-08-11T22:19:15-07:00'
authors:
  - bendu
label: missing-grub-menu-of-windows-operating-system
license: CC-BY-4.0
tags:
  - Windows
  - Linux
  - OS
  - Debian
---

I came across this problem after I installed both Debian and Windows 7 system on my laptop.
After searching online, I found a solution to this problem.

1. Open /etc/default/grub as root user and make sure the following line is somewhere in the file and uncommented:

   ```
    GRUB_DISABLE_OS_PROBER=false
   ```

1. Run command `update-grub2` and then reboot your computer.

This solution is not just for Windows and Linux dual boot.
It is also for dual/multiple Linux operating systems boot.
