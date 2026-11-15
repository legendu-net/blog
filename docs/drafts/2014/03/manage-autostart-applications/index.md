---
title: Manage Autostart Applications
created: '2014-03-22T12:35:14-07:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: manage-autostart-applications
license: CC-BY-4.0
tags:
  - Linux
  - autostart
  - desktop
  - application
  - launching
  - desktop environment
  - GNOME
  - KDE
  - Xfce
  - LXQT
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. Autostart `*.desktop` configuration files
   are located in directories
   `/etc/xdg/autostart`
   and
   `~/.config/autostart/`
   .
   By default,
   autostart applications in `/etc/xdg/autostart`
   are not shown to users in "Startup Applications Preferences"
   while autostart application in `~/.config/autostart`
   are shown to users in "Startup Applications Preferences".

1. If you use multiple Linux desktop environments,
   you can customize `desktop` configuration files
   for different Linux desktop environments.
   Please refer to
   [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)
   for details.

1. By default,
   a `*.desktop` file under `/etc/xdg/autostart` or `~/.config/autostart`
   enables an application to autostart.
   There are 2 ways to disable autostart of the application.

   - Add the line `Hidden=True` into the `desktop` file.
     This is the recommended way.
   - Remove the `desktop` file.
     This is not recommended,
     generally speaking.

1. If you want to disable an autostart application
   defined by a `desktop` file in `/etc/xdg/autostart`,
   you'd
   <span style="color:green">
   better make a copy of the `desktop` file into `~/.config/autostart`
   and disable there
   </span>
   <span style="color:red">
   unless you want to disable it system-wide
   </span>
   .

1. Sometimes,
   it's helpful to delay the start of some applications (e.g., Dropbox).

   - makes your Linux machine boot faster
   - a non-system application might fail to auto start without configuring a delay

   The universal way to configure a delay is to add a `sleep` into the `Exec=` line.
   For example

   ```text
    Exec=sleep 10 && /usr/bin/flatpak run --branch=stable --arch=x86_64 --command=/app/bin/dropbox-app com.dropbox.Client
   ```

   Some Linux desktop environments support their specific keys for delayed autostart in `.desktop` files.
   For example,
   GNOME supports `X-GNOME-Autostart-Delay`.
   However,
   some Linux desktop environments (e.g., KDE)
   don't have such as equivalent.

## A List of Autostart Applications to Disable

- /etc/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
- /etc/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop
- /etc/xdg/autostart/org.kde.kdeconnect.daemon.desktop
- /etc/xdg/autostart/sogoupinyin.desktop
- /etc/xdg/autostart/sogoupinyin-watchdog.desktop
- /etc/xdg/autostart/ubuntu-report-on-upgrade.desktop
- /etc/xdg/autostart/update-notifier.desktop
- /home/dclong/.config/autostart/im-launch.desktop
