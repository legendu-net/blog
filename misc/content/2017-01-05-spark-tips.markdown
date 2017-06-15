UUID: a85907ac-decf-4477-9a47-54086e01ca9b
Status: published
Date: 2017-06-11 11:00:24
Author: Ben Chuanlong Du
Slug: spark-tips
Title: Spark Tips
Category: Programming
Tags: programming, Spark, big data

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


spark-shell --jars ... to add jars and then you can use it!!!

Spark supports two types of shared variables: broadcast variables, 
which can be used to cache a value in memory on all nodes, and accumulators, 
which are variables that are only “added” to, such as counters and sums.

## Links

https://developer.ibm.com/hadoop/2016/07/18/troubleshooting-and-tuning-spark-for-heavy-workloads/

http://blog.prabeeshk.com/blog/2014/10/31/install-apache-spark-on-ubuntu-14-dot-04/

http://mbonaci.github.io/mbo-spark/

http://www.simonouellette.com/blog/spark-join-when-not-to-use-it

https://bzhangusc.wordpress.com/2015/11/20/use-sbt-console-as-spark-shell/

https://spark-summit.org/2015/events/interactive-graph-analytics-with-spark/



## Questions

can I setup a client by myself?
RDD.saveAsTextFile cannot write to my own directory?!!!
spark shell ls？

### Hive

http://stackoverflow.com/questions/18129581/how-do-i-output-the-results-of-a-hiveql-query-to-csv

https://hadoopsters.net/2015/09/18/hadoop-tutorial-how-to-export-hive-table-to-csv-file/

https://analyticsanvil.wordpress.com/2016//python-jdbc-dyanmic-hive-scripting/ 

Hive table, if I need a small part of a big Hive table, does hive load in all data or try to be smart? it seems that it's hard ...

### sbt

sbt OneJar seems to be a good option

http://www.scala-sbt.org/0.13/docs/Running.html

http://www.scala-sbt.org/0.13/docs/index.html

### Hadoop

hadoop fs -rm -r -skipTrash /tmp/chdu_item_desc

Hadoop FS compress http://stackoverflow.com/questions/5571156/hadoop-how-to-compress-mapper-output-but-not-the-reducer-output

Hadoop FS compress: http://www.ericlin.me/disable-hive-output-compression

### Maven

http://scala-ide.org/docs/tutorials/m2eclipse/

m2eclipse-scala

### Scala

scala:convert a seq of string to biginit? how to map ... which fun to use?

http://stackoverflow.com/questions/17461453/build-scala-and-symbols-meaning

http://stackoverflow.com/questions/32763142/scala-project-with-maven-in-intellij-does-not-compile

https://www.ivankrizsan.se/2016/03/27/creating-a-scala-project-with-maven-dependency-management-for-gatling-testing-in-intellij-idea/

