Status: published
Date: 2019-06-26 18:36:06
Author: Benjamin Du
Slug: tips-on-xonsh
Title: Tips on Xonsh
Category: Programming
Tags: programming, Python, shell, xonsh, Python evaluation

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


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


[Bash to Xonsh Translation Guide¶](https://xon.sh/bash_to_xsh.html)
