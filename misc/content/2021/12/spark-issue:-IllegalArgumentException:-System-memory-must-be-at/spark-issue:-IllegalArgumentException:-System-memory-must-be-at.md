Status: published
Date: 2021-12-05 13:02:47
Modified: 2021-12-05 13:08:35
Author: Benjamin Du
Slug: spark-issue:-IllegalArgumentException:-System-memory-must-be-at-least
Title: Spark Issue: IllegalArgumentException: System Memory Must Be At Least
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, IllegalArgumentException, heap size, memory

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

Exception in thread "main" java.lang.IllegalArgumentException: System memory 466092032 must be at least 471859200. Please increase heap size using the --driver-memory option or spark.driver.memory in Spark configuration.

## Causes

Not enough heap size (dirver memory). 

## Solutions 

Increase heap size using the `--driver-memory` option or `spark.driver.memory` in Spark configuration.
