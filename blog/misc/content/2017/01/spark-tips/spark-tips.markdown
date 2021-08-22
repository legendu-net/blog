Status: published
Date: 2017-01-05 23:55:46
Author: Ben Chuanlong Du
Slug: processing-big-data-using-spark
Title: Processing Big Data Using Spark
Category: Computer Science
Tags: programming, Spark, big data, tips
Modified: 2021-01-05 23:55:46

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## General Tips

1. Please refer to 
    [Spark SQL](http://www.legendu.net/misc/blog/spark-sql-tips/)
    for tips specific to Spark SQL.

2. It is almost always a good idea to filter out null value in the joinining columns before joining
    no matter it is an inner join or an outer join 
    (of course if the rows containing null matters in your use case, you have to do a union of those records).
    Spark (at least in Spark 2.3 and older) is stupid enough not to filter out joining keys/columns with null values before even INNER join
    (even if null values are dropped after inner join).
    This means that if a joining key/column has lots of null values, 
    it get shuffle into the same node in SortMergeJoin.
    This can cause a serious data skew issue.

3. When you join 2 tables and apply filtering conditions on those 2 tables, 
    it is suggested that you explictly use subqueries to filtering first and then do the join.
    (This is generally true for other SQL databases too.)

    - Explict is always better than implicit. 
        This makes sure that SQL do the filtering first before join
        rather than relying on the SQL engine optimization.

    - This makes things easier if you need to leverage Spark SQL hints.

2. It is always a good idea to check the execution plan of your Spark job 
    to make sure that things are as expected
    before you actually run it.

2. Before you use a HDFS table, 
    have a rough estimation of the tables size 
    and check the number of underlying files of the talbe.
    This helps you
        - have a rough idea of the complexity of the Spark job
        - get a idea of the rough number of tasks in the Spark job
        - decide the best number of shuffle partitions to use
    Notice that due to bad design,
    some HDFS table might have a huge number (more than 100k) of underlying files.
    This will causes your Spark job to have too many (small) tasks,
    which not only makes your Spark application run slow 
    but also might causes vairous issues such as 
    [Spark Issue: Total Size of Serialized Results Is Bigger than spark.driver.maxResultSize](http://www.legendu.net/misc/blog/spark-issues-total-size-bigger-than-maxresultsize/)
    and
    [Spark Issue: Too Large Table for Auto BroadcastHashJoin](http://www.legendu.net/misc/blog/spark-issue-too-large-table-for-auto-BroadcastHashJoin/)
    .

2. When you select columns from a table (or from joining of multiple tables),
    it is always a good idea to include partition/bucket columns in the final output.

1. If you have a really large Spark job which fails with high chance due too large complexity,
    you can check whether there are independent sub jobs in the big job.
    If so,
    it is often a good idea to submit separate Spark applications for each independent sub jobs.
    One typical example is when you do a large simulation. 
    Each iterator in the simulation can be seen as an independent job (of other iterators).
    If the whole simulation is too large and fails with high chance,
    you can break down the simulation into smaller piece.
    One useful trick is to use hash and/or modulus to help you cut the large job into smaller and reproducible ones. 
    You can then submit a Spark application for each of the smaller jobs.
    The advantage of this approach is 2 fold.
    First, 
    each of the smaller jobs can run reliably and have a much higher chance to suceed. 
    Second, 
    shall any of the smaller jobs fail, 
    you run rerun that specific job (this is why reproducible is important) instead of rerunning the whole large simulation.

2. It is suggested that you always call `spark.stop()` 
    when the SparkContext object is no longer needed (typically at the end of your Spark/PySpark application).
    This helps reduce the weird issue that all your output is written to the cluster successfully 
    but your Spark applications fails.
    For more discussions, 
    please refer to http://apache-spark-user-list.1001560.n3.nabble.com/SparkContext-stop-td17826.html.

## Sharing Variables

Spark supports two types of shared variables: broadcast variables,
which can be used to cache a value in memory on all nodes,
and accumulators,
which are variables that are only “added” to, such as counters and sums.


## Spark Submit

1. All the options `--files`, `--jars` and `--archives` 
    support both local files and remote files on HDFS. 
    
1. After submitting a Spark application, 
    if the network connection get lots, 
    the Spark application submitted will be killed.
    You can nohup or tmux to submit your Spark application 
    so that loss of network connection won't kill your Spark application.
    Or another way is to just submit your Spark application
    from a server that has very stable network connection.

3. Best to use the JVM option `-XX:MaxDirectMemorySize` to limit the maximum directory memory used.
    This helps avoid the issue of memory exceding limit.

        :::bash
        --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G \

2. If you are sure that your Spark application is production ready,
    it is better to submit it with the option `--deploy-mode cluster`.
    However the default option (`--deploy-mode client`) is good for debugging.
    And also, `--deploy-mode client` is much faster to submit generally speaking.
    It is suggested that you use `--deploy-mode client` for ad hoc Spark applications
    and `--deploy-mode cluster` for production ready applications that need to be run many times.

        :::bash
        #!/bin/bash
        /apache/spark2.3/bin/spark-submit \
            --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
            --master yarn \
            --deploy-mode cluster \
            --queue your_queue \
            --num-executors 200 \
            --executor-memory 10G \
            --driver-memory 15G \
            --executor-cores 4 \
            --conf spark.yarn.maxAppAttempts=2 \
            --conf spark.dynamicAllocation.enabled=true \
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G \
            --class your.package.SomeClass \
            --jars /path/to/jar/dependencies \
            /path/to/compiled/jar arg1 arg2 ...

    If you have used Kotlin in your Spark application,
    you need to include `kotlin-stdlib.jar` via the `--jars` option.

        :::bash
        #!/bin/bash
        /apache/spark2.3/bin/spark-submit \
            --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
            --master yarn \
            --deploy-mode cluster \
            --queue your_queue \
            --num-executors 200 \
            --executor-memory 10G \
            --driver-memory 15G \
            --executor-cores 4 \
            --conf spark.yarn.maxAppAttempts=2 \
            --conf spark.dynamicAllocation.enabled=true \
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G \
            --class your.package.SomeClass \
            --jars /path/to/kotlin-stdlib.jar \
            /path/to/compiled/jar arg1 arg2 ...

## Spark Shell

1. The `--jars` option of `spark-shell` can be used to add JAR dependencies.

2. `spark-shell` accepts `--queue` (for specifying the queue to submit jobs) as parameter!
If you run `spark-shell` and encounter the issue of "ERROR SparkContext: Error initializing SparkContext" 
due to "application submitted by user to unknown queue",
you have to pass the queue that you can access to `spark-shell`.

        :::bash
        spark-shell --queue my_queue

## Spark Cluster Master URL

https://spark.apache.org/docs/latest/submitting-applications.html#master-urls


## References

[awesome-spark](https://github.com/awesome-spark/awesome-spark)

https://developer.ibm.com/hadoop/2016/07/18/troubleshooting-and-tuning-spark-for-heavy-workloads/

http://blog.prabeeshk.com/blog/2014/10/31/install-apache-spark-on-ubuntu-14-dot-04/

http://mbonaci.github.io/mbo-spark/

http://www.simonouellette.com/blog/spark-join-when-not-to-use-it

https://bzhangusc.wordpress.com/2015/11/20/use-sbt-console-as-spark-shell/

https://spark-summit.org/2015/events/interactive-graph-analytics-with-spark/

https://www.slideshare.net/SparkSummit/understanding-memory-management-in-spark-for-fun-and-profit

http://apache-spark-user-list.1001560.n3.nabble.com/SparkContext-stop-td17826.html

