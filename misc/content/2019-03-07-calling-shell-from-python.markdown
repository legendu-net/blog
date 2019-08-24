Status: published
Date: 2019-08-24 05:59:01
Author: Benjamin Du
Slug: calling-shell-from-python
Title: Calling Shell from Python
Category: Programming
Tags: programming, Python, shell, os.system, subprocess

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



1. It is suggested that you always use full path of command as the environment is not always identical across machines.

2. Generally speaking,
    functions in the module `subprocess` are preferred to the function `os.system`
    as functions in the module `subproces` are more flexible. 
    However, 
    be careful when you use `subprocess.call` to replace `os.system`.
    You might want to pass the option `check=True` 
    to turn on exception throwing on erros (turned off by default)
    if the status of running a command matters. 

3. `echo` and pipe is common trick to feed input into another comamnd. 
    For exampel, 
    suppose `kinit` is an authentication command that takes a password interactively,
    you can use the following command to authenticate directly without typing password interactively.

        echo 'your_password' | kinit

    This trick works with the `os.system` function in Python.
    Basically `os.system` takes whatever you run in shell and run it.
    Methods in `subprocess` does not take pipe commands by default. 
    If the pipe is used to feed input into another command,
    you can simply use the `input` argument of methods in `subprocess`.
    For example,

        subprocess.check_output(['kinit'], input=b'your_password')

    If you do want to use pipe directly in methods of `subprocess`, 
    you can set the option `shell=True`.


## subprocess

1. It is suggested that you use the method `subprocess.run` as much as possible 
  instead of the older high-level APIs (`subprocess.call`, `subprocess.check_call`, `subprocess.check_output`).
```
sys.stdout
subprocess.STDOUT
os.devnull
subprocess.DEVNULL

with open(os.devnull, 'w') as devnull:
    pass
```


To suppress the output, you can redirect to /dev/null

import os
import subprocess

with open(os.devnull, 'w') as devnull:
    subprocess.run(['ls', '-l'], stdout=devnull)
    # The above only redirects stdout...
    # this will also redirect stderr to /dev/null as well
    subprocess.run(['ls', '-l'], stdout=devnull, stderr=devnull)
    # Alternatively, you can merge stderr and stdout streams and redirect
    # the one stream to /dev/null
    subprocess.run(['ls', '-l'], stdout=devnull, stderr=subprocess.STDOUT)
If you want to capture the output (to use later or parse), you need to use subprocess.PIPE

import subprocess
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout)

# To also capture stderr...
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout)
print(result.stderr)

# To mix stdout and stderr into a single string
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(result.stdout)

## Capture Output

1. You can use the option `capture_output=True` in Python 3.7+.
  And you can emulate this using `stdout=PIPE, stderr=PIPE` in Python 3.6.
  

https://stackoverflow.com/questions/53209127/subprocess-unexpected-keyword-argument-capture-output


## [shlex](https://docs.python.org/3/library/shlex.html)

Parsing Shell commands.


## References

https://stackoverflow.com/questions/41171791/how-to-suppress-the-output-of-subprocess-run

https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline

https://docs.python.org/3/library/subprocess.html#replacing-os-system
