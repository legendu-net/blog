UUID: 05e465c7-cb32-400b-9101-52043a8c6876
Status: published
Date: 2017-03-18 19:48:18
Author: Ben Chuanlong Du
Slug: docker-tips
Title: Docker Tips
Category: Software
Tags: software, docker, container, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## TODO

docker: sbt and maven for the intellij version

a VM on ali, tengxun or ..., very necessary, use it for many purposes, ..., e.g., private docker registry, proxy server, shadowsocks, jupyterlab, etc.

## Installation

Install docker on Ubuntu 16.04 using the commands below.
```bash
wajig install docker.io
gpasswd -a $(whoami) docker
newgrp docker
```

## Tricks and Traps

1. ADD vs COPY: ADD auto untar which is tricky 

2. Don't forget to forward port while using docker containers. 
For example, if use Git in a docker container,
you probably have to forward ports to 22 and 80 as Git uses HTTP(s) and SSH protocol which listen on these 2 prots.

3. Amazon aws indeed have issues in China, try another cloud service ...

4. Docker images are saved in `/var/lib/docker`. 
You can link the directory to another place to save images elsewhere.
Another way is to change the configuration file of Docker.
For example, 
you can add the following into `/etc/default/docker` 
to save docker images into `/mnt` (instead of the default location).
```
DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4 -g /mnt"
```

5. If you use the `-v` option when starting a Docker container, 
make sure that you have r/w access to it otherwise the Docker container might fail to start.

6. docker: Error response from daemon: Get https://registry-1.docker.io/v2/dclong/jupyterlab-rstudio/manifests/latest: dial tcp 50.17.62.194:443: getsockopt: connection refused just restart docker deamon resolves the issue ...
retry or restart the docker daemon.
```bash
service docker restart
```

## General Tips

1. multiple running instances of the same docker image do not interact with each other. 
The are running isolated.

2. Inside a docker container, 
files created belong to the user in the container. 
If the files are created in a mounted host directory,
then on the host these files belong to the user that started the docker container.
It does not matter which user it is inside the docker container. 

3. docker requires root, but if the user is the docker group, 
then no need to run docker with sudo 
as the docker group is sudo equivalent

4. You have to tag an image into a docker repository 
so that you can push the image into the repository. 

5. Docker caches building operations. 
When cache for an operation is available, 
Docker use the cache layer directly and avoiding building the layer again.

6. If you are in the `docker` group, 
you can run docker commands without `sudo`,
o.w., you have to use `sudo`.

7. docker `ARG` for build-time and `ENV` for run-time

## Docker Commands

```bash
service docker restart
docker run -p 8888:8888 66c9887513b9
docker run -d -p 8888:8888 jupyter/all-spark-notebook
docker run -it ubuntu:16.04
docker run -dit -p 8888:8888 -v /mnt:/home/jovyan/work dclong/jupyterlab-spark-all
docker run -dit -p 80:80 -v /wwwroot:/usr/local/apache2/htdocs/ httpd
docker run -dit -p 80:80 -v /wwwroot:/usr/local/apache2/htdocs/ httpd
docker run -d -p 8787:8787 -v /wwwroot:/home/rstudio rocker/rstudio
docker run -d -p 8888:8888 -v /wwwroot:/home/jovyan/work jupyter/all-spark-notebook
```

Copying file between a docker container and the host.
docker cp foo.txt mycontainer:/foo.txt 
docker cp mycontainer:/foo.txt foo.txt


## Links

[Private Docker Registry](https://docs.docker.com/registry/deploying/)

[Configure automated builds on Docker Hub](https://docs.docker.com/docker-hub/builds/)

[Configure automated builds with Bitbucket](https://docs.docker.com/docker-hub/bitbucket/)

https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/

https://coderwall.com/p/4g8znw/things-i-learned-while-writing-a-dockerfile

http://stackoverflow.com/questions/25311613/docker-mounting-volumes-on-host

http://stackoverflow.com/questions/26500270/understanding-user-file-ownership-in-docker-how-to-avoid-changing-permissions-o

https://chrisjean.com/fix-apt-get-update-the-following-signatures-couldnt-be-verified-because-the-public-key-is-not-available/

https://github.com/docker/docker/issues/22599

http://stackoverflow.com/questions/28056522/access-host-database-from-a-docker-container

https://docs.docker.com/engine/reference/commandline/tag/

https://docs.docker.com/engine/reference/commandline/push/

### Communicate with Host

http://stackoverflow.com/questions/23439126/how-to-mount-host-directory-in-docker-container

http://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container

http://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-via-repository

### UI Related
1. [Running GUI Apps with Docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
2. <http://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container>
2. <https://github.com/kevana/ui-for-docker>
2. <https://www.eclipse.org/community/eclipse_newsletter/2015/june/article3.php>
2. <https://hub.docker.com/r/tiokksar/eclipse/~/dockerfile/>
2. <https://hub.docker.com/r/tiokksar/eclipse/~/dockerfile/>
2. <https://medium.com/google-cloud/my-ide-in-a-container-49d4f177de#.2mhkzmp8a>
2. <https://blog.jessfraz.com/post/docker-containers-on-the-desktop/>
2. <https://store.docker.com/community/images/consol/ubuntu-xfce-vnc>

### Misc
1. <https://getcarina.com/docs/troubleshooting/stop-nonresponsive-running-container/>
2. <https://medium.com/@saturnism> 
3. <http://openhome.cc/Gossip/CodeData/DockerLayman/DockerLayman3.html>
4. <https://twitter.com/saturnism/status/645366585981538304>


1. [Docker Reference](https://docs.docker.com/engine/reference/builder/)

2. [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)


