UUID: 51843213-1af4-416b-95e2-fdde1ac10f38
Status: published
Date: 2017-06-11 19:16:48
Author: Ben Chuanlong Du
Slug: docker-installation
Title: Docker Installation
Category: Software
Tags: software, docker, installation

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Install docker on Ubuntu 16.04 using the commands below.

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
wajig update
wajig install docker-ce
gpasswd -a $(whoami) docker
newgrp docker
```
