---
title: 'Spark Issue: Could Not Execute Broadcast in 300S'
created: '2022-01-22T11:11:13-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: spark-issue-could-not-execute-broadcast-in-300s
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - broadcast
  - broadcastTimeout
  - autoBroadcastJoinThreshold
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> Caused by: org.apache.spark.SparkException: Could not execute broadcast in 600 secs. You can increase the timeout for broadcasts via spark.sql.broadcastTimeout or disable broadcast join by setting spark.sql.autoBroadcastJoinThreshold to -1

## Possible Causes

1. Broadcast was too large or the network was slow which caused the boradcast to timeout.
   Notice that is usually a superficial cause instead of the deep root cause.

1. DataFrame caching failed due to failure of Spark nodes.
   If so,
   you will see other error message such as
   [block rdd_123_456 could not be removed as it was not found on disk or in memory](spark-issue-block-could-not-be-removed-as-it-was-not-found-on-disk-or-in-memory)
   .

## Possible Solutions

1. Increase the timeout for broadcast
   (e.g., `--conf spark.sql.broadcastTimeout=600s`)
   or totally disable broadcast join
   (e.g., `--conf spark.sql.autoBroadcastJoinThreshold=-1`)
   .
   Since broadcast timeout is usually a superficial cause,
   this is unlikely to fix the issue in the Spark application.
   However,
   it helps to eliminate one possible cause at least.

1. Refer to
   [block rdd_123_456 could not be removed as it was not found on disk or in memory](spark-issue-block-could-not-be-removed-as-it-was-not-found-on-disk-or-in-memory)
   for possible solutions.
