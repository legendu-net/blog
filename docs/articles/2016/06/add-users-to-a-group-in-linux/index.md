---
title: Add Users to a Group in Linux
created: '2016-06-10T19:05:41-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: add-users-to-a-group-in-linux
license: CC-BY-4.0
tags:
  - Linux
  - sudo
  - user
  - groups
  - gpasswd
  - usermod
---

There are several ways to add users to a group in Linux.
The following uses the `sudo` group as illustration.

1. `gpasswd`, `usermod` and `adduser` can all be used to add a user to a given group.
   However, it is suggested that you use `gpasswd` as it is more portable and intuitive.

   ```
    gpasswd -a user_name sudo
    newgrp sudo

    usermod -aG sudo user_name
    newgrp sudo

    # works on Ubuntu but not CentOS
    adduser user_name sudo
    newgrp sudo
   ```

   Just adding an user to a group might not make it work right away.
   The command `newgrp sudo` make the group `sudo` in effect right away.
   Of course, you can log out and then log in to make it work.

1. Some desktop environment (e.g., GNome, Cinnamon, KDE, etc.) can also do this for you.
   Taking Cinnamon as an example,
   you can follow the steps below to add/remove groups for a user.

   1. Open `System Settings`.

   1. Click `Users and Groups`.

   1. Select the user you want modify.

   1. Click on `Groups`.

   1. Check/uncheck groups from the prompt list.

   1. Click the OK to save the changes.
