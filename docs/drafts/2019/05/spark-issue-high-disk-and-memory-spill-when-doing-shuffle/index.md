---
title: 'Spark Issue: High Disk and Memory Spill When Doing Shuffle'
created: '2019-05-24T15:08:21-07:00'
date: '2026-11-15T09:23:42-08:00'
authors:
  - bendu
label: spark-issue-high-disk-and-memory-spill-when-doing-shuffle
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - big data
  - error
  - memory
  - disk
  - spill
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

High disk and memory spill when doing shuffle.

## Cause

Insufficient executor memory (you can monitor this spill metrics from Spark UI).

## Solution

1. Increase executor memory.

   ```
    ::bash
    --executor-memory=4G
   ```

1. For jobs that do not need to persist data in memory
   we can reduce the cache storage size and enlarge the memory portion for shuffle.

   ```bash
   --conf spark.shuffle.memoryFraction=0.4
   --conf spark.storage.memoryFraction=0.1
   ```
