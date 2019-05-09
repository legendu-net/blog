Status: published
Date: 2019-05-09 21:21:15
Author: Ben Chuanlong Du
Slug: useful-tools-extensions-for-jupyterlab
Title: Useful Tools and Extensions for JupyterLab
Category: Software
Tags: software, JupyterLab, extension, plugin, JupyterHub, nbdime

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Useful Tools

### [jupyter/nbdime](https://github.com/jupyter/nbdime)

Tools for diffing and merging of Jupyter notebooks.
Notice that nbdime integrates with git well.

You can use the following command to configure nbdime for Git.

    nbdime config-git (--enable | --disable) [--global | --system]

Register nbdime with Git for the current project/repository.

    nbdime config-git --enable

Deregister nbdime with Git for the current project/repository.

    nbdime config-git --disable


Register nbdime with Git for global users.

    nbdime config-git --enable --global

Deregister nbdime with Git for global users.

    nbdime config-git --disable --global

### jupyterhub

### sudospawner


## Useful Plugins/Extensions for Jupyter Notebook/Lab


www.draw.io is also interesting,

1. [jupyterlab-toc](https://github.com/jupyterlab/jupyterlab-toc)

2. [jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen)

Very slow when there are lots of files.

1. [jupyterlab-monaco](https://github.com/jupyterlab/jupyterlab-monaco)

2. [jupyterlab-drawio](https://github.com/QuantStack/jupyterlab-drawio)

3. [jupyterlab-latex](https://github.com/jupyterlab/jupyterlab-latex)

4. [jupyterlab_spellchecker](https://github.com/ijmbarr/jupyterlab_spellchecker)

5. [jupyterlab-flake8](https://github.com/mlshapiro/jupyterlab-flake8)

A non polished product. Too much messages.

6. [jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)

7. [Voila](https://github.com/QuantStack/voila)

8. [qgrid](https://github.com/quantopian/qgrid)

9. [jupyterlab-google-drive](https://github.com/jupyterlab/jupyterlab-google-drive)
Not sure whether this is useful.

10. [jupyterlab-spreadsheet](https://github.com/quigleyj97/jupyterlab-spreadsheet)

4. [jupyterlab_geojson](https://github.com/jupyterlab/jupyterlab_geojson)
```bash
pip3 install jupyterlab_geojson
jupyter labextension install --py --sys-prefix jupyterlab_geojson
jupyter labextension enable --py --sys-prefix jupyterlab_geojson
```

5. [ipywidgets](https://github.com/ipython/ipywidgets/tree/master/jupyterlab_widgets)
    Interactive HTML widgets (slider, button, textbox, etc.) for Python Notebook.

        pip install jupyterlab_widgets
        jupyter labextension install --sys-prefix --py jupyterlab_widgets
        jupyter labextension enable --sys-prefix --py jupyterlab_widgets

    Examples of custom widget libraries built upon ipywidgets are

    - bqplot a 2d data visualization library enabling custom user interactions.

    - pythreejs a Jupyter - Three.js wrapper, bringing Three.js to the notebook.

    - ipyleaflet a leaflet widget for Jupyter.

6. [widget-cookiecutter](https://github.com/jupyter/widget-cookiecutter)

    pip3 install cookiecutter

7. jupyter_declarativewidgets

8. jupyter-wysiwyg, does not integrate jupyterlab ...
