Status: published
Date: 2019-08-21 12:14:37
Author: Benjamin Du
Slug: spark-issue-duplicated-partitions
Title: Spark Issue: Duplicated Partitions
Category: Computer Science
Tags: programming, Spark, issue, duplicate, overwrite, big data, Spark issue
Modified: 2021-03-21 12:14:37

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

There seems to be an issue in Spark that it might fail to overwrite files 
even if mode of `spark.write` is set to be "overwrite".
