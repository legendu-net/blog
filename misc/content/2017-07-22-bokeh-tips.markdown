UUID: b67401b6-5ce8-455d-883f-ac02e2f678b1
Status: published
Date: 2017-08-26 21:12:26
Author: Ben Chuanlong Du
Slug: bokeh-tips
Title: Bokeh Tips
Category: Programming
Tags: programming, Python, visualization, Bokeh, Bokeh server, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

<http://bokeh.pydata.org/en/latest/>

1. Bokeh supports both charts and data tables.

2. Bokeh server is a very convenient way to build a dashboard.

## Questions

Can u combine bokeh and Jupyter Notebook to quickly prototype and then deploy? 
This requires support of Bokeh server in Jupyter Notebook.


bokeh, not numeric values, no corresponding warnings due to HTML ...
be careful ...

```
bokeh serve --allow-websocket-origin=server_ip:5006 sliders.py
```
