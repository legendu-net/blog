---
title: Batch File Renaming Using "rename"
created: '2016-05-12T11:04:38-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: batch-file-renaming-using-rename
license: CC-BY-4.0
tags:
  - Linux
  - rename
  - shell
  - tip
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

It is suggested that you use Python script to rename files in batch.

Change names of `.txt` files to lowercase.

```bash
rename 'y/A-Z/a-z/' *.txt
```

Get rid of `(1)` in file names.

```bash
rename 's/\(1\)//' *
```
