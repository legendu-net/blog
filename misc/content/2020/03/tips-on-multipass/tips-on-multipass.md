Status: published
Date: 2020-03-03 17:27:18
Author: Benjamin Du
Slug: tips-on-multipass
Title: Tips on Multipass
Category: Software
Tags: software, Multipass, Ubuntu, virtual machine, Docker, virtualization, LXD
Modified: 2022-07-31 17:54:16

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Multipass vs LXD

1. LXD supports both containers and VMs while multipass supports only (Ubuntu) VMs.

2. LXD is more lightweight compared to multipass.

3. LXD does not require CPU virtualization while multipass relies on CPU virtualization.

4. Multipass is very user-friendly 
  while LXD requires some manual configuration and is much harder to use.

## General Tips

1. You can consider Multipass as a lightweight Ubuntu specific Docker equivalence. 

## Installation

sudo snap install multipass

## Find available images

multipass find

## Launch a fresh instance of the current Ubuntu LTS

multipass launch ubuntu

## Check out the running instances

multipass list

## Learn more about the VM instance you just launched

multipass info dancing-chipmunk

## Sharing data with the instance

The recommended way to share data between your host and the instance is the mount command:

    :::bash
    multipass mount $HOME keen-yak
    multipass info keen-yak
    …
    Mounts:         /home/ubuntu => /home/ubuntu
    From this point on /home/ubuntu will be available inside the instance. Use umount to unmount it again and you can change the target by passing it after the instance name:

    :::bash
    multipass umount keen-yak
    multipass mount $HOME keen-yak:/some/path
    multipass info keen-yak                
    …
    Mounts:         /home/michal => /some/path
    You can also use copy-files to just copy files around - prefix the path with <name>: if it’s inside an instance:

    :::bash
    multipass copy-files keen-yak:/etc/crontab keen-yak:/etc/fstab .

## Connect to a running instance

multipass shell dancing-chipmunk

## Run commands inside an instance from outside

multipass exec dancing-chipmunk -- lsb_release -a

## Stop an instance to save resources

multipass stop dancing-chipmunk

## Delete the instance
multipass delete dancing-chipmunk

## References

https://github.com/canonical/multipass

https://discourse.ubuntu.com/t/working-with-multipass-instances/8422

[Use Canonical's Multipass to display Linux GUI applications on macOS desktop](https://techsparx.com/linux/multipass/display-gui-on-mac.html)

[Ubuntu Multipass - Better than Docker?](https://www.freshbrewed.science/ubuntu-multipass-better-than-docker/index.html)
