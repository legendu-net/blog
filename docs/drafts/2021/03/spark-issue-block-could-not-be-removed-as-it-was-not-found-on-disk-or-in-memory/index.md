---
title: 'Spark Issue: Block Could Not Be Removed as It Was Not Found on Disk or in Memory'
created: '2021-03-24T09:23:07-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: spark-issue-block-could-not-be-removed-as-it-was-not-found-on-disk-or-in-memory
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - block
  - remove
  - not found
  - disk
  - memory
  - big data
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

Block rdd_123_456 could not be removed as it was not found on disk or in memory.

## Cause

1. The execution plan of a DataFrame is too complicated.

1. Not enough memory to persist DataFrames
   (even if you used the default persist option `StorageLevel.MEMORY_AND_DISK`).

## Possible Solutions

1. Try triggering an eager DataFrame persist
   (by calling `DataFrame.count` after `DataFrame.persit`)
   .
   If you can stand some loss of performance,
   try using `DataFrame.checkpoint`
   instead of `DataFrame.persist`.
   For more discussions on DataFrame persist vs checkpoint,
   please refer to
   [Persist and Checkpoint DataFrames in Spark](persist-and-checkpoint-dataframes-in-spark)
   .

1. Increase executor memory (`--executor-memory`).
   If you persist DataFrame using the option `OFF_HEAP`,
   increase memory overhead.

1. Use the storage level which consumes less memory.
   For example,
   if you have been using the default storage level `StorageLevel.MEMORY_AND_DISK` (in PySpark 2)
   you can try `StorageLevel.MEMORY_AND_DISK_SER` or `StorageLevel.DISK_ONLY`.

1. Do not persist DataFrames (at the cost of lower performance).
   Notice that even if you persist DataFrames to disk only,
   you might still encounter this issue due to lack of disk space for caching.

1. Increase the number of partitions,
   which makes each partition smaller.

1. Increase the number of executors (`--num-executors`),
   which increases the total disk space for caching.

1. Reduce the number of cores per executor (`--execuor-cores`).

1. Ask Hadoop/Spark admin to increase local disk space for caching.
