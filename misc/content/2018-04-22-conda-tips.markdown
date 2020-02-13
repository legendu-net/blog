Status: published
Date: 2020-02-13 10:36:13
Author: Ben Chuanlong Du
Slug: conda-tips
Title: Tips on Conda
Category: Programming
Tags: programming, Python, conda, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. conda and executables installed by conda might not be able to run by sudo directly. 
    If this happends, 
    use the full path of the executable
    or add the option `-E "PATH=$PATH"` to sudo.
    
        sudo -E env "PATH=$PATH" <command> [arguments]

2. By defaut, conda installs things into /opt/conda.

## Conda Environment

Create a conda virtual environment with Python 3.7, numpy, pandas and scikit-learn installed.
    :::bash
    conda create -n myenv python=3.7 numpy pandas scikit-learn

The virtual environment can be packed 
([conda-pack](https://conda.github.io/conda-pack/index.html) required) 
into a `tar.gz` file 
and be used on other machines with the same type of OS.

    :::bash
    conda activate myenv
    conda pack -o myenv.tar.gz

If you have issues creating a conda virtual environment 
(e.g., due to package not found in the current conda channel),
you can create a bare conda virtual environment,
install `pip` into the environment 
and then use `pip` to install the needed packages.
For example,
the below code creates a conda virtual environment 
with the Python package `optimuspyspark` installed.

:::bash
conda create -n optimus
conda activate optimus
conda install pip
pip install optimuspyspark


## Administering a multi-user conda installation

https://conda.io/docs/user-guide/configuration/admin-multi-user-install.html

## My Conda Packages

https://anaconda.org/legendu/sqlalchemy-teradata

## References

https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html
