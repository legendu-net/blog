Status: published
Date: 2019-05-24 14:48:33
Author: Benjamin Du
Slug: spark-issue-too-large-table-for-auto-BroadcastHashJoin
Title: Spark Issue: Too Large Table for Auto BroadcastHashJoin
Category: Computer Science
Tags: programming, Spark, issue, big data, error, BroadcastHashJoin, broadcast, Spark issue
Modified: 2021-03-24 14:48:33

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptoms

### Symptom 1
16/04/17 11:17:36 ERROR scheduler.TaskSetManager: Total size of serialized results of 126 tasks (1137.3 MB) is bigger than spark.driver.maxResultSize (1024.0 MB)
16/04/17 11:17:36 ERROR yarn.ApplicationMaster: User class threw exception: org.apache.spark.SparkException: 
Job aborted due to stage failure: Total size of serialized results of 114 tasks (1029.0 MB) is bigger than spark.driver.maxResultSize (1024.0 MB)
org.apache.spark.SparkException: Job aborted due to stage failure: Total size of serialized results of 114 tasks (1029.0 MB) is bigger than spark.driver.maxResultSize (1024.0 MB)

### Symptom 2
16/04/17 11:23:15 INFO executor.Executor: Finished task 196.0 in stage 6.0 (TID 610). 9455052 bytes result sent to driver
16/04/17 11:23:46 WARN netty.NettyRpcEndpointRef: Error sending message [message = Heartbeat(157,[Lscala.Tuple2;@56be55da,BlockManagerId(157, 45017))] in 1 attempts
org.apache.spark.rpc.RpcTimeoutException: Futures timed out after [10 seconds]. This timeout is controlled by spark.executor.heartbeatInterval

 

## Cause

When the BroadcastHashJoin is executed, 
for some reason,
the driver clones N copies (N is the number of executors) of the broadcasted table size, 
(in my case: 75MB) 
and broadcast it to each executor. 
If the N is like 300, 
the total memory required for driver is at least: $75MB * 300 = 22.5GB$,
larger than the executor memory.
It will cause driver no-response (OOM).

## Solution

1. Do not use `BroadcastHashJoin`.

    - For SparkSQL (SQLContext): do not call the function `broadcast(obj)`.

    - For SparkSQL (HiveContext): set `spark.sql.autoBroadcastJoinThreshold=10MB` (or less)

    - For RDD: do not use broadcast variable

2. If one of the tables for joining contains too large number of partitions
    (which results in too many jobs),
    repartition it to reduce the number of partitions before joining.

## References 

https://issues.apache.org/jira/browse/SPARK-17556