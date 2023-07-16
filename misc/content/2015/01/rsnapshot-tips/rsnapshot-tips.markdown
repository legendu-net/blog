Status: published
Date: 2015-01-22 14:25:22
Author: Ben Chuanlong Du
Title: Backup Files Using "rsnapshot" 
Slug: rsnapshot-tips
Category: Software
Tags: software, rsnapshot, backup, synchronization, rsync
Modified: 2020-05-22 14:25:22

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

To truncate the relative path while backing up using Rsnapshot:

1. Uncomment the line started with `rsync_long_args`.

2. Remove the `--relative` option and add the `--no-relative` option.

