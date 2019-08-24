Status: published
Date: 2019-08-24 17:40:29
Author: Benjamin Du
Slug: tips-on-subprocess
Title: Tips on Subprocess
Category: Programming
Tags: programming, Python, subprocess, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

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

## To also capture stderr...

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


## References 

https://docs.python.org/3/library/subprocess.html#subprocess.Popen

https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python

https://codecalamity.com/run-subprocess-run/
