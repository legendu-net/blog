---
title: Using SQL in R
created: '2016-01-08T15:47:42-08:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: using-sql-in-r
license: CC-BY-4.0
tags:
  - programming
  - CRAN
  - SQL
  - database
  - RJDBC
  - teradataR
  - RODBC
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. It is suggested that you do not use paste to concatenate SQL queries,
   but rather have a complete SQL query with special marked variables
   and then substitute the marked variables with aproprivate values.
   This makes the SQL code much easier to understand.
   For example,

```R
q = "
select
    id,
    name
from
    table
where
    id in (${IDs})
"
```

You can then substitute `${IDs}` with the right values.\
Some people might against this due to injection attack,
but I really do not think this is a problem
as database users usually do not have write permissions to public tables.
I value readability more here.

## JDBC

1. `RJDBC` is a usable but has some glitches.

1. You cannot end a SQL statement with a semicolon when using `RJDBC`.
   This means that you can send only a single query at a time when using `RJDBC`,
   which is not efficient.

1. `RJDBC::dbWriteTable` has a bug for Teradata.
   As an workaround,
   you can generate SQL statement to insert data by yourself
   (which is tedious of course).

1. RJDBC has a bug on schema when checking whether a table exists or not.
   For example, if there is a (non volatile) table `p_chdu_t.employees`.
   'dbExistsTable('employees')' returns `TRUE`
   but `dbExistsTable('p_chdu_t.employees')` returns `FALSE`.
   This impacts server functions in RJDBC.

## ODBC

1. RODBC

1. teradataR
