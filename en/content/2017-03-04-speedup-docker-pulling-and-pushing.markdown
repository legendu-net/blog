UUID: 709db98e-f0f6-456c-8fbd-248f28157e98
Status: published
Date: 2017-03-04 15:48:24
Author: Ben Chuanlong Du
Slug: speedup-docker-pulling-and-pushing
Title: Speedup Docker Pulling and Pushing
Category: Software
Tags: software, Docker, speedup, performance, DaoCloud

Pulling/pushing Docker images is extremely slow in China. 
One way to speedup Docker visiting is to use [DaoCloud](https://www.daocloud.io/) as a proxy.
All you have to do is simply adding the following line into the file `/etc/default/docker`.
```text
DOCKER_OPTS="--registry-mirror='http://a92c904a.m.daocloud.io'"
```
Please refer to <https://www.daocloud.io/mirror#accelerator-doc> for more details.
