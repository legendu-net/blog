UUID: 902f18b9-7675-4cfe-9e87-26f56e722fbd
Status: published
Date: 2017-06-11 10:10:04
Author: Ben Chuanlong Du
Slug: proxychains-tips
Title: Proxychains Tips
Category: Programming
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Example of proxychains configuration.

```text
strict_chain
quiet_mode
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.1/255.0.0.0

[ProxyList]
socks5     127.0.0.1 1080
```

2. no special requirement on .ssh/config

3. socks5 is recommended

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

    It is possibly due to alias used with proxychains.
    For example, 
    I have the alias defined.

        alias ssh.analytics='ssh analytics_server_ip'

    `proxychains4 ssh.analytics` throws the above error message
    while `proxychains4 ssh analytics_server_ip` works well.
