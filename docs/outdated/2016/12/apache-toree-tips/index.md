---
title: Apache Toree Tips
created: '2016-12-12T20:32:58-08:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: apache-toree-tips
license: CC-BY-4.0
tags:
  - programming
  - Apache Toree
  - Jupyter
  - notebook
  - JupyterLab
  - Jupyter Lab
  - Spark
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<https://github.com/apache/incubator-toree/blob/master/etc/examples/notebooks/magic-tutorial.ipynb>

```bash
anaconda3/bin/jupyter toree install --user --spark_home=/apache/spark
```

## Dependency Managemnt

```
%AddJar jar_url
%AddDeps
printHelp(printStream, """%AddDeps my.company artifact-id version""")


%AddDeps com.databricks spark-csv_2.10 1.2.0 --transitive


%AddDeps tech.tablesaw tablesaw-core 0.11.6 --transitive


kernel.magics.addDeps("com.databricks spark-csv_2.10 1.2.0 --transitive")


%AddDeps org.apache.spark spark-mllib_2.10 1.6.2
%AddDeps com.github.haifengl smile-core 1.1.0 --transitive
%AddDeps io.reactivex rxscala_2.10 0.26.1 --transitive
%AddDeps com.chuusai shapeless_2.10 2.3.0 --repository https://oss.sonatype.org/content/repositories/releases/
%AddDeps org.tmoerman plongeur-spark_2.10 0.3.9 --repository file:/Users/tmo/.m2/repository


%AddDeps "graphframes" % "graphframes" % "0.1.0-spark1.6" --repository http://dl.bintray.com/spark-packages/maven
```

Currently it supports only https://repo1.maven.org/maven2/, but not all projects deploy there.
