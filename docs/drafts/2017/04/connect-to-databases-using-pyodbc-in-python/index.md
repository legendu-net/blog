---
title: Connect to Databases Using pyodbc in Python
created: '2017-04-22T15:02:59-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: connect-to-databases-using-pyodbc-in-python
license: CC-BY-4.0
tags:
  - programming
  - pyodbc
  - Python
  - tips
  - ODBC
  - database
  - SQL
  - Vertica
  - Teradata
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

pyodbc only supports qmark

https://github.com/mkleehammer/pyodbc/wiki

## Unicode Converter Buffer Overflow

This issues arises in Python3 but not Python2,
so the simplest way is to use Python2 if you do not have use Python3.
And make sure do not use unicode queries.

1. If you are using `pyodbc` in Python3 to query Vertica,
   then set the `VERTICAINI` environment variable
   and set `DriverManagerEncoding=UTF-16` in `vertica.ini`.
   For more information,
   please refer to the issue
   [Not working with Python 3.4.3 on OS X (Vertica driver) #44](https://github.com/mkleehammer/pyodbc/issues/44)
   on GitHub.
