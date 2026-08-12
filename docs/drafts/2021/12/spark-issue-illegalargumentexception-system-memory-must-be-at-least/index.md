---
title: 'Spark Issue: IllegalArgumentException: System Memory Must Be at Least'
created: '2021-12-05T13:02:47-08:00'
date: '2026-08-11T22:19:22-07:00'
authors:
  - bendu
label: spark-issue-illegalargumentexception-system-memory-must-be-at-least
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - IllegalArgumentException
  - heap size
  - memory
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

Exception in thread "main" java.lang.IllegalArgumentException: System memory 466092032 must be at least 471859200. Please increase heap size using the --driver-memory option or spark.driver.memory in Spark configuration.

## Causes

Not enough heap size (dirver memory).

## Solutions

Increase heap size using the `--driver-memory` option or `spark.driver.memory` in Spark configuration.
