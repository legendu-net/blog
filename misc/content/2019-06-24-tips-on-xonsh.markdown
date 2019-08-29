Status: published
Date: 2019-08-29 19:30:28
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

## Background Mode for Subprocess

https://github.com/xonsh/xonsh/issues/1477#event-2481368935

## References

[Bash to Xonsh Translation Guide¶](https://xon.sh/bash_to_xsh.html)

[Run Control File](https://xon.sh/xonshrc.html)

[Updating and customizing xonsh](https://xon.sh/customization.html)

[Environment Variables](https://xon.sh/envvars.html)

[Xonribs](https://xon.sh/xontribs.html)

[Environment Variables](https://xon.sh/envvars.html)

https://github.com/xonsh/xonsh/issues/1477#event-2481368935

https://stackoverflow.com/questions/39724184/how-to-write-a-multi-command-alias-in-xonsh/39761905#39761905
