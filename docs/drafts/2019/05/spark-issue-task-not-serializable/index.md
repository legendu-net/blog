---
title: 'Spark Issue: Task Not Serializable'
created: '2019-05-22T10:11:48-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: spark-issue-task-not-serializable
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - serialiation
  - error
  - big data
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Please refer to
[Spark Issue: \_Pickle.Picklingerror: Args[0] from __Newobj__ Args Has the Wrong Class](spark-issue-_pickle.picklingerror-args-0-from-__newobj__-args-has-the-wrong-class)
for a similar serialization issue in PySpark.

## Error Message

> org.apache.spark.SparkException: Job aborted due to stage failure: Task not serializable: java.io.NotSerializableException: ...

## Possible Causes

Some object sent to works from the driver is not serializable.

## Solutions

1. Don't send the non-serializable object to workers.

1. Use a serializable version if you do want to send the object to workders.

## References

https://github.com/databricks/spark-knowledgebase/blob/master/troubleshooting/javaionotserializableexception.md
