---
title: Visualization Using Bokeh in Python
created: '2017-07-22T15:07:28-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: visualization-using-bokeh-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - visualization
  - Bokeh
  - Bokeh server
  - tips
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

HoloViews and hvplot are much better alternatives which supports Bokeh as the backend.

## Links

<http://bokeh.pydata.org/en/latest/>

## Installation

```
sudo pip3 install bokeh jupyter holoviews
```

## Usage

```
bokeh serve --allow-websocket-origin=*:5006 dash.ipynb
```

it seems that only 5006 works ...
might be because ...

## Questions

Can u combine bokeh and Jupyter Notebook to quickly prototype and then deploy?
This requires support of Bokeh server in Jupyter Notebook.

bokeh, not numeric values, no corresponding warnings due to HTML ...
be careful ...

```
bokeh serve --allow-websocket-origin=server_ip:5006 sliders.py
```

## jupyterlab_bokeh

```
sudo apt install libgif-dev
sudo jupyter labextension install jupyterlab_bokeh
```
