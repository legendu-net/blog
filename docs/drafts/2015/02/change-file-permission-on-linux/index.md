---
title: Change File Permission on Linux
created: '2015-02-15T23:45:23-08:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: change-file-permission-on-linux
license: CC-BY-4.0
tags:
  - Linux
  - file permission
  - file system
  - filesystem
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
R: 4
W: 2
X: 1

Make a directory readable to other people.

```sh
chmod 755 dir
```

Make a file readable to other people.

```sh
chmod 644 file
```

Make a directory and all its subcontents readable to other people.

```sh
# make the dir and its subcontents readable and executable
chmod 755 -R dir
# remove executable permission from files
find dir -type f | xargs chmod -x
```
