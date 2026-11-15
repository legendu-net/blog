---
title: A JNI Error Has Occurred
created: '2019-12-03T10:14:14-08:00'
date: '2026-11-15T09:22:46-08:00'
authors:
  - bendu
label: a-jni-error-has-occured
license: CC-BY-4.0
tags:
  - programming
  - Java
  - JNI error
  - dependency management
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Error Messages

Error: A JNI error has occurred, please check your installation and try again

Caused by: java.lang.ClassNotFoundException: org.apache.spark.sql.SparkSession

## Cause

Some dependencies (Spark in this case) is not specified as a runtime dependency.
It is often a good idea to exclude Spark from the runtime dependencies
and only specify it as test dependencies.
However,
you will not be able to run your code directly in local.
Test can still be run of course.
