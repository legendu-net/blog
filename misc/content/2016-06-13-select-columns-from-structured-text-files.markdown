UUID: a57587d8-9b0b-4c74-b5f3-f1bcd2aa7d4f
Status: published
Date: 2018-01-01 16:15:21
Author: Ben Chuanlong Du
Slug: select-columns-from-structured-text-files
Title: Select Columns from Structured Text Files
Category: Programming
Tags: programming, SQL, awk, cut, text file, data manipulation, column, field

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

cut
```sh
cut -d\t -f1,3 file.txt
```
awk
```sh
awk -F'\t' '{print $1 "\t" $3}' file.tsv 
```
Unfortuantely, 
neither `cut` or `awk` honors escaped characters.

The tool [q](https://github.com/harelba/q) is a better alternative. 
q
```sh
q -t -H 'select c1, c3 from file.txt'
```

ebay/tsv-utils-dlang 
looks interesting.
