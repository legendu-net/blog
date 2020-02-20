Status: published
Date: 2020-02-19 16:12:34
Author: Benjamin Du
Slug: subtle-differences-among-Spark-DataFrame-and-PySpark-DataFrame
Title: Subtle Differences Among Spark DataFrame and PySpark Dataframe
Category: Programming
Tags: programming, big data, Spark, PySpark, DataFrame, difference

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. Besides using the `col` function to reference a column,
    Spark/Scala DataFrame supports using `$"col_name"` 
    (based on implicit conversion and must have `import spark.implicit._`)
    while PySpark DataFrame support using `df.col_name` 
    (similar to what you can do with a pandas DataFrame).

    |                     | Spark/Scala        | PySpark            |
    |---------------------|--------------------|--------------------|
    |                     | col\("col\_name"\) | col\("col\_name"\) |
    | Implicit Conversion | $"col\_name"       | X                  |
    | Dot reference       | X                  | df\.col\_name      |

    
2. `DataFrame.where` and `DataFrame.filter` are equivalent in PySpark 
    while a Spark/Scala DataFrame does not have the `where` method.

3. `===` (null safe equality comparison) is supported in Spark/Scala but not available in PySpark.
