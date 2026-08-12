---
title: 'Spark Issue: RuntimeError: Arrow Legacy IPC Format Is Not Supported'
created: '2022-04-03T19:07:14-07:00'
date: '2026-08-11T22:19:21-07:00'
authors:
  - bendu
label: spark-issue-runtimeerror-arrow-legacy-ipc-format-is-not-supported
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - PySpark
  - issue
  - error
  - exception
  - Arrow
  - legacy
  - IPC
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> RuntimeError: Arrow legacy IPC format is not supported in PySpark, please unset ARROW_PRE_0_15_IPC_FORMAT

## Possible Causes

You are using PySpark 3.0+ with one (or both) of the following options.

--conf spark.yarn.appMasterEnv.ARROW_PRE_0_15_IPC_FORMAT=1
--conf spark.executorEnv.ARROW_PRE_0_15_IPC_FORMAT=1

## Possible Solutions

PySpark 3.0+ has better built-in support of Arrow (compared to PySpark 2).
There's no need to configure `ARROW_PRE_0_15_IPC_FORMAT`.
Getting of the above options from your PySpark configuration should fix the issue.
