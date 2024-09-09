Status: published
Date: 2022-07-28 10:33:40
Modified: 2022-07-28 10:33:40
Author: Benjamin Du
Slug: format-a-disk-on-linux
Title: Format a Disk on Linux
Category: Computer Science
Tags: Computer Science, hardware, disk, drive, hard, SSD, format, partition, ext4, mkfs

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Locate the right disk to operate on.
    A few commands might help you.
    For example,
    you can use the command `ls /dev/sd*` to list all hard drives
    and the command `ls /dev/nvme*` to list NVME (SSD) drives.
    Or you can simply use the command `lsblk` to list all block devices 
    (which include all hard and solid-state disks).

2. Create disk partition tables using the command `fdisk`.

        :::bash
        fdisk /dev/sdb
        fdisk /dev/nvme0n1

3. Format partitions to the right format (`ext4` recommended).
    For example,
    the following command formats the partition `/dev/sdb3` as ext4.

        :::bash
        mkfs.ext4 /dev/sdb3
        mkfs.ext4 /dev/nvme0n1p1

## References

- [Formatting NVME Partition on CentOS 7](https://thelinuxcluster.com/2018/07/09/formatting-nvme-partition-on-centos-7/)