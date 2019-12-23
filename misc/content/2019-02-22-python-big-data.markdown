Status: published
Date: 2019-12-23 09:59:33
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

1. If you have relative large memory, 
    say more than 20G, 
    on your (single) machine, 
    you can handle (filtering, sorting, merging, etc.) 
    millions (magnitude of 1E6) of rows in pandas DataFrame without any pressure. 
    When you have more than 10 millions rows 
    or the memory on your (single) machine is restricted,
    you should consider using big data tools such as Dask and PySpark.

2. Both Dask and PySpark are very easy to use (assume that you are familar with pandas and Spark DataFrame).

3. PySpark (even standalone on a single machine) is a clear win over Dask 
    in almost all perspectives (features, speed, volume of data that can be handled). 
    For example,
    PySpark is able to join 2 tables of millions of row on a single machine with very limited memory.
    However, Dask fails to work (or takes unbearly long time) with the same amount of resources.
    And also, PySpark supports sorting large DataFrame 
    while there is no easy way to sort large DataFrame in Dask.

4. Do NOT use the Jupyter/Lab plugin `jupyterlab-lsp` 
    if you work on big data in Jupyter/Lab.
    The plugin `jupyterlab-lsp` has issues with large DataFrames 
    (both with pandas and PySpark DataFrames)
    and can easily crash your Jupyter/Lab server 
    even if you have enough memory.

To sum up, 
stick with pandas DataFrame if you have relative small data (say, millions of rows) 
and relative large memory (say, more than 20G).
If you do have to leverage big data tools, 
PySpark is prefereed to Dask.

## Dask

[Hands on the Python Module dask](http://www.legendu.net/misc/blog/hands-on-the-python-module-dask/)

## PySpark

http://www.legendu.net/misc/blog/tips-on-pyspark/

http://www.legendu.net/misc/blog/pyspark-optimus-data-profiling/

## References

https://www.dataquest.io/blog/pandas-big-data/
