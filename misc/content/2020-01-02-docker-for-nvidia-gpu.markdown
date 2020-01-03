Status: published
Date: 2020-01-02 17:22:48
Author: Benjamin Du
Slug: docker-for-nvidia-gpu
Title: Docker for Nvidia Gpu
Category: Software
Tags: software, Docker, GPU

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. Install Nvidia driver on your Linux machine.
    For example,
    you can install Nvidia driver using the command below on Ubuntu.

        :::bash
        sudo apt-get install cuda-drivers

    You do not have to install the CUDA toolkit on your Linux host machine.

2. Make sure that you have Docker 19.03+ installed on your Linux machine.

3. Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) on your Linux machine.
    For example,
    you can install it on Ubuntu 16.04/18.04
    and Debian Jessie/Stretch/Buster using the following comamnds.

        :::bash
        # Add the package repositories
        distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
        curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
        curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

        sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
        sudo systemctl restart docker

2. Run official Nvidia Docker images.
    Please refer to https://github.com/NVIDIA/nvidia-docker#usage for examples.

## References

https://github.com/NVIDIA/nvidia-docker

https://github.com/NVIDIA/nvidia-docker#ubuntu-16041804-debian-jessiestretchbuster

[How Do I Install the Nvidia Driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver).
