Status: published
Date: 2022-04-03 18:58:34
Modified: 2022-04-03 19:13:38
Author: Benjamin Du
Slug: spark-issue:-ArrowTypeError:-Expect-a-type-but-got-a-different-type
Title: Spark Issue: ArrowTypeError: Expect a Type but Got a Different Type
Category: Computer Science
Tags: Computer Science, programming, Spark, Spark issue, error, exception, ArrowTypeError

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

> pyarrow.lib.ArrowTypeError: Expected a string or bytes dtype, got int64

## Possible Causes

A `pandas_udf` tag specifies a return type of `String`
but the corresponding pandas udf returns a different type (`int64`).
Below is such an example.

    @pandas_udf(returnType="string")
    def calc_suit(id: pd.Series) -> pd.Series:
        return pd.Series(get_the_suit(id_) for id_ in id)

## Possible Solutions

Change the `pandas_udf` tag to `@pandas_udf(returnType="long")`
or make the corresponding pandas udf return a string (or bytes).




