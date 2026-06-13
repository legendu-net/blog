---
title: Python Logging
created: '2019-03-12T10:43:38-07:00'
date: '2026-06-12T22:31:50-07:00'
authors:
  - bendu
label: python-logging
license: CC-BY-4.0
tags:
  - programming
  - Python
  - logging
  - loguru
  - rich
---

## General Tips

1. [logging](python-logging)
   is a Python module for logging coming with the standard library
   while
   [loguru](python-logging-made-stupidly-simple-with-loguru)
   is a popular 3rd-party logging library.
   Unless you do not want your Python package/script to depend on 3rd-party libraries,
   `loguru` is preferred to `logging` for multiple reasons.

   - loguru is easy and fun to use
   - Good out-of-box experience. They default settings work well for most situations.
     For example,
     loguru works with Spark by default while logging needs additional configurations.

1. [rich](https://github.com/willmcgugan/rich)
   is a Python library for rich text and beautiful formatting in the terminal.

## References

https://github.com/Delgan/loguru/issues/120

https://realpython.com/python-logging/

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels

[PyLint message: logging-format-interpolation](https://stackoverflow.com/questions/34619790/pylint-message-logging-format-interpolation)

[Python Logging Made Stupidly Simple With Loguru](python-logging-made-stupidly-simple-with-loguru)
