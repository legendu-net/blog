---
title: Working Remotely in Linux
created: '2012-05-01T23:20:51-07:00'
date: '2026-11-15T09:17:56-08:00'
authors:
  - bendu
label: working-remotely-in-linux
license: CC-BY-4.0
tags:
  - software
  - remote
  - Linux
  - desktop
  - NoMachine
  - rustdesk
---

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

- rdp
  - Linux DE Built-ins
    - KDE Plasma: System Settings -> System -> Remote Desktop
  - Windows App (macOS)
- VNC
  - vino
  - tight VNC
  - remmina
  - [noVNC](https://novnc.com/info.html)
- NoMachine
  - commercial but free for personal use
- [rustdesk](https://github.com/rustdesk/rustdesk)
- [Chrome Remote Desktop](https://remotedesktop.google.com/home)
  - Linux support is limited to Debian/Ubuntu series.
- Teamviewer
  - commercial
- [Parsec](https://parsec.app)
  - commercial, monthly subscription

## From Linux to Windows

### Remote Desktop

- rdp

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

### Command Line Mode Using `ssh`

### Remote File System

- SAMBA

### Remote Desktop

- NoMachine
