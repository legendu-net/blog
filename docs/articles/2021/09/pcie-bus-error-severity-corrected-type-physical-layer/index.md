---
title: 'PCIe BUS Error: Severity=Corrected, Type=Physical Layer'
created: '2021-09-06T12:47:10-07:00'
date: '2026-11-15T09:17:09-08:00'
authors:
  - bendu
label: pcie-bus-error-severity-corrected-type-physical-layer
license: CC-BY-4.0
tags:
  - OS
  - Linux
  - issue
  - error
  - kernel
  - PCIe
  - bus
  - Corrected
  - pci=noaer
  - pci-nomsi
---

## Explanation of the Error

See
[Chat with Geminie: PCIe BUS Error: Severity=Corrected, Type=Physical Layer](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221A9Alzo5Bjaf1x0To03yD9Ws15EL5GHMd%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## Symptoms

Below are step-by-step symptoms from superficial to root causes.

1. Your Linux system becomes very slow
   even if the system has enough CPU and memory resources.

1. `top` reports a large portion of CPU waiting on IO.

1. `sudo iotop` reports `jbd2` using lots of disk IO.

1. The command `ls -lhS /var/log/*log | head`
   shows a few obviously large log files.
   Generally speaking,
   a log file in MBs is considered large.

1. A large log file shows frequent error/warning messages.
   For example,
   The kernel log file `/var/log/kern.log`
   shows the following error message frequently.

   > PCIe-Bus-Error:-severity=Corrected,-type=Physical-Layer

A faster alternative way to check whether your machine is experiencing this issue
is to directly search for the keyword `PCIe-Bus-Error` in log files.

```bash
ls /var/log/*log | xargs grep PCI-Bus-Error
```

If you see lots of occurrences of the following line,
then your machine is likely experiencing the issue.

> PCIe-Bus-Error:-severity=Corrected,-type=Physical-Layer

## Solution

1. Empty large log files.
   Taking `/var/log/kern.log` as an example,
   you can empty it using the following command.
   Notice that you'd better NOT remove log files.

   ```bash
   cat /dev/null | sudo tee /var/log/kern.log
   ```

1. Edit the GRUB file `/etc/default/grub`
   to add the `pci=nomsi` parameter
   to the `GRUB_CMDLINE_LINUX_DEFAULT` directive.

1. Update the GRUB.

   ```bash
   sudo update-grub
   ```

1. If the above steps does not fix the issue,
   try repeating steps 2-3 with other parameters,
   e.g., `pci=noaer` or `pci=mmconf`.

## References

- [Solution: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e6(Receiver ID)](https://codesport.io/linux/solution-pcie-bus-error-severitycorrected-typephysical-layer-id00e6receiver-id/)

- [Troubleshooting PCIe Bus Error severity Corrected on Ubuntu and Linux Mint](https://itsfoss.com/pcie-bus-error-severity-corrected/)

- [Issues with "PCIe Bus Error: severity=Corrected" errors? [partially SOLVED]](https://forums.linuxmint.com/viewtopic.php?t=320473)
