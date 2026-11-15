---
title: Run JAR Applications
created: '2017-08-22T12:17:00-07:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: run-jar-applications
license: CC-BY-4.0
tags:
  - programming
  - Java
  - JAR
  - main
---

If there is only 1 class with a main method
or if there is a Main-Class defined for the JAR,
you can use the following command to run the application.

```
java -jar app.jar
```

If you there are multiple classes with main methods in the JAR,
you can execute any of them using the commands below.

```
java -cp app.jar com.mycomp.myproj.AnotherClassWithMainMethod
```
