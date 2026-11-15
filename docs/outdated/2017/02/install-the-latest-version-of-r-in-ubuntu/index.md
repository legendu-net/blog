---
title: Install the Latest Version of R in Ubuntu
created: '2017-02-20T23:46:45-08:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: install-the-latest-version-of-r-in-ubuntu
license: CC-BY-4.0
tags:
  - programming
  - R
  - CRAN
  - Ubuntu
  - install
  - latest
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

```bash
sudo apt-add-repository -y "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/"
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
sudo apt-get update
sudo apt-get install r-base-dev
```

If `apt-add-repository` is not install yet,
you can install it with the following command.

```bash
sudo apt-get install software-properties-common
```
