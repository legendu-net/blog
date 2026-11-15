---
title: Tips on Teradata SQL Assistant
created: '2018-05-12T22:02:34-07:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: tips-on-teradata-sql-assistant
license: CC-BY-4.0
tags:
  - software
  - Teradata SQL Assistant
  - Teradata SQL
  - IDE
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. You can open multiple Teradata SQL Assistant sessions when necessary.
   This is helpful if you have to connect to multiple data platforms at the time.
   You can have one opened session for each platform
   that you have to operate on.

1. Run only selected/highlighted SQL statement in Teradata SQL Assistant
   Tool -> Query -> Check "Submit only the selected query text, when highlighted"

1. You can record macro in Teradata SQL Assistant which can make things easy.
   For example,
   you can use macro to auto fill in table tables.

1. Teradata SQL Assistant does not automatically load a SQL file
   if it is modified in another editor.
   To refresh the file,
   you can just close the SQL file and reopen it.

1. There are 2 ways to export Teradata SQL query results.
   First, you can directly copy the results (to Excel, etc.) if the result is not too big.
   Second, you can click the menu `File -> Export Results`.
   Teradata SQL Assistant will then show "Future results will be Exported to a file"
   on top of the SQL code editor.
   Every time before you run your SQL code,
   you will be prompt to type in or choose a file to export the result to.
   If a file you typed in or chose exists,
   Teradata SQL Assistant will let you choose
   whether to overwrite the file or to append result to the file.

1. You cannot close a SQL file in Teradata SQL Assistant
   if it is the only one opened.
   To close it,
   you have to open a new query first and then close it.
   That is there must be at least one SQL file open in Teradata SQL Assistant all the time.

1. You can click the "Explain" button in Teradata SQL Assistant
   to estimate the time and space complexity.
   Another way is to prefix your SQL code by the keyword `explain`.

1. Menu: View -> Show History

   To temporarily comment out some of your SQL query
   1 Highlight the code you want to comment out.
   2 On the Query Window toolbar, click or press Ctrl-D to comment out the highlighted text.

1. SQL: Let Teradata SQL remember the last saved directory?
