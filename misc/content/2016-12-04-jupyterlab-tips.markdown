UUID: 866ecf58-079e-4cec-9978-c9782410a0d0
Status: published
Date: 2016-12-30 17:17:12
Author: Ben Chuanlong Du
Slug: jupyterlab-tips
Title: JupyterLab Tips
Category: Software
Tags: software, JupyterLab, Jupyter

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

[Running a notebook server](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html)

## General Tips

1. performance on big csv ... very slow, even switching ...
use a relatively small part of csv ...

2. hard to do interactive UI in JupyterLab right now ...
many interactive UI pacakges in R relies on RStudio to work.

3. Convert Jupyter Notebook to another format.
```bash
jupyter nbconvert --to FORMAT notebook.ipynb
```

## Useful Extensions

[jupyterlab_geojson](https://github.com/jupyterlab/jupyterlab_geojson)
```bash
pip3 install jupyterlab_geojson
jupyter labextension install --py --sys-prefix jupyterlab_geojson
jupyter labextension enable --py --sys-prefix jupyterlab_geojson
```
[ipywidgets](https://github.com/ipython/ipywidgets/tree/master/jupyterlab_widgets)
Interactive HTML widgets (slider, button, textbox, etc.) for Python Notebook.
```bash
pip install jupyterlab_widgets
jupyter labextension install --sys-prefix --py jupyterlab_widgets
jupyter labextension enable --sys-prefix --py jupyterlab_widgets
```
Examples of custom widget libraries built upon ipywidgets are

    bqplot a 2d data visualization library enabling custom user interactions.
    pythreejs a Jupyter - Three.js wrapper, bringing Three.js to the notebook.
    ipyleaflet a leaflet widget for Jupyter.

[widget-cookiecutter](https://github.com/jupyter/widget-cookiecutter)
```bash
pip3 install cookiecutter
```
jupyter_declarativewidgets
jupyter-wysiwyg, does not integrate jupyterlab ...
sudospawner
jupyterhub


## Related R Packages
### IRKernel
### repr

[Bash Kernel](https://github.com/takluyver/bash_kernel)

## SAS
SAS University Edition has built-in support of Jupyter Notebook now. 
https://support.sas.com/software/products/university-edition/faq/jn_whatis.htm


## Links
https://toree.incubator.apache.org/documentation/user/quick-start
https://datascience.berkeley.edu/10-data-science-newsletters-subscribe/ 
https://github.com/jupyter-incubator/declarativewidgets
https://github.com/jupyter-incubator/dashboards
http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html
https://wiki.vip.corp.ebay.com/display/krylov/Jupyterhub
https://wiki.vip.corp.ebay.com/display/ShippingTeam/Using+our+Krylov+instances+with+JupyterHub
http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/
https://groups.google.com/forum/#!topic/jupyter/iaaKOeRwyjs
https://toree.incubator.apache.org/documentation/user/installation.html
https://github.com/michhar/useR2016-tutorial-jupyter/blob/master/INSTALLATIONS.md
http://stackoverflow.com/questions/31855794/whats-the-best-way-to-share-jupyter-notebooks-with-non-programmers
https://www.polymer-project.org/1.0/
https://github.com/jupyter-incubator/declarativewidgets
http://nbgrader.readthedocs.io/en/stable/
http://webcomponents.org/
https://geomesa.atlassian.net/wiki/display/GEOMESA/How+to+install+the+Scala+Spark+(Apache+Toree)+Jupyter+kernel+with+GeoMesa+support

## IRKernel
it seems that matrix is not displayed correctly, shown as vector
df is display correctly
flush.console doesn't work well ...
.Last.value for R ...
.Last.value, seem not working in jupyter (0.7)

2. currently irkernel does not implement magics 

## Questions
1. jupyterlab多人改同一个notebook会发生什么情况
2. How to use JupyterLab for blogging? e.g., if you write a blog about R/Python, it's best to illustrate in JupyterLab, but how to easily integrate into Pelican?
3. change behavior of default layout?
4. font size of editor?
5. use bash as a sub shell cell?
6. use other installed kernel languages as sub shell cells?

