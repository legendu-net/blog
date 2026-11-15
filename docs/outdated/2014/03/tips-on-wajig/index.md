---
title: Tips on Wajig
created: '2014-03-07T22:54:45-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: tips-on-wajig
license: CC-BY-4.0
tags:
  - Wajig
  - Linux
  - package management
  - tips
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

`apt` and `aptitude` are preferred to wajig.

[Wajig on Debian Wiki](https://wiki.debian.org/Wajig)

1. You can type enter the CLI of `wajig` by typing `wajig` in terminal,
   so that you can use commands of `wajig` directly
   instead of typing `wajig` every time.

   ```
    :::bash
    $ wajig
    wajig>
   ```

## sudo apt install

From the documentation,
`sudo apt install` is equivalent to `apt-get install --no-install-recommends`.
`sudo apt install-r` is equivalent to `apt-get install`.

## wajig search

1. `wajig search` use regular expression by default.
   For example,
   `wajig search g++` does not search for literal `g++` but any package that contains `g`.
   To search for `g++` related packages,
   you can use `wajig search g\\+\\+` instead.

1. Let wajig also search description

   ```
    :::bash
    wajig search -v youtube
   ```

## wajig download

1. Download a package for install later.
   This is very helpful if the package is big.

   ```
    :::bash
    wajig download pkg_name
   ```

1. Remove all GNOME desktop related packages

   ```
    :::bash
    sudo apt list | awk '{print $2}' | grep -i ^gnome | xargs sudo apt purge
   ```

1. install a package of specific version using wajig

   ```
    :::bash
    wajig search libssl/testing
   ```

1. check which repository a package comes from

   ```
    :::bash
    wajig policy geary
   ```

1. To install backport packages, use

   ```
    :::bash
    sudo apt install libreoffice/wheezy-backports
    apt-get -t wheezy-backports libreoffice
   ```

   It does not work if you use

   ```
    :::bash
    sudo apt install libreoffice/stable-backports
   ```

## Download Packages (for Installation Later)

If your network speed is a concern,
you can download a package for installation later using the command below.

```
:::bash
wajig download pkg_name  
```

## Issues

1. it seems to me that `sudo apt purge package_name` fails to remove packages sometimes
   even though it seems to succeed.
