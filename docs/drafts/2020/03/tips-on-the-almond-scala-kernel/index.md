---
title: Tips on the Almond Scala Kernel
created: '2020-03-24T18:33:39-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: tips-on-the-almond-scala-kernel
license: CC-BY-4.0
tags:
  - computer science
  - Scala
  - Almond
  - JupyterLab
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. `kernel.silent(true)`
   supress outputs of cells.

1. Currently each line in a cell have an output,
   which is messy.
   There are 2 ways to avoid this.

   ```
    :::scala
    val resObj = {
        ...
        ...
    }

    {{
        ...
        ...
    }}
   ```

## References

[Use Spark with the Almond Scala Kernel in JupyterLab](use-spark-with-the-almond-scala-kernel-in-jupyterlab)

[Specify Dependencies in the Almond Scala Kernel in JupyterLab](specify-dependencies-in-the-almond-scala-kernel-in-jupyterlab)
