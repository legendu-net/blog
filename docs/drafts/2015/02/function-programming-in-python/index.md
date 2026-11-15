---
title: Function Programming in Python
created: '2015-02-05T22:58:56-08:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: function-programming-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - map
  - functional programming
  - reduce
  - apply
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. The built-in function `map` applies a function to each element of an iterable.
   `map` is not useful mostly of time as Python has list comprehension, etc.
   `map` support iterating multiple iterables at the same time.

   ```
    map(f, sequence1, sequence2)
   ```

   which is equivalent to

   ```
    [f(x1, x2) for x1, x2 in zip(sequence1, sequence2)]
   ```

1. There are some useful functions in the modules `functools` and `operator`.
   Below is the functional programming way of summing all elements in an array.

   ```
    functools.reduce(operator.add, L)
   ```

## References

http://briansimulator.org/

https://pypi.python.org/pypi/brian/
