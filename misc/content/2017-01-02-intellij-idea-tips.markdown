UUID: f7982e28-2aa2-4829-ab77-2c8904408b1b
Status: published
Date: 2017-08-26 20:25:35
Author: Ben Chuanlong Du
Slug: intellij-idea-tips
Title: Intellij Idea Tips
Category: Software
Tags: software, IDE, IntelliJ IDEA, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. The first scala project might very long time to generate the directories 
depending on your network speed. 
SBT needs to download some JARs and when the download is complete, 
it will generate the `src` directory.
It suggests that you work in environment with good network connection
when using IntelliJ.


2. sbt (rather than Maven) is required if you want to use Scala worksheet in IntelliJ IDEA. 
You might see the following error if Maven is use.

        scalac error: bad option: '-make:transitive' on mvn package via command line

As a matter of fact, 
sbt is recommended over Maven for developing Scala, 
generally speaking. 
First, 
sbt is better supported in IntelliJ IDEA. 
The Maven archetype for Scala is too old in IntelliJ.
You have to update the file pom.xml immediately after you create a Maven based Scala project in IntelliJ IDEA.


## Scala Project Using Maven in IntelliJ

https://www.ivankrizsan.se/2016/03/27/creating-a-scala-project-with-maven-dependency-management-for-gatling-testing-in-intellij-idea/



## Reload Dependencies

https://stackoverflow.com/questions/20413605/how-to-force-intellij-idea-to-reload-dependencies-from-build-sbt-after-they-chan

## Use ScalaTest 

http://www.scalatest.org/user_guide/using_scalatest_with_intellij


## Questions

1. how to port intellij configuration files from one machine to another one?

2. how to pop up auto completion suggestions while typing?


