Status: published
Date: 2020-09-20 14:47:06
Author: Benjamin Du
Slug: tips-on-jupyter-book
Title: Tips on Jupyter-Book
Category: Computer Science
Tags: Computer Science, jupyter-book, Markdown, notebook, Jupyter, JupyterLab
Modified: 2022-12-20 17:51:52

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

xinstall jb -ic

## Configuration 

`xinstall jb -c` creates a copy of configuration file `_config.yml` in the current directory.
By default,
The configuration file `_config.yml` in the current directory (if exists) is used.
So `jb build --config _config.yml *.ipynb` is equivalent to `jb build *.ipynb`.

## References 

- [Jupyter Book 101: Beautiful, publication-quality documents from computational material](https://www.youtube.com/watch?v=lZ2FHTkyaMU)

- [jupyter-book - Official Doc](https://jupyterbook.org/intro.html)

- [jupyter-book @ GitHub](https://github.com/executablebooks/jupyter-book)

- [The command-line interface](https://jupyterbook.org/reference/cli.html?highlight=verbose#the-command-line-interface)

- [Build Your Book](https://jupyterbook.org/start/build.html)

- [Configure book settings](https://jupyterbook.org/customize/config.html?highlight=timeout)

- [Hide or remove content](https://jupyterbook.org/interactive/hiding.html?highlight=hide%20code#hide-or-remove-content)

- [Execute and cache your pages](https://jupyterbook.org/content/execute.html?highlight=timeout)
