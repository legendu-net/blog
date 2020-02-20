Status: published
Date: 2020-02-20 15:04:45
Author: Benjamin Du
Slug: packaging-python-dependencies-for-pyspark-using-pex
Title: Packaging Python Dependencies for PySpark Using Pex
Category: Programming
Tags: programming, PySpark, Python, dependency, packaging, pex

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.


1. Unlike `conda-pack`,
    you do need to have `pyspark` installed in the pex environment file 
    to work with PySpark.
    It is suggested that you also have `findspark` installed 
    (for locating Spark/Python if `PYTHONPATH` is not set.).

        :::bash
        #!/bin/bash

        /apache/spark2.3/bin/spark-submit \
            --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
            --master yarn \
            --deploy-mode cluster \
            --queue YOUR_QUEUE \
            --num-executors 200 \
            --executor-memory 10G \
            --driver-memory 15G \
            --executor-cores 4 \
            --conf spark.yarn.maxAppAttempts=2 \
            --conf spark.dynamicAllocation.enabled=true \
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --conf spark.pyspark.driver.python=./env.pex \
            --conf spark.pyspark.python=./env.pex \
            --conf spark.executorEnv.PEX_ROOT=./tmp \
            --files env.pex \
            $1


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

3. Now you can use the `pex` comamnd to 
    [build pex environment files as usual](http://www.legendu.net/misc/blog/tips-on-pex/). 
    The built pex environment files use `./tmp` as thee pex root directory by default.

4. If you run into the following Py4JError,
    then either set the environment variable PYTHONPATH (Python path in Spark),
    or use `findspark` to locate Spark in your Python code.

        :::python
        import findspark
        findspark.init("/apache/spark")

    For more details, 
    please refer to 
    [Run pyspark scripts with python3 instead of pyspark](https://hang-hu.github.io/spark/2018/10/31/Run-pyspark-scripts-with-python3-instead-of-pyspark.html)
    .

    > Py4JError: An error occurred while calling None.org.apache.spark.api.python.PythonAccumulatorV2. Trace:
    > py4j.Py4JException: Constructor org.apache.spark.api.python.PythonAccumulatorV2([class java.lang.String, class java.lang.Integer, class java.lang.String]) does not exist


If you found this to be too much hassle
or if you do not mind of the higher overhead/latency,
conda-pack is a better option to use with PySpark.
Please refer to
[Packaging Python Dependencies for PySpark Using Conda-Pack](http://www.legendu.net/misc/blog/packaging-python-dependencies-for-pyspark-using-conda-pack/)
for more details on how to use conda-pack with PySpark.

## References

https://github.com/pantsbuild/pex

https://medium.com/criteo-labs/packaging-code-with-pex-a-pyspark-example-9057f9f144f3

[Run pyspark scripts with python3 instead of pyspark](https://hang-hu.github.io/spark/2018/10/31/Run-pyspark-scripts-with-python3-instead-of-pyspark.html)

