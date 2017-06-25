UUID: 7cda85b2-c49e-412a-8760-67b38eab1ebe
Status: published
Date: 2017-06-17 10:17:28
Author: Ben Chuanlong Du
Slug: apache-toree-tips
Title: Apache Toree Tips
Category: Programming
Tags: programming, Apache Toree, Jupyter Notebook, JupyterLab, Jupyter Lab, Spark

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

<https://github.com/apache/incubator-toree/blob/master/etc/examples/notebooks/magic-tutorial.ipynb>

## Dependency Managemnt

```scala
%AddJar jar_url
%AddDeps
printHelp(printStream, """%AddDeps my.company artifact-id version""")
```

## Questions

1. multiple version of scala? How?
