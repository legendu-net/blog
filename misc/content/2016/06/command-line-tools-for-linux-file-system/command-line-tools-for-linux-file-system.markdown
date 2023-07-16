Status: published
Date: 2016-06-24 18:50:50
Author: Ben Chuanlong Du
Slug: command-line-tools-for-linux-file-system
Title: Command Line Tools for Linux File System
Category: OS
Tags: Linux, file system, filesystem, shell, terminal, command line
Modified: 2021-09-20 17:08:25

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


Please refer to
[Command Line Tools for Mac File System](http://www.legendu.net/misc/blog/command-line-tools-for-mac-file-system/)
for the macOS version.


1. List disk information.

        df
        df /HOME

3. Format disk partitions.

        mkfs.ext4 /dev/sdb3

        mkfs.ntfs /dev/sdb3

        mkfs.exfat /dev/sdb3

2. Management disk partition tables.

        fdisk /dev/sdb

4. Report disk usage.

        du -lhd 1 .

5. dd

        dd if=... of=... bs=1M; sync

6. badblocks

7. lsblk

## References 

[How To – Linux List Disk Partitions Command](https://www.cyberciti.biz/faq/linux-list-disk-partitions-command/)

[10 Commands to Check Disk Partitions and Disk Space on Linux](https://www.binarytides.com/linux-command-check-disk-partitions/)
