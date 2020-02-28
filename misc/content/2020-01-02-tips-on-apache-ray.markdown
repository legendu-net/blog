Status: published
Date: 2020-02-27 16:00:24
Author: Benjamin Du
Slug: tips-on-apache-ray
Title: Tips on Apache Ray
Category: Programming
Tags: programming, Apache Ray, distributed computing

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Configure a Private Ray Cluster

https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html

https://ray.readthedocs.io/en/latest/autoscaling.html

https://ray.readthedocs.io/en/latest/autoscaling.html#quick-start-private-cluster

https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html

## Tutorials and Examples

[How to scale Python multiprocessing to a cluster with one line of code](https://medium.com/distributed-computing-with-ray/how-to-scale-python-multiprocessing-to-a-cluster-with-one-line-of-code-d19f242f60ff)
demonstrates how you can scale a Python multiprocess application 
to run an Apache Ray cluster 
with only one line change of your code 
(change `import multiprocessing.Pool` to `ray.util.multiprocessing.Pool`).


## Kubernetes

https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/kubernetes/example-full.yaml

## Ray with Spark 



## References

https://github.com/ParallelSSH/parallel-ssh

https://ray.readthedocs.io/en/latest/walkthrough.html#remote-functions-tasks

https://arrow.apache.org/docs/python/plasma.html#the-plasma-in-memory-object-store

https://readthedocs.org/projects/ray/downloads/pdf/latest/

https://ray.readthedocs.io/en/latest/package-ref.html
