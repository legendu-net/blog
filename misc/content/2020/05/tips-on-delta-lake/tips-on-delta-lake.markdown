Status: published
Date: 2020-05-19 19:49:16
Author: Benjamin Du
Slug: tips-on-delta-lake
Title: Tips on Delta Lake
Category: Computer Science
Tags: Computer Science, big data, Spark, delta lake, Databricks
Modified: 2021-09-20 11:12:54

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

![Delta Lake](https://miro.medium.com/max/1400/1*EQsNOZqNPsx5eelVJRh9jQ.png)

## Delta Table 

convert to delta [db_name.]table_name
[partitioned by ...]
[vacuum [retain number hours]]

vaccum 

describe history db_name.table_name

can select from historical snapshot 
can also rollback to a historical snapshot 
rollback is kind of dangerous as once rollback,
commits after the rollback version are remove so that you cannot undo the rollback!



## References 

[Delta Lake PySpark Examples](https://github.com/delta-io/delta/tree/master/examples/python)

[Delta Lake在eBay的实践：Spark SQL增删改查](https://www.slidestalk.com/w/137)

[Table Deletes, Updates, and Merges](https://docs.delta.io/0.4.0/delta-update.html)

[Delta lake , ACID transactions for Apache Spark](https://medium.com/@achilleus/delta-lake-acid-transactions-for-apache-spark-2bf3d919cda)

[Delta Lake quickstart](https://docs.databricks.com/delta/quick-start.html)

[Table batch reads and writes](https://docs.delta.io/0.7.0/delta-batch.html#create-a-table)

[Table deletes, updates, and merges](https://docs.delta.io/0.7.0/delta-update.html)

[Presto and Athena to Delta Lake integration](https://docs.delta.io/0.7.0/presto-integration.html#step-3-update-manifests)
