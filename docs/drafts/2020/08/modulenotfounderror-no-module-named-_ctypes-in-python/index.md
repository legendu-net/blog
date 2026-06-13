---
title: 'ModuleNotFoundError: No Module Named _Ctypes in Python'
created: '2020-08-14T10:47:00-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: modulenotfounderror-no-module-named-_ctypes-in-python
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - ctypes
  - _ctypes
  - ModuleNotFoundError
  - error
  - exception
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Issue

The error message "ModuleNotFoundError: No Module Named \_Ctypes"
is thrown when using Python.

## Cause

A crucial built-in module, \_ctypes,
is either missing from your Python installation or cannot be located.

For more discussions,
please refer to
[Chat with Gemini - Resolving \_ctypes Module Not Found](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221XBVxZepSxAYqCPelMgHG000RIFLu5a8w%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## Solution

1. Remove Python.

1. Install `libffi-dev`

   ```bash
   sudo apt-get update
   sudo apt-get install libffi-dev
   ```

1. Reinstall Python.

## References

- [Exception and Error Handling in Python](exception-and-error-handling-in-python)

- [Python3: ImportError: No module named '\_ctypes' when using Value from module multiprocessing](https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul)
