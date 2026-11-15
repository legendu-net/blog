---
title: Tips on Scala
created: '2016-03-24T19:09:23-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: tips-on-scala
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - functional programming
  - big data
  - Spark
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

- [Scala Root Package](http://www.scala-lang.org/api/current/#package)
- [Scala Documentation](http://docs.scala-lang.org/index.html)
- [Scala Tutorial](http://docs.scala-lang.org/tutorials/)
- [Scala Coding Style](http://docs.scala-lang.org/style/)
- [Scala Glossary](http://docs.scala-lang.org/glossary/)
- [Scala Cheatsheet](http://docs.scala-lang.org/cheatsheets/)
- [Scala Style Guide](https://github.com/databricks/scala-style-guide)

## Trick & Traps

- [Scala and 22](https://underscore.io/blog/posts/2016/10/11/twenty-two.html)

## General Tips

1. IntelliJ IDEA is the recommended IDE.
   Eclipse (with the Scala IDE plugin) is alternative.

## Style

1. avoid using break, continue, return even though you can use them in Scala

1. avoid using while loop but don't go too crazy

## scala.util.Random

It is a wrapper of `java.util.Random` which is NOT a high quality random number generator.

## Argument Parsing

Scala Args Parsing

https://github.com/scopt/scopt

## Links

http://blog.plasmaconduit.com/reduve-vs-fold-in-scala/

http://stackoverflow.com/questions/9727637/new-keyword-in-scala

### Collections

http://docs.scala-lang.org/overviews/collections/overview.html

http://docs.scala-lang.org/overviews/collections/performance-characteristics.html

http://alvinalexander.com/scala/understanding-scala-collections-hierarchy-cookbook

http://stackoverflow.com/questions/19478244/how-does-a-case-anonymous-function-really-work-in-scala
