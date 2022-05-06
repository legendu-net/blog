#!/bin/bash
# symbolic link
ln -svf $(pwd)/blog.py ~/.local/bin/blog

# deps
if [ $(hostname) != "jupyterhub-pelican" ]; then
    python3 -m pip install \
        loguru \
        beautifulsoup4 typogrify \
        pelican "pelican-jupyter==0.10.0" pelican-render-math \
        "dsutil[jupyter] @ git+https://github.com/dclong/dsutil@main"
fi

# git submodules
git submodule init && git submodule update --recursive --remote

