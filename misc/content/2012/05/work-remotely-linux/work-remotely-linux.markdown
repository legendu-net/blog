Status: published
Title: Working Remotely in Linux
Date: 2012-05-01 23:20:51
Slug: work-remotely-linux
Author: Ben Chuanlong Du
Category: OS
Tags: software, remote, Linux, desktop, NoMachine, rustdesk
Modified: 2023-02-08 11:53:40

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## From Linux to Linux

### Command Line Mode Using `ssh`

1. Using X forwarding, you can also run GUI applications on the server.
    This is not recommended unless it's short quick work.

### Remote File System

- nfs
    - NFS has better performance (compared to sshfs and samba)
        but it's less secured.

- sshfs

    - You'd better use a mount point which you have full access to,
        otherwise, you have use the root user to access the mount point. 

    - You'd better add yourself to the `fuse` (which is required by sshfs) group.

- samba

### Remote Desktop

- NoMachine

- [rustdesk](https://github.com/rustdesk/rustdesk)

- VNC (e.g., vino or tight vnc, remmina)

- Teamviewer

## From Linux to Windows

### Remote Desktop

- Remmina

- rdesktop

- NoMachine

- Teamviewer

### Remote File System 

- SAMBA

    - Open nautilus file manager and press `CTRL + L` to show the address field.

    - Type in `smb://host_name/folder` in the address field and press enter.

    - Type in your user name and password in the prompt to login. 

## From Windows to Linux

### Comand Line Mode Using `ssh` 

### Remote File System
- SAMBA
### Remote Desktop
- NoMachine
