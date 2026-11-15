---
title: Run Unix/Linux Commands in SAS
created: '2015-05-17T16:36:48-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: run-unix-linux-commands-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - Unix
  - Linux
  - command
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

SAS can run Unix/Linux commands everywhere using

```SAS
x command;
```

For example,
to create a directory named "abc" in your home directory.

```SAS
x mkdir ~/abc;
```

It can even run user-defined shell scripts,
which is great.
even though you can use unix/linux command in sas,
it seems that it is not robust and it is often hard
to test whether the command has run successfully.
It is suggested that you avoid using unix/linux commands in sas.
