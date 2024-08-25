#!/bin/bash
# symbolic link
mkdir -p $HOME/.local/bin/
ln -svfT "$(pwd)/blog.py" $HOME/.local/bin/blog

# deps
if [ $(hostname) != "jupyterhub-pelican" ]; then
    python3 -m pip install --user --break-system-packages \
        loguru \
        pyyaml \
        beautifulsoup4 typogrify \
        pelican "pelican-jupyter==0.10.0" pelican-render-math \
        aiutil[jupyter]
fi

# git submodules
#git submodule init && git submodule update --recursive --remote

