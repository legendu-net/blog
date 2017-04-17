UUID: f9177d34-2da8-42d1-84cf-ea9f8754f6ad
Status: published
Date: 2017-04-17 09:53:22
Author: Ben Chuanlong Du
Slug: working-with-a-cluster-of-servers
Title: Working With Cluster of Servers
Category: Software
Tags: software, server, cluster, Python, fabric, rundeck

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

I used to rely on bash a lot, 
but there are more advanced tools for managing cluster of servers.

1. ClusterSSH 

2. `Fabric` (Fabric3 for Python3) is a Python package 
which allows you write simple pythonic script to manage cluster of servers.
Fabric has issues with Unicode-only characters right now. 
Supressing outputs (of shell commands) containing unicode can help avoid potential `UnicodeEncodeError`.

3. `rundeck` is a great enterprise level cluster management tool.
