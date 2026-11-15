---
title: Use q to Query Text File Using SQL Syntax
created: '2016-06-05T16:19:58-07:00'
date: '2026-11-15T09:28:29-08:00'
authors:
  - bendu
label: use-q-to-query-text-file-using-sql-syntax
license: CC-BY-4.0
tags:
  - programming
  - SQL
  - structured text
  - CSV
  - TSV
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

It is suggested that you use Python
instead of [q](http://harelba.github.io/q/)
to manipulate text files!

## Installation on Ubuntu

```bash
sudo apt install python3-q-text-as-data
```

## General Tips

1. The semantics of `q` is identical to `sqlite`.
   `q` preserve the original order of rows if no sorting (order by) is applied.
   You force querying by the order of insertion
   by adding an `order by rowid` if needed (similar to sqlite).

1. Output in quote mode does not work well.
   Double quotes are not escaped.

1. Joins do not work on files with different separators.
   You have to convert them to have the same field separator first
   and then perform joins.

1. If no header, then use c$i$ to stand for the $i^{th}$ column.

## Examples

1. Randomly select 500 records.

   ```
    q "select * from text_file order by random() limit 5"
   ```

1. Sample with acceptance ratio 0.01.

   ```
    q "select * from text_file where random() % 100 = 0"
   ```

1. Use `-` to stand the piped in output.

   ```
    head -n 1000 text_file | q "select * from - where age < 30"
   ```

1. Use q to find Docker images without repository names.

   ```
    docker images | tail -n +2 | q 'select c3 from - where c1 = "<none>"' 
   ```

1. Remove all images belong to the eclipse organization with the help of sed and q.

   ```
    docker images | sed 's/ \+/\t/g' | q -tH "select [image id] from - where repository like 'eclipse/%'" | xargs docker rmi
   ```

## Alternative Tools

1. [textql](https://github.com/dinedal/textql) (developed in Go)
   is a very similar tool to [q](http://harelba.github.io/q/).
   It has even simpler syntax than q.
   However,
   it has several disadvantages compared to q.
   First, it is not as actively maintained as q.
   Second, no easy way to install except in Mac (using Homebrew).
   You have to install from source by yourself in Linux and Windows.

1. You can import text files into database tables and work on them.
   SQLite3 is a great choice (of embedded database).
   As a matter of fact,
   both q and textql are based on SQLite3.
   You can refer to https://www.sqlite.org/cvstrac/wiki?p=ImportingFiles
   on how to importing files into SQLite3.
   If you prefer a client-server database,
   you can either MySQL, etc.

   ```
    CREATE TABLE foo (
        id Int, 
        msg VarChar(255), 
        value Decimal(8, 4)
    )
    ;

    LOAD DATA INFILE '/tmp/data.txt' 
    INTO TABLE foo
    ;
   ```

## References

http://harelba.github.io/q/
