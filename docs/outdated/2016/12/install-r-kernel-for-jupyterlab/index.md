---
title: Install R Kernel for JupyterLab
created: '2016-12-25T20:22:24-08:00'
date: '2026-11-15T12:20:06-08:00'
authors:
  - bendu
label: install-r-kernel-for-jupyterlab
license: CC-BY-4.0
tags:
  - programming
  - R
  - CRAN
  - IRKernel
  - Jupyter
  - JupyterLab
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Install JupyterLab.

```bash
sudo apt install python3 python3-pip python3-setuptools
sudo -H pip3 install jupyter jupyterlab
sudo jupyter serverextension enable --py jupyterlab --sys-prefix
```

2. Install dev libraries required by IRKernel (or its dependent packages).

```bash
sudo apt install libssl-dev libcurl4-openssl-dev
```

If you are still on Ubuntu 14.04,
you might have to force `libssl` to downgrade.

```bash
sudo apt install libssl1.0.0/trusty
```

3. Upgrade R to the latest version.

```bash
sudo apt update && sudo apt install r-base-core
```

4. Upgrade R packages to the latest version.
   Open an R sesseion using `sudo` and run the following statement.
   It takes a while, so be patient.

```R
update.packages(ask = F, checkBuilt = T)
```

5. Install IRkernel and register it.

```R
# install dependencies packages of IRKernel
install.packages(c('repr', 'IRdisplay', 'crayon', 'pbdZMQ', 'devtools'))
# install IRkernel
devtools::install_github('IRkernel/IRkernel')
# register IRkernel
IRkernel::installspec() 
```

If for any reason you cannot install devtools,
you can manually download IRkernel and its dependencies and install them.

```R
install.packages('evaluate')
install.packages('uuid')
# assume you have downloaded IRkernel-0.7.1.tar.gz
install.packages('IRkernel-0.7.1.tar.gz')
```

6. Configure JupyterLab.
   First, run the following command to generate a configuration file for JupyterLab.

```bash
jupyter lab --generate-config
```

Second, edit the configuration file as needed.
\- ip
\- browser
\- working directory

7. Make sure that the directory `~/.local/share/jupyter` and its subcontents belogn to you rather than `root`.
   If they belong to `root` then change the own to you by running the following command.

```bash
sudo chown -R username:usergroup ~/.local/share/jupyter
```

8. Start JupyterLab.

```bash
nohup jupyter lab &
```

## Issues

1. Matrices are not displayed correctly.
   They are shown as vectors instead.
   However,
   data frames are displayed correctly.

1. flush.console does not work well.

1. .Last.value retrieves the return value of the last expression in R.
   It is not working in Jupyter 0.7 or older.

1. IRKernel does not implement magics currently.
