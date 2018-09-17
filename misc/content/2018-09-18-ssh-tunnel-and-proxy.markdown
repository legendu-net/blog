UUID: 87b30504-5bb2-478b-be49-1ae1027fe610
Status: published
Date: 2018-09-18 00:07:35
Author: Ben Chuanlong Du
Slug: ssh-tunnel
Title: SSH Tunnel
Category: Software
Tags: software, SSH tunnel, socks proxy

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

```
ssh -i /path_to_key -fND 1080 user@server_ip
```
If you want the tunnel to be accessible by other machines as well
rathe than the localhost only, 
you can bind it to all IPs.
```
ssh -i /path_to_key -fND "*:1080" user@server_ip
```

## References

[Proxy Using SSH Tunnel](https://www.systutorials.com/944/proxy-using-ssh-tunnel/)

[Quick-Tip: SSH Tunneling Made Easy](http://www.revsys.com/writings/quicktips/ssh-tunnel.html)
