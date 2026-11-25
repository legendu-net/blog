---
title: Tricks on ANY_VALUE with HAVING MAX in GoogleSQL
created: '2026-11-24T21:32:31.659080-08:00'
date: '2026-11-24T21:32:31.659089-08:00'
authors:
  - bendu
label: tricks-on-any_value-with-having-max-in-googlesql
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - SQL
  - GoogleSQL
  - BigQuery
  - ZetaSQL
  - database
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Overview and Dialect Availability

In GoogleSQL (formerly ZetaSQL, used by BigQuery and Cloud Spanner),
`ANY_VALUE(c1 HAVING MAX ts)` returns the value of `c1`
from a row where `ts` attains its maximum value within each group
(and `HAVING MIN ts` does the same for the minimum).
BigQuery also provides `MAX_BY(c1, ts)` and `MIN_BY(c1, ts)` as direct synonyms
for `ANY_VALUE(c1 HAVING MAX ts)` and `ANY_VALUE(c1 HAVING MIN ts)`.

If multiple rows tie for the maximum `ts`,
GoogleSQL skips rows where `c1` is `NULL` (as if `IGNORE NULLS` were set)
and nondeterministically picks one of the remaining tied rows.

| Engine / Dialect | Equivalent Function |
| :--- | :--- |
| GoogleSQL / BigQuery | `ANY_VALUE(x HAVING MAX y)` or `MAX_BY(x, y)` |
| DuckDB / Spark SQL / Trino / Snowflake | `MAX_BY(x, y)` |
| ClickHouse | `argMax(x, y)` |
| PostgreSQL | `DISTINCT ON`, `ORDER BY y DESC LIMIT 1`, or `FIRST_VALUE` |

## Watch Out for `NULL` in `ts`

When using `ANY_VALUE(c1 HAVING MAX ts)`, be careful if `ts` can be `NULL`:

1. **Rows with `ts IS NULL` are ignored by `HAVING MAX`:**
   `HAVING MAX ts` evaluates the maximum over non-`NULL` values of `ts`.
   If *all* rows in a group have `ts IS NULL`, the result is `NULL`.
2. **A `NULL` `c1` on the winning row(s) still returns `NULL`:**
   `HAVING MAX ts` narrows the candidate rows to those with the maximum `ts` *first*,
   and `ANY_VALUE` selects from that restricted pool (preferring non-`NULL` `c1` values if any exist among the tied rows).
   If *every* row tied at the maximum `ts` has `c1 IS NULL`,
   the function returns `NULL` rather than falling back to an earlier row with a non-`NULL` `c1`.
3. **Guarding `NULL` timestamps:**
   If you want `NULL` timestamps treated as the earliest possible time (so non-`NULL` timestamps always win,
   while still allowing a `NULL`-timestamp row to be picked if no non-`NULL` timestamp exists),
   use `COALESCE` with a minimum sentinel timestamp such as `TIMESTAMP '0001-01-01 00:00:00 UTC'`:

   ```sql
   SELECT
     id,
     ANY_VALUE(c1 HAVING MAX COALESCE(ts, TIMESTAMP '0001-01-01 00:00:00 UTC')) AS latest_c1
   FROM events
   GROUP BY id;
   ```

   If `NULL` timestamps should be excluded altogether, filter them out with `WHERE ts IS NOT NULL`.

## Both Arguments Can Be Expressions: As-Of Timestamp `t` Tricks

Both `c1` and `ts` in `ANY_VALUE(c1 HAVING MAX ts)` can be arbitrary expressions.
This makes it possible to compute the latest value up to a cutoff timestamp `t` (`ts <= t`)
in a single `GROUP BY` pass without a separate subquery or join.

### Trick 1: Sentinel Timestamp vs. `NULL` for `ts > t`

You can demote rows after `t` by mapping their `having_expression` to a sentinel minimum timestamp
that does not appear in your data:

```sql
-- Caution: if ALL rows in a group have ts > t, every row ties on the sentinel timestamp
-- and ANY_VALUE(c1 ...) will leak a post-t row's c1!
ANY_VALUE(c1 HAVING MAX IF(ts <= t, ts, TIMESTAMP '0001-01-01 00:00:00 UTC'))
```

Notice the edge case: if a group has **no** rows with `ts <= t`,
every row gets the sentinel timestamp `0001-01-01 00:00:00 UTC`,
so `ANY_VALUE` will still pick one of the `ts > t` rows.

Alternatively, mapping post-`t` timestamps to `NULL` causes `HAVING MAX` to ignore them completely
and return `NULL` when no row satisfies `ts <= t`:

```sql
ANY_VALUE(c1 HAVING MAX IF(ts <= t, ts, NULL))
```

### Trick 2: Transform Both Value and Timestamp Expressions

To prevent leaking a post-`t` value when using a sentinel timestamp—or when you want an explicit non-`NULL` default
(such as `0`) whenever no row satisfies `ts <= t`—transform **both** arguments:

1. Map timestamps `> t` to a smaller sentinel timestamp that will not appear in the database.
2. Map values `c1` corresponding to timestamps `> t` to `NULL` or a default/smallest value.

Note that when the masked value is `NULL`, this produces the same result as Trick 1's `IF(ts <= t, ts, NULL)`;
Trick 2 is mainly useful when you want an explicit non-`NULL` fallback value such as `0`.

```sql
SELECT
  id,
  ANY_VALUE(
    IF(ts <= t, c1, NULL)
    HAVING MAX IF(ts <= t, ts, TIMESTAMP '0001-01-01 00:00:00 UTC')
  ) AS c1_as_of_t,
  ANY_VALUE(
    IF(ts <= t, val, 0)
    HAVING MAX IF(ts <= t, ts, TIMESTAMP '0001-01-01 00:00:00 UTC')
  ) AS val_as_of_t_or_zero
FROM events
GROUP BY id;
```

Even if every row in a group has `ts > t` and ties on the sentinel timestamp,
all candidate values in that tied pool have already been masked to `NULL` (or `0`),
so no post-`t` data can leak through.

## Comparison with Window Functions (`ROW_NUMBER` / `QUALIFY`)

- **Prefer `ANY_VALUE(... HAVING MAX ...)`** when you already have a `GROUP BY`,
  only need one or a few columns at the latest timestamp,
  or want to compute multiple as-of horizons (`t1`, `t2`, `t3`) in a single table scan:
  ```sql
  SELECT
    id,
    ANY_VALUE(IF(ts <= t1, c1, NULL) HAVING MAX IF(ts <= t1, ts, NULL)) AS c1_t1,
    ANY_VALUE(IF(ts <= t2, c1, NULL) HAVING MAX IF(ts <= t2, ts, NULL)) AS c1_t2
  FROM events
  GROUP BY id;
  ```
- **Prefer `QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY ts DESC, tie_breaker DESC) = 1`**
  when you need deterministic multi-column tie-breaking or need to project many columns from the winning row
  without repeating `HAVING MAX` on each column.

## References

- [BigQuery Aggregate Functions: `ANY_VALUE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#any_value)
- [BigQuery Aggregate Functions: `MAX_BY`](https://cloud.google.com/bigquery/docs/reference/standard-sql/aggregate_functions#max_by)
- [](#tips-on-zetasql)
- [](#tips-on-bigquery)
