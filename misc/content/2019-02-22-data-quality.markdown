Status: published
Date: 2019-02-22 03:36:11
Author: Benjamin Du
Slug: data-quality
Title: Data Quality
Category: Database
Tags: database, big data, data quality, data check

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

- Upper and lower bounds tests and Inter Quartile Range Checks(IQR) and standard deviations

- Aggregate level checks (after manipulating data, there should still be the ability to explain how the data aggregates back to the previous data set)

- Tracking percentage of nulls and dropped columns (Define what is an acceptable amount)

- Data Type Checks (This should be done earlier at the application level, as well as data value constraints e.g. WA is a state abbreviation KZ is not)

- Tracking Data Inserts

- Wherever data comes from, whether it is flat files, IPs, users, etc. This should all be tracked. Especially if it is specific files. 
    If your team finds out that the data from a specific file was inaccurate. 
    Then it would want to remove it. If you have tracked what file the data came from, this is easy.

## Useful Libraries

1. athena 

2. [pydqc](https://github.com/SauceCat/pydqc)

3. [DataGristle](https://github.com/kenfar/DataGristle)

## Books

Python Business Intelligence Bookbook


## References

https://towardsdatascience.com/introducing-pydqc-7f23d04076b3

https://medium.com/@SeattleDataGuy/good-data-quality-is-key-for-great-data-science-and-analytics-ccfa18d0fff8

https://dzone.com/articles/java-amp-apache-spark-for-data-quality-amp-validat
