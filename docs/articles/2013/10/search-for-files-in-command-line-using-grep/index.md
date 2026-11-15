---
title: Search for Files in Command-line Using grep
created: '2013-10-22T14:53:28-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: search-for-files-in-command-line-using-grep
license: CC-BY-4.0
tags:
  - tips
  - grep
  - egrep
---

The article
[14 Practical examples of the grep command](http://www.librebyte.net/en/gnulinux/14-practical-examples-of-the-grep-command/)
has some good examples on how to use the `grep` command.

1. The Perl style (option `-P`) regular expression is more powerful
   than the basic (default) and extended (option `-E`) regular expression.
   It is suggested that you use the perl style as much as possible.
   However,
   be careful about unimplemented features.

1. The option `-n`/`--line-number` prefixes each line of output with the 1-based line number within its input file.
   And the option `-o`/`--only-matching` prints only the matched (non-empty) parts of a matching line,
   with each such part on a separate output line.
   Both of those options are very useful.

1. Search in current directory recursively for files containing the text "video".
   Symbolic links are followed.

   ```
    :::bash
    grep -iR 'video' .
   ```

1. Search in current directory recursively for files containing the text "video".
   Symbolic links are NOT followed.

   ```
    :::bash
    grep -ir 'video' .
   ```
