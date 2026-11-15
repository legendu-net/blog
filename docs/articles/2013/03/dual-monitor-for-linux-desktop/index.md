---
title: Dual Monitor for Linux Desktop
created: '2013-03-20T10:59:38-07:00'
date: '2026-11-15T09:18:03-08:00'
authors:
  - bendu
label: dual-monitor-for-linux-desktop
license: CC-BY-4.0
tags:
  - DE
  - Linux
  - monitor
  - dual
---

1. Type `xrandr` or `xrandr -q` in terminal to display information of all available output device.
   Then you can use the following commands to set dual display.

   ```
    xrandr --output VGA1 --auto 
    xrandr --output VGA1 --same-as LVDS1 --auto
    xrandr --output VGA1 --mode 1024x800
    xrandr --output VGA1 --off
   ```

where `VGA1` and `LVDS1` should be replaced by with appropriate device names.

10. When use multi-monitors in Linux,
    you need to have close resolutions in order for same (mirror) display to work well.
