---
title: Use Spark with Apache Toree Kernel in Juptyerlab
created: '2020-03-23T17:47:21-07:00'
date: '2026-08-11T22:19:26-07:00'
authors:
  - bendu
label: use-spark-with-apache-toree-kernel-in-juptyerlab
license: CC-BY-4.0
tags:
  - computer science
  - Spark
  - Scala
  - Apache Toree
  - JupyterLab
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The Docker image
[dclong/jupyterhub-toree](https://github.com/dclong/docker-jupyterhub-toree)
has Spark and Apache Toree installed and configured.
Since Spark is already installed in it,
you don't need to download and install Spark by yourself.
By default,
a Spark Session object named `spark` is created automatically just like spark-shell.
So, you can use Spark/Scala out-of-box in a JupyterLab notebook with the `Scala - Apache Toree` kernel.

1. Open a JupyterLab notebook with the `Scala - Apache Toree` kernel from the launcher.

1. Use Spark as usual.

   ```
    :::scala
    val df = Range(0, 10).toDF
    df.show
   ```
