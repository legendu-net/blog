UUID: cdc960ec-1edf-4d17-a081-3ad9c7b11702
Status: published
Date: 2017-05-23 22:26:09
Author: Ben Chuanlong Du
Slug: userful-docker-images
Title: Userful Docker Images
Category: Software
Tags: software, Docker, images, container

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## My Docker Images

<https://hub.docker.com/r/dclong>

## Trustable Docker Publishers 

1. [continuumio](https://hub.docker.com/u/continuumio/)
1. eclipse (Eclipse Che)
2. codenvy (Eclipse Che)
3. rocker (R in Docker)
4. mysql

## Official Images

1. [ubuntu](https://hub.docker.com/_/ubuntu/)

2. [CentOS](https://hub.docker.com/r/_/centos/)

3. [MySQL](https://hub.docker.com/_/mysql/)

## Others' Docker Images

### Dropbox 

janeczku/dropbox

You can enable VPN inside the docker so that Dropbox can run smoothly.

### wine 

suchja/wine 

yantis/wine 

lijianying10/wineqq


### HTTP Service

1. [httpd](https://hub.docker.com/_/httpd/)
```bash
docker run -dit -p 80:80 -v /wwwroot:/usr/local/apache2/htdocs/ httpd
```

### Python 

1. [continuumio/anaconda](https://hub.docker.com/r/continuumio/anaconda/)

Anaconda Python distribution.

### Ubuntu

For vnc, probably not a scaling problem but has to set resolution while starting the docker ...

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

### KDE Plasma

[kdeneon/plasma](https://hub.docker.com/r/kdeneon/plasma/)

### Shadowsocks

1. [smounives/shadowsocksr-docker](https://store.docker.com/community/images/smounives/shadowsocksr-docker)
2. [dubuqingfeng/ubuntu-shadowsocks](https://store.docker.com/community/images/dubuqingfeng/ubuntu-shadowsocks)
3. [vimagick/shadowsocks-libev](https://store.docker.com/community/images/vimagick/shadowsocks-libev)
4. [oddrationale/docker-shadowsocks](https://store.docker.com/community/images/oddrationale/docker-shadowsocks)

### Notebooks (Jupyter, JupyterLab and Zeppelin)

1. [jupyter/all-spark-notebook](https://github.com/jupyter/docker-stacks/tree/master/all-spark-notebook)

2. epahomov/docker-zeppelin

4. dylanmei/docker-zeppelin

3. toree spark 1.6 spark docker ...

### Spark

9. shopkeep/spark too old ...

### IDE

1. codenvy/che

2. [eclipse/che](https://hub.docker.com/r/eclipse/che/)

https://store.docker.com/community/images/kdelfour/cloud9-docker

### Misc

3. apihackers/pelican

5. devurandom/firefox

7. sitespeedio/sitespeed.io

8. brook/ubuntu-14.04.3-baidupcs

2. [haugene/transmission-openvpn](https://hub.docker.com/r/haugene/transmission-openvpn/)

### Scala

http://www.slideshare.net/marcuslonnberg/ship-your-scala-code-often-and-easy-with-docker

http://blog.codacy.com/2015/07/16/dockerizing-scala/

https://velvia.github.io/Docker-Scala-Sbt/

https://github.com/stevenalexander/docker-scala-ide

### Android 

thshaw/arc-welder 

### OpenVPN

1. [kylemanna/openvpn](https://hub.docker.com/r/kylemanna/openvpn/)

2. [martin/openvpn/](https://hub.docker.com/r/martin/openvpn/)

### Proxy

1. [minimum2scp/squid](https://store.docker.com/community/images/minimum2scp/squid)

2. [sameersbn/squid @ Docker Hub](https://store.docker.com/community/images/sameersbn/squid) | [sameersbn/docker-squid @ GitHub](https://github.com/sameersbn/docker-squid)

### Database

1. [MySQL](https://hub.docker.com/_/mysql/)
2. [Mongo](https://store.docker.com/images/9147d1b7-a686-4e38-8ecd-94a47f5da9cf?tab=description)
