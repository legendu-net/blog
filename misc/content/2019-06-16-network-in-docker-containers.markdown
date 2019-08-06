Status: published
Date: 2019-08-06 22:07:34
Author: Benjamin Du
Slug: network-in-docker-containers
Title: Network in Docker Containers
Category: Software
Tags: Software, Docker container, network, DNS, proxy

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. DNS is a common issue in Docker containers, 
  especially behind a corporate firewall.
  While the Linux way of handling DNS is to configure the file `/etc/resolv.conf` 
  (or via other related configuration files or tools),
  the Docker way is to pass DNS servers to the container (will be added to `/etc/resolv.conf`) via the option `--dns`. 
  Multiple DNS servers can be passed using multiple `--dsn` options.


2. Due to possible DNS issues in Docker containers, 
  it is suggested that you use IP addresses (e.g., proxy servers) instead of URL names where possible. 


## Configure Proxy for Docker Containers

https://docs.docker.com/network/proxy/

## Configure Proxy for Docker Daemon

https://stackoverflow.com/questions/23111631/cannot-download-docker-images-behind-a-proxy

https://docs.docker.com/config/daemon/systemd/

If you set up http_proxy, https_proxy and restart the Docker daemon, 
it should work.


## References

https://docs.docker.com/config/containers/container-networking/

https://docs.docker.com/v17.09/engine/userguide/networking/work-with-networks/#basic-container-networking-example

https://docs.docker.com/v17.09/engine/userguide/networking/

https://docs.docker.com/v17.09/engine/userguide/networking/configure-dns/

https://docs.docker.com/v17.09/engine/userguide/networking/default_network/configure-dns/

https://docs.docker.com/install/linux/linux-postinstall/#specify-dns-servers-for-docker

https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker

https://stackoverflow.com/questions/24151129/network-calls-fail-during-image-build-on-corporate-network

https://github.com/moby/moby/issues/26330

https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker?rq=1
