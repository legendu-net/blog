---
title: Use Kotlin in a Scala Project
created: '2019-11-27T09:25:16-08:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: use-kotlin-in-a-scala-project
license: CC-BY-4.0
tags:
  - programming
  - JVM
  - Kotlin
  - Scala
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Methods of a Kotlin object can be called in a Scala project by `KotlinObject.INSTANCE.methodToCall()`

1. You might need to provide the Kotlin standard library `kotlin-stdlib.jar`
   in order to run the compiled JAR.
   One way to avoid this is to compile a fat/uber JAR
   that contains all dependencies (including `kotlin-stdlib.jar`).

##. Use Kotlin in Spark/Scala

http://tomstechnicalblog.blogspot.com/2016/11/using-kotlin-language-with-spark.html?m=1

https://thegmariottiblog.blogspot.com/2017/05/lets-make-apache-spark-more-kotlinesque.html
