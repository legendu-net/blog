---
title: 'Spark Issue: Cannot Create a Path from an Empty String'
created: '2019-08-21T12:14:37-07:00'
date: '2026-08-11T22:19:29-07:00'
authors:
  - bendu
label: spark-issue-cannot-create-a-path-from-an-empty-string
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - empty string
  - path
  - error
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Issue

java.lang.IllegalArgumentException: Can not create a Path from an empty string

## Possible Causes

The error you are seeing could be from number of things:

1. parameters , check for \$\{param} in the code and make sure it has value

1. create external table with invalid path (path containing spaces or parameter that is null)

1. insert overwrite directory statement with invalid path.

## Solutions

Identify the root cause and fix accordingly.

## References

https://forums.aws.amazon.com/thread.jspa?threadID=132895
