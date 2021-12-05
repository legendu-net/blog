Status: published
Date: 2021-06-08 08:42:41
Author: Benjamin Du
Slug: vim-keybinds-for-cells-in-jupyterlab-notebooks
Title: Vim Keybinds for Cells of JupyterLab Notebooks
Category: Computer Science
Tags: Computer Science, software, tools, Jupyter, JupyterLab, notebook, cell, Vim, keybindings
Modified: 2021-12-04 20:20:12
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [Firenvim](https://github.com/glacambre/firenvim)
[Firenvim](https://github.com/glacambre/firenvim)
turns your browser into a NeoVim client
which means that you can use it to interact with Jupyter/Lab notebooks using NeoVim.

## [jupyterlab-vim](https://github.com/jwkvam/jupyterlab-vim)
[jupyterlab-vim](https://github.com/jwkvam/jupyterlab-vim)
is a JupyterLab extension which brings Vim keybindings to cells of JupyterLab notebooks.
It can be installed using the following command in JupyterLab 3+.

    :::bash
    pip3 install jupyterlab_vim

And it can be uninstalled using the following command.

    :::bash
    pip3 uninstall jupyterlab_vim

By default, 
a JupyterLab extension is enabled after installtion.
You can disable an extension, 
e.g., jupyterlab_vim, using the following command. 

    :::bash
    sudo jupyter labextension disable @axlair/jupyterlab_vim

And enable it again using the command below.

    :::bash
    sudo jupyter labextension enable @axlair/jupyterlab_vim

## [magma-nvim](https://github.com/dccsillag/magma-nvim)
[magma-nvim](https://github.com/dccsillag/magma-nvim)
enables you to interact with Jupyter/Lab notebooks from NeoVim.

## References 

[Jupyter Notebook + Vim/Neovim](https://alpha2phi.medium.com/jupyter-notebook-vim-neovim-c2d67d56d563)


