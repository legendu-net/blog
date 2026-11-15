---
title: Change Modified Time of Files
created: '2019-05-02T02:40:46-07:00'
date: '2026-11-15T12:20:35-08:00'
authors:
  - bendu
label: change-modified-time-of-files
license: CC-BY-4.0
tags:
  - Linux
  - modified timestamp
  - touch
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Change the modifiled timestamp of a file to the specified timestamp.

   ```
    touch -m -t 201512180130.09 some_file
   ```

1. Change the modified timestamp of a file to the current time.

   ```
    touch -m some_file
   ```

1. Change the modified timestamp of all files in the current directory to the current time.

   ```
    find . -type f -print0 | xargs -0 touch -m
   ```

1. You can use the `stat` command to show the modified timestamps of files.

   ```
    stat -c '%y' some_file
   ```

## References

https://unix.stackexchange.com/questions/118577/changing-a-files-date-created-and-last-modified-attributes-to-another-file
