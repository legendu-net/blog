Status: published
Date: 2021-12-17 11:10:13
Modified: 2021-12-25 13:21:52
Author: Benjamin Du
Slug: spark-issue:-TypeError-withReplacement
Title: Spark Issue: TypeError WithReplacement
Category: Computer Science
Tags: Computer Science, programming, Spark, PySpark, issue, TypeError, withReplacement

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> TypeError: withReplacement (optional), fraction (required) and seed (optional) should be a bool, float and number; however, got [<class 'int'>].


## Causes

An integer number (e.g., `1`) is passed to the `fraction` parameter  of the function `DataFrame.sample` in PySpark.

## Solutions

Use a float number (e.g., `1.0`) instead.

