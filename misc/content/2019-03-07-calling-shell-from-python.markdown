Status: published
Date: 2019-03-08 02:49:28
Author: Benjamin Du
Slug: calling-shell-from-python
Title: Calling Shell from Python
Category: Programming
Tags: programming, Python, shell

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



1. It is suggested that you always use full path of command as the environment is not always identical across machines.

2. `subprocess.check_output` is prefered over `subprocess.run` or `os.system` 
		as the first one will throw exception on errors.

3. `echo` and pipe is common trick to feed input into another comamnd. 
    For exampel, 
    suppose `kinit` is an authentication command that takes a password interactively,
    you can use the following command to authenticate directly without typing password interactively.

        echo 'your_password' | kinit

    This trick works with the `os.system` function in Python.
    Basically `os.system` takes whatever you run in shell and run it.
    However, 
    the trick does not work for `subprocess.check_output`.
    You have to pass interactive input as bytes to the `input` argument of `subprocess.check_output`.

