UUID: c744cc45-eaa3-46e4-925d-a298beb815c0
Status: published
Date: 2017-10-22 13:31:44
Author: Ben Chuanlong Du
Slug: tips-for-running-docker-containers
Title: Tips for Running Docker Containers
Category: Software
Tags: software, docker, running, execute, container

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. Do NOT forget to forward port while using docker containers. 
For example, if use Git in a docker container,
you probably have to forward ports to 22 and 80 as Git uses HTTP(s) and SSH protocol which listen on these 2 prots.

1. avoid mounting things into image, this is actually a general rule.
It is recommend that you always mount to /some_dir and then link to home if needed
Never mount into HOME!!!

3. If you use the `-v` option when starting a Docker container, 
make sure that you have r/w access to it otherwise the Docker container might fail to start.

6. docker: Error response from daemon: Get https://registry-1.docker.io/v2/dclong/jupyterlab-rstudio/manifests/latest: dial tcp 50.17.62.194:443: getsockopt: connection refused just restart docker deamon resolves the issue ...
retry or restart the docker daemon.

        service docker restart

6. If you are in the `docker` group, 
you can run docker commands without `sudo`,
o.w., you have to use `sudo`.

2. Inside a docker container, 
files created belong to the user in the container. 
If the files are created in a mounted host directory,
then on the host these files belong to the user with the same user ID.

3. docker requires root, but if the user is in the docker group, 
then no need to run docker with sudo 
as the docker group is sudo equivalent

1. multiple running instances of the same docker image do not interact with each other. 
The are running isolated.

2. Amazon aws indeed have issues in China, try another cloud service ...

