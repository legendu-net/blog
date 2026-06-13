---
title: Tips on Debian
created: '2013-10-29T17:08:42-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-debian
license: CC-BY-4.0
tags:
  - OS
  - Linux
  - Debian
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Debian is much harder to use than Ubuntu and Ubuntu-based Linux distributions.
It is suggested that you use Ubuntu or an Ubuntu-based Linux distribution
instead of Debian.

## Installation

Please refer to
[Tips on Installing Debian Series Linux Distributions](tips-on-installing-debian-series-of-linux-distributions)
for detailed discussions.

## Wireless

[Wireless for Debian](wirelss-for-debian)

## VirtualBox

It's suggested that you

- always install Linux headers corresponding to the Debian image you have installed on your machine
- install virtualbox in the same repository as the Linux image

## Misc

[Debian Apt Sources List Generator](http://debgen.simplylinux.ch/)

- [Debian downgrade from SID to testing ](http://www.fakeroot.info/2012/12/debian-downgrade-from-sid-to-testing.html)
- [Listing & Downgrading Unstable/Testing Debian Packages](http://archives.ryandaigle.com/articles/2005/10/31/listing-downgrading-unstable-testing-debian-packages)
- [Debian Linux 6: Install and Configure Compiz Eye Candy Effects](http://www.cyberciti.biz/howto/debian-linux/aptget-install-and-configure-compiz-eye-candy-effects/)
- [Intel Wireless WiFi Link, Wireless-N, Advanced-N, Ultimate-N devices](http://wiki.debian.org/iwlwifi)

1. it seems that even Debian testing is outdated, the package ...

1. use apt-file update/search to find the right file ...

1. use sudo dpkg-reconfigure tzdata to change time zone

1. do not use the unstable/sid version unless you are a package developer

1. use all package sources instead of just stable, testing or sid
   and use pin

1. sudo apt install pkg/wheezy-backports
   not sudo apt install pkg/stable-backports
   you can use stable-backports in source.list, however
