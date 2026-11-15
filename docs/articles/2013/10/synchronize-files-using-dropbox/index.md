---
title: Synchronize Files Using Dropbox
created: '2013-10-22T13:36:17-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: synchronize-files-using-dropbox
license: CC-BY-4.0
tags:
  - tips
  - Dropbox
  - synchronizaion
  - backup
  - cloud
  - sync
---

1. Dropbox won't sync files that you don't have read permissions.

1. You'd better not merge an old Dropbox folder while installing/configuring Dropbox.

1. You'd better not store symbolic links in the Dropbox folder,
   because the symbolic links will be replaced by the real files/folders
   when synchronized to other computers.

1. It is not a good idea to put a Git repository into Dropbox.
   First,
   a Git repository usually contains lots of small files
   which downgrades the performance of Dropbox.
   Second,
   it is better to push a Git repository to GitHub, GitLab, etc.

## References

- https://www.addictivetips.com/ubuntu-linux-tips/enable-dropbox-support-in-dolphin-file-manager/
