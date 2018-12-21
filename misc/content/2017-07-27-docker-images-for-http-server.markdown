UUID: aee7e150-6b1f-4544-902b-bc1506054640
Status: published
Date: 2018-04-30 12:55:50
Author: Ben Chuanlong Du
Slug: docker-images-for-http-server
Title: Docker Images for HTTP Server
Category: Software
Tags: software, HTTP server, docker, httpd

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## [httpd](https://hub.docker.com/_/httpd/)
Pull the image. 
```bash
docker pull httpd
```
Start a docker container.
```bash
docker run --name httpd -dit -p 80:80 -v /workdir:/usr/local/apache2/htdocs/ httpd
```