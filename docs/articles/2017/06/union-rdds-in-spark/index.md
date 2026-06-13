---
title: Union RDDs in Spark
created: '2017-06-03T23:49:38-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: union-rdds-in-spark
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - Spark
  - RDD
  - union
---

No deduplication is done (to be efficient) when unioning RDDs/DataFrames in Spark 2.1.0+.

1. Union 2 RDDs.

   ```
    df1.union(df2)
    // or for old-fashioned RDD
    rdd1.union(rdd_2)
   ```

1. Union multiple RDDs.

   ```
    df = spark.union([df1, df2, df3]) // spark is a SparkSession object
    // or for old-fashioned RDD
    rdd = sc.union([rdd1, rdd2, rdd3]) // sc is a SparkContext object
   ```

## References

[Union DataFrames in Spark](union-dataframes-in-spark)

[Union DataFrames in Spark](union-dataframes-in-spark)
