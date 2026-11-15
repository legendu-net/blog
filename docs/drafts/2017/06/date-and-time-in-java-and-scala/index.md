---
title: Date and Time in Java and Scala
created: '2017-06-24T10:37:07-07:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: date-and-time-in-java-and-scala
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - Java
  - date
  - time
  - java.time
  - Joda time
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Use Joda time if you are using JDK \<= 7
and java.time if you are using JDK8 and above.

If you do prefer Scala libraries (when working in Scala),
https://github.com/nscala-time/nscala-time wrapper of Joda time

```
libraryDependencies += "com.github.nscala-time" %% "nscala-time" % "2.16.0"
```

https://github.com/reactivecodes/scala-time
wrapper of java.time

```
// Requires JDK 1.8 and above
"codes.reactive" %% "scala-time" % "0.4.1"
```
