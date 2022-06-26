Status: published
Date: 2022-03-27 17:24:15
Modified: 2022-03-31 18:35:29
Author: Benjamin Du
Slug: spark-issue:-RuntimeException:-Could-not-find-any-configured-addresses-for-URI
Title: Spark Issue: RuntimeException: Could not find any configured addresses for URI
Category: Computer Science
Tags: Computer Science, programming, Spark, Spark issue, RuntimeException, URI, address, RBF, router-based federation, namenode

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> Caused by: java.lang.RuntimeException: Could not find any configured addresses for URI hdfs://clustername-router/

## Possible Causes

This is due to missing `clustername-router` settings in the property `dfs.nameservices` in `hdfs-site.xml`.
It happens when HDFS migrates to router-based federation (RBF)
but the Hadoop client (which is used to submit the Spark application)
is not updated accordingly.

## Possible Solutions

Ask Hadoop admin to fix the configuration issues.

