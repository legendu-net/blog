Status: published
Date: 2020-02-19 01:30:10
Author: Benjamin Du
Slug: packaging-python-dependencies-for-pyspark-using-pex
Title: Packaging Python Dependencies for PySpark Using Pex
Category: Programming
Tags: programming, PySpark, Python, dependency, packaging, pex

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

pip3 install git+https://github.com/dclong/pex

https://github.com/pantsbuild/pex

https://medium.com/criteo-labs/packaging-code-with-pex-a-pyspark-example-9057f9f144f3

By default,
the pex root directory 
(controled by the option `--pex-root` or the environment variable `PEX_ROOT`) 
is `~/.pex`.
Some Spark cluster might not be configured correctly 
for the default pex root to work well.
For example,
I've seen a Spark cluster configures `$HOME` to be `/home`
which makes the default pex root directory to be `/home/.pex`.
This causes permission issues 
as users do not have previleges to create the directory on executor containers.
If this happens, 
you have to set the environment variable `PEX_ROOT` 
to a writable location using thee option `--conf` 
when submitting your PySpark application,
e.g., `--conf spark.executorEnv.PEX_ROOT=./tmp`.
If this doesn't work either (due to Spark issues),
there is one last hacking way (not recommended) to work around it.
The details instructions of the hacking way are listed below.

1. Modified the source code of pex to use `./tmp` 
    as the pex root by default 
    (so that you do not have specify the environment variable `PEX_ROOT`).
    For example,
    dclong/pex is such a fork. 

2. Install the fork (taking dclong/pex as example) using the following command.

        :::bash
        pip3 install git+https://github.com/dclong/pex

3. Now you can use the `pex` comamnd to build pex environment files as usual. 
    The built pex environment files use `./tmp` as thee pex root directory by default.


