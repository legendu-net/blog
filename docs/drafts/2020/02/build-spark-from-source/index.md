---
title: Build Spark from Source
created: '2020-02-20T16:25:13-08:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: build-spark-from-source
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - big data
  - build
  - source
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can download prebuilt binary Spark at
https://spark.apache.org/downloads.html.
This is where you should get started
and it will likely satisfy your need most of the time.
However,
below are instructions on how to build Spark from source if you have to.

https://spark.apache.org/docs/latest/building-spark.html

1. Clone Spark 2.4.5.

   ```
    :::bash
    git clone --depth 1 --branch 2.4.5 https://github.com/apache/spark.git
   ```

1. Use Scala 2.11.

   ```
    :::bash
    ./dev/change-scala-version.sh 2.11
   ```

1. Run dev/make-distribution.sh

   ```
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
   ```

1. Build Spark.

   ```
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
   ```

   This will generate a `Spark-2.4.5-*.tgz` file that you use to deploy.
   Just copy it to your Spark client and unzip it to the right location.

1. If you are building Spark for using in your company,
   you probably need to replace the directory `conf`
   with the customized one for your company.
