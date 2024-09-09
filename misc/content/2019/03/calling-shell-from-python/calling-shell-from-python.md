Status: published
Date: 2019-03-24 06:48:05
Modified: 2019-08-24 06:48:05
Author: Benjamin Du
Slug: calling-shell-from-python
Title: Calling Shell from Python
Category: Computer Science
Tags: programming, Python, shell, os.system, subprocess

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. `subprocess.run` is preferred to the function `os.system`
    for invoking shell commands. 
    For more discussions,
    pleaser refer to 
    [Hands on the Python module subprocess]https://www.legendu.net/en/blog/hands-on-the-python-model-subprocess
    .

2. There are multiple ways to feed input to a shell command programmatically
    instead of interactively via stdin.

    1. Pipe is used to feed the output (text) of a shell command 
        as the input to another shell command.
        What if you have something that is not the output a shell command?
        A simple trick is to echo it and feed it to the shell command.
        The command below is an example 
        of feeding password to the shell command `kinit`.

            :::bash
            echo 'your_password' | kinit

    2. The above trick can be used both for `os.system`
        and `subprocess.run` (with `shell=True`).
        However, 
        `subprocess.run` has an better built-in support 
        to feed input to a shell command via the `input` parameter.

            :::python
            subprocess.run(["kinit"], input=b"your_password")

    3. pexpect

## [shlex](https://docs.python.org/3/library/shlex.html)

Parsing Shell commands.

## References

https://docs.python.org/3/library/subprocess.html
