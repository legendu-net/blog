Status: published
Date: 2013-06-08 08:54:21
Slug: make-your-computer-run-faster
Author: Ben Chuanlong Du
Title: Make Linux Run Faster
Category: OS
Tags: RAM, speedup, SSD, software, optimization, hardware, Linux, fast, performance
Modified: 2021-09-26 21:52:24

 
## Upgrading Hardware

1. Get larger RAM for your computer.
    This is the most important thing to considered
    when upgrading the hardware for your computer.

2. Get a SSD disk.

3. Get a good graphics card (if you have workstation).

## Configuration

1. If your Linux system has a large swap partition, 
    configure `vm.swapness` to be a proper value (10 or even less).
    For more details,
    please refer to
    [SwapFaq](https://help.ubuntu.com/community/SwapFaq)
    .

2. Configure grub. 
    For more discussion,
    please refer to
    [Pcie Bus Error: Severity=Corrected, Type=Physical Layer](http://www.legendu.net/misc/blog/PCIe-Bus-Error:-severity=Corrected,-type=Physical-Layer/)
    .

3. Use the `noatime` option for filesystems. 
    Add the `noatime` option into your fstab for all non-swap partitions.  
    This is not recommended
    unless you really want to squeeze the performance of Linux machine.

## Software-based Optimization

### Linux Distribution and Kernels

1. Use a light-weighted Linux distribution. 
    For example,
    antiX Linux is a light-weighted debian-based Linux operating system.

2. Use a light-weighted desktop environment, e.g., Xfce or LXQt.
    When used with Ubuntu, 
    they correspond to Xubuntu and Lubuntu
    which are both good choices for non-powerful computers.

4. Keep your Linux distribution up to date.
    Generally speaking,
    it is a good idea to use the latest LTS or stable versions.

3. Remove old kernels.

        :::bash
        wajig purge linux-image-<verson>

### Booting Time

[Bootchart](https://www.bootchart.org/)
is a tool for performance analysis and visualization of the GNU/Linux boot process. 
Resource utilization and process information are collected during the boot process 
and are later rendered in a PNG, SVG or EPS encoded chart.

### Lightweight Alternatives

1. Use dash instead of bash which makes boot faster.
    
        :::bash
        wajig install dash
        wajig reconfigure dash

2. Use Evince instead of Okular which is resource hungry  
    and has lots of KDE dependencies.

### Package and Disk Cleanup

2. Identify orphan packages and remove them.

        sudo deborphan | xargs wajig remove --purge
        
3. Clean up packages.
        
        :::bash
        wajig autoremove && wajig autoclean

4. Clean up disk using `localepurge`.
        
        :::bash
        wajig install localepurge
        localpurge

