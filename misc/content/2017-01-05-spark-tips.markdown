UUID: a85907ac-decf-4477-9a47-54086e01ca9b
Status: published
Date: 2017-10-22 13:43:04
Author: Ben Chuanlong Du
Slug: spark-tips
Title: Spark Tips
Category: Programming
Tags: programming, Spark, big data, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Sharing Variables

Spark supports two types of shared variables: broadcast variables, 
which can be used to cache a value in memory on all nodes, 
and accumulators, 
which are variables that are only “added” to, such as counters and sums.

## Spark Shell

spark-shell --jars ... to add jars and then you can use it!!!

spark-shell accepts --queue as parameter ...!!!

## Spark SQL

Spark SQL supports hive sql syntax.
For example,
`spark.sql("show tables in some_schema")` 
returns a DataFrame with tables in the Hive database.


## Spark Cluster Master URL

https://spark.apache.org/docs/latest/submitting-applications.html#master-urls


## Links

https://developer.ibm.com/hadoop/2016/07/18/troubleshooting-and-tuning-spark-for-heavy-workloads/

http://blog.prabeeshk.com/blog/2014/10/31/install-apache-spark-on-ubuntu-14-dot-04/

http://mbonaci.github.io/mbo-spark/

http://www.simonouellette.com/blog/spark-join-when-not-to-use-it

https://bzhangusc.wordpress.com/2015/11/20/use-sbt-console-as-spark-shell/

https://spark-summit.org/2015/events/interactive-graph-analytics-with-spark/



