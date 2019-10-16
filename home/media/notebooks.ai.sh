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