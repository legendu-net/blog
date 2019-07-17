Status: published
Date: 2019-07-17 00:03:15
Author: Benjamin Du
Slug: spark-sql-tips
Title: Spark SQL Tips
Category: Programming
Tags: programming, big data, Spark, Spark SQL

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

[Spark SQL Guide](https://docs.databricks.com/spark/latest/spark-sql/index.html#spark-sql-language-manual)


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
  

## References

https://stackoverflow.com/questions/41254011/sparksql-read-parquet-file-directly

http://www.joefkelley.com/736/
