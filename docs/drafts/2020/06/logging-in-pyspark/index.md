---
title: Logging in PySpark
created: '2020-06-15T11:38:22-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: logging-in-pyspark
license: CC-BY-4.0
tags:
  - computer science
  - big data
  - PySpark
  - Spark
  - loguru
  - logging
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Excessive logging is better than no logging!
   This is generally true in distributed big data applications.

1. Use `loguru` if it is available.
   If you have to use the `logging` module,
   be aware of traps in using it.
   For more details,
   please refer to [Hands on the logging Module in Python](python-logging).
