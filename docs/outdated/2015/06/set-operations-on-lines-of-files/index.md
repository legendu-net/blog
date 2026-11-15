---
title: Set Operations on Lines of Files
created: '2015-06-14T02:12:06-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: set-operations-on-lines-of-files
license: CC-BY-4.0
tags:
  - programming
  - set operations
  - file
  - lines
  - sort
  - uniq
  - comm
  - shell
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

It is suggested that you **use Python instead of shell** script
to manipulate text files!

1. Union lines in 2 files.

   ```
    :::bash
    comm f1 f2
   ```

   Or you can use

   ```
    :::bash
    cat f1 f2 | sort -u | uniq -u
   ```

1. Show symmetric difference

   ```
    :::bash
    comm -3 file1 file2
   ```

1. Show difference of 1 and 2

   ```
    :::bash
    comm -23 file1 file2
   ```

Note that lines in files must be sorted first if you use the command `comm`.
To sort lines in a file,
you can use the following command.

```
:::bash
sort file -o file
```
