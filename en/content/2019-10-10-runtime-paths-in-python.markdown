Status: published
Date: 2019-10-16 09:56:13
Author: Benjamin Du
Slug: runtime-paths-in-python
Title: Runtime Paths in Python
Category: Programming
Tags: programming, Python, runtime paths


`__file__` is the path of the Python script.
Note that if you make a sybolic link to a Python script and run the symbolic link, 
then `__file__` is the path of the symbolic link.
Of course, you can use `os.path.realpath` to get real path of files.


`os.getcwd()` and `'.'` returns/represents the path where the Python script was invoked,
which is often different from `__file__`.
