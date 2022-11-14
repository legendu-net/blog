Status: published
Date: 2015-06-14 02:12:06
Modified: 2021-09-26 13:52:08
Author: Ben Chuanlong Du
Slug: set-operations-on-lines-of-files
Title: Set Operations on Lines of Files
Category: Computer Science
Tags: programming, set operations, file, lines, sort, uniq, comm, shell

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

It is suggested that you **use Python instead of shell** script 
to manipulate text files!

1. Union lines in 2 files.

        :::bash
        comm f1 f2

    Or you can use

        :::bash
        cat f1 f2 | sort -u | uniq -u

2. Show symmetric difference 

        :::bash
        comm -3 file1 file2

3. Show difference of 1 and 2

        :::bash
        comm -23 file1 file2

Note that lines in files must be sorted first if you use the command `comm`.
To sort lines in a file, 
you can use the following command.

    :::bash
    sort file -o file

