UUID: f112de65-cdbc-4cc5-aa90-ab958d217bd5
Status: published
Date: 2017-05-24 20:24:40
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

[The Central Repository](http://search.maven.org/#search)

$HOME/.m2
maven: shade plugin, scala compile plugin, exclude manifest files, ...

import as maven project ...
find an updated version of scala archetype for maven

```sh
mvn package  
mvn clean package  
mvn compile  
mvn build  
mvn -e build
```

intellij scala mavn archtype is too ooooooooooold!!! wait for generate complete and then manaully update the pom file

```XML
<dependency>
    <groupId>org.scalaz</groupId>
    <artifactId>scalaz-core_2.11</artifactId>
    <version>7.2.12</version>
</dependency>
```
```XML
<dependency>
  <groupId>com.ebay.scalaplatform</groupId>
  <artifactId>platform-spark_2.11</artifactId>
  <version>1.0-SNAPSHOT</version>
</dependency>
```



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


## Scala Maven Plugin

```XML
<plugin>
  <groupId>net.alchim31.maven</groupId>
  <artifactId>scala-maven-plugin</artifactId>
  <version>3.2.2</version>
  <executions>
    <execution>
      <goals>
        <goal>compile</goal>
        <goal>testCompile</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```


## Maven Surefire Plugin
for unit testing

## maven-shade-plugin
 
```XML
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>3.0.0</version>
    <configuration>
    <!-- put your configurations here -->
    </configuration>
    <executions>
        <execution>
            <phase>package</phase>
            <goals>
                <goal>shade</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```
