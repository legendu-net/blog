Status: published
Author: Ben Chuanlong Du
Title: Tips on Debian
Date: 2013-10-29 17:08:42
Slug: debian-tips
Category: OS
Tags: OS, Linux, Debian
Modified: 2022-05-04 11:46:15

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Debian is much harder to use than Ubuntu and Ubuntu-based Linux distributions.
It is suggested that you use Ubuntu or an Ubuntu-based Linux distribution
instead of Debian. 

## Installation

Please refer to
[Tips on Installing Debian Series Linux Distributions](https://www.legendu.net/en/blog/tips-for-installing-debian/)
for detailed discussions.

## Wireless

[Wireless for Debian](https://www.legendu.net/misc/blog/wirelss-for-debian)

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

2. use apt-file update/search to find the right file ...

3. use sudo dpkg-reconfigure tzdata to change time zone

4. do not use the unstable/sid version unless you are a package developer

5. use all package sources instead of just stable, testing or sid
    and use pin

6. wajig install pkg/wheezy-backports 
    not wajig install pkg/stable-backports
    you can use stable-backports in source.list, however
