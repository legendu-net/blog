Status: published
Date: 2019-04-29 10:02:51
Author: Ben Chuanlong Du
Slug: shell-alternatives
Title: Shell Alternatives
Category: Programming
Tags: programming, IPython, shell, bash, xonsh, plumbum

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## [IPython](https://github.com/ipython/ipython)

IPython is the best and simpliest Python approach to replace shell so far. 

https://ipython.readthedocs.io/en/stable/interactive/magics.html

https://github.com/ivanov/vim-ipython

1. Use the IPython shell or JupyterLab notebook (preferred) instead of Shell for complicated interactive operations.

2. Be careful about illegal shell commands. 
    For example, 
    `ls )` in Bash shell throws the error message `bash: syntax error near unexpected token )`.
    If you have a equivalent IPython command,
    it will throw the same error message.
    For example, 
    suppose `file` is path of a file which contains `)`
    then `!ls {file}` in IPython will throws the same error message as above. 
    However, 
    this is definitely trickier to debug than the original Bash shell command `ls )`. 
    There are several ways to avoid this.
    First, 
    you can use Python script 
    ([xonsh](https://github.com/xonsh/xonsh) is a great choice is vanilla Python script is too verbose) 
    instead Shell as underlying commands.
    Second, 
    you can show the underlying Shell commands for debugging.

3. You can even run Shell commands on a remote server (via `ssh` or a remote kernel) in JupyterLab notebook. 
    This provide the advantage of leveraging the JupyterLab notebook UI.


## [xonsh](https://github.com/xonsh/xonsh)

Another Python approach to replace shell. 
It looks interesting and quite promising too.

## [plumbum](https://github.com/tomerfiliba/plumbum)

Yet another Python approach as a replacement of shell. 
I personally prefer IPython and xonsh to plumbum.



## References

https://github.com/ninjaaron/replacing-bash-scripting-with-python

https://stackoverflow.com/questions/209470/how-to-implement-common-bash-idioms-in-python