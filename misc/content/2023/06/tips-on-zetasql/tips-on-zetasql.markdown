Status: published
Date: 2023-06-27 23:48:22
Modified: 2023-07-01 18:06:49
Author: Benjamin Du
Slug: tips-on-zetasql
Title: Tips on ZetaSQL
Category: Computer Science
Tags: Computer Science, programming, SQL, ZetaSQL, Google

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[ZetaSQL](https://github.com/google/zetasql)
is a customized SQL dialect, 
along with parser and analyzer, 
that Google uses for products like BigQuery and Spanner.

## [unnest](https://github.com/google/zetasql/blob/master/docs/query-syntax.md#unnest_operator)

cross join if an implicit join is used.
Notice that cross join is equivalen to inner join in this case.

Left join can be used to keep rows which has a null/emtpry array.

```
some {
    proto {
        path 
            {
                repeated
                    {
                        field {
                            key: "key",
                            value: "value",
                        }
                    }
            }
    }
}
```

```
SELECT
  *,
  array(SELECT
    value 
  FROM
    UNNEST(some.proto.path.repated.field)
  WHERE 
    key = 'DESIRED_KEY') AS return_value,
FROM
  ads_signup_events_6
;
```
