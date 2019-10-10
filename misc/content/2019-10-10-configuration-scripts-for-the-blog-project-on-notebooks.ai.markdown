Status: published
Date: 2019-10-10 09:11:51
Author: Benjamin Du
Slug: configuration-scripts-for-the-blog-project-on-notebooks.ai
Title: Configuration Scripts for the Blog Project on Notebooks.Ai
Category: Programming
Tags: programming, notebooks.ai, blog, configuration script

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

:::Bash
apt-get update
apt-get install wajig git
pip3 install pelican
if [[ ! -e blog ]]; then
    git clone git@github.com:dclong/blog.git
fi