Status: published
Date: 2019-06-21 23:37:16
Author: Ben Chuanlong Du
Slug: save-docker-image-in-another-location
Title: Save Docker Image in Another Location
Category: Software
Tags: software, Docker, location

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Docker images are saved in `/var/lib/docker`. 
You can link the directory to another place to save images elsewhere.
Another way is to change the configuration file of Docker.
For example, 
you can add the following into `/etc/default/docker` 
to save docker images into `/mnt` (instead of the default location).
```
DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4 -g /mnt"
```

