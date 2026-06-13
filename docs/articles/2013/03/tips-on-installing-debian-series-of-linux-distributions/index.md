---
title: Tips on Installing Debian Series of Linux Distributions
created: '2013-03-11T01:05:59-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-installing-debian-series-of-linux-distributions
license: CC-BY-4.0
tags:
  - install
  - Linux
  - software
  - Debian
---

## Before Installation

### Debian Specific

1. You'd better not install back ported Debian images,
   as it might cause issues with other software (e.g., VirtualBox).
   It is suggested that you use Debian test.

### Other Debian-based Linux Distributions

1. Download the right ISO image of the Linux distribution
   that you want to install.

1. Create a bootable flash drive.
   Please refer to
   [Ways to Make a Bootable Flash Drive in Linux](ways-to-make-a-bootable-flash-drive-in-linux)
   for detailed discussions.

1. Connect your machine (on which to install the Linux distribution)
   to an ethernet if possible.
   The wireless support on some Linux distributions is still not perfect.
   Depending on the hardware of your machine
   and which Linux distribution you are installing,
   you might need to connect to internet through ethernet network during installation.

1. Make sure the power of your laptop is plugged in.

## During Installation

### Debian Specific

1. It is recommended that you use the text installation.
   The text installation of Debian actually is pretty intuitive and easy to follow.
   The graphical installation of Debian did not work on any of my laptops.
   I am not sure whether the problem has been fixed or not,
   but it does not hurt to use the text installation.

1. If you do not like the default desktop enviroment of Debian (currently GNOME),
   you can deselect the desktop environment during installation.
   This also makes the installation faster.
   You can install a desktop enviroment you like manually after installtion of Debian.

### Other Debian-based Linux Distributions

1. Debian-based Linux distributions keep data in the home directory untouched
   during installation unless you choose to format the partition.
   It is suggested that you do NOT use a separate home directory.
   Following this suggestion,
   you have to set the mount point of the partition to install the Linux distribution
   as `/` (root directory).

1. A swap partition is required for Linux operating systems.
   You have to configure a swap partition during the installation.
   Please refer to
   [SwapFaq](https://help.ubuntu.com/community/SwapFaq)
   on guidelines for the swap partition.

1. If your network is not very fast,
   you can choose not to use network mirrors,
   especially when your installation image is update to date.

## After Installation

Please refer to
[Things to Do After Installing Linux](things-to-do-after-installing-linux)
for detailed discussions.
