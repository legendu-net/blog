Status: published
Date: 2021-09-06 12:47:10
Modified: 2022-05-28 11:26:11
Author: Benjamin Du
Slug: pcie-bus-error:-severity=Corrected,-type=Physical-Layer
Title: PCIe BUS Error: Severity=Corrected, Type=Physical Layer
Category: OS
Tags: OS, Linux, issue, error, kernel, PCIe, Bus, Corrected, pci=noaer, pci-nomsi

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Note: You might have to do this every time you upgrade your Linux kernel!!

## Symptoms

Below are step-by-step symptoms from superficial to root causes.

1. Your Linux system becomes very slow
    even if the system has enough CPU and memory resources.

2. `top` reports a large portion of CPU wating on IO.

3. `sudo iotop` reports `jbd2` using lots of disk IO.

4. The command `ls -lhS /var/log/*log | head` 
    shows a few obviously large log files.
    Generally speaking,
    a log file in MBs is considered large.

5. A large log file shows frequent error/warning messages.
    For example,
    The kernel log file `/var/log/kern.log`
    shows the following error message frequently.

    > PCIe-Bus-Error:-severity=Corrected,-type=Physical-Layer

## Solution

1. Empty large log files.
    Taking `/var/log/kern.log` as an example,
    you can empty it using the following command.
    Notice that you'd better NOT remove log files.

        :::bash
        cat /dev/null | sudo tee /var/log/kern.log
 
2. Edit the GRUB file `/etc/default/grub` 
    to add the `pci=nomsi` parameter 
    to the `GRUB_CMDLINE_LINUX_DEFAULT` directive.

3. Update the GRUB.

        :::bash
        sudo update-grub

4. If the above steps does not fix the issue, 
    try repeating steps 2-3 with other parameters,
    e.g., `pci=noaer` or `pci=mmconf`.

## References 

- [Solution: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e6(Receiver ID)](https://codesport.io/linux/solution-pcie-bus-error-severitycorrected-typephysical-layer-id00e6receiver-id/)

- [Troubleshooting PCIe Bus Error severity Corrected on Ubuntu and Linux Mint](https://itsfoss.com/pcie-bus-error-severity-corrected/)

- [Issues with "PCIe Bus Error: severity=Corrected" errors? [partially SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=320473)
