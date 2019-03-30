Status: published
Date: 2019-03-30 14:41:00
Author: Benjamin Du
Slug: command-line-tools-for-mac-file-system
Title: Command Line Tools for Mac File System
Category: OS
Tags: macOS, file system, filesystem, shell, terminal, command line

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. List disk information.

        diskutil list

2. Management disk partition tables.

        fdisk.

3. Format disk partitions.

        newfs_ext4 /dev/sd3 /path_to_mount_in

        newfs_ntfs /dev/sd3 /path_to_mount_in

        newfs_exfat /dev/sd3 /path_to_mount_in

4. Report disk usage.

        du -lhd 1 .

5. dd

        dd

6. badblocks
