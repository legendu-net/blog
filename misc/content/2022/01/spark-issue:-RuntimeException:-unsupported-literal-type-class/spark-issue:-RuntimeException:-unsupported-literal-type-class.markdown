Status: published
Date: 2022-01-15 14:36:45
Modified: 2022-01-15 14:45:57
Author: Benjamin Du
Slug: spark-issue:-RuntimeException:-unsupported-literal-type-class
Title: Spark Issue: RuntimeException: Unsupported Literal Type Class
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, big data, RuntimeException, type, unsupported

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom 

> java.lang.RuntimeException: Unsupported literal type class java.util.ArrayList [1]

## Possible Causes

This happens in PySpark 
when a Python list is provide where a scalar is required.
Assuming `id0` is an integer column in the DataFrame `df`,
the following code throws the above error.

    :::python
    v = [1, 2, 3]
    df.filter(col("id0") == v)

## Possible Solutions 

1. Use a scalar value for `v` in the above code example. 
2. Use `isin` to check whether the value of `id0` is in the list `v`. 
    
        :::python
        v = [1, 2, 3]
        df.filter(col("id0").isin(v))
