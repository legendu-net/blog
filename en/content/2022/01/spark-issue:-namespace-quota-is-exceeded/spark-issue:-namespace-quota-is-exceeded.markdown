Status: published
Date: 2022-01-06 22:33:54
Modified: 2022-01-17 12:21:16
Author: Benjamin Du
Slug: spark-issue:-namespace-quota-is-exceeded
Title: Spark Issue: Namespace Quota Is Exceeded
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, NSQuotaExceededException, namespace, quota, big data



## Symptom

> Caused by: org.apache.hadoop.hdfs.protocol.NSQuotaExceededException: The NameSpace quota (directories and files) of directory /user/user_name is exceeded: quota=163840 file count=163841

## Cause 

The namespace quota of the directory `/user/user_name` is execeeded.

## Solutions

1. Remove non-needed files from the directory `/user/user_name` to release some namespace quota. 

2. As a long-term solution, 
    you can also try to apply for more resource for the HDFS directory `/user/user_name`.
    