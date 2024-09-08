Status: published
Date: 2022-07-28 15:04:26
Modified: 2024-03-04 22:36:30
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

    ![](https://private-user-images.githubusercontent.com/824507/310008334-e5502514-15eb-4864-9b3c-ee86fd69596a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk2MjA4NTUsIm5iZiI6MTcwOTYyMDU1NSwicGF0aCI6Ii84MjQ1MDcvMzEwMDA4MzM0LWU1NTAyNTE0LTE1ZWItNDg2NC05YjNjLWVlODZmZDY5NTk2YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwNVQwNjM1NTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xYmEyYjMzOTNlN2RhY2ZmY2EzMDU0ZWRiOTk2ZmYzNDk5ZWUzNDEzMGZmYWQyNDBkYjk1MGYxMzg5MGUyMTY1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.PRzxml3vkdlD6XHqT0EDgcgWbWqq2Lew4TcPR98L0sA)

2. In a local development environment,
    the best way is to install Google Cloud SDK CLI and use it to authenticate. 


## References

- [google-cloud-python @ GitHub](https://github.com/googleapis/google-cloud-python)

