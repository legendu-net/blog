Status: published
Date: 2019-07-03 07:55:45
Author: Benjamin Du
Slug: tips-on-xonsh
Title: Tips on Xonsh
Category: Programming
Tags: programming, Python, shell, xonsh, Python evaluation

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

https://github.com/xonsh/xonsh/wiki/Cheatsheet

## Python Evaluation

### [Python Evalation with `@()`](https://xon.sh/tutorial.html#python-evaluation-with)

The code below prints `1 2 3` in xonsh.
```xonsh
x = [1, 2, 3]
echo @(x)
```

### Python Evalation with f-string.

The Python variales are casted to string directly.
For example, 
the code below prints `[1, 2, 3]` in xonsh.
```xonsh
x = [1, 2, 3]
echo f'{x}'
```

## Force (Shell) Subprocess

1. use `os.system` or `subprocess.run`

2. wrap the command in `$[]`

3. for some commands, you just need to put part of it into single/double quotes.
    For example, 
    xonsh fails to recognize `pip3 install dask[complete]` as a shell command 
    while it recognize `pip3 install "dask[complete]"` as a shell command.


[Bash to Xonsh Translation Guide¶](https://xon.sh/bash_to_xsh.html)
