Status: published
Date: 2020-08-22 08:53:56
Author: Benjamin Du
Slug: A-comprehensive-list-of-issues-in-spark-applications
Title: A Comprehensive List of Common Issues in Spark Applications
Category: Computer Science
Tags: Computer Science, Spark, issue, big data, error, Spark issue
Modified: 2021-12-05 14:28:31

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## List of Common Issues 

Please refer to 
<http://www.legendu.net/misc/tag/spark-issue.html>
for a comprehensive list of Spark Issues and (possible) causes and solutions.

## Debugging Tips 

### Spark/Hadoop Applications UI

1. The `Jobs` tab (default) to check jobs stages, number of jobs, etc. 

2. The `Environment` tab contains information about environment variables 
    and Spark configurations.  
    It is helpful if you forget configurations set for your Spark application
    or if you want to confirm that configurations for your Spark application are correct.

2. The `SQL` tab contains all Spark SQLs in your Spark application.
    you can click on each SQL to see visualization of its execuation plans.
    This visualiation of execuation plan has more information than the one in the `Jobs` tab.
    Notice that statistics after each stage will be update in this visualiation
    as the Spark application runs.
    This is extremely helpful for 
        - identifying unexpected behaviors of Spark job
        - better understanding of complexity of your Spark job 
        - tuning parameters to speed up your Spark application 

### Debug Your Spark Application 

Below a few things to check while you debug your Spark applications.

1. Make sure the number of tasks is as expected. 

2. Check the execution plan of your Spark job to make sure the join type is as expected. 
    This is critical for improve the performance of your Spark application.
    For example, 
    you might expect Spark to use BroadcastHashJoin but it actually used SortMergeJoin.

## Tips on Spark Configuration to Avoid Issues 

1. It is suggested that you keep `--driver-memory` to be at least `2G`.

2. If you are not sure, 
    keep `--executor-cores` to be less than 4. 
    For debugging purpose, 
    it is better to reduce `--executor-cores` to be 1.

3. Set a large value for `MaxDirectoMemorySize` for JVM.

        :::bash
        --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G \
