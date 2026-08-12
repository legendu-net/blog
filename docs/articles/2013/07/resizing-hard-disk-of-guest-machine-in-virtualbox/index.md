---
title: Resizing Hard Disk of Guest Machine in VirtualBox
created: '2013-07-20T10:57:11-07:00'
date: '2026-08-11T22:19:14-07:00'
authors:
  - bendu
label: resizing-hard-disk-of-guest-machine-in-virtualbox
license: CC-BY-4.0
tags:
  - partition
  - gparted
  - VirtualBox
  - software
  - vmdk
  - resize
  - resizing
---

Suppose you have virtual hard disk in VirtualBox called `xp.vdi`,
you can resize it (megabytes) using the following command.

```
VBoxManage modifyhd xp.vdi --resize 40960
```

The command currently doesn't support vmdk virtual disk.
So if you have a virtual disk called `xp.vmdk`,
you have to first convert it into a vdi disk using command

```
VBoxManage clonehd --format VDI xp.vmdk xp.vdi
```

and then resize the vdi file using previous command.
If you want a (resized) vmdk virtual disk rather than a vdi virtual disk,
you can convert the resized vdi virtual disk to vmdk format using the following command.

```
VBoxManage clonehd --format vmdk xp.vdi xp.vmdk
```

Note that the above commands only resize the virtual disk,
it doesn't resizes partitions inside the virtual disk.
You must manually resize partiions.
This is easy to do for Windows 7/8 guest machines.
If have other type of guest machiens (e.g., XP),
you can use partition tools (e.g., GParted) to manually resize partitions.
Take GParted for example,
you can download it,
mount it into a virtual CD/DVD,
boot your guest machine into GParted,
and then use the graphical tool to resize partitions.
It's very intuitive once you get there.
