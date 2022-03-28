Status: published
Date: 2022-03-27 17:24:15
Modified: 2022-03-27 17:34:30
Author: Benjamin Du
Slug: spark-issue:-RuntimeException:-Could-not-find-any-configured-addresses-for-URI
Title: Spark Issue: RuntimeException: Could not find any configured addresses for URI
Category: Computer Science
Tags: Computer Science, programming, Spark, Spark issue, RuntimeException, URI, address

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> Caused by: java.lang.RuntimeException: Could not find any configured addresses for URI hdfs://apollo-router/

## Possible Causes

The Spark cluster to which the Spark application is submitted to 
is not well configured. 
If no HDFS prefix is provided for a HDFS path, 
the HDFS prefix `hdfs://apollo-router/` is used.
For example,
the HDFS path `/user/dclong` is recognized as `hdfs://apollo-router`.

## Possible Solutions

1. Ask Spark admin to fix the configuration issue.

2. Use a full HDFS path. 
    For example,
    assume `hdfs://cluster-name` is the correct prefix.
    Instead of `/user/dclong`,
    you can use `hdfs://cluster-name/user/dclong`.

