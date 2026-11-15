---
title: Tips on Spark MLlib
created: '2019-05-16T23:45:42-07:00'
date: '2026-11-15T12:20:35-08:00'
authors:
  - bendu
label: tips-on-spark-mllib
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - big data
  - MLlib
  - machine learning
  - AI
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Spark MLlib RDD-based API supports
   [stratified sampling](https://spark.apache.org/docs/latest/mllib-statistics.html#stratified-sampling)
   but the DataFrame-based API hasn't implemented it yet as of Spark 2.4.3.

sample keys (not rows) with equal probability

## References

https://spark.apache.org/docs/latest/ml-guide.html

https://spark.apache.org/docs/latest/ml-statistics.html
