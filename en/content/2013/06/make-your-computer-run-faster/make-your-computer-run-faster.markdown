Status: published
Date: 2013-06-08 08:54:21
Slug: make-your-computer-run-faster
Author: Ben Chuanlong Du
Title: Make Linux Run Faster
Category: OS
Tags: RAM, speedup, SSD, software, optimization, hardware, Linux, fast, performance
Modified: 2022-06-11 15:50:27

 
## Benchmark Tools for Linux

[phoronix-test-suite](https://github.com/phoronix-test-suite/phoronix-test-suite/)
is currently the best benchmark tool for Linux.
You can use it to figure out the bottleneck of performance of your Linux machine.
Please refer to
[Benchmark Your Linux Machine Using phoronix-test-suite](https://www.legendu.net/misc/blog/benchmark-your-linux-machine-using-phoronix-test-suite)
for more discussions.


[BCC](https://github.com/iovisor/bcc)
is a toolkit for creating efficient kernel tracing and manipulation programs
leveraging extended Berkeley Packet Filters (eBPF).

## Upgrading Hardware

1. Get larger RAM for your computer.

2. Get a SSD disk.

3. Get a good graphics card (if you have workstation).

## Configuration

1. Configure GRUB to fix PCIe BUS errors if any. 
    Please refer to
    [Pcie Bus Error: Severity=Corrected, Type=Physical Layer](https://www.legendu.net/misc/blog/PCIe-Bus-Error:-severity=Corrected,-type=Physical-Layer/)
    for detailed discussions
    .
    Notice that you might have to do this 
    every time you upgrade your Linux kernel.

2. Reduce GRUB timeout to a smaller value.
    Please refer to
    [Reduce GRUB Timeout](https://www.legendu.net/misc/blog/reduce-grub-timeout)
    for detailed discussions
    .

2. Configure `vm.swapness` to be a proper value (10 or even less),
    if your Linux system has a large swap partition.
    For more details,
    please refer to
    [SwapFaq](https://help.ubuntu.com/community/SwapFaq)
    .

3. Choose a fast mirror.
    If you are using Ubuntu, 
    a fast mirror will be automatically decided based on your location. 
    However, 
    if you are using other Linux distribution (e.g., Linux Mint),
    you might have to choose a fast mirror manually.

4. Use the `noatime` option for filesystems. 
    Add the `noatime` option into your fstab for all non-swap partitions.
    This is 
    <span style="color:red">
    NOT recommended
    </span>
    unless you really want to squeeze the performance of Linux machine.

5. Remove non-necessary autostart applications
    and configure a delay to must-have autostart applications.
    Please refer to
    [Manage Autostart Applications](https://www.legendu.net/misc/blog/manage-autostart-apps)
    for detailed discussions.

6. Disable non-needed systemd services.
    Please refer to
    [Manage systemd Services and Units](https://www.legendu.net/misc/blog/manage-systemd-services-units)
    for detailed discussions.

7. If you use the GNOME desktop environment,
    configuare "Gnome Shell Search" to disable unnecessary applications.
    ![gnome-shell-search-config](https://user-images.githubusercontent.com/824507/170840843-f085a295-4071-4ee8-929f-62d1e57c67f6.png)

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


## References

- [PackageKitD Uses Too Much CPU or Disk IO](https://www.legendu.net/misc/blog/packagekitd-uses-too-much-cpu-or-disk-io/)
