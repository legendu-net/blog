---
title: Desktop Environments for Linux
created: '2013-08-13T22:09:04-07:00'
date: '2026-11-15T09:14:48-08:00'
authors:
  - bendu
label: desktop-environments-for-linux
license: CC-BY-4.0
tags:
  - DE
  - Linux
  - desktop environment
  - Xfce
  - GNOME
  - KDE
  - Unity
  - lightdm
  - gdm3
  - kdm
  - mdm
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. desktop files in /usr/share/applications/
   different DEs might have different format.
   At least I know that a desktop file created by Xfce cannot be used in GNOME,
   not sure the opposite works or not.
   The icon entry in the desktop file can be defined as a full path.

1. Do not remove Iceweasel in GNOME
   even if you have installed other web browsers like Firefox, Chrome, etc.
   Some GNOME components depends on Iceweasel.
   Removing Iceweasel might have undesirable effect on your GNOME desktop environment.

## Desktop Environments

1. [COSMIC](https://system76.com/cosmic)
1. LXQt
1. Xfce
1. KDE
1. Gnome
1. Cinnamon

## Desktop Manager

1. lightdm
   lightdm might have problems when multiple desktop environments are installed.

1. gdm3

1. kdm

### Tiling Windows Manager

1. Xmonad
1. i3
