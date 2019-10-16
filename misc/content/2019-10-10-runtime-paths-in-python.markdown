Status: published
Date: 2019-10-16 01:24:46
Author: Benjamin Du
Slug: runtime-paths-in-python
Title: Runtime Paths in Python
Category: Programming
Tags: programming, Python, runtime paths

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

`__file__` is the path of the Python script.
Note that if you make a sybolic link to a Python script and run the symbolic link, 
then `__file__` is the path of the symbolic link.
Of course, you can use `os.path.realpath` to get real path of files.
`os.getcwd()` and `'.'` returns/represents the path where the Python script was invoked,
which is often different from `__file__`.
