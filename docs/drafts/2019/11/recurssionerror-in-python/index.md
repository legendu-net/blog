---
title: RecurssionError in Python
created: '2019-11-01T19:28:38-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: recurssionerror-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - tail recursion elemination
  - RecursionError
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Python does not support tail recursion elemination.
   Large recursion should be implemented as loop instead to avoid RecursionError.

1. pylint encouter RecursionError ...

## References

- [Exception and Error Handling in Python](exception-and-error-handling-in-python)

- [Recursion Error While Handling Recursion Error](https://nickdrozd.github.io/2019/06/03/recursion-error.html)

- [Python: maximum recursion depth exceeded while calling a Python object](https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object)

- [Tail Recursion Elimination](http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html)
