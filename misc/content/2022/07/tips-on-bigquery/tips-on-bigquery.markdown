Status: published
Date: 2022-07-28 15:04:26
Modified: 2024-02-27 22:45:03
Author: Benjamin Du
Slug: tips-on-bigquery
Title: Tips on BigQuery
Category: Computer Science
Tags: Computer Science, programming, BigQuery, SQL, query, database, cloud, Google

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[Loading data into BigQuery](https://www.youtube.com/watch?v=Abzj-Vyhi74)

[BigQuery Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

[Introduction to SQL in BigQuery](https://cloud.google.com/bigquery/docs/introduction-sql)

## Data Types

- [BigQuery Data Types Explained](https://blog.coupler.io/bigquery-data-types/)

## Questions

1. Can you set Vim keybindings for editors?

2. how to connect to a BigQuery database?

## Authentication 

1. On GCP products with the right access scope,
    no authentication is required.

    https://private-user-images.githubusercontent.com/824507/308447049-681a5007-de8e-42d6-87f9-2f8f8ef8c317.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDkxMDI4MzcsIm5iZiI6MTcwOTEwMjUzNywicGF0aCI6Ii84MjQ1MDcvMzA4NDQ3MDQ5LTY4MWE1MDA3LWRlOGUtNDJkNi04N2Y5LTJmOGY4ZWY4YzMxNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIyOFQwNjQyMTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZDQyYjdiMGE3NTQxNDJkN2UyMTliMWIyZDA5ZGE1Y2ZlYzIxMmIwMjdmNTM1YTRmYjdlNzIxYTEyODZlYmNlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.8Urrfh6t73ON2TcZdFJkQbaEsSSXEikLUsu4K612ZcM


2. In a local development environment,
    the best way is to install Google Cloud SDK CLI and use it to authenticate. 


## References

- [google-cloud-python @ GitHub](https://github.com/googleapis/google-cloud-python)

