Status: published
Date: 2019-10-04 03:32:56
Author: Benjamin Du
Slug: tips-on-pyspark
Title: Tips on PySpark
Category: Programming
Tags: programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. You can run PySpark interactively using the `pyspark` command
  and submit a PySpark job to the cluster using the `spark-submit` command.
	For more details, 
	please refer to
	[Launching Applications with spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit<Paste>).


    :::Bash
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
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --conf spark.pyspark.driver.python=/usr/share/anaconda3/bin/python \
            --conf spark.pyspark.python=/usr/share/anaconda3/bin/python \
            /path/to/test_pyspark.py

    :::Python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName('Test PySpark').enableHiveSupport().getOrCreate()
    spark.sql("select * from some_table limit 5").write.mode("overwrite").parquet("output")


## References

[Managing dependencies and artifacts in PySpark](https://bytes.grubhub.com/managing-dependencies-and-artifacts-in-pyspark-7641aa89ddb7)
