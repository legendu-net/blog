UUID: 866ecf58-079e-4cec-9978-c9782410a0d0
Status: published
Date: 2017-11-18 10:37:32
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

1. `find.scala | xargs vim` makes terminal fail to display correctly.
`reset` resolves the issue.

1. performance on big csv ... very slow, even switching ...
    use a relatively small part of csv ...

2. hard to do interactive UI in JupyterLab right now ...
    many interactive UI pacakges in R relies on RStudio to work.

3. Convert Jupyter Notebook to another format.

        jupyter nbconvert --to FORMAT notebook.ipynb

4. Notice that you'd better turn off proxies while using JupyterLab. 


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
2. How to use JupyterLab for blogging? e.g., if you write a blog about R/Python, it's best to illustrate in JupyterLab, but how to easily integrate into Pelican?
3. change behavior of default layout?
4. font size of editor?
5. use bash as a sub shell cell?
6. use other installed kernel languages as sub shell cells?

