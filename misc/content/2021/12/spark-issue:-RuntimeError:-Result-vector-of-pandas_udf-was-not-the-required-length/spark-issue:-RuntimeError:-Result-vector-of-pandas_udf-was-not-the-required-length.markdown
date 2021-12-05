Status: published
Date: 2021-12-05 14:02:58
Modified: 2021-12-05 14:08:44
Author: Benjamin Du
Slug: spark-issue:-RuntimeError:-Result-vector-of-pandas_udf-was-not-the-required-length
Title: Spark Issue: RuntimeError: Result Vector of pandas_udf Was Not the Required Length
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, PySpark, subprocess, pandas_udf, length

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

> Runtimeerror: Result vector of pandas_udf was not the required length: expected 1, got 101456

## Cause 
The length of the result returned by the pandas UDF does not match the length of its input series. 
Notice that if your pandas UDF parses the stdout of a command,
it is possible that extra prints to the stdout was introduced which breaks the parsing. 

## Solution
Fix issue in the pandas UDF. 