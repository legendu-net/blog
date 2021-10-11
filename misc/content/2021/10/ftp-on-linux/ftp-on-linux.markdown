Status: published
Date: 2021-10-10 14:00:53
Modified: 2021-10-10 14:07:58
Author: Benjamin Du
Slug: ftp-on-linux
Title: Ftp on Linux
Category: Computer Science
Tags: Computer Science, Linux, FTP, SFTP

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation in Ubuntu

wajig install ftp

## FTP

1. Most FTP severs accpets only SFTP connections,
    which means that you have to log into those servers using `sftp` instead of `ftp`.
    The tricky part is that connecting to those servers using `ftp` might hang without meaningful error messages.
    So if you encounter issues log into a FTP server using `ftp`,
    try `sftp` instead.

        :::bash
        sftp user@server [port]

1. ftp transfer non-text use binary mode
