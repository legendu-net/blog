UUID: f1e2d3ad-b3b8-44ae-b4e9-478da736e187
Status: published
Date: 2017-08-26 20:18:18
Author: Ben Chuanlong Du
Slug: mount-samba-on-mac
Title: Mount Samba on Mac
Category: Mac OSX
Tags: Mac OSX, mount, SAMBA

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## GUI

Go -> Connect to Server

smb://path_to_dir

## Command Line

    mount -t smbfs //user@server/sharename share

    mount_smbfs //user@SERVER/folder ./mntpoint
