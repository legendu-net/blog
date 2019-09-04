Status: published
Author: Ben Chuanlong Du
Title: Tips for SQLite3
Date: 2019-09-04 19:35:25
Slug: sqlite-tips
Category: Software
Tags: tips, SQLite3, database, FTS5, full-text search

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. `.schema` show create statement of a table

2. You can force query to keep the original order of rows 
    by applying `order by rowid`.

3. SQLite3 supports full-text search by the FTS5 extension (since 3.9.0).
  It is suggested that you use the `porter` tokenizer for English searching.
  Please refer to Section *4.3. Tokenizers* of [SQLite FTS5 Extension](https://sqlite.org/fts5.html) for more details.

4. Avoid keeping SQLite database file on a NFS filesystem, 
  as the locking mechanism might not work correctly.
  For details, 
  please refer to https://www.sqlite.org/draft/faq.html#q5.

5. The window functions are supported since 
  [SQLite 3.25.0](https://www.sqlite.org/releaselog/3_25_0.html).
  Notice that the official Python release 3.6.x does not have SQLite 3.25.0.
  You have to use official Python release Python 3.7+ if you need SQLite 3.25.0+.
  However, the Anaconda Python 3.6+ releases include SQLite 3.25.0+.

## Recursive Common Table Expressions

https://www.sqlite.org/lang_with.html

https://stackoverflow.com/questions/34659643/split-a-string-into-rows-using-pure-sqlite

## Issues

https://stackoverflow.com/questions/25705671/python-attributeerror-module-object-has-no-attribute-connect

## References

https://sqlite.org/fts5.html

http://www.sqlitetutorial.net/sqlite-full-text-search/

https://stackoverflow.com/questions/50332436/syntax-error-when-using-row-number-in-sqlite3
