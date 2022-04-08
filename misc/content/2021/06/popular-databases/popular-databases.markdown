Status: published
Date: 2021-06-10 10:33:02
Author: Benjamin Du
Slug: popular-databases
Title: Popular Databases
Category: Computer Science
Tags: Computer Science, programming, database, MySQL, ClickHouse, TiDB, neo4j, Elasticsearch, TiDB, TDengine, Redis
Modified: 2022-04-08 09:36:52
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


<table style="width:100%">
  <tr>
    <th> Name </th>
    <th> Opensource/Free </th>
    <th> Best Use Case </th>
    <th> Comment </th>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/mysql"> MySQL </a>
    <a href="#footnote7">[1]</a>
    </td>
    <td> Opensource </td>
    <td> </td>
    <td> the most popular opensource database </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/ClickHouse/ClickHouse"> ClickHouse </a>
    <a href="#footnote7">[2]</a>
    </td>
    <td> Opensource </td>
    <td> OLAP for big data </td>
    <td> Has very good performance </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/pingcap/tidb"> TiDB </a>
    <a href="#footnote7">[3]</a>
    </td>
    <td> Opensource </td>
    <td> OLAP for big data </td>
    <td> good performance, support integration with Spark </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/redis"> Redis </a>
    <a href="#footnote7">[4]</a>
    </td>
    <td> Opensource </td>
    <td> Distributed in-memory cache for real-time applications </td>
    <td> </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/neo4j"> neo4j </a>
    <a href="#footnote7">[5]</a>
    </td>
    <td> Opensource </td>
    <td> Graph applications </td>
    <td> The most popular graph database </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/elastic"> Elasticsearch </a>
    <a href="#footnote7">[6]</a>
    </td>
    <td> Opensource </td>
    <td> Out-of-the-box search engine for large documents </td>
    <td> Designed as a search engine but also popularly used as a database </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/taosdata/TDengine"> TDengine </a>
    <a href="#footnote7">[7]</a>
    </td>
    <td> Opensource </td>
    <td> IoT </td>
    <td> IoT, good performance </td>
  </tr>
</table>

[2] [ClickHouse](https://github.com/ClickHouse/ClickHouse)
is an open-source column-oriented database management system 
that allows generating analytical data reports in real time.

## [yugabyte-db](https://github.com/YugaByte/yugabyte-db)
[yugabyte-db](https://github.com/YugaByte/yugabyte-db)

## MongoDB
MongoDB is a document-oriented, disk-based database optimized 
for operational simplicity, schema-free design and very large data volumes. 

## Distributed In-memory Cache

A distributed in-memory cache is essentially a distributed key-value storage/database.
You can think it as a hashmap over network.

[Redis](https://github.com/redis)
is the most popular in-memory cache which is implemented in C.
[memcached](https://github.com/memcached/memcached)
is another (not so popular) in-memory cache and is also implemented in C.
[pelikan](https://github.com/twitter/pelikan)
is Twitter's unified cache backend
which is implemented in C and Rust.

## References

- [6.1 The Challenge of Distributed Database Systems](https://berb.github.io/diploma-thesis/original/061_challenge.html)

- [MySQL vs PostgreSQL -- Choose the Right Database for Your Project](https://developer.okta.com/blog/2019/07/19/mysql-vs-postgres)

- [Why Uber Engineering Switched from Postgres to MySQL](https://eng.uber.com/postgres-to-mysql-migration/)

[Yes We Can! Distributed ACID Transactions with High Performance](https://blog.yugabyte.com/yes-we-can-distributed-acid-transactions-with-high-performance/)

[A Beginner’s Guide to CAP Theorem for Data Engineering](https://www.analyticsvidhya.com/blog/2020/08/a-beginners-guide-to-cap-theorem-for-data-engineering/)
