UUID: 866ecf58-079e-4cec-9978-c9782410a0d0
Status: published
Date: 2017-12-02 16:56:15
Author: Ben Chuanlong Du
Slug: jupyterlab-tips
Title: JupyterLab Tips
Category: Software
Tags: software, JupyterLab, Jupyter, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Resources

[28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

https://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/

http://arogozhnikov.github.io/2016/09/10/jupyter-features.html

[Running a notebook server](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html)

## General Tips


1. You might lose data if you edit a notebook in multiple places 
    (e.g., in different browsers or on different machines)!

2. If you have a notebook open on a machine 
    but have it edited before on another machine, 
    the changes might not be synchronized automatically.
    If you jump to edit the notebook on the current machine without refreshing it, 
    you might loss data.
    Even if JupyterLab do warn you about the notebook is changed on the disk,
    it is a hassle to go back to figure out new changes you've made.
    To avoid data loss,
    you'd better close notebook tabs and reopen them
    if you switch to another machine to use JupyterLab. 

2. Shutdown a kernel will kill the kernel associated with a notebook
    but it won't affect content in the notebook if no code is running. 
    After shutdowning the kernel, 
    a notebook behaves like a pure text editor.

1. `find.scala | xargs vim` makes terminal fail to display correctly.
    `reset` resolves the issue.

2. hard to do interactive UI in JupyterLab right now ...
    many interactive UI pacakges in R relies on RStudio to work.

3. Convert Jupyter Notebook to another format.

        jupyter nbconvert --to FORMAT notebook.ipynb

4. Notice that you'd better turn off proxies while using JupyterLab. 

## JupyterLab Extenions

https://jupyterlab.readthedocs.io/en/stable/user/extensions.html

https://github.com/topics/jupyterlab-extension

https://medium.com/@subpath/jupyter-lab-extensions-for-data-scientist-e0d97d529fc1

https://github.com/mauhai/awesome-jupyterlab



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


## Questions
1. jupyterlab多人改同一个notebook会发生什么情况
2. How to use JupyterLab for blogging? 
    For example, if you write a blog about R/Python, 
    it's best to illustrate in JupyterLab, 
    but how to easily integrate into Pelican?
3. change behavior of default layout?
4. font size of editor?
5. use bash as a sub shell cell?
6. use other installed kernel languages as sub shell cells?

