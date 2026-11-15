---
title: Alternative to the rm Command in Linux
created: '2019-05-02T02:41:04-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: alternative-to-the-rm-command-in-linux
license: CC-BY-4.0
tags:
  - Linux
  - shell
  - rm
  - Trash
  - mv
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

As is know to all,
it can be dangerous to use the `rm` command directly in Linux/Unix.
A simple idea is to define other commands/alias/script to replace it.
For example,
I have a shell script named `trash` which moves files (as input arguments) to the system's Trash directory.

```
trash files_to_remove
```

Another even simpler way is to directly move files to the directory `/tmp`.

```
mv files_to_remove /tmp
```
