Status: published
Date: 2017-04-22 15:02:59
Author: Ben Chuanlong Du
Title: Connect to Databases Using pyodbc in Python
Slug: pyodbc-tips
Category: Computer Science
Tags: programming, pyodbc, Python, tips, ODBC, database, SQL, Vertica, Teradata
Modified: 2020-05-22 15:02:59

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

pyodbc only supports qmark

https://github.com/mkleehammer/pyodbc/wiki

## Unicode Converter Buffer Overflow 

This issues arises in Python3 but not Python2,
so the simplest way is to use Python2 if you do not have use Python3. 
And make sure do not use unicode queries.

1. If you are using `pyodbc` in Python3 to query Vertica, 
    then set the `VERTICAINI` environment variable
    and set `DriverManagerEncoding=UTF-16` in `vertica.ini`. 
    For more information, 
    please refer to the issue 
    [Not working with Python 3.4.3 on OS X (Vertica driver) #44](https://github.com/mkleehammer/pyodbc/issues/44)
    on GitHub.
