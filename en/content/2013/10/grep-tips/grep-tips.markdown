Status: published
Author: Ben Chuanlong Du
Date: 2013-10-22 14:53:28
Modified: 2021-09-26 21:59:25
Title: Search for Files in Command-line Using grep
Slug: grep-tips
Category: OS
Tags: tips, grep, egrep


The article 
[14 Practical examples of the grep command](http://www.librebyte.net/en/gnulinux/14-practical-examples-of-the-grep-command/)
has some good examples on how to use the `grep` command.

1. The Perl style (option `-P`) regular expression is more powerful 
    than the basic (default) and extended (option `-E`) regular expression. 
    It is suggested that you use the perl style as much as possible.
    However, 
    be careful about unimplemented features. 

2. The option `-n`/`--line-number` prefixes each line of output with the 1-based line number within its input file.
    And the option `-o`/`--only-matching` prints only the matched (non-empty) parts of a matching line, 
    with each such part on a separate output line.
    Both of those options are very useful.

3. Search in current directory recursively for files containing the text "video".
    Symbolic links are followed.

        :::bash
        grep -iR 'video' .

4. Search in current directory recursively for files containing the text "video".
    Symbolic links are NOT followed.

        :::bash
        grep -ir 'video' .
