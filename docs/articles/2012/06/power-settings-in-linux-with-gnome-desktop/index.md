---
title: Power Settings in Linux with GNOME Desktop
created: '2012-06-03T10:17:32-07:00'
date: '2026-11-15T12:20:30-08:00'
authors:
  - bendu
label: power-settings-in-linux-with-gnome-desktop
license: CC-BY-4.0
tags:
  - configuration
  - battery
  - power
  - Linux
  - GNOME
---

Full control of the power settings in Linux with Gnome Desktop can be done through
**dconf-editor** at org->gnome->settings-daemon->plugins->power.
The default way to determine low battery, critical low battery and to carray out
critical low action is by counting left battery time.
You can change the way to measuring percentage of battery.
To get help on what an entry means, single click on the entry.
