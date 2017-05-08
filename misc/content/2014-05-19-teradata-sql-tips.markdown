UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Teradata SQL Tips
Author: Ben Chuanlong Du
Date: 2017-05-08 21:12:48
Slug: teradata-sql-tips
Category: Programming
Tags: programming, tips, Teradata SQL

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

- [Teradata Open Source Project on GitHub](https://github.com/Teradata)
- [Teradata SQL笔记](http://cuishen.iteye.com/blog/638968)
- [无知的比较：R和Teradata SQL(附赠TD经验几枚)](http://www.loyhome.com/%E6%97%A0%E7%9F%A5%E7%9A%84%E6%AF%94%E8%BE%83%EF%BC%9Ar%E5%92%8Cteradata-sql%E9%99%84%E8%B5%A0td%E7%BB%8F%E9%AA%8C%E5%87%A0%E6%9E%9A/)
- [The SQL Server DBA’s Guide to Teradata](http://sqlfool.com/mssql-dba-guide-to-teradata/)

## Syntax

6. Always end a complete Teradata SQL statement with a semicolon. 
Sometimes in Some SQL (e.g., SAS), 
the codes runs OK without an ending semicolon but sometimes might not. 
It is always good practice to end a complete SQL statement with a semicolon.

1. Commands in Teradata (and other versions of SQL) SQL are case-insensitive.

2. You can use `sel` as short for `select` in Teradata SQL,
however, 
it is suggested that you always use `select` instead of `sel`. 
This is because `sel` is not support in some other versions of SQL.
You can use SQL template to generate code for you if you are tired of typing.

3. Use `--` for one line comment and `/*...*/` for multiple line comment.
The `/*...*/` way is recommended as it is a widely used way for commenting.

4. The `as` keyword is optional when creating column aliases,
however, 
it is tricky in `create table` statement.
When you create table schema, 
you cannot not use the keyword `as` 
but when you create a table using a query you must use the keyword `as`.
```SQL
create table A /*no as here*/(
    a integer, 
    b char(20), 
    c decimal(12,3), 
    d date 
)
;

create table A as /*must use as here*/(
    select * from B
)
with data 
primary index (id)
;
```


5. `union (all)` does not match column names.
Columns of the two tables to be united together must have the same order. 
If the types of a column does not match, 
then the type of the first column is used 
and the corresponding columns of other tables will be casted into this type.

2. Both count and sum can be used to count the number of rows satisfying some condition. 
Generally speaking, count is preferred because it is able to remove duplicated records. 
For example, suppose we have a table A with columns `case_id` (non-unique) 
and `sar` (Y or N). We can count the number of rows with `sar = Y` using 
```SQL
sum(
    case(
        when sar = 'Y' then
            1
        else
            0
    end)
) as n
```
How, 
if `case_id` has duplicated values and we want to count the number of distinct cases with `sar = 1`, 
then `sum` does not work well. In stead, we can use 
```SQL
count(
    case(
        when sar = 'Y' then
            case_id
        else
            null
        end)
) as n
```
It is recommended that you always use `count` to count rows satisfying a condition.

4. In a case statement, 
at most one `when/else` branch is executed. 
As soon as a `when/else` statement is executed, 
it jumps out (like `break;` in C) of the case statement instead of continuing to the next branch.

14. Do not use natural joins (relying on same column names for joining) as it is dangerous to do so.

17. When joining multiple tables, 
SQL will determine the best way to perform the joins. 
So do not help the SQL compiler when you do multiple joins.

1. The precedence of logical operators are `not`, `and` and `or`. 
However, 
it is suggested that you always use parentheses to make your code easier to understand.

2. Displays the code used to generate the view or table.
```SQL
show table table_name;
```

5. Display table schema (i.e., show column names and attributes).
```SQL
help table table_name;
```
or you can use
```SQL
help column table_name.*;
```

## Null Values

3. Most functions in SQL (unless specially for `null` values) ignore 
`null` values like they never appear in the table. 

### Create an Empty Table

You can manually specify the structure of the table.
```SQL
create table A /*no as here*/(
    a integer, 
    b char(20), 
    c decimal(12,3), 
    d date 
)
;
```

Or you if there is an table (e.g., B) of the same structure, 
you can 
```SQL
create table A as B
with no data;
```
or
```SQL
create table A as /*as cannot be omitted here*/(
    select * from B
)
with no data 
primary index (id)
;
```
Notice that the syntax of Teradata SQL is different from other SQL languages 
when creating a table using a select clause. 
You have to end the statement with `with data;` or `with no data;`.
`with data` means that you want to append the selected records into the created table
while `with no data` creates an empty table.

## Database Information
1. Get version of Teradata SQL. 
```SQL
select * from dbc.dbcinfo;
```

## Error Message
1. unknown error, probably network issue

2. Error code 3754: precision error, character, numeric, .. -> float ...

## Performance Tips
1. if performance is an issue, avoid using sub queries, use temp tables instead ...

## Trick and Trap
1. Instead of using macros of other extensions of SQL 
(which many versions of SQL does not support),
an better alternative is to call SQL in other languages (Python, R, etc.).
This also makes it easier to do visualization or generalize reports. 

2. In Teradata, the maximum row size is approx 64K bytes. 
So that you cannot define columns of size greater than 64K.
For example, 
you cannot define a column of size 65K.

3. You cannot create a new table using `insert into`.
`insert into` can only insert into an existing table.

## Date
Be careful when you work with date in SQL.
A non-exist date can result in tricky errors.
For example (note that `2016-09-31` does not exist)
```SQL
where dt between '2016-09-01' and '2016-09-31'  
```
in Teradata throws the error message "a character string failed to convert to a numeric value".


