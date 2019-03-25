Status: published
Date: 2019-03-24 12:58:44
Author: Benjamin Du
Slug: best-filesystem-format-for-cross-platform-data-exchanging
Title: Best Filesystem Format for Cross-Platform Data Exchanging
Category: OS
Tags: OS, macOS, external drive, filesystem format

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


FAT32, exFAT, NTFS, ext4

Currently the best format to use is **exFAT** it is supported by all major operating systems 
and still has good performance.

Actually, 
check whether ext4 is supported by all the 3 major OS now. 
Windows 10 support WSL, so it might be able to mount ext4 directly.


Can external drive can accessed in virtual machines?
If so, it might be a good solution!
