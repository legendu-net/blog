Status: published
Date: 2022-04-03 18:42:10
Modified: 2022-04-03 18:56:03
Author: Benjamin Du
Slug: spark-issue:-getQuotaUsage
Title: Spark Issue: GetQuotaUsage
Category: Computer Science
Tags: Computer Science, programming, Spark, Spark issue, exception, error, getQuotaUsage, getContentSummary, quota, Router

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom I

> py4j.protocol.Py4JJavaError: An error occurred while calling o156.getQuotaUsage.

## Symptom II

> org.apache.hadoop.ipc.RemoteException(java.io.IOException): The quota system is disabled in Router.

## Possible Causes

As the error message in symptom II, 
the quota system is disabled in Router.

## Possible Solutions

Remove the usage of `org.apache.hadoop.fs.FileSystem.getQuotaUsage` from the code. 
You can use other alternatives, 
e.g., 
you can use `org.apache.hadoop.fs.FileSystem.getContentSummary(path_hdfs).getLength()`
if you just need the size of a HDFS path.

