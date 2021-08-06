Status: published
Date: 2014-10-10 11:25:18
Author: Benjamin Du
Slug: understand-execuation-of-sql-statements
Title: Understand Execuation of SQL Statements
Category: Computer Science
Tags: programming, SQL, join on, having, where, group by, null value
Modified: 2021-07-31 11:52:22


## Execuation Order

A SQL statement selects rows and columns from a big (rectangular) table. 
You put columns that you want to select after `SELECT` 
and rows you want to select after `FROM`.
A SQL statement is executed as follows.
First, 
the (INNER|LEFT|RIGHT|FULL) `JOIN (ON)` is executed if any (see more explanation later).
Second, 
the `WHERE` condition is executed. Conditions before grouping (aggregation) must go into the `WHERE` clause.
Third, 
`GROUP BY (HAVING)` is executed. 
Conditions after grouping (aggregation) must go into the `HAVING` clause.
Fourth, 
the `SORT BY` statement is executed if any.
Last, columns (specified in the `FROM` clause) are selected.

## Traps in Outer Join

`OUTER JOIN` in SQL is very tricky 
and you have to be very careful when using outer joins!

1. It is suggested that you avoid or minize the use of outer joins.

2. Avoid using complicated queries when an outer join is involved.
    Split queries into simpler ones (one join at a time) if outer join is involved.

2. Understand the tables you are using. 
    Make sure that your logic is correct.

### Filter Conditions in `JOIN ON` vs in `WHERE`

An `INNER JOIN` first creates a cross join of tables in the `JOIN` clause 
(i.e., a Cartesian product of rows from tables in the `JOIN` clause), 
then it selects rows satisfying the `ON` condition from the cross join result. 
A `LEFT/RIGHT/FULL JOIN` consists of 2 sub steps. 
First, an `INNER JOIN (ON)` is performed. 
Second, unmatched rows in the left/right/both table(s) are appended into the resulting table of `INNER JOIN (ON)`. 
This means that all rows in the left/right/both table(s) will be in the resulting table
if there is no `WHERE` or `HAVING` condition in the query.
Notice that unmatched rows in the left/right/both table(s) uses `NULL` values for columns in the other table,
which is different from the Cartesian product (which uses values of the matched row). 
After joining, 
the `WHERE` clause is executed. 
This means that the `WHERE` condition is executed after the `ON` condition in `JOIN`. 
For an `INNER JOIN`, 
the `WHERE` condition can be put in the `ON` condition 
using `AND` because no extras (unmatched rows) are appended after the `ON` condition is executed. 
However, for a `LEFT/RIGHT/FULL JOIN` (extra unmatched rows are appended after `ON` condition is executed) 
the `WHERE` condition cannot be combined with the `ON` condition (using `AND`), generally speaking. 
For example,

    :::sql
    SELECT *
    FROM 
        A
    INNER JOIN 
        B
    ON
        A.id = B.id
    WHERE 
        B.id > 10
    ;

returns the same result as 

    :::sql
    SELECT *
    FROM 
        A
    INNER JOIN 
        B
    ON
        A.id = B.id AND B.id > 10
    ;

However, 

    :::sql
    SELECT *
    FROM 
        A
    LEFT JOIN 
        B
    ON
        A.id = B.id
    WHERE 
        B.id IS null
    ;

returns different result from

    :::sql
    SELECT *
    FROM 
        A
    LEFT JOIN 
        B
    ON
        A.id = B.id AND B.id IS null
    ;

generally speaking 
(
unless `LEFT JOIN` is equivalent to `INNER JOIN`, 
e.g., when the left table `A` is a subset of the right table B
on the joining columns
). 
For good practice, you'd better separate the `WHERE` and `ON` conditions.

Let's see some real examples to better understand the execution of SQL code.
Suppose we have 2 tables A and B (see below) both of which contain only 1 integer column named `id`.

|id|
|--:|
|1|
|2|
|3|
|4|
|5|
|6|
|7|
|8|
|9|
|10|
|11|
|12|
|13|
|14|
|15|

|id|
|--:|
|1|
|2|
|3|
|4|
|5|
|6|
|7|
|8|
|9|
|10|
|12|
|15|

The following presents some join queries and corresponding results.
Note that question marks (`?`) stand for null values in the following results.

    :::sql
    /*
    A inner join B
    Only matched rows are kept, which is easy to understand.
    */
    SELECT 
        A.id,
        B.id
    FROM
        A
    INNER JOIN
        B
    ON
        A.id = B.id
    ;

||A.id|B.id|
|::|:---:|:---:|
|1|6|6|
|2|3|3|
|3|10|10|
|4|12|12|
|5|9|9|
|6|4|4|
|7|5|5|
|8|1|1|
|9|15|15|
|10|8|8|
|11|2|2|
|12|7|7|

    :::sql
    /*
    A left join B
    Unmatched rows in A are kept but B.id is null for these unmatched rows.
    */
    SELECT 
        A.id,
        B.id
    FROM
        A
    LEFT JOIN
        B
    ON
        A.id = B.id
    ;

Notice `B.id` is set to null for rows in table A that do not have matching rows in table B.

||A.id|B.id|
|::|:---:|:---:|
|1|11|?|
|2|6|6|
|3|13|?|
|4|3|3|
|5|10|10|
|6|12|12|
|7|9|9|
|8|4|4|
|9|5|5|
|10|1|1|
|11|15|15|
|12|14|?|
|13|8|8|
|14|2|2|
|15|7|7|

    :::sql
    select 
        A.id,
        B.id
    from
        A
    left join
        B
    on
        A.id = B.id
    and 
    B.id > 10 
    ;

||A.id|B.id|
|::|:--:|:--:|
|1|11|?|
|2|6|?|
|3|13|?|
|4|3|?|
|5|10|?|
|6|12|12|
|7|9|?|
|8|4|?|
|9|5|?|
|10|1|?|
|11|15|15|
|12|14|?|
|13|8|?|
|14|2|?|
|15|7|?|

    :::sql
    /*
    Use where to further select records after inner join.
    Together with the query above, 
    it shows the different between `on condition1 and condition2` and `on condition1 where condition2`.
    */
    select 
        A.id,
        B.id
    from
        A
    left join
        B
    on
        A.id = B.id
    where 
    A.id > 10 
    ;

||id|id|
|::|:--:|:--:|
|1|11|?|
|2|13|?|
|3|12|12|
|4|15|15|
|5|14|?|

    :::sql
    /*
    Use where to further select records. 
    Notice that rows with B.id being `null` are dropped 
    because they are not eligible for condition `B.id >10`.
    */
    select 
        A.id,
        B.id
    from
        A
    left join
        B
    on
        A.id = B.id
    where 
    B.id > 10 
    ;

||A.id|B.id|
|::|:--:|:--:|
|1|12|12|
|2|15|15|

### Extra Filtering Conditions 

In an inner join, 
some filtering condtions might be optional.
For example, 
it does not matter whether you add filtering condition `t2.id > 10` 
into the `WHERE` clause or not in the following query.

    :::sql
    SELECT 
        *
    FROM 
        A
    JOIN
        B
    ON
        A.id = B.id
    WHERE 
        A.id > 10

And people tend to add this condition to help speed up the SQL performance.
However, 
the filtering condition `t2.id > 10` is likely to make a difference 
when an outer join (e.g., left join) is used.

    :::sql
    SELECT 
        *
    FROM 
        A
    LEFT JOIN 
        B
    ON 
        A.id = B.id
    WHERE 
        A.id > 10 

### Join First vs Filter First 

In an inner join, 
it does NOT matter whether you do joining first or filtering first.
For example, 
the following 2 queries return the same results.

    :::sql
    SELECT 
        *
    FROM
        A
    JOIN
        B
    ON 
        A.id = B.id
    WHERE 
        A.c1 ...
    AND 
        B.c2 ...
    ;

    SELECT 
        *
    FROM
        (SELECT * FROM A WHERE A.c1 ...)
    JOIN
        (SELECT * FROM B WHERE B.c2 ...)
    ;

However, 
**whether you do joining or filtering first on tables matters in outer joins.**
For example the 2 queries below are likely to yield different results.

    :::sql
    SELECT 
        *
    FROM
        A
    LEFT JOIN
        B
    WHERE 
        A.c1 ...
    AND 
        B.c2 ...
    ;

    SELECT 
        *
    FROM
        (SELECT * FROM A where A.c1 ...)
    LEFT JOIN
        (SELECT * FROM B where B.c2 ...)
    ;

This issue is similar to the issue of `JOIN ON` vs `WHERE` issue,
however, 
it is more likily to happen in the Spark world.
In the big data era, 
people are switching from traditional database to Spark. 
In Spark, DataFrame is the recommended way. 
However, 
in Spark people typically do filtering on tables/DataFrames first to improve performance
while in traditional SQL people typically do filtering after joining.
So you now you see if you translate some traditional SQL code to Spark,
it's easy to make mistakes.
**Always be careful when an outer join is used in SQL/Spark.**

There are 2 situations when the above 2 outer join queries are equivalent.

1. When left join is equivalent to inner join, 
    which happens when t1 is a subset of t2 on the joining columns.

2. **When the filering conditions in where in on columns of the left table only.**
    For example,

        :::sql
        SELECT 
            *
        FROM
            A
        LEFT JOIN
            B
        WHERE 
            A.c1 ...
        ;

        SELECT 
            *
        FROM
            (SELECT * FROM A where A.c1 ...)
        LEFT JOIN
            B
        ;

### Order of Join

In inner joins, 
the order of joining doesn't matter (in terms of final results).
For example, 
the following 2 queries return the same results.

    :::sql
    SELECT
        *
    FROM 
        t1
    JOIN
        t2
    JOIN 
        t3

    SELECT
        *
    FROM
        t1
    JOIN
        t3
    JOIN
        t2

However, 
the order of joinning matters if an outer join is used.

For example, 
the following 2 queries are likely to return different results.
The reason is that the join of t1 and t2 not nencessarily keep all rows in t2. 

    :::sql
    SELECT
        *
    FROM 
        t1
    JOIN
        t2
    LEFT JOIN 
        t3

    SELECT
        *
    FROM
        t1
    JOIN
        t3
    RIGHT JOIN
        t2

When t1 join t2 keeps the same rows as t2, 
then the 2 pseudo queries above are equivalent.
This happens when t2 is a subset of t1 on the joinning columns.
For example, when t1 is a lookup table that containg all situations that appears in t2. 


This kind of complicated joins is not recommended. 
It is suggested that you split it into simpler queries (one join at a time). 
If you insist using such complicated queries, 
well, 
make sure you know what you are doing.

### Filtering Condition in Subquery vs Fitering Condition in Join On

1. Similarly,
    there's no difference in an inner join.
    However,
    there might be difference in an outer join.

2. Conditions on the right table in a left-join-on clause 
    can be moved into a subquery which filters on the right table first.
    For example, 
    the 2 left outer join queries return the same result.

        SELECT
            *
        FROM 
            A
        LEFT JOIN
            B 
        ON
            A.id = B.id AND B.col ...

        SELECT
            *
        FROM 
            A
        LEFT JOIN
            (SELECT * FROM B WHERE B.col ...) 
        ON
            A.id = B.id

## References

https://social.msdn.microsoft.com/Forums/getfile/208801
