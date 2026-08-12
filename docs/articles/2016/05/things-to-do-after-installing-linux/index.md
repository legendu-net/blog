---
title: Things to Do after Installing Linux
created: '2016-05-04T20:59:32-07:00'
date: '2026-08-11T22:39:32-07:00'
authors:
  - bendu
label: things-to-do-after-installing-linux
license: CC-BY-4.0
tags:
  - Linux
  - OS
  - installation
---

Note: The tips here are for Debian-based Linux distributions
(Debian, Ubuntu, LinuxMint, Pop!\_OS, AntiX, etc.).

## Debian Specific

1. If you installed Debian without a desktop environment,
   and wants to install a customized desktop environment now,
   make sure to install a DE manager (e.g., gdm, lightdm, etc.) as well.
   without a login/DE manager,
   Linux won't boot into DE automatically.
   Of course,
   you can still manually start X using `startx`.

1. Edit the APT (advance package tool) configuration file `/etc/apt/sources.list`.
   By default,
   Debian uses the installing media as a repository after installation.
   However,
   the media is usually removed and thus unavailable after installation.
   So,
   you probably want to delete or comment out the repository using the installing media.
   Also,
   if you did not use a network mirror duing installation,
   you have to add a debian repository into the APT configuration file manually.
   For example,
   you can add the following lines into the APT configuration file.

   ```
   deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free
   deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free
   ```

   It is suggested that you include `contrib` and `non-free` in the repository.
   This ensures that you can also use many non-open source but cost-free softwares.

1. Install the `sudo` package and configure it.
   You have to switch to root to install packages.
   To switch to root,
   type in `su` (super user) in the terminal.
   You will be asked for the password of root.
   After authentication,
   you are in root user.
   Notice that the prompt character is `#` (instead of `$`) for the root user.
   You can type `apt-get install sudo` in the terminal (as root) to install the package `sudo`.
   After installation of `sudo`,
   you have to add your user name to the `sudo` group.
   To do this,
   run the following command as root.

   ```
   adduser your_user_name sudo
   ```

   However,
   this will not take effect immediately.
   To notify the change (of group permission) to the system,
   you can run the following command as root.

   ```
   newgrp sudo
   ```

   If this does not work,
   you can manually log out and then log in
   and the change of group permissions will take effect.
   Now you are in the `sudo` group,
   you can use `sudo` (instead of the root user) to run commands
   that need root permission.
   You can now exit the root terminal (by running `exit`)
   if you are still in the root terminal.

1. If the wireless network is not working,
   refer to
   [Wireless for Debian](wirelss-for-debian)
   for possible solutions.

## LMDE Specific

1. By default, LMDE installs 486 on 32 bit computers.
   If your computer has more than 1 cores/processors,
   you can upgrade to 686-pae manually by running the following command in terminal
   and then reboot your computer.

   ```
    sudo apt install linux-image-3.0.0-1-686-pae
   ```

## Other Debian-based Linux Distributions

1. Tune settings to make your Linux machine run faster.
   For more discussions,
   please refer to
   [Make Linux Run Faster](make-linux-run-faster)
   .

1. Upgrade the system.

   ```
    :::bash
    sudo apt update && sudo apt upgrade
   ```

1. Swap the `Caps Lock` key with the `Escape` key.
   Please refer to
   [Map Keys in Linux](map-keys-in-linux)
   for detailed discussions.

1. Install must-have software.

   - aria2, uGet
   - Chrome, Firefox
   - Sogou Pinyin
   - Transimission
   - Dropbox, Baidu Netdisk

   This list might not be the best for everyone.
   For a general list of useful software/tools for Linux,
   please check the post [Useful Tools in Linux](useful-tools-in-linux).
