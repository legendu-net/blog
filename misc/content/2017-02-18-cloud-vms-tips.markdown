UUID: b9b3da8d-aec5-43b1-bf8e-8cfd6efb3f5f
Status: published
Date: 2017-02-18 12:50:34
Author: Ben Chuanlong Du
Slug: cloud-vms-tips
Title: Cloud VMs Tips
Category: Cloud
Tags: cloud, VMs, ports, AWS EC2

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. Make sure you have needed ports open. 
I deployed a docker image for RStudio on my AWS EC2 but cannot connect to it. 
It turned out that I did open the port that RStudio listens to.
