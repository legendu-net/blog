Status: published
Date: 2019-06-21 21:20:15
Author: Ben Chuanlong Du
Slug: sql-style-and-formatter
Title: SQL Style and Formatter
Category: Programming
Tags: programming, SQL, SQL formatter, SQL style

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


[SQL translation](https://www.jooq.org/translate/)

## SQL Style and Formatting

https://www.sqlstyle.guide/

1. `||` works differently on different date types. 
    This is because different data types have different (default) padding/formatting styles.
    You can manually cast date types to produce the format you want. 

2. some people like to put `,` 
    before column names in select, 
    I don't think this is a good practices, 
    as what if we want to remove the first column? 
    it similarly inconvenient to removing the last column when put comma after column names

## SQL Formatter

1. <http://sqlformat.org/>

2. <http://www.dpriver.com/pp/sqlformat.htm>

3. <http://www.sql-format.com/>

4. <http://www.tsqltidy.com/>


## [andialbrecht/sqlparse](https://github.com/andialbrecht/sqlparse)

## References

https://stackoverflow.com/questions/3310188/what-free-sql-formatting-tools-exist

http://stackoverflow.com/questions/1394998/parsing-sql-with-python