Status: published
Date: 2022-01-18 10:11:28
Modified: 2022-02-10 09:00:02
Author: Benjamin Du
Slug: spark-issue:-SIGBUS
Title: Spark Issue: SIGBUS
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, big data, SIGBUS

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> CalledProcessError: Command './pine' died with <Signals.SIGBUS: 7>.

## Possible Causes 
 
SIGBUS (bus error) is a signal that happens 
when you try to access memory that has not been physically mapped
.
There are several things which might cause a SIGBUS error. 

1. Memory alignment issues with the CPU, 
    e.g., 
    trying to read a long from an address which isn't a multiple of 4.

2. Access memory region that was once file-backed, 
    but the original file got truncated in the iterim. 
    For example,
        - device failure
        - A NFS was used and the network disconnected
    causing memory mapped file on the NFS failed to load.

## Possible Solutions 

1. In the context of Spark/PySpark,
    the first cause usually happens if you call C/C++ code
    which uses pointers to manipulate memory.
    Fix memory miss alignment issues in the C/C++ code if any.

2. In thecontext of Spark/PySpark,
    the second cause is more likely than the first one 
    and it typically means a device failure or network disconnection.
    You can simplfy retry your Spark/PySpark application.
    If you still encounter the same issue,
    try with increased `spark.executor.memory` and `spark.driver.memoryOverhead`.
    If your Spark application consists of a few big jobs,
    try splitting big jobs into smaller ones might also help.

## References 

- [signal(7) — Linux manual page](https://man7.org/linux/man-pages/man7/signal.7.html)

- [Use mmap With Care](https://www.sublimetext.com/blog/articles/use-mmap-with-care)
