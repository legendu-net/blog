Status: published
Author: Ben Chuanlong Du
Date: 2014-02-15 12:10:03
Title: General Tips on SQL
Slug: sql-tips
Category: Computer Science
Tags: programming, SQL, tips, IDE, sqldep, queryscope, queryViz, SQLAlchemy, database
Modified: 2021-07-29 19:59:32

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

## Performance

1. Avoid implicit data convertion!
    This might cause full table scan which hurts performance badly.
    For more discussions,
    please refer to
    [一条垃圾SQL，把 64 核 CPU 快跑崩了！](https://mp.weixin.qq.com/s/mdl4Xa9zbl-CUBCi4Io-Tg)
    .

1. If performance is an issue, temp tables are preferred to subqueriess.

2. When you create a table by selecting records from another table,
    it is best to specify a primary index
    even if the original table has primary indexes.
    The reason is that the data you've selected might not have the same distribution as the original data.
    Specifying a good primary index not only improve the performance of queries
    but can also reduces the percentage of wasted spaces.


## Misc

1. If you want to do some analysis on a time window of data,
    it is best to choose a continuous window during a certain month if possible.
    This makes it simple (no need to use date/time function) to work with the dates later.

2. Outer join is preferred over inner join if you doing some exploring analyses
    (unless you absolute know that inner join is sufficient) 
    as it preserves more information.
    It is often the case when doing exploring analyses that you run an inner join and then found that you really need a left/right join.
    This can be a great waste of time if your analysis consist of many steps and you have to go back to the very beginning change an inner join to an outer join.
    On the contrary, 
    it does not hurt that your run a left/right join when you found that you really just need an inner join.
    However, 
    DO be careful when you use outer joins as they are tricky too!
    If using left/right join, 
    prefer to keep column in the left/right table.

3. `window_function() over (partition by col1, col2 order by col3)`
    Be careful that a default window of unbounded prceeding to the current row is used by default when you sort partitions.
    Due to this, some window functions requires full information (such as last, max, mean, rank, etc.) won't give you the right results.
    However, windows functions that only require partial information (such as first, row_number, etc.) work as expected.
    For this reason, 
        - first is preferred over last
        - row_number is preferred over rank

5. `row_number() over ()` It is allowed to specify no partition for window functions.
    In that case, all records is treated as one partition.

6. When using integer constant in SQL code, prefer BigInt, i.e., suffix them with `L`.
    This can save you troubes of overflow if count/sum a large table.

7. Always assume there are data issues (such as missing values, duplicates, etc.) unless forced by table constraints
    as this is often the fact.

8. If you write some database-based application,
    never delete anything and just mark records (to be deleted) as hidden instead.


1. If space and performance is not critical, 
    to make it is easier for collabarating,
    you can define all columns as type of varchar. 
    The advantage is that no one has to remember the type of columns. 

2. Good to keep all kind of IDs even if you won't need them currently, 
    you nev.. know when you are going to need them ...

3. Avoid using subqueries in SQL. 
    Use CTE (with clause) instead
    which is equivalent but much more readable.

1. Avoid using resvered keywords (e.g., `title`) as column/table name, 
    even if you can use "keyword" but still other people might forget for not obvious keywords like title

2. JDBC is preferred over ODBC for 3 reason. 
    First, JDBC is easier to set up.
    Second, JDBC has better performance.
    Last but not least, JDBC has wider support.

3. `*` stand for all fields. 
    If you want all fields of a specific table,
    then prefix `*` with the table name, 
    e.g., `t.*`. 
    This is helpful when you join multiple tables.
    Another thing is that `*` cannot be followed by more fields. 
    However, `t.*` can (where `t` is a table).
 
1. Some versions of SQL use `as` when creating aliases for selected fields 
    while some other versions of SQL don't.

2. analytical functions are powerful
    row_number() over partition
    another way is to use self join

3. `select count(*) from table t;`
    no grouping, kind of default grouping, all record are in a default group

4. Use `=` instead of `==` for comparison.
    Quote strings using single quotation marks instead of double quotation marks.

5. refresh in SQLDeveloper to show newly created talbes

6. You must put all columns of the SELECT 
    in the GROUP BY or use aggregate functions on them 
    which compress the results to a single value (like MIN, MAX or SUM) 
    according to SQL standard.
    MySQL does not conform to this standard
    and the results returned is not well defined sometimes 
    when you don't follow the SQL standard.

7. the select distinct, distinct describes record, not column.

## Tricks and Traps

1. [Ten SQL Tricks that You Didn’t Think Were Possible (Lukas Eder)](https://www.youtube.com/watch?v=mgipNdAgQ3o)

1. You cannot use `order by` when insert records into a table using select .
    this is easy to understand as first SQL does not save data in order. 
    second, ordering in select might conflict with ordered columns (e.g., auto increment columns).
    Finally, select never garantee any ordering.
    You have to apply order by any way. 

2. It is always good practice to indicate the version of SQL in your sql code ....
    as others cannot easily tell whether you are using Teradata SQL, Oracel SQL or MS SQL
    not to mention the version (if version specific feature is used).

1. extra semicolon somewhere causes mistakes

2. case when, break at first match, no need to manually break (unlike C/C++)

3. avoid using keywords as column names, 
    if you do want use a keyword as a column name, 
    you have to double quote it (e.g., "as"). 
    can also use [], '', in MS SQL, etc.

4. always specify (unique) primary index when you create a table 

8. if not group by statement, then all records as 1 group 
    if there is a aggregation function.

9. be careful when you use the 
    `delete from table_name` command, 
    as you might mistakely delete all rows 
    if you forget the `where` clause or has an extra `;` before ...

1. sometimes you want add "missing" rows (compared to some "full" table). 
    the first step is of course to create such a full table, 
    and join the two tables to find "missing" rows

3. Even if observations in a table is sorted, 
    you have to rely on the `order by` clause to get sorted observations.
    That is the `select` statement without `order by` guarantees no specific order of observations.
    This is true for all versions of SQLs.

## Syntax

1. `()` can be used and sometimes make people confused ... function or keyword ...

## Operators

1. Prefer `<>` as the not equal sign as not all versions of SQL support `!=` as the not equal sign.

2. extra `;` can be really dangerous ... 

## Comment

1. Amost all versions of SQL support `--` as single-line comment.
    and `/* ... */` as multiple-line comment.
    MySQL also support `#` as single-line comment.

## References

- [Understand Execuation of SQL Statements](http://www.legendu.net/en/blog/understand-execuation-of-sql-statements)

- [Spark SQL](http://www.legendu.net/misc/blog/spark-sql-tips/)

- [Hive SQL](http://www.legendu.net/misc/blog/hive-tips/)

- [SQL Style And Formatter](http://www.legendu.net/misc/blog/sql-style-and-formatter/)

- [Tips on Sqlfluff](http://www.legendu.net/misc/blog/tips-on-sqlfluff/)

- [Questions on SQL](http://www.legendu.net/misc/blog/sql-questions/)

- [Chapter 4. Query Performance Optimization](https://www.oreilly.com/library/view/high-performance-mysql/9780596101718/ch04.html)

- [Ten SQL Tricks that You Didn’t Think Were Possible (Lukas Eder)](https://www.youtube.com/watch?v=mgipNdAgQ3o)
