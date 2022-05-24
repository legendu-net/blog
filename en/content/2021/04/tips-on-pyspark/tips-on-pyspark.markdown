Status: published
Date: 2021-04-30 11:49:58
Modified: 2022-05-19 02:25:00
Author: Benjamin Du
Slug: tips-on-pyspark
Title: Process Big Data Using PySpark
Category: Computer Science
Tags: programming, PySpark, Python, Spark, tips, HPC, high performance computing

1. PySpark 2.4 and older does not support Python 3.8.
    You have to use Python 3.7 with PySpark 2.4 or older.

2. It can be extremely helpful to run a PySpark application locally to detect possible issues
    before submitting it to the Spark cluster.

        :::bash
        #!/usr/bin/env bash
        PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
        /path/to/spark-2.3.1-bin-hadoop2.7/bin/spark-submit \
            --conf spark.yarn.maxAppAttempts=1 \
            --conf spark.yarn.appMasterEnv.ARROW_PRE_0_15_IPC_FORMAT=1 \
            --conf spark.executorEnv.ARROW_PRE_0_15_IPC_FORMAT=1 \
            --conf spark.sql.execution.arrow.enabled=True \
            --conf spark.pyspark.driver.python=.venv/bin/python3 \
            --conf spark.pyspark.python=.venv/bin/python3 \
            script_to_run.py --arg1 v1 --arg2 v2

3. You can run PySpark interactively using the `pyspark` command
  and submit a PySpark job to the cluster using the `spark-submit` command.
	For more details, 
	please refer to
	[Launching Applications with spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit).
    Below is an example of shell script for submitting a PySpark job using `spark-submit`.

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
            --conf spark.yarn.appMasterEnv.ARROW_PRE_0_15_IPC_FORMAT=1 \
            --conf spark.executorEnv.ARROW_PRE_0_15_IPC_FORMAT=1 \
            --conf spark.sql.execution.arrow.enabled=True \
            --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G \
            --conf spark.pyspark.driver.python=/usr/share/anaconda3/bin/python \
            --conf spark.pyspark.python=/usr/share/anaconda3/bin/python \
            /path/to/_pyspark.py

    If you use a portable Python environment named `env.tar.gz`,
    you can submit a PySpark application using the following shell script.

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
            --conf spark.yarn.appMasterEnv.ARROW_PRE_0_15_IPC_FORMAT=1 \
            --conf spark.executorEnv.ARROW_PRE_0_15_IPC_FORMAT=1 \
            --conf spark.sql.execution.arrow.enabled=True \
            --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G \
            --conf spark.pyspark.driver.python=./env/bin/python \
            --conf spark.pyspark.python=./env/bin/python \
            --archives env.tar.gz#env \
            $1

    And below is a simple example of `_pyspark.py`.

        :::Python
        from pyspark.sql import SparkSession
        from pyspark.sql.functions import *

        spark = SparkSession.builder.appName("Test PySpark").enableHiveSupport().getOrCreate()
        sql = """
                SELECT * 
                FROM some_table 
                TableSample (100000 Rows)
            """
        spark.sql(sql).write.mode("overwrite").parquet("output")

    Notice that I have prefixed an underscore to the name of the file.
    This is a simple but useful trick to avoid unintentional module conflictions in Python. 
    For example, 
    if you name your PySpark script `pyspark.py`,
    your PySpark application will fail to work 
    as your script `pyspark.py` is loaded as a module named `pyspark` 
    which hides the official `pyspark` module in Python.
    It is suggestion that adopt the trick of "prefixing an underscore to file names"
    when submitting a PySpark job.

4. If you have multiple versions of Spark installed,
    the exported Spark environment variables might intervent with each other 
    and cause some of them fail to work.
    For example, 
    if you have both a cluster version of Spark and a local version of Spark installed,
    you might failed to submit Spark applications using `spark-submit`.
    One simple fix to this problem is 
    to manually configure a right version of the `PATH` environemnt varible 
    before you invoke the command `spark-submit` of the local version of Spark.

        :::bash
        PATH=/bin:/sbin:/usr/bin:/usr/sbin /path/to/spark-submit ...

    As a matter of fact,
    this is the way to fix most PATH related issues in Linux/Unix.

5. PySpark does not support converting `$"col"` to a Column implicitly. 
    However, 
    the function `pyspark.sql.functions.col` works the same as in Spark.

6. [Pandas UDFs](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html#pandas-udfs-aka-vectorized-udfs)
    is preferred to UDFs.
    Please refer to 
    [User-defined Function (UDF) in PySpark](http://www.legendu.net/en/blog/pyspark-udf/)
    for more discussions.

7. [pyspark-stubs](https://github.com/zero323/pyspark-stubs)
    can be leveraged for static type checking for PySpark project.

## Use PySpark in Jupyter/Lab Notebooks

1. The trick is to use the Python library `findspark` to find and initiate Spark for use in notebook. 

        :::python
        from pathlib import Path
        import findspark
        findspark.init(str(next(Path("/opt/").glob("spark-*"))))
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.appName("PySpark_Notebook") \
            .enableHiveSupport().getOrCreate()

    Notice that the following 2 lines of code must be before any code that involving Spark.
    The example here might seems obvious, 
    however,
    it might not so obvious if you import a module which creates a SparkSession object.

        :::python
        from pathlib import Path
        import findspark
        findspark.init(str(next(Path("/opt/").glob("spark-*"))))

2. When working with relatively large data in a local version of Spark in Jupyter/Lab notebook,
    you might easily encounter OOM errors. 
    The trick to increase the driver memory using the option `.config("spark.driver.memory", "50g")`.

        :::python
        from pathlib import Path
        import findspark
        findspark.init(str(next(Path("/opt/").glob("spark-*"))))
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.appName("PySpark_Notebook") \
            .master("local[*]") \
            .config("spark.driver.memory", "50g") \
            .enableHiveSupport().getOrCreate()
        
3. The command-line option `--jars` is equivalent to `spark.jars` when you use `--conf`.
    This means that you can use `.config("spark.jars", "/path/to/file.jar")` 
    to add JARs to a Spark/PySpark application in Jupyter/Lab notebook.

        :::python
        from pathlib import Path
        import findspark
        findspark.init(str(next(Path("/opt/").glob("spark-*"))))
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.appName("PySpark_Notebook") \
            .config("spark.jars", "/path/to/file.jar") \
            .config("spark.driver.memory", "50g") \
            .enableHiveSupport().getOrCreate()

3. If you want to leverage a Spark cluster in a Jupyter/Lab notebook,
    there are a few things (Hadoop queue, driver IP and driver port) you need to configure.
    Below is an illustration.
    
        :::python
        import socket
        import findspark
        findspark.init("/apache/spark2.3")
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.master("yarn").appName("PySpark_Cluster") \
            .config("spark.yarn.queue", "your-hadoop-queue>") \
            .config("spark.driver.host", socket.gethostbyname(socket.gethostname())) \
            .config("spark.driver.port", "30202") \
            .enableHiveSupport().getOrCreate()

    Notice that the SparkContext object will be expired after inactive for a while.
    It won't help if you run the above code again in notebook
    because a SparkSession (even if it is invalid any more due to expiration of the underlying SparkContext) has already been created.
    You can of course restart the Python kernel and then create a new SparkSession.
    However, 
    you will lose all Python objects in the notebook by doing this.
    A better alternative is to manually stop the SparkSession by calling `spark.stop()` 
    and then run the above code in notebook again.
    This way, the Python objects (e.g., pandas DataFrame you have created)
    will still be alive for you to use.

5. When you run Spark or PySpark in a Jupyter/Lab notebook, 
    it is recommended that you show ERROR messages only. 
    Otherwise, 
    there might be too much logging information polluting your notebook. 
    You can set the log level of Spark to `ERROR` using the following line of code.

        :::python
        spark.sparkContext.setLogLevel("ERROR")

    For more details, 
    please refer to 
    [Configure Log4J for Spark](http://www.legendu.net/misc/blog/configure-log4j-for-spark/)
    .

## Python Dependencies for PySpark

Listed below are several ways to handle dependencies for PySpark.

1. [Build a portable Python environment using python-build-standalone](http://www.legendu.net/en/blog/packaging-Python-Dependencies-for-PySpark-Using-python-build-standalone)
2. [Build a portable Python environment using conda-pack](http://www.legendu.net/en/blog/packaging-python-dependencies-for-pyspark-using-conda-pack)
3. [Packaging Python dependencies using pex](http://www.legendu.net/misc/blog/packaging-python-dependencies-for-pyspark-using-pex)

Building a portable Python environment using python-build-standalone is the recommended approach.

## References

- [PySpark API Reference](https://spark.apache.org/docs/latest/api/python/reference/)

- [Best Practices Writing Production-Grade PySpark Jobs](https://developerzen.com/best-practices-writing-production-grade-pyspark-jobs-cb688ac4d20f)

- [Packaging code with PEX — a PySpark example](https://medium.com/criteo-labs/packaging-code-with-pex-a-pyspark-example-9057f9f144f3)

- [awesome-spark](https://github.com/awesome-spark/awesome-spark)
