#!/bin/bash

if [[ $(id -u) == 0 ]]; then
    prefix=''
else
    prefix=sudo
fi
$prefix apt-get install python3 python3-setuptools python3-pip
pip3 install --user loguru

mkdir -p $HOME/archives
git clone git@github.com:dclong/blog.git $HOME/archives/blog
git clone git@github.com:dclong/config.git $HOME/archives/config
git clone git@bitbucket.org:dclong/dsutil.git $HOME/archives/dsutil

$HOME/archives/config/linstall.py sshc -ic
$HOME/archives/config/linstall.py ipy3 -ic
$HOME/archives/config/linstall.py svim -ic