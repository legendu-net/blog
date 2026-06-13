---
title: Misc Tips on Ubuntu
created: '2013-10-19T12:20:43-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: misc-tips-on-ubuntu
license: CC-BY-4.0
tags:
  - tips
  - Ubuntu
  - Linux
  - OS
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

Please refer to
[Tips on Installing Debian Series Linux Distributions](tips-on-installing-debian-series-of-linux-distributions)
for detailed discussions.

## Misc

[How to solve boot problems with Ubuntu after kernel upgrade](http://www.dedoimedo.com/computers/ubuntu-initrd-bug.html)

[Ubuntu Sources List Generator](https://repogen.simplylinux.ch/)

1. If a user never logged in before,
   removal disks won't be mounted.
   However,
   you can always mount the disk manually.

1. If a user never logged in before, the vino-server is not usable.
   There is a solution if gdm is used,
   but I don't know how to resolve this problem when lightdm is used.
   One good way is to let ubuntu login automatically and then lock screen automatically.
   You can also think about whether the way you used in Debian is applicable to Ubuntu.

1. For some reason I don't know, lightdm fails to restart after running "sudo service lightdm restart".
   However, it starts if I login into tty and start it manually by "sudo service lightdm start".
   I think this probably means that something is wrong stopping the lightdm service.

## Check Whether a Ubuntu Server Has a Desktop Installed

Look at
Check the directory `/usr/share/xsessions/` to see
if there are any X sessions available on the Ubuntu server.

```
:::bash
ls /usr/share/xsessions/
```
