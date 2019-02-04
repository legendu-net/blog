UUID: 6af44d1e-d4a3-4515-82b6-a84917961027
Status: published
Date: 2018-09-17 22:14:31
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

1. The maven cache is save to the following directory
    `/tmp/share/beakerx/maven/cache/`.

## SQL

1. Connect to SQLite3 in memory.

        %defaultDatasource jdbc:sqlite:fts5.sqlite3

    It seems to me that SQLite3 in BeakerX does not support the in-memory mode,
    which is not a big deal. 
