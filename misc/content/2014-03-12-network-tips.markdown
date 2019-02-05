Status: published
Author: Ben Chuanlong Du
Date: 2017-03-19 09:57:51
Slug: network-tips
Title: Network Tips
Category: Internet
Tags: internet, web, network, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 

## General Tips

1. Use the same wireless network name and password 
    so that your laptop and phone recognize it automatically.
    This makes things much more convenient.

## Debugging Network Issues

1. Check whether you have block some services in /etc/hosts.allow or iptables, etc.

2. http://192.168.0.1/ is the router address

3. Turn off wireless router and moderm. 
    Start wireless router and wait for 30 seconds,
    and then start the moderm.

## List Network Cards 

    lspci | egrep -i --color 'network|ethernet'

Or you can use 

    lshw -class network

## IP Address

1. To get the your external ip address, use the following simple command.

        curl ifconfig.me

    Or you can directly search "my public ip" on Google.

2. To scan for all ips in a local network, you can use the following command.

        arp-scan -l

    You can specify an device to scan by the option `-I`.

        arp-scan -l -I dev

    where "dev" is the device name of your net card. 
    For example, 
    if you use wireless network, "dev" is probably "wlan0".

## Network Monitoring

1. `vnStat` is a console-based tool for monitoring network traffic bandwidth usage. 
    It uses the network interface statistics provided by the kernel as information source. 
    This means that vnStat won't actually be sniffing any traffic 
    and also ensures light use of system resources. 

2. Tcpdump is a network sniffer tool.

## References

- [Arch Linux Doc - NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager)
- [List Network Cards on Linux](https://www.cyberciti.biz/faq/linux-list-network-cards-command/)

http://www.linuxandubuntu.com/home/best-network-monitoring-tools-for-linux

https://www.ittsystems.com/linux-network-monitor-tools-and-software/

https://techtalk.gfi.com/the-top-20-free-network-monitoring-and-analysis-tools-for-sys-admins/

https://www.tecmint.com/20-netstat-commands-for-linux-network-management/

https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/
