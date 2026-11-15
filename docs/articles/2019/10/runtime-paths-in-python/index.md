---
title: Runtime Paths in Python
created: '2019-10-18T10:20:43-07:00'
date: '2026-11-15T09:16:20-08:00'
authors:
  - bendu
label: runtime-paths-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - runtime paths
---

`__file__` is the path of the Python script.
Note that if you make a symbolic link to a Python script and run the symbolic link,
then `__file__` is the path of the symbolic link.
Of course, you can use `os.path.realpath` to get real path of files.

`pathlib.Path.cwd()`, `os.getcwd()` and `'.'` returns/represents the path where the Python script was invoked,
which is often different from `__file__`.
