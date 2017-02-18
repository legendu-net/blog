UUID: 9ba8c173-8851-4beb-bda4-a68e1360a23f
Status: published
Date: 2016-06-01 22:19:41
Author: Ben Chuanlong Du
Slug: map-keys-in-linux
Title: Map Keys in Linux
Category: Linux
Tags: Linux, keyboard, mapping, swap, setxkbmap, Cinnamon, GNOME, keys

## Desktop Environment

1. Some desktop environment (e.g., GNOME, Cinnamon, etc.) can do this for you.
For exampel, 
you can follow the steps below to map the Caps Lock key in Cinnamon.

System Settings -> Keybord -> Keybord layouts -> Options (on the right-bottom corner) -> Caps Lock key behavior
and select the behavior you want.

## setxkbmap
Swap the Caps and the Escape keys.
```bash
setxkbmap -option -option caps:swapescape
```

Unfortunately, the key mapping partially pass to virtual machines or remote desktops,
which is the worst scenario. 
It is suggested that you turn off the mapping on the Linux host 
when you work in a VM or a remote desktop.

