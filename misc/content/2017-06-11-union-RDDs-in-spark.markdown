UUID: bbf469f4-c773-4ff9-a7e1-0e43d8fbad10
Status: published
Date: 2017-06-11 11:09:53
Author: Ben Chuanlong Du
Slug: union-RDDs-in-spark
Title: Union Rdds in Spark
Category: Programming
Tags: programming, Scala, Spark, RDD, union

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


No deduplication is done (to be efficient) when unioning RDDs.

1. Union 2 RDDs.

```scala
rdd1.union(rdd_2)
```

2. Union multiple RDDs.
```scala
rdd = sc.union([rdd1, rdd2, rdd3])
```
