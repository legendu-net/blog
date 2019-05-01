Status: published
Date: 2019-05-01 16:50:47
Author: Benjamin Du
Slug: alternative-to-the-rm-command-in-linux
Title: Alternative to the Rm Command in Linux
Category: Linux
Tags: Linux, Shell, rm, Trash, mv

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

As is know to all,
it can be dangerous to use the `rm` command directly in Linux/Unix. 
A simple idea is to define other commands/alias/script to replace it.
For example, 
I have a shell script named `trash` which moves files (as input arguments) to the system's Trash directory.

    trash files_to_remove

Another even simplier way is to directly move files to the directory `/tmp`.

    mv files_to_remove /tmp
