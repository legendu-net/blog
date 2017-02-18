UUID: 1ed7fbf4-fbcc-44be-89b3-c4bc2df3970e
Status: published
Date: 2016-08-15 23:40:15
Author: Ben Chuanlong Du
Slug: using-sql-in-r
Title: Using SQL in R
Category: Programming
Tags: programming, CRAN, SQL, database, RJDBC, teradataR

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. `RJDBC` is a good library for SQL querying from databases. 

2. A SQL statement should always be ended by a semicolon.
However, 
you should never end a SQL statement with a semicolon 
when using `RJDBC`.

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
You can then substitute `${IDs}` with the right values.  
Some people might against this due to injection attack,
but I really don't think this is a problem as database users usually don't have write permissions to public tables.
I value readability more here.

4. `RJDBC::dbWriteTable` has a bug for Teradata. 
The package `teradataR` is alternative when working with Teradata. 
If you have to stick to to `RJDBC`, 
you can generate SQL statement to insert data by yourself
(which is tedious of course). 
