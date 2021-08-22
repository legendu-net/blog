Status: published
Date: 2018-04-16 09:18:10
Author: Ben Chuanlong Du
Slug: tips-on-docker-compose
Title: Tips on Docker Compose
Category: Software
Tags: software, Docker Compose, tips
Modified: 2021-02-16 09:18:10

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Installation

`docker-compose` can be installed using the following command on Ubuntu.

    :::bash
    wajig install docker-compose

And docker -compose can be installed using brew on macOS.

    :::bash
    brew install docker-compose

## Examples

```
version: '3'
services:
  jupyterhub-ds:
    image: "dclong/jupyterhub-ds"
    ports:
      - "8000:8000"
    environment:
      - DOCKER_USER=dclong
      - DOCKER_USER_ID=1000
      - DOCKER_PASSWORD=dclong
      - DOCKER_GROUP_ID=1000
      - DOCKER_ADMIN_USER=dclong
    entrypoint: /scripts/sys/init.sh
```

## Shell Commands

Shell commands cannot be used in a Docker-Compose file or a `env` file directly,
which is a big limitation of Docker-Compose.

https://github.com/docker/compose/issues/4081

## Nvidia GPU Support 

[Enabling GPU access with Compose](https://docs.docker.com/compose/gpu-support/)

https://github.com/docker/compose/pull/7929

https://github.com/docker/compose/issues/6691

## Environment Variables

https://docs.docker.com/compose/environment-variables/

## NFS

https://forums.docker.com/t/docker-swarm-nfs-mount/39007

https://stackoverflow.com/questions/45282608/how-to-directly-mount-nfs-share-volume-in-container-using-docker-compose-v3

## References

https://docs.docker.com/compose/install/

[Using Docker-Compose, how to execute multiple commands](https://stackoverflow.com/questions/30063907/using-docker-compose-how-to-execute-multiple-commands)

https://github.com/docker/compose

https://github.com/jupyter-incutbator/dashboards_setup/tree/master/docker_deploy
