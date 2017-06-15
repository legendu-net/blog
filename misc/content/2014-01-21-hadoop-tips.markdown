UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2017-06-11 20:08:06
Slug: hadoop-tips
Title: Hadoop Tips
Category: Software
Tags: big data, Hadoop, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 


hadoop fs -cat
hadoop fs -mkdir
hadoop fs -put
hadoop fs -get
hadoop fs -getmerge /hdfs/path /path/in/linux
hadoop fs -copyFromLocal /path/in/linux /hdfs/path
hadoop fs -put /path/in/linux /hdfs/path
hdfs dfs -du [-s] [-h] URI [URI …] 


1. no update, have to update locally and upload to hadoop
3. by default 3 reps of each block of data, 3 reps is the best according to many discussions
4. hadoop is for large data of course
5. because of false tolorence/replication of data, you acutally use more space on Hadoop
6. master node (name node): data about data, primary and secondary master node, for reliable
7. data nodes (slave nodes), edge node, access point for the external applications, tools, and users that need to utilize the hadoop environment
11. edge nodes (gate to hadoop), name nodes, data nodes
