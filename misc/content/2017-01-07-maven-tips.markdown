UUID: f112de65-cdbc-4cc5-aa90-ab958d217bd5
Status: published
Date: 2017-03-24 23:51:16
Author: Ben Chuanlong Du
Slug: maven-tips
Title: Maven Tips
Category: Programming
Tags: programming, Maven, tips, Java, Scala

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

mvn package
$HOME/.m2
maven: shade plugin, scala compile plugin, exclude manifest files, ...

import as maven project ...
find an updated version of scala archetype for maven

mvn package  
mvn clean package  
mvn compile  
mvn build  
mvn -e build

intellij scala mavn archtype is too ooooooooooold!!! wait for generate complete and then manaully update the pom file

```XML
<plugin>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>2.0.2</version>
    <configuration>
        <source>1.6</source>
        <target>1.6</target>
    </configuration>
</plugin>
```

```XML
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <configuration>
         <mainClass>net.legendu.App</mainClass>
    </configuration>
</plugin>
```
