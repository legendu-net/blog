Status: published
Date: 2020-02-20 12:02:58
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

1. Clone Spark 2.4.5.

    :::bash
    git clone --depth 1 --branch 2.4.5 https://github.com/apache/spark.git

2. Use Scala 2.11.

    :::bash
    ./dev/change-scala-version.sh 2.11

3. Run dev/make-distribution.sh

    :::bash
    ./dev/make-distribution.sh \
        --name hadoop2.7 \
        --tgz \
        -Pyarn \
        -Phive \
        -Phive-thriftserver \
        -Phadoop-2.7 \
        -Dhadoop.version=2.7.3 \
        -Dscala-2.11

4. Build Spark.
    
    :::bash
    ./build/mvn \
        -Pyarn \
        -Phive \
        -Phive-thriftserver \
        -Phadoop-2.7 \
        -Dhadoop.version=2.7.3 \
        -Dscala-2.11 \
        -DskipTests \
        clean package
