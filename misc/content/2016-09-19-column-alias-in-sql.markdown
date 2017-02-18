UUID: dc85f9a3-6f9b-46b3-9b6e-115ea581b6aa
Status: published
Date: 2016-10-16 09:03:52
Author: Ben Chuanlong Du
Slug: column-alias-in-sql
Title: Column Alias in SQL
Category: Programming
Tags: programming, SQL, column alias, Teradata, Oracle

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


Logically any `SELECT` is processed in following order:
```SQL
from
where
group by
having
olap functions
qualify
select 
sample
order by
```
Besides the proprietary `QUALIFY/SAMPLE` every DBMS will do it exactly the same.
When you use a column alias in
`where`, `group by`, `having`, `olap functions` or `quality`
the column list is not yet created, 
thus using an alias should fail.

However, there are a few exceptions.  
Both Teradata SQL and MySQL allows using column aliases in
`where`, `group by`, `having`, `olap functions` and `quality`.
Even if column aliases are allowed in Teradata and MySQL, 
you should never alias to an existing column name 
to avoid confusing the optimizer and/or end user).

## Allow Column Alias 
1. Teradata SQL
2. MySQL

## Disallow Column Alias 
1. Oracle SQL


