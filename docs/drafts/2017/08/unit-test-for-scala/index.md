---
title: Unit Test for Scala
created: '2017-08-22T12:59:02-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: unit-test-for-scala
license: CC-BY-4.0
tags:
  - programming
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Both ScalaTest and spec2 are good unit testing frameworks.
   ScalaTest is more flexible is recommended.

## ScalaTest

only `assert` is supported.

```
:::bash
assert(expr1 === expr2, optional_msg)
```

The JUnit methods `assertTrue`, `assertEquals` and `assertArrayEquals`
are not supported by default.
You have to import them from JUnit if you want use them.

```
:::bash
import org.scalatest.junit.AssertionsForJUnit
import org.junit.Assert.{assertEquals, assertNotNull}
```

https://www.programcreek.com/scala/org.junit.Assert.assertEquals

http://www.scalatest.org/

Keep eyes on sbt-idea ...,
check whether a plugin for IntelliJ is available, ...

https://github.com/mpeltonen/sbt-idea

It seems that supersafe has issues with scala 2.12.2 ...

https://github.com/scalatest/scalatest/issues/1156

Try the following:

When we add the plug-in in `projects/build.sbt`:

```
addSbtPlugin("com.artima.supersafe" % "sbtplugin" % "1.1.2")
```

We must not add the above plug-in anywhere else

Add to `~/.sbt/0.13/global.sbt`

```
resolvers += "Artima Maven Repository" at "http://repo.artima.com/releases"
```

Do not add this resolver anywhere else

Make sure you have an empty line before and after each of the sbt lines

## Specs2

```
"org.specs2" % "specs2-core_2.11" % "3.7.2" % "test",

"org.specs2" % "specs2-mock_2.11" % "3.7.2" % "test"
```
