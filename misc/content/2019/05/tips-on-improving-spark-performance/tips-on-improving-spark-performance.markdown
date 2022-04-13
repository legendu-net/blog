Status: published
Date: 2019-05-05 09:10:38
Author: Benjamin Du
Slug: improve-spark-performance
Title: Improve the Performance of Spark
Category: Computer Science
Tags: programming, Computer Science, Spark, tuning, Spark SQL, SQL, performance, database, big data
Modified: 2022-04-12 17:56:58


**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Plan Your Work

1. Have a clear idea about what you want to do is very important, 
    especially when you are working on an explorative project. 
    It often saves you time to plan your work a little 
    before jumping into it.

## Data Storage

1. Use Parquet as the data store format.
    While Spark/Hive supports many different data formats, 
    Parquet is the optimal data format to use.
    When creating a Hive table, 
    use the Spark SQL syntax to create a Spark-based Parquet format instead of Hive-based Parquet format.
    That is you use a query like

        :::sql
        CREATE TABLE table_name (id Int, name String) USING Parquet
    
    instead of 

        :::sql
        CREATE TABLE table_name (id Int, name String) STORE AS Parquet
    
    or

        :::sql
        CREATE TABLE table_name (id Int, name String)

    The last 2 SQL queries uses Hive-based Parquet format 
    which might not benefit from some Spark execution optimizations.

2. Use partition or bucket columns on large tables.
    For more details discussions,
    please refer to
    [Partition and Bucketing in Spark](http://www.legendu.net/misc/blog/partition-bucketing-in-spark)
    .

## SQL Query / DataFrame API

1. Accelerate table scan by adding proper filter conditions.
    Use proper filter conditions in your SQL statement to avoid full table scan. 
    Proper filter conditions on Partition, Bucket and Sort columns 
    helps Spark SQL engine to fast locate target dataset to avoid full table scan,
    which accelerates execution.

2. Several smaller queries (achieving the same functionality) is preferred to 
    a big query (using complex features and/or subqueries).
    For example,
    `window_function(...) over (partition by ... order by ...)` 
    can be achieved using a `group by` followed with a inner join.
    The latter approach (using `group by` + `inner join`) runs faster in Spark SQL generally speaking.

3. Be cautious about the method `RDD.collect` as it retrieves all data in an RDD/DataFrame to the driver.
    This will likely cause an out-of-memory issue if the RDD/DataFrame is big.
    Even if not, 
    it will make your Spark application run slowly.


### Reduce (Unnecessary) Data Before Computation

1. Apply filtering conditions to keep only needed columns and rows.

2. Prefer the method `reduceByKey` over the method `groupByKey` when aggregating a RDD object in Spark.

### Using Cache / Persist

1. Persist a DataFrame which is used multiple times and expensive to recompute.
    Remembe to unpersist it too when the DataFrame is no longer needed. 
    Even Spark evict data from memory using the LRU (least recently used) strategy
    when the caching layer becomes full,
    it is still beneficial to unpersist data as soon as it is no used any more to reduce memory usage.

2. Spark DataFrame is lazily computed but computed again if needed.
    It can greatly boost the perfromance of your Spark application
    if you cache/persist the intermediate Spark DataFrame 
    which is used in mutliple places.
    Notably,
    if a Spark DataFrame containing randomly generately values
    and is used in multiple places,
    you must cache/persist it to ensure the correct logic
    (otherwise the DataFrame will have different values each time it is used).

### Optimize Joins

1. Spark automatically decides 
    which kind of joins (Broadcast Join, Sort Merge Join, Bucket Join) to perform. 
    Generally speaking,
    you should not change the default threshold for deciding which join to use.
    However,
    you should hint/help Spark to use the right join when applicable.

    - Do NOT split a medium sized table and boradcast each splitted part. 
        Just let Spark pick the right join (which will be the Sort Merge Join) in this case.
        Also notice that the splitting tricky might not work in non-inner joins.

    - BroadcastHashJoin, i.e., map-side join is fast. 
        Use BroadcastHashJoin if possible. 
        Notice that BroadcastHashJoin only works for inner joins. 
        If you have a outer join,
        BroadcastHashJoin won't happend even if you explicitly Broadcast a DataFrame.

    - Notice that BroadcastJoin only works for inner joins. 
        If you have a outer join,
        BroadcastJoin won't happend even if you explicitly Broadcast a DataFrame.

3. Make sure that keys to join in Spark DataFrames have the same type!
    When joining 2 large DataFrames in Spark, 
    Bucket Join is usually the best approach.
    However, 
    if the keys in the 2 DataFrame have inconsistent types 
    the bucket table will do a type cast 
    which makes Spark think the value of the original column 
    is not enough resulting in Sort Merge Join (instead of Bucket Join).

4. Add cast for join key to use bucket

    Joining columns of different types prevents Spark SQL from doing the best optimization.
    A simple fix is to cast columns to be the same type when joining them.
    For example,
    let's assume `A.id` is `Decimal(18, 0)` 
    and `B.id` is `BigInt`.
    Use

        SELECT 
            A.* 
        FROM
            A
        INNER JOIN 
            B
        ON 
            cast(A.id AS BigInt) = B.id 

    instead of

        SELECT 
            A.* 
        FROM
            A
        INNER JOIN 
            B
        ON 
            A.id = B.id 


## Size of Tasks in a Spark Application 

1. Best to have tasks each of which can be finished in a few minutes. 
    Having long running tasks (>30 minutes) 
    will likely degrade the performance of the whole application.

2. 100K is the ball park of upper limit of number of tasks. 
    If you have an application which has more than 100k (very small) tasks, 
    the performance is degraded. 
    However, 
    having too few tasks reduces the parallelism 
    and might hurt the performance of your Spark application too. 
    Generally speaking,
    it is safe to keep the number of tasks to 3k - 100k. 
    If you are unsure, 10k is a good start point. 

## Execuation Plan

1. Avoid having too large execution plans. 
    Specially, 
    avoid mixing repartition/coalesce with other execution plans. 
    Better to do a cache/checkpoint (or manually write data to disk) 
    before you do repartition/coalesce. 

## Data Serialization

According to https://spark.apache.org/docs/latest/tuning.html#data-serialization,
Spark 2.0.0+ internally uses the Kryo serializer 
when shuffling RDDs with simple types, arrays of simple types, or string type 
and Spark automatically includes Kryo serializers for the many commonly-used core Scala classes 
covered in the AllScalaRegistrar from the Twitter chill library. 
So unless one uses customized classes inside RDD/DataFrame, 
there is little benefit to switch to kryo for serialization.
When you do use customized classes and/or complicated nested data structures in big DataFrames, 
you might want to consider using the Kryo serializer.

## Tune Spark Job Configurations

[Part 3: Cost Efficient Executor Configuration for Apache Spark](https://medium.com/expedia-group-tech/part-3-efficient-executor-configuration-for-apache-spark-b4602929262)

[How to control the parallelism of Spark job](http://www.openkb.info/2018/06/how-to-control-parallelism-of-spark-job.html)

[How does Spark achieve parallelism within one task on multi-core or hyper-threaded machines](https://stackoverflow.com/questions/36671644/how-does-spark-achieve-parallelism-within-one-task-on-multi-core-or-hyper-thread)


### Dynamic Allocation
1. Enable dynamic allocation but with a limit on the max number of executors.

        :::bash
        ...
        --conf spark.dynamicAllocation.enabled=true \
        --conf spark.dynamicAllocation.maxExecutors=1000 \
        ...

### AQE in Spark 3+
1. Enable adaptive query execution in Spark 3.0+.

        :::bash
        ...
        --conf spark.adaptive.query.execution=true \
        ...

### Speculation
3. Generally speaking, 
    it is not a good idea to turn on **speculation** in Spark. 
    The reason is that is is usually very tricky to define "slowness".
    There are 3 levels of time out: process -> node -> rack
    through `spark.locality.wait.<level_name>`.
    The default setting is 3s in the global timeout setting (`spark.locality.wait`)
    which is comparatively too short in shared computer clusters in many companies.

### `spark.task.cpus` vs `spark.executor.cores`	
1. The default value of `spark.task.cpus` is 1. 
    When a value greater than 1 is set,
    it allows multithreading inside each task. 
    The option `spark.task.cpus` interacts with `spark.executor.cores`
    (alias of `--executor-cores`)
    to control the number of parallel tasks in each executor.
    Let `k = spark.executor.cores / spark.tasks.cpus` (integer division),
    then at most `k` tasks will run in parallel in each executor.
    If `spark.executor.cores` is not a multiple of `spark.task.cpus`,
    then `r = spark.executor.cores % spark.tasks.cpus` virtual cores
    are wasted in each executor.
    So,
    you should always set `spark.executor.exores`
    to be a multiple of `spark.executor.cores`.

2. Generally speaking,
    you should avoid having big tasks and then try to leveraging multithreading to speed up each tasks. 
    Instead,
    you should have smaller single-threaded tasks 
    and leverage Spark for parallism.

3. Multhreading does not seem to work if you call a shell command 
    (which supports multithreading)
    from PySpark 
    even if you set `spark.task.cpus`
    to be greater than 1!

## UDFs vs map/flatMap

1. Most spark operations are column-oriented. 
    If you want to do some operation that is hard to expression as column expressions
    but is rather very easy to express as row expressions,
    you can either use UDFs or the `map`/`flatMap` methods.
    Currently, 
    the methods `map`/`flatMap` of DataFrame are still experimental
    so you'd use UDFs at this time.

## When to Reshuffle

1. Situations (e.g., merging small files or splitting huge files) 
    that requires explicitly increasing or decreasing the number of RDD partiitons.

2. Before multiple bucket joins, it is usually benefical to repartition DataFrames by the same key.

[Cost Based Optimizer in Apache Spark 2.2](https://databricks.com/blog/2017/08/31/cost-based-optimizer-in-apache-spark-2-2.html)

## References

[Tuning Spark](https://spark.apache.org/docs/latest/tuning.html)

https://github.com/databricks/spark-knowledgebase

