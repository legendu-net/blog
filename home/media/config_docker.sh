#!/bin/bash

# link from home_host
cp -r /home_host/$(id -un)/.ssh $HOME/
ln -svf /home_host/$(id -un)/archives $HOME/
ln -svf /home_host/$(id -un)/.dbay_profile $HOME/
ln -svfT /workdir/user/$(id -un) $HOME/projects

# install Python packages
pip3 install --user --upgrade /workdir/pkgs/dbay-*.*.*.whl
pip3 install --user --upgrade /workdir/pkgs/dsutil-*.*.*.whl

$HOME/archives/config/linstall.py git -c
$HOME/archives/config/linstall.py svim -ic
$HOME/archives/config/linstall.py ipy3 -c
