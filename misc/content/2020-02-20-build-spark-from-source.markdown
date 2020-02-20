Status: published
Date: 2020-02-20 11:51:29
Author: Benjamin Du
Slug: build-spark-from-source
Title: Build Spark from Source
Category: Programming
Tags: programming, Spark, big data, build, source

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

https://spark.apache.org/docs/latest/building-spark.html

    :::bash
    ./dev/change-scala-version.sh 2.11
    ./dev/make-distribution.sh --name hadoop2.7 --tgz -Pyarn -Phive -Phive-thriftserver -Phadoop-2.7 -Dhadoop.version=2.7.3 -Dscala-2.11
    ./build/mvn -Pyarn -Phive -Phive-thriftserver -Phadoop-2.7 -Dhadoop.version=2.7.3 -Dscala-2.11 -DskipTests clean package
