#!/bin/bash
# symbolic link
ln -svf $(pwd)/blog.py ~/.local/bin/blog

# deps
if [ $(hostname) != "jupyterhub-pelican" ]; then
    python3 -m pip install \
        loguru \
        beautifulsoup4 typogrify \
        pelican "pelican-jupyter==0.10.0" pelican-render-math \
        aiutil[jupyter]
fi

# git submodules
git submodule init && git submodule update --recursive --remote

