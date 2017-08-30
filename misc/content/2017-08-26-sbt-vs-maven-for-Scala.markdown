UUID: 3dc04113-32f3-4587-a2b4-7f2e73174229
Status: published
Date: 2017-08-26 20:26:44
Author: Ben Chuanlong Du
Slug: sbt-vs-maven-for-Scala
Title: sbt vs Maven for Scala
Category: Programming
Tags: programming, Scala, sbt, Maven

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

http://www.hammerlab.org/2017/04/06/scala-build-tools/


1. sbt is recommended over Maven for developing Scala, 
generally speaking. 
First, 
sbt is better supported in IntelliJ IDEA. 
The Maven archetype for Scala is too old in IntelliJ.
You have to update the file pom.xml immediately after you create a Maven based Scala project in IntelliJ IDEA.

[sbt-pom-reader](https://github.com/sbt/sbt-pom-reader)
