UUID: 467c9878-be45-4928-8b4e-d8dd97be3691
Status: published
Date: 2016-08-15 21:47:25
Author: Ben Chuanlong Du
Slug: rename-tips
Title: Tips About "rename" 
Category: Linux
Tags: Linux, rename, shell, tip

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Change all PDF names to lowercase.
```bash
rename 'y/A-Z/a-z/' *.pdf
```
Get rid of `(1)` in file names.
```bash
rename 's/\(1\)//' * 
```

