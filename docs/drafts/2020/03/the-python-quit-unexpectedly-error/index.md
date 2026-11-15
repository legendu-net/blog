---
title: The Python Quit Unexpectedly Error
created: '2020-03-05T11:11:51-08:00'
date: '2026-11-15T12:20:37-08:00'
authors:
  - bendu
label: the-python-quit-unexpectedly-error
license: CC-BY-4.0
tags:
  - programming
  - Python
  - error
  - quit
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

If you are using Homebrew, you can reinstall a corrupted Python environment like this:

brew uninstall --ignore-dependencies --force python python@2
unset PYTHONPATH
brew install python python@2
I had another "quit unexpectedly" issue and this resolved it for me.

https://bugs.python.org/issue36154
