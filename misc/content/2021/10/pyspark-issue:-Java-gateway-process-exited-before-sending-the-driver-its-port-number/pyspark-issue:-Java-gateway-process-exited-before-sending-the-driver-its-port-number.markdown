Status: published
Date: 2021-10-10 14:23:22
Modified: 2021-10-10 14:26:10
Author: Benjamin Du
Slug: pyspark-issue:-Java-gateway-process-exited-before-sending-the-driver-its-port-number
Title: PySpark Issue: Java Gateway Process Exited Before Sending the Driver Its Port Number
Category: Computer Science
Tags: Computer Science, programming, PySpark, Spark, Java, Python, big data, JAVA_HOME

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

I countered the issue when using PySpark locally.
It turned out to be caused by a misconfiguration of the environment variable `JAVA_HOME` in Docker.

## References 

[PySpark: Exception: Java gateway process exited before sending the driver its port number](https://stackoverflow.com/questions/31841509/pyspark-exception-java-gateway-process-exited-before-sending-the-driver-its-po)