Status: published
Date: 2019-02-11 19:21:20
Author: Benjamin Du
Slug: spark-sql-tips
Title: Spark SQL Tips
Category: Programming
Tags: programming, big data, Spark, Spark SQL

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



1. Spark SQL supports hive sql syntax.
    For example,
    `spark.sql("show tables in some_schema")`
    returns a DataFrame with tables in the Hive database.

2. JSON, ORC, Parquet and CSV files can be queried using Spark SQL without creating a table on the Spark DataFrame.

## References

https://stackoverflow.com/questions/41254011/sparksql-read-parquet-file-directly
