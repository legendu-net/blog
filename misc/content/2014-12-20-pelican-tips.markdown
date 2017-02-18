UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-09-26 16:54:11
Author: Ben Chuanlong Du
Slug: pelican-tips
Title: Pelican Tips
Category: Programming
Tags: programming, Pelican, blog, formula, dollar sign

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. `\$` need to be escaped

2. for the latex plugin, 
equation align environment works but need to use `\newline` in stead of `\\`

1. can i use pelican directly in python instead of calling the system command?

## plugins

Pelican 3.3 must use
PLUGIN_PATH = "plugins", must not use list
in later versions you can use
PLUGIN_PATHS = ["plugins"], can use a list

## Issues

1. It seems that the search issue is due to pelican, the default value site:legendu.net was omitted.
It should be pasted together and then sent to google

## Search
1. yahoo search does not work for your current theme
