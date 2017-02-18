UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-02-24 13:55:51
Slug: dropbox-tips
Title: Dropbox Tips
Category: Software
Tags: tips, Dropbox, Synchronizaion, backup, cloud

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 


1. Dropbox won't sync files that you don't have the right permissions.

2. You'd better not merge an old Dropbox folder while installing/configuring Dropbox.

3. Using symbolic links in dropbox folder is problematic:
the symbolic links get synced as real files/directories on other computers
It might have problem if you push things to a repository and give the symbolic link to public for downloading. Strickly speaking, this is a problem of using symbolic with GIT not with Dropbox.
