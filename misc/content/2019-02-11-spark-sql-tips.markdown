Status: published
Date: 2019-08-31 02:01:24
Author: Benjamin Du
Slug: spark-sql-tips
Title: Spark SQL Tips
Category: Programming
Tags: programming, big data, Spark, Spark SQL

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

[Spark SQL Guide](https://docs.databricks.com/spark/latest/spark-sql/index.html)


0. It is suggested that you use Spark SQL syntax as much as possible 
  instead of the the Spark DataFrame syntax (even though DataFrame provides more static syntax check)
  as SQL is a universal language.

1. Spark SQL follows hive sql syntax.
    For example,
    `spark.sql("show tables in some_schema like '*perf*'")`
    returns a DataFrame with tables in the Hive database.

2. JSON, ORC, Parquet and CSV files can be queried using Spark SQL without creating a table on the Spark DataFrame.

        select
            *
        from
            csv.`hdfs://cluster_name/path_to_csv`
        where
            rand() <= 0.01
        distribute by
            rand()
        sort by
            rand()
        limit 10000

3. Position alias is supported in Spark SQL!

4. Spark SQL supports bool expressions/columns. 
  However, you cannot sum a bool expression/column directly.
  You have to either cast it to Int/BigInt or use the old-school case clause.

5. `select * from some_table limit 5` runs slow if the table `some_table` is large.
  you can limit the selection to a specific partition (if the table is partitioned) to speed it up.


6. You can use the following code to show the creation code of a Hive table in Spark.
```
println(spark.sql("show create table some_table").collect()(0)(0))
```

## Spark SQL Create Table

1. The `CREATE TABLE` clause is equivalent to the method `DataFrame.saveAsTable`,
  which write the DataFrame into a Hive table (format of the Hive table can be specified).
  You can also create (or replace) a global/temporary view, 
  which is lazily computed.
  Notice that a view can be cached too once computed if you explicitly do so
  (by calling `spark.cacheTable` or use Spark SQL hint).


## Spark SQL Hint

1. You can use 
  [Spark SQl hint](https://docs.databricks.com/spark/latest/spark-sql/language-manual/select.html#hints)
  to fine control the behavior of Spark application.
  Specially, 
  a hint for skew join is supported in Spark Spark!
  You can use it to help Spark optimizing the joining when the involved columns are skewed.

https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-hint-framework.html#specifying-query-hints
  
## References

https://stackoverflow.com/questions/41254011/sparksql-read-parquet-file-directly

http://www.joefkelley.com/736/
