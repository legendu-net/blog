Status: published
Author: Ben Chuanlong Du
Date: 2013-10-22 13:36:17
Title: Synchronize Files Using Dropbox
Slug: dropbox-tips
Category: Software
Tags: tips, Dropbox, Synchronizaion, backup, cloud
Modified: 2021-09-25 13:32:49

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. Dropbox won't sync files that you don't have read permissions.

2. You'd better not merge an old Dropbox folder while installing/configuring Dropbox.

3. You'd better not store symbolic links in the Dropbox folder,
    because the symbolic links will be replaced by the real files/folders 
    when synchronized to other computers.

4. It is not a good idea to put a Git repository into Dropbox.
    First, 
    a Git repository usually contains lots of small files 
    which downgrades the performance of Dropbox.
    Second, 
    it is better to push a Git repository to GitHub, GitLab, etc.

## References

- https://www.addictivetips.com/ubuntu-linux-tips/enable-dropbox-support-in-dolphin-file-manager/