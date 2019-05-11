Status: published
Date: 2019-05-11 01:59:02
Author: Benjamin Du
Slug: spark-issue-application-submission-is-not-finished
Title: Spark Application Submission Is Not Finished
Category: Programming
Tags: programming, Spark, big data, issue

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Error Message

> Application submission is not finished, submitted application application__1524215324275_0081 is still in ...

## Possible Causes

The Resource Manager needs to write too much data to ZooKeeper and hit the buffer limit.

## Solution

Ask the Spark Cluster admin to increase the ZooKeeper buffer limit.
