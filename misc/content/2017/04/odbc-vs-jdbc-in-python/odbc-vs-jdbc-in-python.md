Status: published
Date: 2017-04-30 12:06:09
Author: Ben Chuanlong Du
Slug: sql-database-client-server-protocols
Title: SQL Database Client-server Protocols
Category: Computer Science
Tags: programming, Python, ODBC, JDBC, database, SQL, TurbODBC, pyarrow, pyarrow.jvm, Java, Arrow Flight, API, protocol
Modified: 2022-10-16 15:55:29

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. [Apache Arrow Flight](https://www.legendu.net/misc/blog/tips-on-apache-arrow-flight-sql)
    is the future protocol for querying Databases!
    It use columnar data and leverages Apache Arrow to avoid unnecessary copy of data,
    which makes it able to query large data much (about 100x) faster than ODBC and JDBC.

2. Overall speaking,
    Python has better ODBC support than JDBC support.
    Most database related packages in Python support or rely on ODBC.
    Currently, 
    ODBC packages also have richer features than JDBC packages.
    However,
    it is not an easy job to install and configure ODBC drivers for non-open source databases (e.g., Teradata),
    in which situations JDBC is more convenient.

## JDBC Packages in Python

1. [JDBC + pyarrow.jvm](https://uwekorn.com/2020/12/30/fast-jdbc-revisited.html)
    is currently the best way to query SQL databases. 

2. [jpype.dbapi2](https://jpype.readthedocs.io/en/latest/dbapi2.html#)
    provides an implementation of 
    the Python [DBAPI2](https://peps.python.org/pep-0249/)
    .
    However, 
    it is about 20x slower than the approach of JDBC + pyarrow.jvm.

3. [JayDeBeApi](https://github.com/baztian/jaydebeapi)
    is outdated and unmaintained.

4. PyAthenaJDBC is a JDBC package specifically for Amazon Athena.

## ODBC Packages in Python

1. [TurbODBC](https://github.com/blue-yonder/turbodbc)
    is likely the fastest ODBC Python package.
    [pyodbc](https://github.com/mkleehammer/pyodbc)
    is another (less efficient) alternative.

2. [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
    are general purpose packages relying on ODBC.

2. There are lots of database specific packages relying on ODBC.
    For example,
    [teradata](https://github.com/Teradata/PyTd)
    is a Python package for Teradata SQL which relies on ODBC or RESTful.

## Database Modules

1. json: JSON parsing.

2. sqlite3

3. [jreese/aiosqlite](https://github.com/jreese/aiosqlite)

4. PyMySQL, MySQLdb

5. PyMongo

6. teradata

7. pyodbc, pypyodbc: Python ODBC bridget.

8. SQLAlchemy

9. sqlalchemy-teradata


## Misc

http://docs.python-guide.org/en/latest/scenarios/db/


the teradata package is weird, the file option can be used to run multiple statements in file ...
but if I manually pass a string, it doesn't work ... check the implementation ...
https://support.microsoft.com/en-us/help/3103282/teradata-odbc-configuration-on-linux
https://developer.teradata.com/tools/articles/teradata-sqlalchemy-introduction
https://github.com/Teradata/sqlalchemy-teradata
http://developer.teradata.com/tools/reference/teradata-python-module#Installing
http://stackoverflow.com/questions/34948453/read-teradata-query-into-pandas


## ORM

1. [SQLAlchemy](https://www.sqlalchemy.org/)
    is the most popular ORM package for Python.
    [peewee](https://github.com/coleifer/peewee)
    and
    [orator](https://github.com/sdispater/orator)
    are lightweight ORM solutions compared to `SQLAlchemy`.


http://stackoverflow.com/questions/10797794/multiple-queries-executed-in-java-in-single-statement

http://stackoverflow.com/questions/4493614/sqlalchemy-equivalent-of-pyodbc-connect-string-using-freetds

https://developer.teradata.com/tools/articles/teradata-sqlalchemy-introduction

http://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure

http://stackoverflow.com/questions/29525808/sqlalchemy-orm-conversion-to-pandas-dataframe/29528804#29528804


## JDBC

https://analyticsanvil.wordpress.com/2016/06/08/python-jdbc-dyanmic-hive-scripting/

https://github.com/minatverma/pythonWorks/blob/master/DQM.py

https://www.fullstackpython.com/databases.html

http://docs.python-guide.org/en/latest/scenarios/db/

## References

- [It’s Time to Replace ODBC & JDBC](https://www.dremio.com/blog/is-time-to-replace-odbc-jdbc/)

- [https://www.youtube.com/watch?v=OLsXlKb_XRQ](Apache Arrow Flight SQL: High Performance, Simplicity, and Interoperability for Data Transfers)

- [DB-API V2.0](https://www.python.org/dev/peps/pep-0249/)

https://www.fullstackpython.com/object-relational-mappers-orms.html

https://docs.python-guide.org/scenarios/db/

https://www.python.org/dev/peps/pep-0249/
