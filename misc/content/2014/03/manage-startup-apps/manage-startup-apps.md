Status: published
Author: Ben Chuanlong Du
Date: 2014-03-22 12:35:14
Modified: 2020-05-22 12:35:14
Title: Manage Autostart Applications
Slug: manage-autostart-apps
Category: OS
Tags: Linux, autostart, desktop environment, GNOME, KDE, Xfce, LXQT

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

2. If you use multiple Linux desktop environments,
    you can customize `desktop` configuration files 
    for different Linux desktop environments.
    Please refer to
    [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)
    for details.

2. By default,
    a `*.desktop` file enables an application to autostart.
    There are 2 ways to disable autostart of the application.

    - Add a line `X-GNOME-Autostart-enabled=false` 
        (or similarly for other Linux desktop environment) 
        into the `desktop` file. 
        This is the recommended way.
    - Remove the `desktop` file.
        This is not recommended, 
        generally speaking.

3. If you want to disable an autostart application 
    defined by a `desktop` file in `/etc/xdg/autostart`,
    you'd 
    <span style="color:green">
    better make a copy of the `desktop` file into `~/.config/autostart`
    and then disable it
    </span>
    <span style="color:red">
    unless you want to disable it system-wide
    </span>
    .

4. For a must-have autostart application (e.g., Dropbox),
    it might help to configure a delay to launch it 
    so that your Linux machine can boot faster.

        :::text
        X-GNOME-Autostart-Delay=30

## A List of Autostart Applications to Disable

- /etc/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
- /etc/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop
- /etc/xdg/autostart/org.kde.kdeconnect.daemon.desktop
- /etc/xdg/autostart/sogoupinyin.desktop
- /etc/xdg/autostart/sogoupinyin-watchdog.desktop
- /etc/xdg/autostart/ubuntu-report-on-upgrade.desktop
- /etc/xdg/autostart/update-notifier.desktop
- /home/dclong/.config/autostart/im-launch.desktop
