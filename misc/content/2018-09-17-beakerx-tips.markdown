Status: published
Date: 2019-04-23 10:53:06
Author: Ben Chuanlong Du
Slug: beakerx-tips
Title: Beakerx Tips
Category: Software
Tags: software, BeakerX, JupyterLab, Maven

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

[BeakerX dependencies](https://github.com/twosigma/beakerx/blob/master/configuration.yml#L6)
Currently Java 8 is request.

1. The maven cache is save to the following directory
    `/tmp/share/beakerx/maven/cache/`.

2. Set JVM properties for Beakerx.

https://github.com/twosigma/beakerx/issues/7666

https://github.com/twosigma/beakerx/blob/master/FAQ.md

## SQL

1. Connect to SQLite3.

        %defaultDatasource jdbc:sqlite:fts5.sqlite3

2. Connect to SQLite3 in memory

        %defaultDatasource jdbc:sqlite::memory:
    or
        %defaultDatasource jdbc:sqlite:

3. The SQLite3 JDBC driver is located at 
    `/usr/local/lib/python3.6/dist-packages/beakerx/kernel/sql/lib/sqlite-jdbc-3.21.0.jar`.
    You can manually replace it with a higher version to upgrade it.
