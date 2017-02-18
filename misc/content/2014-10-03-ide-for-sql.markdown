UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-10-23 16:41:44
Author: Ben Chuanlong Du
Slug: ide-for-sql
Title: IDE for SQL
Category: Software
Tags: software, Teradata SQL Assistant, IDE, SQL

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Editor

1. DbVisualizer (free and pro editions available)

2. Oracle SQL Developer (free)

3. SQuirreL SQL Client (open source)

0. Both Toad (Oracel SQL IDE) and Teradata SQL Assistant uses F5 to run queries.

## Teradata Studio

1. Teradata studio 可以改默认workspace 吗

## Oracle SQL Developer

2. how to show line numbers in oracle sql developer?

oracle sql developer: how to change language to English?
oracle sql develop, by default, run the current query, ";" matters ..., 
a good way is to always select the code and then run it ... 

## Teradata SQL Assistant

1. You can open multiple Teradata SQL Assistant sessions when necessary.
This is helpful if you have to connect to multiple data platforms at the time.
You can have one opened session for each platform 
that you have to operate on.

2. Run only selected/highlighted SQL statement in Teradata SQL Assistant
Tool -> Query -> Check "Submit only the selected query text, when highlighted"

3. You can record macro in Teradata SQL Assistant which can make things easy.
For example, 
you can use macro to auto fill in table tables.

1. Teradata SQL Assistant does not automatically load a SQL file 
if it is modified in another editor. 
To refresh the file, 
you can just close the SQL file and reopen it. 

2. There are 2 ways to export Teradata SQL query results.
First, you can directly copy the results (to Excel, etc.) if the result is not too big.
Second, you can click the menu `File -> Export Results`. 
Teradata SQL Assistant will then show "Future results will be Exported to a file" 
on top of the SQL code editor.
Every time before you run your SQL code,
you will be prompt to type in or choose a file to export the result to.
If a file you typed in or chose exists, 
Teradata SQL Assistant will let you choose 
whether to overwrite the file or to append result to the file.

3. You cannot close a SQL file in Teradata SQL Assistant 
if it is the only one opened. 
To close it, 
you have to open a new query first and then close it. 
That is there must be at least one SQL file open in Teradata SQL Assistant all the time.

6. You can click the "Explain" button in Teradata SQL Assistant 
to estimate the time and space complexity. 
Anothe way is to prefix your SQL code by the keyword `explain`.

7. Menu: View -> Show History

To temporarily comment out some of your SQL query
1 Highlight the code you want to comment out.
2 On the Query Window toolbar, click or press Ctrl-D to comment out the highlighted text. 


10. SQL: Let Teradata SQL remember the last saved directory?
