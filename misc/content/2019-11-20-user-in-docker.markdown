Status: published
Date: 2019-11-20 09:17:31
Author: Benjamin Du
Slug: user-in-docker
Title: User in Docker
Category: Software
Tags: Software, Docker, user, container

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## User switching in Docker

1. `USER some_user` in Dockerfile, some_user has to exists
2. `su` in Dockerfile or shell scripts
3. `docker run --user some_user`