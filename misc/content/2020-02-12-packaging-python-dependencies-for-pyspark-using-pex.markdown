Status: published
Date: 2020-02-19 01:38:08
Author: Benjamin Du
Slug: packaging-python-dependencies-for-pyspark-using-pex
Title: Packaging Python Dependencies for PySpark Using Pex
Category: Programming
Tags: programming, PySpark, Python, dependency, packaging, pex

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

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

4. If you run into the following Py4JError,
    then either set the environment variable PYTHONPATH (Python path in Spark),
    or use `findspark` to locate Spark in your Python code.

        :::python
        import findspark
        findspark.init("/hadoop/spark")

    For more details, 
    please refer to 
    [Run pyspark scripts with python3 instead of pyspark](https://hang-hu.github.io/spark/2018/10/31/Run-pyspark-scripts-with-python3-instead-of-pyspark.html)
    .

    > Py4JError: An error occurred while calling None.org.apache.spark.api.python.PythonAccumulatorV2. Trace:
    > py4j.Py4JException: Constructor org.apache.spark.api.python.PythonAccumulatorV2([class java.lang.String, class java.lang.Integer, class java.lang.String]) does not exist


## References

https://github.com/pantsbuild/pex

https://medium.com/criteo-labs/packaging-code-with-pex-a-pyspark-example-9057f9f144f3

[Run pyspark scripts with python3 instead of pyspark](https://hang-hu.github.io/spark/2018/10/31/Run-pyspark-scripts-with-python3-instead-of-pyspark.html)

