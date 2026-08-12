---
title: 'PySpark Issue: Java Gateway Process Exited before Sending the Driver Its Port Number'
created: '2021-10-10T14:23:22-07:00'
date: '2026-08-11T22:39:32-07:00'
authors:
  - bendu
label: pyspark-issue-java-gateway-process-exited-before-sending-the-driver-its-port-number
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - PySpark
  - Spark
  - Java
  - Python
  - big data
  - JAVA_HOME
---

I countered the issue when using PySpark locally
(the issue can happen to a cluster as well).
It turned out to be caused by a misconfiguration of the environment variable `JAVA_HOME` in Docker.

## References

[PySpark: Exception: Java gateway process exited before sending the driver its port number](https://stackoverflow.com/questions/31841509/pyspark-exception-java-gateway-process-exited-before-sending-the-driver-its-po)
