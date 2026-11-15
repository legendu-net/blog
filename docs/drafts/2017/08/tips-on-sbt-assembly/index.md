---
title: Tips on sbt Assembly
created: '2017-08-22T15:03:24-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: tips-on-sbt-assembly
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - sbt
  - sbt-assembly
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Add sbt-assembly as a dependency in project/assembly.sbt:

```
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.5")
```

## References

[sbt-assembly on GitHub](https://github.com/sbt/sbt-assembly)

[Shade with SBT](http://manuzhang.github.io/2016/10/15/shading.html)

[Creating Scala Fat Jars for Spark on SBT with sbt-assembly Plugin](http://queirozf.com/entries/creating-scala-fat-jars-for-spark-on-sbt-with-sbt-assembly-plugin)
