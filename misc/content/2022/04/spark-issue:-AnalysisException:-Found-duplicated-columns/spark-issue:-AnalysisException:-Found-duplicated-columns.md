Status: published
Date: 2022-04-03 18:51:57
Modified: 2022-04-03 19:04:02
Author: Benjamin Du
Slug: spark-issue:-AnalysisException:-Found-duplicated-columns
Title: Spark Issue: AnalysisException: Found Duplicated Columns
Category: Computer Science
Tags: Computer Science, programming, Spark, Spark issue, error, exception, AnalysisException, duplicated columns

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> pyspark.sql.utils.AnalysisException: Found duplicate column(s) when inserting into ...

## Possible Causes

As the error message says, 
there are duplicated columns in your Spark SQL code. 

## Possible Solutions

Fix the duplicated columns issues in your Spark SQL.
For example,
you can remove duplicated columns from your code
or you can use different column names.

