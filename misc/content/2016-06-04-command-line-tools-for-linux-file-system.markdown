UUID: 7caebdd0-8af6-4a5a-a338-eeb121c1f023
Status: published
Date: 2016-07-09 19:00:47
Author: Ben Chuanlong Du
Slug: command-line-tools-for-linux-file-system
Title: Command Line Tools for Linux File System
Category: Linux
Tags: Linux, file system, filesystem, shell, terminal, command line

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Report System Disks
```sh
df
df /HOME
```

```sh
du
```

## Management Disk Partition Tables
fdisk

## Format Disk Partitions
The commands `mkfs.ext4`, `mkfs.ntfs` and `mkfs.fat` can be used 
to format a partition (note: partition NOT device)
as `EXT4`, `NTFS` and `FAT32` respectively.

## Others
3. badblocks
4. dd