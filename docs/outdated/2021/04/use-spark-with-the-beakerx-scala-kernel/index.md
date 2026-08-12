---
title: Use Spark with the BeakerX Scala Kernel
created: '2021-04-23T17:23:46-07:00'
date: '2026-08-11T22:19:32-07:00'
authors:
  - bendu
label: use-spark-with-the-beakerx-scala-kernel
license: CC-BY-4.0
tags:
  - computer science
  - Spark
  - Scala
  - BeakerX
  - JupyterLab
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Open a JupyterLab notebook with the BeakerX Scala kernel from the launcher.

1. Download Spark (say, 2.3.1) dependencies.

   ```
    :::scala
    %%classpath add mvn
    org.apache.spark spark-core_2.11 2.3.1
    org.apache.spark spark-sql_2.11 2.3.1
   ```

1. Create a SparkSession object.

   ```
    :::scala
    import org.apache.spark.sql.SparkSession
    import org.apache.spark.sql.functions._

    val spark = SparkSession.builder()
        .master("local[2]")
        .appName("Spark Example")
        .config("spark.some.config.option", "some-value")
        .getOrCreate()

    import spark.implicits._
   ```

1. Use Spark as usual.

   ```
    :::scala
    val df = Range(0, 10).toDF
    df.show
   ```
