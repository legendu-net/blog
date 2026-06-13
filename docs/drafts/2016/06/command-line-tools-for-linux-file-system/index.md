---
title: Command Line Tools for Linux File System
created: '2016-06-24T18:50:50-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: command-line-tools-for-linux-file-system
license: CC-BY-4.0
tags:
  - Linux
  - file system
  - filesystem
  - shell
  - terminal
  - command line
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Please refer to
[Command Line Tools for Mac File System](command-line-tools-for-mac-file-system)
for the macOS version.

1. List disk information.

   ```
    df
    df /HOME
   ```

1. Format disk partitions.

   ```
    mkfs.ext4 /dev/sdb3

    mkfs.ntfs /dev/sdb3

    mkfs.exfat /dev/sdb3
   ```

1. Management disk partition tables.

   ```
    fdisk /dev/sdb
   ```

1. Report disk usage.

   ```
    du -lhd 1 .
   ```

1. dd

   ```
    dd if=... of=... bs=1M; sync
   ```

1. badblocks

1. lsblk

## References

[How To – Linux List Disk Partitions Command](https://www.cyberciti.biz/faq/linux-list-disk-partitions-command/)

[10 Commands to Check Disk Partitions and Disk Space on Linux](https://www.binarytides.com/linux-command-check-disk-partitions/)
