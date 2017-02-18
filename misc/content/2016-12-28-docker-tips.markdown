UUID: 05e465c7-cb32-400b-9101-52043a8c6876
Status: published
Date: 2017-02-18 09:19:15
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

1. [Docker Reference](https://docs.docker.com/engine/reference/builder/)

2. [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)

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

docker -v option, make sure that you have r/w access to it otherwise docker service might fail

https://docs.docker.com/engine/reference/commandline/tag/

https://docs.docker.com/engine/reference/commandline/push/



Install docker on Ubuntu 16.04 using the commands below.
```bash
wajig install docker.io
gpasswd -a $(whoami) docker
newgrp docker
```

sudo docker run -p 8888:8888 66c9887513b9
docker run -d -p 8888:8888 jupyter/all-spark-notebook
sudo docker run -it ubuntu:16.04

Copying file between a docker container and the host.
docker cp foo.txt mycontainer:/foo.txt 
docker cp mycontainer:/foo.txt foo.txt

docker build -t firefox .



## Use [DaoCloud](https://www.daocloud.io/) to Speed Up Pulling/Pushing 
Please refer to <https://www.daocloud.io/mirror#accelerator-doc>
Or you can directly add the following line in the file `/etc/default/docker`.
```text
DOCKER_OPTS="--registry-mirror='http://a92c904a.m.daocloud.io'"
```

## Interesting Docker Images

### Ubuntu

for vnc, probably not a scaling problem but has to set resolution while starting the docker ...

1. [consol/ubuntu-xfce-vnc](https://store.docker.com/community/images/consol/ubuntu-xfce-vnc)

    works well, seems like a good choice
    ```bash
    docker run -it -p 5901:5901 -p 6901:6901 -e VNC_RESOLUTION=800x600 consol/ubuntu-xfce-vnc
    ```

2. [dorowu/ubuntu-desktop-lxqt-vnc](https://store.docker.com/community/images/dorowu/ubuntu-desktop-lxde-vnc)

    works, novnc in HTML doesn't scale very well
    password: ubuntu

3. [dorowu/ubuntu-desktop-lxde-vnc](https://store.docker.com/community/images/dorowu/ubuntu-desktop-lxde-vnc)

    works, novnc in HTML doesn't scale very well
    password: ubuntu

1. [ensky/ubuntu-nxserver-xfce](https://store.docker.com/community/images/ensky/ubuntu-nxserver-xfce)

    Works, free NX client is a little bit ugly
    had to create a new user, don't know the password

4. welkineins/ubuntu-xfce-vnc-desktop
Failed.

3. atomney/nxdesktop
https://github.com/atomney/nxdesktop
failed to login 
username: nomachine
password: nomachine

### Shadowsocks
1. [smounives/shadowsocksr-docker](https://store.docker.com/community/images/smounives/shadowsocksr-docker)
2. [dubuqingfeng/ubuntu-shadowsocks](https://store.docker.com/community/images/dubuqingfeng/ubuntu-shadowsocks)
3. [vimagick/shadowsocks-libev](https://store.docker.com/community/images/vimagick/shadowsocks-libev)
4. [oddrationale/docker-shadowsocks](https://store.docker.com/community/images/oddrationale/docker-shadowsocks)

### Trustable Docker Publishers 

1. eclipse
2. codenvy 
3. rocker (R cores)

### Notebooks (Jupyter, JupyterLab and Zeppelin)

1. [jupyter/all-spark-notebook](https://github.com/jupyter/docker-stacks/tree/master/all-spark-notebook)

4. dit4c/dit4c-container-jupyterlab

6. epahomov/docker-zeppelin

### Spark

9. shopkeep/spark too old ...

### IDE

1. codenvy/che

2. eclipse/che

https://store.docker.com/community/images/kdelfour/cloud9-docker

### Misc

3. apihackers/pelican
5. devurandom/firefox
7. sitespeedio/sitespeed.io
8. brook/ubuntu-14.04.3-baidupcs

https://github.com/Theasker/scripts

## Links

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


## Questions
docker save/export?
which account is used when writing files to host?
docker: can it handle big files?
running docker using sudo vs not using sudo?
proxy via docker?
what if I set a vpn in docker, will it be effect in docker only or also on host?

2. does docker build cache operations?
e.g., if there are 2 commands,
the first succeeds but the second one fails. 
will it cache the first command?
When I modify the second command and run biuld again, 
will it skip the first command?
probably not, seems hard to do ...

3. best practice for authentication required service in docker, 




### Scala

http://www.slideshare.net/marcuslonnberg/ship-your-scala-code-often-and-easy-with-docker

http://blog.codacy.com/2015/07/16/dockerizing-scala/

https://velvia.github.io/Docker-Scala-Sbt/

https://github.com/stevenalexander/docker-scala-ide
