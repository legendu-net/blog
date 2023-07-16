Status: published
Date: 2017-02-19 10:23:04
Author: Ben Chuanlong Du
Slug: cloud-vms-tips
Title: Cloud VMs Tips
Category: Cloud
Tags: cloud, VMs, ports, AWS EC2
Modified: 2017-02-19 10:23:04

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. VPN/proxy

2. Make sure you have needed ports open. 
I deployed a docker image for RStudio on my AWS EC2 but cannot connect to it. 
It turned out that I did open the port that RStudio listens to.
