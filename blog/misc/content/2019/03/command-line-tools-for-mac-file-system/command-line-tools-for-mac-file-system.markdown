Status: published
Date: 2019-03-10 08:56:36
Author: Benjamin Du
Slug: command-line-tools-for-mac-file-system
Title: Command Line Tools for Mac File System
Category: OS
Tags: macOS, file system, filesystem, shell, terminal, command line, diskutil
Modified: 2021-08-02 09:19:43

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

**Note**: When work both in Linux and macOS,
a painful burden to use command-line is to remember subtle differences between Linux commands and macOS commands.
A a matter of fact, 
GNU tools can be used in macOS
and it is suggested that you use GNU tools (instead of the macOS version of tools)
so that you can have unified command-line experience across operations systems.
Please refer to 
[Install GNU Utils Using Homebrew](http://www.legendu.net/en/blog/install-gnu-utils-using-homebrew)
on how to install GNU tools on macOS
and
[Command Line Tools for Linux File System](http://www.legendu.net/misc/blog/command-line-tools-for-linux-file-system/)
on Linux commands.


If you insist on using the macOS version of tools, 
continue to read the content below. 

1. Notice that disks in macOS are often named as `/dev/diskXsY`
    where `X` and `Y` are numbers.

2. It is suggested that you use the unified command `diskutil` 
    (instead of scattered commands such as `df`, `newfs_*`, etc.)
    to manage (list, format, partition, etc.) disks in macOS.

        :::bash
        diskutil partitionDisk /dev/diskX 2 MBR \
            ExFAT NewVolumeA 100M \
            ExFAT NewVolumeB R
        diskutil eraseVolume ExFat NewVolume /dev/diskXsY


3. List disk information.

        :::bash
        diskutil list

4. Unmount a volume.

        :::bash
        diskutil unmount /path/to/mounted/volume

2. Management disk partition tables.

        :::bash
        fdisk

3. Format disk partitions.

        :::bash
        newfs_ext4 /dev/sd3 /path_to_mount_in
        newfs_ntfs /dev/sd3 /path_to_mount_in
        newfs_exfat /dev/sd3 /path_to_mount_in

4. Report disk usage.

        :::bash
        du -lhd 1 .

5. dd

        :::bash
        dd

6. badblocks

## References

- [Install GNU Utils Using Homebrew](http://www.legendu.net/en/blog/install-gnu-utils-using-homebrew)

- [Command Line Tools for Linux File System](http://www.legendu.net/misc/blog/command-line-tools-for-linux-file-system/)

- [How to format multiple exFAT partitions on USB drive?](https://apple.stackexchange.com/questions/218818/how-to-format-multiple-exfat-partitions-on-usb-drive)

- [How to Erase a Disk from Command Line in Mac OS X](https://osxdaily.com/2016/08/30/erase-disk-command-line-mac/)

- [How do you make filesystems in mac OSX](https://unix.stackexchange.com/questions/271826/how-do-you-make-filesystems-in-mac-osx)
