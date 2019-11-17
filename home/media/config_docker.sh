#!/bin/bash

cp -r /home_host/$(id -un)/.ssh $HOME/
ln -svf /home_host/$(id -un)/archives $HOME/
ln -svfT /workdir/user/$(id -un) $HOME/projects

xinstall --sudo git -ic
xinstall svim -ic
xinstall ipy3 -c
xinstall dsutil -ic
