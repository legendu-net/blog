Status: published
Date: 2019-03-08 09:47:48
Author: Ben Chuanlong Du
Slug: python-modules-for-visualization
Title: Python Modules for Visualization
Category: Programming
Tags: programming, visualization, Python, HoloViews, bokeh, plotly, matplotlib, pandas

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## JS based Modules

### [Cufflink](https://github.com/santosjorge/cufflinks)

Enables plotly plots in pandas DataFrame (via the `iplot` method) directly. 

https://plot.ly/pandas/getting-started/

https://medium.com/@kbrook10/day-7-data-visualization-how-to-use-plotly-and-cufflinks-for-interactive-data-visualizations-3a4b85fdd999

### HoloViews

HoloViews is my favorate JS-based visualization package in Python.
It has the simpliest yet rigorous syntax.

### bokeh

Bokeh is a great JS-based package for visualization in Python and is also available in other programming languages.
It is a free and opensource alternative to plotly (which is not totally free).
Both bokeh and plotly is feature-rich.
They supports all kinds of charts, data table and can easily build a dashboard.

### [plotly](https://plot.ly/python/user-guide/)

Plotly is great (even better than Bokeh) but unfortunately not totally free (very limited API calls per day).

## `matplotlib` based Modules

### matplotlib

The old default visualization package in Python.


has display issues without x server ...

http://stackoverflow.com/questions/11264521/date-ticks-and-rotation-in-matplotlib

http://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib

http://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib

### pandas

`pandas` integrates some visualization features based on matplotlib.
It makes things convenient if you have to work with data frame a lot.


## References

http://jakevdp.github.io/blog/2014/01/10/d3-plugins-truly-interactive/

http://blog.ynema.com/?p=192
