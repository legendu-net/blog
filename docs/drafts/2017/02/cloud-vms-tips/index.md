---
title: Cloud VMs Tips
created: '2017-02-19T10:23:04-08:00'
date: '2026-11-15T12:20:34-08:00'
authors:
  - bendu
label: cloud-vms-tips
license: CC-BY-4.0
tags:
  - cloud
  - VMs
  - ports
  - AWS EC2
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. VPN/proxy

1. Make sure you have needed ports open.
   I deployed a docker image for RStudio on my AWS EC2 but cannot connect to it.
   It turned out that I did open the port that RStudio listens to.
