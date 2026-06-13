---
title: Tips on conda-pack
created: '2021-04-30T12:13:17-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-conda-pack
license: CC-BY-4.0
tags:
  - programming
  - conda-pack
  - conda
  - dependency
  - virtual environment
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**
It is suggested that you use python-build-standlone instead of conda-pack to build portable Python environments.
Please refer to
[Packaging Python Dependencies for PySpark Using Python-Build-Standalone](packaging-python-dependencies-for-pyspark-using-python-build-standalone)
for more details.

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. All packages in a virtual environment must be managed by conda (rather than pip)
   so that it can be packe using conda-pack.

1. When using a conda-pack virtual environment with PySpark,
   the Python package `pyyspark` comes with Spark is automatically injected into PYTHONPATH
   so that users do not have to install `pyspark` into the virtual environemnt by themselves.
   As a matter of fact,
   the `pyspark` comes with Spark is always used
   even if you have a local copy installed
   when you submit a PySpark application with a conda-pack virtual environment.
   For more discussions,
   please refer to [this isue](https://github.com/conda/conda-pack/issues/102).

## References

[Pack a Conda Virtual Environment](tips-on-conda-pack-a-conda-virtual-environment)

https://conda.github.io/conda-pack/

https://conda.github.io/conda-pack/cli.html
