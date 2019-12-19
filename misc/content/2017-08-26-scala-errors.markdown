Status: published
Date: 2019-12-19 00:00:59
Author: Ben Chuanlong Du
Slug: scala-errors
Title: Scala Errors
Category: Programming
Tags: programming, Scala, error, issue, version

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. Java Version Issue

Unsupported major minor version 

https://stackoverflow.com/questions/22489398/unsupported-major-minor-version-52-0



## java.lang.NoSuchMethodError: scala.Product.$init$

> Fixing the Scala error: java.lang.NoSuchMethodError: scala.Product.$init$

It probably means 
This error is likely due to that you have a mismatch in the Scala versions 
you are using in your project. 
For example, 
I was using Scala 2.11 but mistakely specified Scala 2.12 for `scala_xml` for testing.
It is suggested that you never hardcode Scala versions but instead define Scala versions (full version and compact version) 
in variables and use the version variables when specifying dependencies.

https://alvinalexander.com/misc/fixing-scala-error-java-lang.nosuchmethoderror-scala.product-init