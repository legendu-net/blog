Status: published
Date: 2021-09-06 12:47:10
Modified: 2021-09-26 12:13:54
Author: Benjamin Du
Slug: PCIe-Bus-Error:-severity=Corrected,-type=Physical-Layer
Title: Pcie Bus Error: Severity=Corrected, Type=Physical Layer
Category: Computer Science
Tags: Computer Science, OS, Linux, issue, error, kernel, PCIe, Bus, Corrected, pci=noaer, pci-nomsi

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Sympton

Your Linux system becomes very slow. 
`top` reports a large portion of CPU wating on IO
and `sudo iotop` reports `jbd2` using lots of disk IO.
Use the following command to find large log files.

    :::bash
    ls -lS /var/log/*log | head

Use the following command to check kernel logs.

    :::bash
    tail /var/log/kern.log

## Solution

1. Remove log files clogging your hardrive.
 
2. Edit the grub file `/etc/default/grub` 
    to add the `pci=nomsi` parameter to the `GRUB_CMDLINE_LINUX_DEFAULT` directive.

3. Update the grub.

        :::bash
        sudo update-grub

4. If the above does not fix the issue, 
    try adding the parameter `pci=noaer` to the `GRUB_CMDLINE_LINUX_DEFAULT` directive in the grub file,
    and then update the grub.

## References 

[Solution: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e6(Receiver ID)](https://codesport.io/linux/solution-pcie-bus-error-severitycorrected-typephysical-layer-id00e6receiver-id/)

[Troubleshooting PCIe Bus Error severity Corrected on Ubuntu and Linux Mint](https://itsfoss.com/pcie-bus-error-severity-corrected/)

[Issues with "PCIe Bus Error: severity=Corrected" errors? [partially SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=320473)
