UUID: 559e7882-d431-4a76-b1f7-9eb950bbc42f
Status: published
Date: 2017-02-18 11:57:33
Author: Ben Chuanlong Du
Slug: sql-on-text-file
Title: SQL on Text File
Category: Programing
Tags: programming, SQL, structured text, CSV, TSV

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## [q](http://harelba.github.io/q/)

You can use the following command to install `q` on Debian series of Linux distributions.
```bash
wajig install python3-q-text-as-data
```

1. Output in quote mode does not work well. 
Double quotes are not escaped.

2. Joins do not work on files with different separators. 
You have to convert them to have the same field separator first
and then perform joins. 

2. the syntax matches sqlite syntax.

3. Randomly select 500 records.
```sh
q "select * from text_file order by random() limit 5"
```
```sh
-- sample with acceptance ratio 0.01
q "select * from text_file where random() % 100 = 0"
```

4. Use `-` to stand the piped in output. 
```SQL
head -n 1000 text_file | q "select * from - where age < 30"
```

4. If no header, then use c$i$ to stand for the $i^{th}$ column.

5. The semantics of `q` is identical to `sqlite`. 
`q` preserve the original order of rows if no sorting (order by) is applied.
You force querying by the order of insertion 
by adding an `order by rowid` if needed (similar to sqlite).

Below is an example to use `q` together with other tools (`head`) to quickly query records.

```bash
# show all docker images
docker images | tail -n +2 | q 'select c3 from - where c1 = "<none>"' | xargs docker rmi
# the output is not very well structured, get rid of title make it structred (separated by space)
docker images | tail -n +2 
# use q to find images without repository names
docker images | tail -n +2 | q 'select c3 from - where c1 = "<none>"' 
# remove those images in batch
docker images | tail -n +2 | q 'select c3 from - where c1 = "<none>"' | xargs docker rmi
```
Another good way is to use `awk` (see example command below). 
In this example, 
`awk` is even more convenient as it does require the input to be structured text.
```bash
docker images | awk '{ if ($1 == "<none>") print $3 }'
```


## [fsql](https://metacpan.org/pod/distribution/App-fsql/bin/fsql)

Perl based.

## [textql](https://github.com/dinedal/textql)

No active development.

## [squeal](https://fedorahosted.org/squeal/)

No active development.

Below are some heavier solutions.

## SQLite

<https://www.sqlite.org/cvstrac/wiki?p=ImportingFiles>

## PostgreSQL

you can use the copy command to import a file into PostgreSQL and work on it.

## MySQL

```MySQL
create table foo(id int, msg varchar(255), value decimal(8,4));
load data infile '/tmp/data.txt' into table foo;
```
