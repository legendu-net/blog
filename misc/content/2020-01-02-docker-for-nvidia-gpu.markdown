Status: published
Date: 2020-01-28 10:22:07
Author: Benjamin Du
Slug: docker-for-nvidia-gpu
Title: Docker for Nvidia GPU
Category: Software
Tags: software, Docker, GPU

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. Install Nvidia CUDA Tookit on your Linux machine
    following instructions at https://developer.nvidia.com/cuda-downloads.
    For example,
    you can install Nvidia CUDA Tookit 10.2 on Ubuntu 16.04 using the following commands.

        :::bash
        wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-ubuntu1604.pin
        sudo mv cuda-ubuntu1604.pin /etc/apt/preferences.d/cuda-repository-pin-600
        wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1604-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
        sudo dpkg -i cuda-repo-ubuntu1604-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
        sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
        sudo apt-get update
        sudo apt-get -y install cuda

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
        sudo apt-get update 
        sudo apt-get install -y nvidia-container-toolkit
        sudo systemctl restart docker
        # or depending on whether systemd is used to manage services
        sudo service docker restart

2. Run official Nvidia Docker images.
    Please refer to 
    [nvidia-docker#usage](https://github.com/NVIDIA/nvidia-docker#usage) 
    for examples.

## References

https://github.com/NVIDIA/nvidia-docker

https://github.com/NVIDIA/nvidia-docker#ubuntu-16041804-debian-jessiestretchbuster

[How Do I Install the Nvidia Driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver).
