---
title: Docker Images for Remote Desktop
created: '2017-07-27T12:16:56-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: docker-images-for-remote-desktop
license: CC-BY-4.0
tags:
  - software
  - Docker
  - remote desktop
  - KDE
  - Ubuntu
  - VNC
  - NoMachine
  - x11docker
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. [x11docker](https://github.com/mviereck/x11docker)
   runs GUI applications and desktops in docker and podman containers.

1. [NoMachine](remote-desktop-using-nomachine-on-linux)
   is recommended for remote Desktop.

1. If VNC is used for accessing remote desktop environment in a Docker container,
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

1. [dorowu/ubuntu-desktop-lxqt-vnc](https://store.docker.com/community/images/dorowu/ubuntu-desktop-lxde-vnc)

   works, novnc in HTML doesn't scale very well
   password: ubuntu

1. [dorowu/ubuntu-desktop-lxde-vnc](https://store.docker.com/community/images/dorowu/ubuntu-desktop-lxde-vnc)

   works, novnc in HTML doesn't scale very well
   password: ubuntu

1. [ensky/ubuntu-nxserver-xfce](https://store.docker.com/community/images/ensky/ubuntu-nxserver-xfce)

   Works, free NX client is a little bit ugly
   had to create a new user, don't know the password

## Deepin

[dockerfile-x11docker-deepin](https://github.com/mviereck/dockerfile-x11docker-deepin)

[deepin-desktop-docker](https://gitee.com/daze456/deepin-desktop-docker)
