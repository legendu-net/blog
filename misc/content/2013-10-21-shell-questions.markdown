UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-03-13 01:23:52
Slug: shell-questions
Title: Shell Questions
Category: Programming,
Tags: questions, programming, shell

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
Bash

0. see how to write options like -p ... need parse arguments, is there an easy way to do this?
after this is done, add a password option for your backup function

1. bash has vi mode and emacs mode,
the default is emacs mode, set -o vi ...
this is so cool

2. use xargs to pass results to a command for execuation
if the command does not accept pile directly

3. how does bash deal with relative paths? relative path mentioned in a file, 
what the base path, the path of the directory containing the file or the home directory?	

4. is there any way to extract part of results of the output of a command? e.g., first output of ls or first line of ...?

5. how to write documentation for user-define bash functions?

6. why funname(){} sometimes does not work? it seems that function fname {} always works. 

1. is their any container in bash language? it seems that bash is very nasty

2. whitespace has meaning in bash, and thus cannot be added or omitted ...

3. is possible to run bash script like ruby and python? i.e., define a function in a 
script, use the file directory without source it first.

4. when you have to use many nested quotes, 
things become very complicated,
not sure how to get it right. 

5. what's the best way to find a file with a given content? if not sure where the file is 
grep vs find which is better?

6. free -m shows free memory available, it shows more valuable information than the top command


1. find . -iname '*rdata', it seems that their's difference whether you use quotation or not
you'd better always use quotes

2. why sometimes people use #!/usr/bin/env ruby instead of #!/usr/bin/ruby?


3. how to use grep to find string like "-r-"?

4. how to flush echo?

5. is alias visible in sub shells?
i don't think so

6. How to combine tables horizontally?
