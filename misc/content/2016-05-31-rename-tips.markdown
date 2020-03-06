Status: published
Date: 2019-04-18 17:57:21
Author: Ben Chuanlong Du
Slug: rename-tips
Title: Tips About "rename" 
Category: OS
Tags: Linux, rename, shell, tip

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Change names of `.txt` files to lowercase.
```bash
rename 'y/A-Z/a-z/' *.txt
```

Get rid of `(1)` in file names.
```bash
rename 's/\(1\)//' * 
```

