UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2016-07-13 22:42:20
Slug: transfer-files-over-network-in-linux
Title: Transfer Files over Network in Linux
Category: internet
Tags: internet, Linux, network, web, transfer, file system, nfs, SSH

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
## Network Drive/Remote File System

### NFS 

1. very fast, 
2. not secure, 
3. Unix/Linux only, 

Summary: good for local network (e.g., family) sharing.

### Samba 

1. fast, 
2. secure, 
3. cross-platform

Summary: good for general purpose where performance is not critical.

### SSHFS 

1. slow
2. very secure
3. Unix/Linux only

Summary: good for situations where security is critial but performance is not.

## Other Tools

scp/rsync

mbuffer
Send (on host)
    mbuffer -s 1M -m 10M -i trusty-desktop-amd64.iso -O 192.168.0.6:13977
Receive (on client)
    mbuffer -s 1M -m 10M -I 13977 -o trusty.iso

