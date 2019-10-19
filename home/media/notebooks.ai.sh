#!/bin/bash

ln -svf /app/ /workdir/
mkdir -p /app/pkgs
apt-get update -y
apt-get install -y wajig git
pip3 install pelican loguru
mkdir -p archives
ln -svf /app/archives /root/
# blog
if [[ ! -e archives/blog ]]; then
    git clone git@github.com:dclong/blog.git archives/
fi
git -C archives/blog submodule init
git -C archives/blog submodule update --recursive --remote
# config
if [[ ! -e archives/config ]]; then
    git clone git@github.com:dclong/config.git archives/
fi
python3 archives/config/linstall.py poetry -ic
python3 archives/config/linstall.py xonsh -ic
python3 archives/config/linstall.py bash_it -ic
python3 archives/config/linstall.py svim -ic
