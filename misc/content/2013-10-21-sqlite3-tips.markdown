Status: published
Author: Ben Chuanlong Du
Title: Tips for SQLite3
Date: 2019-07-24 22:08:24
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

3. SQLite3 supports full-text search by the FTS5 extension.
  It is suggested that you use the `porter` tokenizer for English searching.
  Please refer to Section *4.3. Tokenizers* of [SQLite FTS5 Extension](https://sqlite.org/fts5.html) for more details.

4. Avoid keeping SQLite database file on a NFS filesystem, 
  as the locking mechanism might not work correctly.
  For details, 
  please refer to https://www.sqlite.org/draft/faq.html#q5.

## Recursive Common Table Expressions

https://www.sqlite.org/lang_with.html

https://stackoverflow.com/questions/34659643/split-a-string-into-rows-using-pure-sqlite

## References

https://sqlite.org/fts5.html

http://www.sqlitetutorial.net/sqlite-full-text-search/

