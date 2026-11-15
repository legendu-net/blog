---
title: Tips on ZetaSQL
created: '2023-06-27T23:48:22-07:00'
date: '2026-11-15T09:25:05-08:00'
authors:
  - bendu
label: tips-on-zetasql
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - SQL
  - ZetaSQL
  - Google
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[ZetaSQL](https://github.com/google/zetasql)
is a customized SQL dialect,
along with parser and analyzer,
that Google uses for products like BigQuery and Spanner.

## [unnest](https://github.com/google/zetasql/blob/master/docs/query-syntax.md#unnest_operator)

cross join if an implicit join is used.
Notice that cross join is equivalent to inner join in this case.

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
