Status: published
Date: 2019-03-07 03:32:59
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
		as the first one will throw exception on errors


`os.system` works on `echo 'password' | kinit`
however sp.check_out(['echo', password, '|', 'kinit']) doesn't work

I think you should use the input parameter to pass password to kinit ...<Paste>


