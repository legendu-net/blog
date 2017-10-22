UUID: 51843213-1af4-416b-95e2-fdde1ac10f38
Status: published
Date: 2017-10-22 13:24:32
Author: Ben Chuanlong Du
Slug: docker-installation
Title: Install the Latest Version of Docker CE on Ubuntu
Category: Software
Tags: software, docker, installation, ubuntu, latest, docker-ce

You can install the latest version of Docker CE on Ubuntu 16.04 using the commands below.

    # add repository
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    # install docker
    wajig update
    wajig install docker-ce
    # add user to the docker group
    gpasswd -a $(whoami) docker
    newgrp docker
