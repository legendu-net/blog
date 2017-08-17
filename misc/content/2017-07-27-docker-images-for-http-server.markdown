UUID: aee7e150-6b1f-4544-902b-bc1506054640
Status: published
Date: 2017-08-17 08:40:34
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


1. [httpd](https://hub.docker.com/_/httpd/)
```bash
docker run -dit -p 80:80 -v /wwwroot:/usr/local/apache2/htdocs/ httpd
```

