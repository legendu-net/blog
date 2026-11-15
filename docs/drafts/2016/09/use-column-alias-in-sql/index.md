---
title: Use Column Alias in SQL
created: '2016-09-14T20:37:13-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: use-column-alias-in-sql
license: CC-BY-4.0
tags:
  - programming
  - SQL
  - column alias
  - Teradata
  - Oracle
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Logically any `SELECT` is processed in following order:

   1. from
   1. where
   1. group by
   1. having
   1. olap functions
   1. qualify
   1. select
   1. sample
   1. order by

   Besides the proprietary `QUALIFY/SAMPLE` every DBMS will do it exactly the same.
   When you use a column alias in
   `where`, `group by`, `having`, window function or `qualify`
   the column list is not yet created,
   thus using an alias should fail.
   However,
   there are a few exceptions.\
   Both Teradata SQL and MySQL allows using column aliases in
   `where`, `group by`, `having`, `olap functions` and `qualify`.
   For those SQL variants which do not support using a column alias
   in `where`, `group by`, `having`, window functions or `qualify`,
   you can use subqueries instead.

1. Spark/Hive SQL does not support using column aliases
   in `where`, `group by`, `having` or window functions.
   However,
   column aliases can be used in Spark DataFrame APIs
   as long as it is used in a subsequent method invoke.
   For example,
   the following code does not work in PySpark
   because the column alias `new_column_alias` is used in the same method invoke.

   ```
    :::python
    df.select(
        col("col1").alias("new_column_alias"),
        (col("new_column_allias") + 1).alias("another_column_alias")
    )
   ```

   However,
   the following code works
   as the column alias `new_colun_alias` is used in a subsequent method invoke.

   ```
    :::python
    df.select(
        col("col1").alias("new_column_alias")
    ).withColumn("another_column_alias", col("new_column_alias") + 1)
   ```

   Since Spark SQL and DataFrame APIs can be mixed together in Spark applications,
   things become very flexible and thus convenient.

1. Even if column aliases are allowed in Teradata and MySQL,
   you should never alias to an existing column name
   to avoid confusing the optimizer and/or end user).
   If you do alias to an existing column name in Teradata,
   the original column instead of the alias is used
   in `where`, `group byy`, `having`, window function or `qualify`.

## Allow Column Alias

1. Teradata SQL
1. MySQL

## Disallow Column Alias

1. Spark SQL
1. Oracle SQL
