Status: published
Date: 2021-10-10 23:58:37
Modified: 2021-11-29 00:16:00
Author: Benjamin Du
Slug: rust-and-spark
Title: Rust and Spark
Category: Computer Science
Tags: Computer Science, programming, Rust, Spark, big data, distributed, PySpark, pandas_udf, Shell, subprocess

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


The simplest and best way is to leverage `pandas_udf` in PySpark.
In the pandas UDF, 
you can call `subprocess.run` to run any shell command 
and capture its output.



[Spark and Rust - How to Build Fast, Distributed and Flexible Analytics Pipelines with Side Effects](https://blog.phylum.io/spark-and-rust-how-to-build-fast-distributed-and-flexible-analytics-pipelines)

RDD's have a relatively little-known method, pipe(). It isn't documented in depth, but it is deceptively simple. It will pipe the RDD's contents into the stdin of a provided command and read back its stdout as an RDD of strings. The documentation mentions it would be suited for "Perl or bash script(s)", but nobody is stopping us from doing different things as long as we respect that protocol!


