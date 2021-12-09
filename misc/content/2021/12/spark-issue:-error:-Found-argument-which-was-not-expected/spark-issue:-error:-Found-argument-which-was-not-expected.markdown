Status: published
Date: 2021-12-05 13:57:21
Modified: 2021-12-05 13:57:21
Author: Benjamin Du
Slug: spark-issue:-error:-Found-argument-which-was-not-expected
Title: Spark Issue: Error: Found Argument Which Was Not Expected
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, PySpark, argument, not expected, subprocess

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom 

> Error: b"error: Found argument '--id1-path' which wasn't expected, or isn't valid in this context ...

## Cause 

The argument `--id1-path` is not a valid argument to the command called by Python.

## Solutions 

Fix the non-valide argument of the command called by Python. 

