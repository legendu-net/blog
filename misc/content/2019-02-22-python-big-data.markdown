Status: published
Date: 2019-12-20 11:18:58
Author: Benjamin Du
Slug: python-big-data
Title: Python Big Data
Category: Programming
Tags: programming, Python, big data, Dask, PySpark

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

There are multiple ways to handle big data in Python,
among which Dask and PySpark are the w most popular ones.

1. Both Dask and PySpark are very easy to use.

2. PySpark (even standalone on a single machine) is a clear win over Dask 
    in both speed and the amount of data that it can handle.
    For example,
    PySpark is able to join 2 tables of millions of row on a single machine with very limited memory.
    However, Dask fails to work (or takes unbearly long time) with the same amount of resources.

To sum up, 
PySpark is prefereed to Dask.

## Dask

[Hands on the Python Module dask](http://www.legendu.net/misc/blog/hands-on-the-python-module-dask/)

## PySpark

## References

https://www.dataquest.io/blog/pandas-big-data/
