---
title: Install the rJava Package in R
created: '2013-12-10T01:44:32-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: install-the-rjava-package-in-r
license: CC-BY-4.0
tags:
  - R
  - rJava
  - Java
  - Linux
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

The most convenient way is to install the corresponding Linux package if exists.

```R
sudo apt-get install r-cran-rjava
```

However, this Linux package is often outdated.
Follow the steps below if you'd rather install rJava manually.

1. Install OpenJDK and configure Java.

   ```
    sudo apt-get install openjdk-7-*
    sudo R CMD javareconf
   ```

1. Install the `rJava` package in R.

   ```
    install.packages("rJava").
   ```

If it does not work,
please set the `JAVA_HOME` environment variable manually in step 1
and then try step 2 again.

```Bash
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre
```
