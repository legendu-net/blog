Status: published
Date: 2020-02-27 20:11:55
Author: Benjamin Du
Slug: deploy-apache-ray
Title: Deploy Apache Ray
Category: Programming
Tags: programming, Apache Ray, distributed computing, deploy, deployment, setup, configure, Kubernetes, Spark, cluster

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## [Manual Cluster Setup](https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html)

It is very easy to set up Apache Ray on a small cluster manually.
The instructions at
[Manual Cluster Setup](https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html)
is very clear.
Just one comment.
You do not need to configure SSH keys for nodes in the cluster for manual configuration.
When you start the master node manually (using the command `ray start --head`), 
it will print a command to add new nodes into the cluster.
The command 
(e.g., ray start --address='10.148.186.18:12030' --redis-password='5241590000000000')
includes the Redis password for authentication to join the cluster.

## Configure a Private Ray Cluster

https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html

https://ray.readthedocs.io/en/latest/autoscaling.html

https://ray.readthedocs.io/en/latest/autoscaling.html#quick-start-private-cluster

https://ray.readthedocs.io/en/latest/using-ray-on-a-cluster.html


## Kubernetes

https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/kubernetes/example-full.yaml

## Ray with Spark 
