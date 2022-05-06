Status: published
Date: 2022-05-03 22:51:18
Modified: 2022-05-03 22:51:18
Author: Benjamin Du
Slug: install-dictionary-words-for-linux
Title: Install Dictionary Words for Linux
Category: Computer Science
Tags: Computer Science, programming, Linux, words, wamerican

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Words is a standard file on Unix and Unix-like operating systems, 
and is simply a newline-delimited list of dictionary words. 
It is used by Vim and spell-checking programs.
The words file is usually stored in /usr/share/dict/words or /usr/dict/words.
If the words file is missing,
you might encounter the following error message (when using Vim). 

![error](https://user-images.githubusercontent.com/824507/166628768-b05e27a4-0c7b-4793-98d4-f78591b139ed.png)

A simple way to fix the issue (on Debian-series of Linux distributions)
is to install the `wamerican` package.

    :::bash
    wajig install wamerican
