Status: published
Date: 2019-10-15 21:03:59
Author: Benjamin Du
Slug: configuration-scripts-for-the-blog-project-on-notebooks.ai
Title: Configuration Scripts for the Blog Project on Notebooks.Ai
Category: Programming
Tags: programming, notebooks.ai, blog, configuration script

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

# TODO: save the following code as script and provide a comamnd download and run it!!!

    :::Bash
    #!/bin/bash

    ln -svf /app/ /workdir/
    mkdir /workdir/pkgs
    apt-get update
    apt-get install wajig git
    pip3 install pelican
    mkdir -p archives
    ln -svf /app/archives /root/
    cd archives
    # blog
    if [[ ! -e blog ]]; then
        git clone git@github.com:dclong/blog.git
    fi
    git submodule init
    git submodule update --recursive --remote
    # config
    if [[ ! -e config ]]; then
        git clone git@github.com:dclong/config.git
    fi
    config/linstall.py poetry -ic
    config/linstall.py xonsh -ic
    config/linstall.py bash_it -ic
    config/linstall.py svim -ic