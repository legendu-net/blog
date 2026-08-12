---
title: Work with Teradata SQL in Python
created: '2017-05-17T11:47:48-07:00'
date: '2026-08-11T22:19:34-07:00'
authors:
  - bendu
label: work-with-teradata-sql-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - Teradata SQL
  - Teradata
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things under legendu.net/outdated are outdated technologies
that the author does not plan to update any more.
Please look for better alternatives.
\*\*

## ODBC

### teradata

1. `teradata` relies on either ODBC or RESTful.
   If you use teradata with ODBC,
   it is suggested that you use CentOS (docker can be leveraged) as Teradata SQL offers official RPM packages for CentOS
   but offers no official DEB package for Ubuntu.

1. It seems that Teradata ODBC 16.20 no longer requires unixODBC
   and actually it shouldn't be install in order for Teradata ODBC 16.20 to work.

### pyodbc

1. pyodbc works for Teradata too.

## JDBC

1. JDBC + pyarrow.jvm

## CLIv2

1. giraffez
