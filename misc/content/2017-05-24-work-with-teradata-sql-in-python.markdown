UUID: 00f6124a-aa41-4987-8f93-2b2164a28042
Status: published
Date: 2017-05-24 20:04:21
Author: Ben Chuanlong Du
Slug: work-with-teradata-sql-in-python
Title: Work With Teradata SQL in Python
Category: Programming
Tags: programming, Python, Teradata SQL, teradata, JayDeBeApi, pyodbc

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. `teradata` and `JayDeBeApi` (with necessary JARs)  works well for Teradata
while `pyodbc` has encoding issues sometimes. 
`teradata` is recommended.

2. `teradata` relies on either ODBC or RESTful.
If you use teradata with ODBC, 
it is suggested that you use CentOS (docker can be leveraged) as Teradata SQL offers official RPM packages for CentOS 
but offers no official DEB package for Ubuntu.
