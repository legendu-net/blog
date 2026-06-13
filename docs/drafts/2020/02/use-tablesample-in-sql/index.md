---
title: Use TableSample in SQL
created: '2020-02-28T09:27:28-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: use-tablesample-in-sql
license: CC-BY-4.0
tags:
  - programming
  - SQL
  - Spark
  - Spark SQL
  - PostgreSQL
  - TABLESAMPLE
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The limit clause (or the method `DataFrame.limit` if you are using Spark)
is a better alternative if randomness is not critical.

## PostgreSQL

```sql
SELECT id from table TABLESAMPLE BERNOULLI(10) WHERE age < 20 LIMIT 30;
```

CANNOT use

```sql
SELECT id from table WHERE age < 20 TABLESAMPLE BERNOULLI(10) LIMIT 30;
```

Notice that `WHERE` is applied after `TABLESAMPLE`.
If you want to filter a table first and then do a sampling,
you can create a temporary table first
or you can leverage common table expression (CTE).

## Spark SQL

Similar to PostgreSQL.
However,
Spark has DataFrame APIs
and you can use the method `DataFrame.sample` to achieve the same purpose.
Notice that `DataFrame.sample` accepts only fraction (double value between 0 and 1)
instead of number of rows (integer value) as the parameter.
As a matter of fact,
sampling a specific number of rows in Spark does not performance a simple random sampling,
it is implemented as `LIMIT`
It is suggested that you always sample a fraction instead of sampling a specific number of rows in Spark
if randomness is important.

```
# avoid 
select * from table_name TABLESAMPLE (100 ROWS) 
# use the following instead
select * from table_name TABLESAMPLE (1 PCT) 
```

## References

- [Sample Rows from a Spark DataFrame](sample-rows-from-a-spark-dataframe)

- [SQL Equivalent](sql-equivalent)

- https://stackoverflow.com/questions/51502443/is-sample-n-really-a-random-sample-when-used-with-sparklyr
