Status: published
Author: Ben Chuanlong Du
Date: 2019-04-11 23:52:08
Slug: hadoop-fs-tips
Title: Hadoop Filesystem Tips
Category: Software
Tags: big data, Hadoop, filesystem, file system, tips

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

3. Check size of a directory.

    hdfs dfs -du [-s] [-h] URI [URI …] 

    hadoop fs -rm -r -skipTrash /tmp/chdu_item_desc

## Parquet Format

Hadoop commands do not support merging Parquet files. 
You can use [apache/parquet-mr](https://github.com/apache/parquet-mr) to merge Parquet files.

## Hadoop FS compress 

http://stackoverflow.com/questions/5571156/hadoop-how-to-compress-mapper-output-but-not-the-reducer-output

http://www.ericlin.me/disable-hive-output-compression



1. no update, have to update locally and upload to hadoop

3. by default 3 reps of each block of data, 3 reps is the best according to many discussions

4. hadoop is for large data of course

5. because of false tolorence/replication of data, you acutally use more space on Hadoop

6. master node (name node): data about data, primary and secondary master node, for reliable

7. data nodes (slave nodes), edge node, access point for the external applications, tools, and users that need to utilize the hadoop environment

11. edge nodes (gate to hadoop), name nodes, data nodes

## References

https://stackoverflow.com/questions/6504107/the-way-to-check-a-hdfs-directorys-size
