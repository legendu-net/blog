Status: published
Date: 2019-03-10 10:27:02
Author: Benjamin Du
Slug: install-newer-version-of-sqlite3-on-debian
Title: Install Newer Version of SQLite3 on Debian Jessie
Category: OS
Tags: Linux, SQLite3, Debian, backports, SQLite
Modified: 2021-09-26 16:30:42

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Open `/etc/apt/sources.list` and add the following line to the end.

        :::text
        deb http://www.backports.org/debian jessie-backports main contrib non-free

    or

        :::text
        deb http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free
        deb-src http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free

2. Make sure the GPG signatures are correct by running the following command.

        :::bash
        sudo apt-get update
        sudo apt-get install debian-backports-keyring

3. Install SQLite3.

        :::bash
        sudo apt-get update
        sudo apt-get -t jessie-backports install sqlite3 libsqlite3-dev
