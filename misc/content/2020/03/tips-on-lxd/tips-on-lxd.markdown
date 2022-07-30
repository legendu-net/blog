Status: published
Date: 2020-03-10 11:45:40
Author: Benjamin Du
Slug: tips-on-lxd
Title: Tips on LXD
Category: Computer Science
Tags: Computer Science, Docker, container, LXD, LXC
Modified: 2022-07-29 16:19:44

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. LXD only works in Linux.
    It is not supported on macOS or Windows.

2. LXD does not require a CPU which supports virtualization. 

3. Docker is a more user-friendly alternative to LXD containers
  and multipass is a more user-friendly alternative to LXD virtual machines.
  It is suggested that you use Docker/multipass instead of LXD.

## [Installation](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#2-install-lxd)

    sudo snap install lxd
    gpasswd -a $(id -un) lxd
    newgrp lxd

## [Setup LXD](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#3-setup-lxd)

    lxd init

## [Launch a container](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#4-launch-a-container)

    lxc list
    lxc launch ubuntu:22.04
    lxc exec stirring-beagle -- ls -la
    lxc exec -t stirring-beagle /bin/bash


## Publish LXD Images

https://ubuntu.com/tutorials/create-custom-lxd-images

https://ubuntu.com/blog/publishing-lxd-images

https://medium.com/@tcij1013/lxc-lxd-cheetsheet-effb5389922d

https://github.com/lxc/lxd/issues/6805

[LXDHub](https://lxdhub.xyz/remote/images/images)

## References

- [LXD @ GitHub](https://github.com/lxc/lxd)

- [macOS and "LXD installed and running?" error](https://github.com/lxc/lxd/issues/4015)

- [LXDHub](https://lxdhub.xyz/remote/images/images)

- [NVidia CUDA inside a LXD container](https://ubuntu.com/blog/nvidia-cuda-inside-a-lxd-container)
