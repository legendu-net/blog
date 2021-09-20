Status: published
Date: 2020-01-18 01:02:42
Author: Benjamin Du
Slug: docker-for-nvidia-gpu
Title: Docker for Nvidia GPU
Category: Software
Tags: software, Docker, GPU, Nvidia
Modified: 2021-09-19 21:19:46

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Instruction on Using Nvidia GPU (CUDA) for Computing in Docker

1. Install Nvidia `cuda-drivers` (or equivalent) on your Linux machine
    following instructions at 
    [CUDA Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux).
    Notice that instead of installing `cuda` (using `sudo apt-get install cuda`),
    it is suggested that you install `cuda-drivers` only (using `sudo apt-get install cuda-drivers`).
    This is because the CUDA toolkit (the package `cuda`) is not needed on your Linux host machine to 
    run GPU-enabled Docker container starting from Docker 19.03.
    Of course, 
    it doesn't hurt to install the package `cuda` besides using more disk spaces.

2. Confirm that the CUDA drivers have been installed correctly. 

        :::bash
        nvidia-smi 

    If the command `nvidia-smi` is available 
    but raises the following error message, 

    > NVIDAI-SMI has failed because it couldn't communicate with the NVIDIA driver.  
    > Make sure that the latest NVIDIA driver is installed and running.`

    reboot your Linux machine and try again.

2. Make sure that you have Docker 19.03+ installed on your Linux machine.

3. Install 
    [nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) 
    on your Linux machine.
    For example,
    you can install it on the Debian-series of Linux distributions 
    (Debian, Ubuntu, Linux Mint, etc.)
    using the following comamnds.

        :::bash
        distribution=$(. /etc/os-release; echo $ID$VERSION_ID)
        curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
        curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
        sudo apt-get update 
        sudo apt-get install -y nvidia-docker2

4. Restart Docker.
    You can use one of the following command 
    (depending on whether systemd is used to manage services).

        :::bash
        sudo systemctl restart docker
        # or 
        sudo service docker restart

5. Test that GPU-enabled Docker containers can be run correctly.

        :::bash
        docker run --gpus all nvidia/cuda:10.2-base nvidia-smi

6. Extend official Nvidia Docker images to customize your own Docker images for GPU applications if needed.
    [nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04](https://hub.docker.com/layers/nvidia/cuda)
    is the best Docker image to extend, generally speaking.
    If you are using PyTorch (which has built-in CUDA and CUDNN),
    you can use [nvidia/cuda:10.1-base-ubuntu18.04](https://hub.docker.com/layers/nvidia/cuda) to reduce the size of your Docker image.
    [floydhub/dockerfiles](https://github.com/floydhub/dockerfiles)
    and
    [PyTorch Dockerfile](https://github.com/pytorch/pytorch/blob/master/docker/pytorch/Dockerfile)
    are good examples to refer to.
    If you want to use Python packages that do not have built-in CUDA and CUDNN support, 
    you might have to install the library `cuda-10-1` manually.

        :::bash
        sudo apt-get install cuda-10-1

7. Run GPU applications in Docker containers. 
    Please refer to 
    [nvidia-docker#usage](https://github.com/NVIDIA/nvidia-docker#usage) 
    for examples.

## General Tips on GPU

0. You can list all GPU devices using the following command in Linux.

        :::bash
        lspci -v | grep VGA

1. You can use the following command to query the live GPU usage on both Windows and Linux. 

        :::shell
        nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max,pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv -l 5

    For more discussions,
    please refer to
    [Useful nvidia-smi Queries](https://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries)
    and 
    [Visualize Nvidia GPU Usage](http://www.legendu.net/misc/blog/visualize-Nvidia-GPU-usage)
    .
    In additional,
    you can use the command `nvtop` to check the live usage of GPUs on Linux.
    `nvtop` is recommended 
    as it presents simple visualizations in addition to the current usage statistics.
    `nvtop` can be install on Ubuntu using the following command.

        :::bash
        apt-get install nvtop

## Docker & Ubuntu Repositories

https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/

[nvidia/cuda:11.0-cudnn-base-ubuntu20.04](https://gitlab.com/nvidia/container-images/cuda/-/blob/master/dist/11.0/ubuntu20.04-x86_64/base/Dockerfile)

[nvidia/cuda:11.0-cudnn-runtime-ubuntu20.04](https://gitlab.com/nvidia/container-images/cuda/-/blob/master/dist/11.0/ubuntu20.04-x86_64/runtime/Dockerfile)

[nvidia/cuda:11.0-cudnn-devel-ubuntu20.04](https://gitlab.com/nvidia/container-images/cuda/-/blob/master/dist/11.0/ubuntu20.04-x86_64/devel/Dockerfile)

https://github.com/floydhub/dockerfiles

## References

- [CUDA Installation Guide for Microsoft Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)

- [Nvidia CUDA Linux Repositories](https://developer.download.nvidia.com/compute/cuda/repos/)

- [How to install CUDA on Ubuntu 20.04 Focal Fossa Linux](https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux)

- https://github.com/NVIDIA/nvidia-docker

- https://github.com/NVIDIA/nvidia-docker#ubuntu-16041804-debian-jessiestretchbuster

- [How Do I Install the Nvidia Driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver).