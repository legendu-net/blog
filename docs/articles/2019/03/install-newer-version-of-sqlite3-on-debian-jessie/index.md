---
title: Install Newer Version of SQLite3 on Debian Jessie
created: '2019-03-10T10:27:02-07:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: install-newer-version-of-sqlite3-on-debian-jessie
license: CC-BY-4.0
tags:
  - Linux
  - SQLite3
  - Debian
  - backports
  - SQLite
---

1. Open `/etc/apt/sources.list` and add the following line to the end.

   ```
    :::text
    deb http://www.backports.org/debian jessie-backports main contrib non-free
   ```

   or

   ```
    :::text
    deb http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free
    deb-src http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free
   ```

1. Make sure the GPG signatures are correct by running the following command.

   ```
    :::bash
    sudo apt-get update
    sudo apt-get install debian-backports-keyring
   ```

1. Install SQLite3.

   ```
    :::bash
    sudo apt-get update
    sudo apt-get -t jessie-backports install sqlite3 libsqlite3-dev
   ```
