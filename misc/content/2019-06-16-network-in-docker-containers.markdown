Status: published
Date: 2019-07-30 07:46:57
Author: Benjamin Du
Slug: network-in-docker-containers
Title: Network in Docker Containers
Category: Software
Tags: Software, Docker container, network, DNS, proxy

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. DNS is a common issue in Docker containers, especially behind a corporate firewall.
  In that situation, using IP is one possible solution.

Docker mounts /etc/resolv.conf, ..., etc. 


https://docs.docker.com/install/linux/linux-postinstall/#specify-dns-servers-for-docker

https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker

https://stackoverflow.com/questions/24151129/network-calls-fail-during-image-build-on-corporate-network

https://github.com/moby/moby/issues/26330

https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker?rq=1
