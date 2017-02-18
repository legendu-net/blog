UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Config Tips
Author: Ben Chuanlong Du
Date: 2014-09-07 12:23:22
Slug: config-tips
Category: Software
Tags: software, configuration, Linux, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 

1. On company and other computers that you cannot use git, 
you'd better make local copies for configuration files 
instead of using symbolic links.

2. Better to use host specific configuration files. 
For example, export.sh -> export_FDKLLL.sh in the Cygwin directory.

3. If you work in a Linux environemnt (either a Linux machine or Cygwin/MobaXterm)
in which you cannot push/pull using `git` 
(or you do not to push changes of configurations file to the remote repository 
because the change is only for that environment only), 
you should make a local copy of configuration file.
For example, 
if you work on a computer name "y570" 
and you do not want to push changes of `export.sh` made on this machine, 
you'd better put these changes into a new file 
named `export_y570.sh` in the same directory.

1. keep local config files is a good idea, anyway you don't need them in other places
