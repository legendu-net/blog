Status: published
Date: 2017-07-27 12:16:56
Author: Ben Chuanlong Du
Slug: docker-images-for-remote-desktop
Title: Docker Images for Remote Desktop
Category: Software
Tags: software, docker, remote desktop, KDE, Ubuntu, VNC, NoMachine, x11docker
Modified: 2021-12-11 14:05:51

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

## Tips and Traps

1. [x11docker](https://github.com/mviereck/x11docker)
    runs GUI applications and desktops in docker and podman containers. 

2. [NoMachine](http://www.legendu.net/misc/blog/remote-desktop-using-nomachine-on-linux)
    is recommended for remote Desktop.

2. If VNC is used for accessing remote desktop environment in a Docker container,
    you might haveto manually set the resolution while starting the docker container 
    so that you get the best experience.

### KDE Plasma

[kdeneon/plasma](https://hub.docker.com/r/kdeneon/plasma/)

### Ubuntu

1. [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)


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

## Deepin

[dockerfile-x11docker-deepin](https://github.com/mviereck/dockerfile-x11docker-deepin)

[deepin-desktop-docker](https://gitee.com/daze456/deepin-desktop-docker)
