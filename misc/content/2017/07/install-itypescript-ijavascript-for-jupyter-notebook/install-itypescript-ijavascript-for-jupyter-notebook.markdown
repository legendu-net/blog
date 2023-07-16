UUID: 403e0a6d-a732-4cdf-a3e5-09f30bdece08
Status: published
Date: 2017-07-22 12:33:12
Author: Ben Chuanlong Du
Slug: install-itypescript-ijavascript-for-jupyter-notebook
Title: Install ITypescript/IJavascript for Jupyter Notebook
Category: Computer Science
Tags: programming, Jupyter Notebook, JavaScript, JS, TypeScript, IJavascript, ITypeScript
Modified: 2017-10-22 12:33:12

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

https://github.com/nearbydelta/itypescript

https://github.com/n-riesco/ijavascript/

    wajig install nodejs npm
    sudo ln -s /usr/bin/nodejs /usr/bin/node

    sudo npm install -g itypescript
    sudo its --hide-undefined --ts-install=global


    sudo npm install -g ijavascript
    sudo ijsinstall --hide-undefined --install=global
