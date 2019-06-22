Status: published
Date: 2019-06-22 19:44:53
Author: Benjamin Du
Slug: spark-issue-too-many-containers-asked
Title: Spark Issue Too Many Containers Asked
Category: Programming
Tags: programming, Spark, issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Error Message

> org.apache.hadoop.yarn.exceptions.InvalidResourceRequestException: Too many containers asked, 16731530.

![image](https://user-images.githubusercontent.com/824507/57563512-99b88f80-7353-11e9-8993-aee9a302c209.png)

## Possible Causes

"Too many containers asked" is a protection mechanism of the Resource Manager.
It might be triggered when dynamic allocation is enabled.

## Solutions

1. Disable Spark dynamic allocation.

        --conf spark.dynamicAllocation.enabled=false

2. Limit Spark default parallelism (say, to 200).

        spark.default.parallelism
