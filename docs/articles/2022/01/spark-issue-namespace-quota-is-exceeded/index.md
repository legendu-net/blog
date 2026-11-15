---
title: 'Spark Issue: Namespace Quota Is Exceeded'
created: '2022-01-06T22:33:54-08:00'
date: '2026-11-15T09:17:13-08:00'
authors:
  - bendu
label: spark-issue-namespace-quota-is-exceeded
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - NSQuotaExceededException
  - namespace
  - quota
  - big data
---

## Symptom

> Caused by: org.apache.hadoop.hdfs.protocol.NSQuotaExceededException: The NameSpace quota (directories and files) of directory /user/user_name is exceeded: quota=163840 file count=163841

## Cause

The namespace quota of the directory `/user/user_name` is exceeded.

## Solutions

1. Remove non-needed files from the directory `/user/user_name` to release some namespace quota.

1. As a long-term solution,
   you can also try to apply for more resource for the HDFS directory `/user/user_name`.
