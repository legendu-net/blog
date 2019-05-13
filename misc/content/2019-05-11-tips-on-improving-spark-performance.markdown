Status: published
Date: 2019-05-13 21:30:05
Author: Benjamin Du
Slug: tips-on-improving-spark-performance
Title: Tips on Improving Spark Performance
Category: Programming
Tags: programming, Spark, performance, tuning

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


1. Prefer the method `reduceByKey` over the method `groupByKey` when aggregating a RDD object in Spark.

2. Be cautious about the method `RDD.collect` as it retrieves all data in an RDD/DataFrame to the driver.
    This will likely cause an out-of-memory issue if the RDD/DataFrame is big.
    Even if not, 
    it will make your Spark application run slowly.


## References

[Tuning Spark](https://spark.apache.org/docs/latest/tuning.html)

https://github.com/databricks/spark-knowledgebase

