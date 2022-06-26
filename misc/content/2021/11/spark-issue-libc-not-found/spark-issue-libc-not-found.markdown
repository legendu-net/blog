Status: published
Date: 2021-11-30 11:34:46
Modified: 2021-11-30 11:34:46
Author: Benjamin Du
Slug: spark-issue-libc-not-found
Title: Spark Issue Libc Not Found
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, big data, libc, glibc, not found, version

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

> /lib64/libc.so.6: version `GLIBC_2.18' not found (required by ...)

## Cause
The required version of GLIBC by the binary executor is not found on Spark nodes. 

## Solution
Recompile your binary executable with the right version of GLIBC.
The recommended approach is build your binary executable 
in a Docker environment with the same OS installed in Spark nodes.
For example,
if CentOS 7.6 is the Linux distribution installed on Spark nodes,
then build your binary executable in a Docker image with CentOS 7.6.