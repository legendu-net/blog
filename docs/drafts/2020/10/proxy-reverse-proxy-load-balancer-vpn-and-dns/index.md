---
title: Proxy, Reverse Proxy, Load Balancer, VPN and DNS
created: '2020-10-03T10:47:34-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: proxy-reverse-proxy-load-balancer-vpn-and-dns
license: CC-BY-4.0
tags:
  - computer science
  - proxy
  - reverse proxy
  - DNS
  - VPN
  - network
  - internet
  - web
  - load balancing
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. socks proxy

1. sshuttle is a poor man's VPN.

[ Expose Local Service to Public ](expose-local-service-to-public)

[ Good Choices of Reverse Proxies ](good-choices-of-reverse-proxies)

## Proxy vs VPN

1. When you connect to a VPN,
   all traffic will be routed through the VPN.
   You don't have the option to route part of the traffic through the VPN.
   On the other hand,
   a proxy server is more flexible.
   It is easy to route some specific traffic through a proxy server.
   As a matter of fact,
   there are many different types of proxy corresponding to different traffic type,
   e.g., http proxy, socks proxy, ftp proxy, etc.
   Generally speaking,
   a specific type of traffic can only be visisted using the right type of proxy server.
   For example,
   a FTP server can only be visited with a FTP proxy.

1. A proxy server is not as secure as a VPN.
   However,
   a proxy server can be used to visit web sites anonymously.

## Proxy vs Reverse Proxy

1. When a client C visits a server S using proxy P,
   the server S knows the proxy P (but not the client C) who visists it.
   When a client C visits a server S which uses a reverse proxy R
   that balancing traffic to servers S1 and S2 (load balancing),
   the client C know only knows the server S but does not know underlying servers S1 and S2.

1. A proxy can be used for caching, anonymity, logging, blocking sites and microservices
   while a reverse proxy can be used for
   caching, load balancing, ingress, canary deployment and miroservices.

1. Proxy and Reverse Proxy can be used together.

For more discussions,
please refer to
[Proxy vs Reverse Proxy Server Explained](https://www.youtube.com/watch?v=SqqrOspasag)
.

## Load Balancer vs Reverse Proxy

Load Balancing is one application (special case) of reverse proxy.
For more discussions,
please refer to
[Load Balancer vs Reverse Proxy (Explained by Example)](https://www.youtube.com/watch?v=S8J2fkN2FeI)
.

## References

- [Good Choices of Reverse Proxies](good-choices-of-reverse-proxies)

- [Proxy vs Reverse Proxy Server Explained](https://www.youtube.com/watch?v=SqqrOspasag)
