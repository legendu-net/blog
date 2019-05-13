Status: published
Date: 2019-05-13 22:00:28
Author: Benjamin Du
Slug: column-row-expressions-in-spark
Title: Column/Row Expressions in Spark
Category: Programming
Tags: programming, Spark, big data, Column, Row, Dataset, map, flatMap

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Spark DataFrame is an alias to Dataset[Row].
Even though a Spark DataFrame is stored as Rows in a Dataset,
built-in operations/functions (in org.apache.spark.sql.functions) for Spark DataFrame are Column-based.
Sometimes, 
there might be transformations on a DataFrame that is hard to express as Column expressions
but rather evey convenient to express as Row expressions. 
The traditional way to resolve this issue is to wrap the row-based function into a UDF.
It's worthing knowing that Spark DataFrame supports map/flatMap APIs 
which works on Rows. 
They are still experimental as Spark 2.4.3.
