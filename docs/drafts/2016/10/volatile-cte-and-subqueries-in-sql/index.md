---
title: Volatile CTE and Subqueries in SQL
created: '2016-10-25T18:45:40-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: volatile-cte-and-subqueries-in-sql
license: CC-BY-4.0
tags:
  - programming
  - CTE
  - SQL
  - volatile
  - with
  - subquery
  - sub query
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. A volatile table persistents in the duration of the connection that creates it
   while a CTE is only accessible by the query following it.
   That is the scope of CTE is narrower and is safer.

1. If performance is a concern, use volatile (temp) tables.

1. Always use a CTE (with clause) instead of a sub query when applicable
   as a CTE is more flexible (can be recursive),
   is reusable,
   and is more readable.

1. A CTE can be recursive and is reusable.

## References

https://www.alisa-in.tech/post/2019-10-02-ctes/

https://stackoverflow.com/questions/706972/difference-between-cte-and-subquery

https://learnsql.com/blog/sql-subquery-cte-difference/

[Common Table Expression (CTE)](http://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-cte.html)
