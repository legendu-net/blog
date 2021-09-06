Status: published
Date: 2013-06-08 08:54:21
Slug: make-your-computer-run-faster
Author: Ben Chuanlong Du
Title: Make Linux Run Faster
Category: OS
Tags: RAM, speedup, SSD, software, optimization, hardware, Linux, fast, performance
Modified: 2021-09-06 12:59:17

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
## Swapness

If your Linux system has a large swap partition, 
configure `vm.swapness` to be a proper value (10 or even less).
For more details,
please refer to
[SwapFaq](https://help.ubuntu.com/community/SwapFaq)
.

## Upgrading Hardware

1. RAM (first thing to be considered)  
2. Disk (considering SSD)
3. Video card (if you have workstation)

## Software-based Optimization

1. Use a light-weighted Linux distribution. 
    For example,
    antiX Linux is a light-weighted debian-based Linux operating system.

2. Use a light-weighted desktop environment, e.g., Xfce or LXQt.
    When used with Ubuntu, 
    they correspond to Xubuntu and Lubuntu
    which are both good choices for non-powerful computers.

3. Remove resource hungry software.
    - Okular: has lots of KDE dependencies

4. Remove non-necessary software.

        :::bash
        deborphan

## Tips for Speeding up Debian Series Linux Operation Systems

The following are some more tips for speeding up Debian Series Linux operation systems.
These Tips also apply to other Linux operation systems, 
except that you have to modify the commands.

1. Upgrade your operating system.

        :::bash
        wajig update && wajig upgrade

2. Use the `noatime` option for filesystems. 
    Add the `noatime` option into your fstab for all non-swap partitions.  

3. Use dash instead of bash (make boot faster)
    
        :::bash
        wajig install dash
        wajig reconfigure dash
        
4. readahead (make boot faster)
    
        :::bash
        wajig install readahead
        # or depending on your Linux distribution, you might have to use
        wajig install ureadahead

5. localepurge
        
        :::bash
        wajig install localepurge
        
6. remove old kernels
        
        :::bash
        # Don't worry. This won't remove the up-to-date Linux kernel.
        wajig purge linux-image-<TAB>
        
7. package cleanup
        
        :::bash
        # find orphan packages
        deborphan
        # auto remove non-needed packages and clean package caches
        wajig autoremove && wajig autoclean
        
8. bootchart
        
        :::bash
        wajig install bootchart

9. preload
        
        :::bash
        wajig install preload
