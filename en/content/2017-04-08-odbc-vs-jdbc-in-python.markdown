UUID: 9fde8ad7-e1b6-420e-8db0-e0046f8eb529
Status: published
Date: 2017-05-24 19:31:11
Author: Ben Chuanlong Du
Slug: odbc-vs-jdbc-in-python
Title: ODBC vs JDBC in Python
Category: Programming
Tags: programming, Python, ODBC, JDBC, database, SQL

Overall speaking, 
Python has better ODBC support than JDBC support. 
Most database related packages in Python support or rely on ODBC. 
Currently, ODBC packages also have richer feathers than JDBC packages.
However, 
it is not an easy job to install and configure ODBC drivers for a non-open source databases. 

## JDBC Packages in Python

1. `JayDeBeApi` is a usable JDBC package for Python (both 2 and 3).

2. `py4jdbc` is another JDBC package which claims to be faster (using Py4j instead of JPype)
but it is relative young compared to JayDeBeApi.

3. Just ignore the JayDeBeApi3 package (for Python3 only). 

4. PyAthenaJDBC is a JDBC package specifically for Amazon Athena.

## ODBC Packages in Python

1. `pyodbc` and `SQLAlchemy` are general purpose packages relying on ODBC. 

2. There are lots of database specific packages relying on ODBC. 
For example, 
`teradata` is a Python package for Teradata SQL which relies on ODBC or RESTful.

