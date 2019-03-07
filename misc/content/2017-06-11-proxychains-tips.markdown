Status: published
Date: 2019-03-07 03:24:27
Author: Ben Chuanlong Du
Slug: proxychains-tips
Title: ProxyChains Tips
Category: Software
Tags: Software, ProxyChains, network, web, proxy

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Installation

### Ubuntu

```
wajig install proxychains
```

### Mac

```
brew install proxychains-ng
```
Notice that the proxychains-ng installed using Homebrew on Mac does not work well right now (as of 2019-03-07).
An alternative way is to use proxychains via Docker on Mac.
The Docker image
[dclong/ubuntu_b](https://cloud.docker.com/repository/docker/dclong/ubuntu_b)
has proxychains (not proxychains-ng) installed.

## Tricks and Traps 

1. Use IP addresses instead of domain names if you do not know how to set up DNS for ProxyChains.

2. no special requirement on .ssh/config

3. socks5 is recommended

4. proxychains ssh -i /path_to_key user@server_ip 


## Example of ProxyChains Configuration

```text
strict_chain
quiet_mode
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.1/255.0.0.0

[ProxyList]
socks5     127.0.0.1 1080
```

## Error Message

1. SSH Configuration

        muxserver_listen bind(): No such file or directory

    This is probably due to configuration of SSH.
    For example,
    if you have the following line in the config file for SSH,
    you have to make sure that the directory `~/.ssh/control` exists.
    ```text
    ControlPath ~/.ssh/control/ssh_%h
    ```

2. Shell Alias

        [proxychains] config file found: /home/chdu/.proxychains/proxychains.conf
        [proxychains] preloading /usr/local/lib/libproxychains4.so
        proxychains can't load process....: No such file or directory

    It is possibly due to alias used with ProxyChains.
    For example,
    I have the alias defined.

        alias ssh.analytics='ssh analytics_server_ip'

    `proxychains4 ssh.analytics` throws the above error message
    while `proxychains4 ssh analytics_server_ip` works well.


1. There seems to be an issue if ProxyChains is directly in a VM,
but it works well if used in a Docker on the VM ...
