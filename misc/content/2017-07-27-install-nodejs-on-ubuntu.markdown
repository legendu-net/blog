UUID: 73d864a1-baff-459d-a310-67b077688ac5
Status: published
Date: 2017-07-27 12:31:02
Author: Ben Chuanlong Du
Slug: install-nodejs-on-ubuntu
Title: Install Nodejs on Ubuntu
Category: Software
Tags: software, NodeJS, installation, Ubuntu

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


```sh
wajig install nodejs npm
```

Notice that it is necessary to create a symbolic link for node, 
as many Node.js tools use this name to execute.

```sh
sudo ln -s /usr/bin/nodejs /usr/bin/node
```
