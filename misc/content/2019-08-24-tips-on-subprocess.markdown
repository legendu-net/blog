Status: published
Date: 2019-08-27 09:39:18
Author: Benjamin Du
Slug: tips-on-subprocess
Title: Tips on Subprocess
Category: Programming
Tags: programming, Python, subprocess, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. The method `subprocess.run` is preferred over the older high-level APIs 
    (`subprocess.call`, `subprocess.check_call`, `subprocess.check_output`).
    The method `subprocess.Popen` (which powers the high-level APIs) can be used if you need advanced control.

2. To suppress the output of `subprocess.run`,
    you can redirect the output to `/dev/null`.
        :::Python
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

3. To capture the output, you have to use the option `stdout=PIPE`.

        :::python
        import subprocess sp
        process = sp.run(['ls', '-l'], stdout=sp.PIPE)
        print(process.stdout)

    Similarly, to capture to the output, you have to use the option `stderr=PIPE`.

        :::python
        import subprocess as sp
        process = sp.run(['ls', '-l'], stdout=sp.PIPE, stderr=sp.PIPE)
        print(process.stdout)
        print(process.stderr)

    To capture both the output and the error in one place, you can use the options `stdout=PIPE, stderr=STDOUT`

        :::python
        import subprocess as sp
        process = sp.run(['ls', '-l'], stdout=sp.PIPE, stderr=sp.STDOUT)
        print(process.stdout)

    Notice that in Python 3.7+ you can capture the output and error by one simple option `capture_output=True`.
    It is equivalent to the options `stdout=PIPE, stderr=PIPE` in older versions of Python.

3. Sometimes running `subprocess.run(cmd)` in a JupyterLab notebook prints nothing even the command `cmd` indeed has output in command-line.
  This is likely due to the fact that the command `cmd` output everything to stderr instead of stdout by mistake.
  

## subprocess.Popen

https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python

```
import subprocess
import shlex
import time

def run_command(cmd):
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            print('----')
        time.sleep(1)
    rc = process.poll()
    return rc
```

## Comparison of Differenct Devices

1. `sys.stdout` is the standard output stream.
  `subprocess.STDOUT` refers to the standard out stream of subprocess.
  It is either `subprocess.PIPE` or `None`.
    :::python
    os.devnull
    subprocess.DEVNULL
    with open(os.devnull, 'w') as devnull:
        pass


## References 

https://docs.python.org/3/library/subprocess.html#subprocess.Popen

https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python

https://codecalamity.com/run-subprocess-run/

https://stackoverflow.com/questions/53209127/subprocess-unexpected-keyword-argument-capture-output
