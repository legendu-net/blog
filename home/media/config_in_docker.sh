#!/bin/bash

# link from home_host
cp -r /home_host/chdu/.ssh $HOME/
ln -svf /home_host/chdu/archives $HOME/
ln -svf /home_host/chdu/.dbay_profile $HOME/
ln -svfT /workdir/user/chdu $HOME/projects

# install Python packages
pip3 install --user --upgrade /workdir/pkgs/dbay-*.*.*.whl
pip3 install --user --upgrade /workdir/pkgs/dsutil-*.*.*.whl

$HOME/archives/config/linstall.py ipy3 -c
