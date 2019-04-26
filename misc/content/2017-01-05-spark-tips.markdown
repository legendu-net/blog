Status: published
Date: 2019-04-26 02:45:41
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


## Spark Submit

1. After submitting a Spark application, 
    if the network connection get lots, 
    the Spark application submitted will be killed.
    You can nohup or tmux to submit your Spark application 
    so that loss of network connection won't kill your Spark application.
    Or another way is to just submit your Spark application
    from a server that has very stable network connection.


## Spark Shell

1. The `--jars` option of `spark-shell` can be used to add JAR dependencies.

2. `spark-shell` accepts `--queue` (for specifying the queue to submit jobs) as parameter!
    If you run `spark-shell` and encounter the issue of "ERROR SparkContext: Error initializing SparkContext" 
    due to "application submitted by user to unknown queue",
    you have to pass the queue that you can access to `spark-shell`.

        spark-shell --queue my_queue

## Spark Cluster Master URL

https://spark.apache.org/docs/latest/submitting-applications.html#master-urls


## References

https://developer.ibm.com/hadoop/2016/07/18/troubleshooting-and-tuning-spark-for-heavy-workloads/

http://blog.prabeeshk.com/blog/2014/10/31/install-apache-spark-on-ubuntu-14-dot-04/

http://mbonaci.github.io/mbo-spark/

http://www.simonouellette.com/blog/spark-join-when-not-to-use-it

https://bzhangusc.wordpress.com/2015/11/20/use-sbt-console-as-spark-shell/

https://spark-summit.org/2015/events/interactive-graph-analytics-with-spark/

https://www.slideshare.net/SparkSummit/understanding-memory-management-in-spark-for-fun-and-profit

