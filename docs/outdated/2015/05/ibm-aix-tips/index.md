---
title: IBM AIX Tips
created: '2015-05-06T23:55:20-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: ibm-aix-tips
license: CC-BY-4.0
tags:
  - Unix
  - IBM
  - AIX
  - tips
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Display the total disk usage of the current directory.

```bash
du -lsm
```

Display the disk usage of sas data set files.

```bash
du -lsm *.sas7bdat
```

Calculate the md5sum of a file.

```bash
csum -h MD5 fileName
```
