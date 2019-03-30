UUID: 7caebdd0-8af6-4a5a-a338-eeb121c1f023
Status: published
Date: 2019-03-30 14:41:00
Author: Ben Chuanlong Du
Slug: command-line-tools-for-linux-file-system
Title: Command Line Tools for Linux File System
Category: OS
Tags: Linux, file system, filesystem, shell, terminal, command line

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. List disk information.

        df
        df /HOME

2. Management disk partition tables.

        fdisk

3. Format disk partitions.

        mkfs.ext4 /dev/sd3 /path_to_mount_in

        mkfs.ntfs /dev/sd3 /path_to_mount_in

        mkfs.exfat /dev/sd3 /path_to_mount_in

4. Report disk usage.

        du -lhd 1 .

5. dd

        dd

6. badblocks
