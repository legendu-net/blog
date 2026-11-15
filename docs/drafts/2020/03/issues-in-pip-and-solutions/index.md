---
title: Issues in pip and Solutions
created: '2020-03-09T16:37:34-07:00'
date: '2026-11-15T12:20:37-08:00'
authors:
  - bendu
label: issues-in-pip-and-solutions
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - pip
  - issue
  - solution
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Abort trap: 6 when using `pip3 search`

The issue is due to to `pyopenssl` using old dependencies.
It can be fixed by removing the Python package `cryptography` package
and then upgrading `cryptography` to version 2.8.

1. Find the location of the Python package cryptography.

   ```bash
   pip3 show cryptograph
   ```

1. Remove the whole package directory.

   ```bash
   sudo rm -rf /path/to/cryptograph
   ```

1. Reinstall the latest version of `cryptograph`.

   ```bash
   pip3 install cryptograph
   ```

https://github.com/pypa/pip/issues/7254
