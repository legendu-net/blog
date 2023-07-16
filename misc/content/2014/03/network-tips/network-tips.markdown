Status: published
Author: Ben Chuanlong Du
Date: 2014-03-03 11:41:59
Modified: 2021-12-24 10:12:50
Slug: network-tips
Title: Tips on Network
Category: Internet
Tags: internet, web, network, tips

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


## Improve Network Speed

[软路由让你的翻墙速度快十倍！LEDE软路由v2ray对比梅林固件(v2ray/LEDE/谷歌云)](https://www.youtube.com/watch?v=WqSCkr8DuRI)

https://zhuanlan.zhihu.com/p/129139369

https://www.zhihu.com/question/332524152

[一个U盘优盘就翻墙 免费拥有VPN翻墙路由器的两种方法 Openwrt/LEDE软路由U盘优盘的制作 ButterflyVPN评测](https://www.youtube.com/watch?v=FeRgNwa0eOA)

## QR Code for WiFi

[WiFi Card](https://github.com/bndw/wifi-card)
print a QR code for connecting to your WiFi (wificard.io)

## VPN/Proxy

https://www.youtube.com/watch?v=F6yh4b7ML5g

## Reverse Proxy 

[nginx](https://github.com/nginx/nginx)

[caddy](https://github.com/caddyserver/caddy)

https://engineering.hashnode.com/after-4-years-with-nginx-we-switched-to-caddy-here-is-why-cjxbv8eb2001ke8s1yl7ndroz

## Expose Local Web Services to Public

Please refer to
[Expose Local Service to Public](https://www.legendu.net/misc/blog/expose-local-service-to-public)
or detailed discussions.

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

## Permanent Change to the File /etc/resolv.conf

Notice that the content of `/etc/resolv.conf` is dynamically managed. 
Content of the file might change after the host machine is rebooted. 
Below are some ways to make changes to the file `/etc/resolv.conf` permanent.
(Notice that below are solutions for Linux machines only.
Do NOT use any of the solutions below when you are building a Docker image
as Docker has its own way of handling DNS.)

1. Make `/etc/resolv.conf` immutable. 

2. Update the file `/etc/dhcp/dhclient.conf`

3. use `resolvconf`

4. more ...

https://kb.isc.org/docs/isc-dhcp-44-manual-pages-dhclientconf

https://www.techrepublic.com/article/how-to-set-dns-nameservers-in-ubuntu-server-18-04/

https://unix.stackexchange.com/questions/128220/how-do-i-set-my-dns-when-resolv-conf-is-being-overwritten

https://unix.stackexchange.com/questions/128220/how-do-i-set-my-dns-when-resolv-conf-is-being-overwritten/163506#163506

https://wiki.debian.org/resolv.conf

https://itsfoss.com/resolvconf-permanent-ubuntu/

https://askubuntu.com/questions/623940/network-manager-how-to-stop-nm-updating-etc-resolv-conf/623956#623956

https://askubuntu.com/questions/157154/how-do-i-include-lines-in-resolv-conf-that-wont-get-lost-on-reboot

https://www.linuxquestions.org/questions/linux-software-2/i-can%27t-change-file-permission-via-chattr-4175553888/

https://stackoverflow.com/questions/48578108/what-the-differences-between-chattr-i-file-and-chmod-w-file

https://askubuntu.com/questions/1006741/what-is-the-difference-between-chmod-and-chattr


## List Network Cards 

    lspci | egrep -i --color 'network|ethernet'

Or you can use 

    lshw -class network

## IP Address

1. To get the your public ip address, use the following simple command.

        :::bash
        curl ifconfig.me

    Or you can use https://www.ipify.org/ 
    which provides A Simple Public IP Address API.

        :::bash
        curl https://api.ipify.org?format=json

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

- [Linux Network Tips](http://www.legendu.net/misc/blog/linux-network-tools)
- [Arch Linux Doc - NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager)
- [List Network Cards on Linux](https://www.cyberciti.biz/faq/linux-list-network-cards-command/)

http://www.linuxandubuntu.com/home/best-network-monitoring-tools-for-linux

https://www.ittsystems.com/linux-network-monitor-tools-and-software/

https://techtalk.gfi.com/the-top-20-free-network-monitoring-and-analysis-tools-for-sys-admins/

https://www.tecmint.com/20-netstat-commands-for-linux-network-management/

https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool/
