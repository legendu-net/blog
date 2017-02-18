UUID: 3fb54c7a-12bb-443b-817b-5aef23d29b8c
Status: published
Date: 2016-12-06 23:15:59
Author: Ben Chuanlong Du
Slug: install-r-kernel-for-jupyterlab
Title: Install R Kernel for JupyterLab
Category: Programming
Tags: programming, R, CRAN, IRKernel, Jupyter, JupyterLab

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. Install JupyterLab.
```bash
wajig install python3 python3-pip
sudo -H pip3 install jupyter jupyterlab
sudo jupyter serverextension enable --py jupyterlab --sys-prefix
```

2. Install dev libraries required by IRKernel (or its dependent packages). 
```bash
wajig install libssl-dev libcurl4-openssl-dev
```
If you are still on Ubuntu 14.04, 
you might have to force `libssl` to downgrade. 
```bash
wajig install libssl1.0.0/trusty
```

3. Upgrade R to the latest version.
```bash
wajig update && wajig install r-base-core
```

4. Upgrade R packages to the latest version. 
Open an R sesseion using `sudo` and run the following statement. 
It takes a while, so be patient. 
```R
update.packages(ask = F, checkBuilt = T)
```

5. Install dependencies R packages of IRKernel.
Run the following command in R.
```R
install.packages(c('repr', 'IRdisplay', 'crayon', 'pbdZMQ', 'devtools'))
devtools::install_github('IRkernel/IRkernel')
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
Second, edit the configuration file as neede. 
    - ip
    - browser 
    - working directory

7. Make sure that the directory `~/.local/share/jupyter` and its subcontents belogn to you rather than `root`.
If they belong to `root` then change the own to you by running the following command.
```bash
sudo chown -R username:usergroup ~/.local/share/jupyter
```

8. Start JupyterLab.
```bash
nohup jupyter lab &
```

## Trouble Shooting

1. Notice that you'd better turn off proxies while using JupyterLab. 


