---
title: RecurssionError in Python
created: '2019-11-01T19:28:38-07:00'
date: '2026-11-15T09:22:29-08:00'
authors:
  - bendu
label: recurssionerror-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - tail recursion elimination
  - RecursionError
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Python does not support tail recursion elimination.
   Large recursion should be implemented as loop instead to avoid RecursionError.

1. pylint encounter RecursionError ...

## References

- [Exception and Error Handling in Python](exception-and-error-handling-in-python)

- [Recursion Error While Handling Recursion Error](https://nickdrozd.github.io/2019/06/03/recursion-error.html)

- [Python: maximum recursion depth exceeded while calling a Python object](https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object)

- [Tail Recursion Elimination](http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html)
