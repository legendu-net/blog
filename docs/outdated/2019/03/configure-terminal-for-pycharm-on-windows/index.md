---
title: Configure Terminal for PyCharm on Windows
created: '2019-03-05T01:48:55-08:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: configure-terminal-for-pycharm-on-windows
license: CC-BY-4.0
tags:
  - programming
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

I personally think it is better to develop in WSL 2 on Windows!

## Ubuntu Shell

1. Install Ubuntu Shell on Windows 10 if it hasn't been installed.

1. File -> Settings -> Tools -> Terminal

1. Replace the Shell path with `C:\Windows\System32\bash.exe`.

Unfortunately the Python virtual environment created in Ubuntu shell cannot be used by PyCharm
as PyCharm (or more precisely, the Windows File System) does not recognize Linux symbolic links.
