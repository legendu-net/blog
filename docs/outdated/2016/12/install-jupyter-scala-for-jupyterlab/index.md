---
title: Install Jupyter-Scala for JupyterLab
created: '2016-12-10T01:52:37-08:00'
date: '2026-11-15T09:28:38-08:00'
authors:
  - bendu
label: install-jupyter-scala-for-jupyterlab
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - Jupyter
  - JupyterLab
  - jupyter-scala
  - kernel
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Note: Apache Toree is a better alternative than Jupyter Scala.
It is suggested that you use Apache Toree instead of Jupyter Scala.

You can install Jupyter Scala following the steps below.

1. Make sure Java and Scala are installed.

   ```
    sudo apt install openjdk-8-jdk scala
   ```

1. Download coursier and move it to a searchable path.
   I place it in `$HOME/bin` which I have included in `$PATH`.

   ```
    curl -L -o coursier https://git.io/vgvpD && chmod +x coursier 
   ```

1. Clone the jupyter-scala repository.

   ```
    git clone git@github.com:alexarchambault/jupyter-scala.git
   ```

1. Run the following command insider the directory to install Jupyter Scala.

   ```
    ./jupyter-scala
   ```

   You might have issues due to no permission to create directories/files under `$HOME/.local/share/jupyter`.
   If that happens,
   change the permission of the directory and try again.

   ```
    sudo chmod -R 777 $HOME/.local/share/jupyter
   ```
