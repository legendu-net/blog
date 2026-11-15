---
title: Cygwin Ports
created: '2016-08-10T13:28:49-07:00'
date: '2026-11-15T09:28:33-08:00'
authors:
  - bendu
label: cygwin-ports
license: CC-BY-4.0
tags:
  - Linux
  - Windows
  - virtualization
  - software
  - Cygwin
  - ports
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Cygwin Ports Project](http://cygwinports.org/)

If you want to use a package that is missing in Cygwin
(especially on the x86_64 version as some packages has not been ported to it yet),
You can install it from
[Cygwin Ports](https://sourceware.org/cygwinports/)
following the instruction below if available.

1. Download the newest version of Cygwin installation program.

1. Launch the Cygwin installation program with the `-K` flag in a Cygwin shell.
   For example,

   ```
    cygstart -- /path/to/setup-x86.exe -K http://cygwinports.org/ports.gpg
   ```

1. On the "Choose Installation Type" page,
   select "Install from Internet".

1. On the "Choose Download Site(s)" page,
   select a distro mirror,
   then enter <ftp://ftp.cygwinports.org/pub/cygwinports>
   in the User URL field and press Add (making sure that both are highlighted).
   You can just select the download site and proceed with it if you have added it before.

1. Proceed with package selection and installation,
   making sure to install any indicated dependencies.
