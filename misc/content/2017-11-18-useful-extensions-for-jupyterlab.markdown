UUID: 64ffad7b-8360-478c-a755-c5337b0fa48d
Status: published
Date: 2017-11-18 10:16:52
Author: Ben Chuanlong Du
Slug: useful-extensions-for-jupyterlab
Title: Useful Extensions for JupyterLab
Category: Software
Tags: software, JupyterLab, extension, plugin

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Useful Plugins/Extensions for Jupyter Notebook/Lab

1. [qgrid](https://github.com/quantopian/qgrid)

2. [jupyterlab_geojson](https://github.com/jupyterlab/jupyterlab_geojson)
```bash
pip3 install jupyterlab_geojson
jupyter labextension install --py --sys-prefix jupyterlab_geojson
jupyter labextension enable --py --sys-prefix jupyterlab_geojson
```

3. [ipywidgets](https://github.com/ipython/ipywidgets/tree/master/jupyterlab_widgets)
    Interactive HTML widgets (slider, button, textbox, etc.) for Python Notebook.

        pip install jupyterlab_widgets
        jupyter labextension install --sys-prefix --py jupyterlab_widgets
        jupyter labextension enable --sys-prefix --py jupyterlab_widgets

    Examples of custom widget libraries built upon ipywidgets are

    - bqplot a 2d data visualization library enabling custom user interactions.

    - pythreejs a Jupyter - Three.js wrapper, bringing Three.js to the notebook.

    - ipyleaflet a leaflet widget for Jupyter.

4. [widget-cookiecutter](https://github.com/jupyter/widget-cookiecutter)

    pip3 install cookiecutter

5. jupyter_declarativewidgets

6. jupyter-wysiwyg, does not integrate jupyterlab ...

7. sudospawner

8. jupyterhub

