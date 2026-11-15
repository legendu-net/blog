---
title: Tips on Minikube
created: '2020-03-10T09:39:25-07:00'
date: '2026-11-15T12:20:37-08:00'
authors:
  - bendu
label: tips-on-minikube
license: CC-BY-4.0
tags:
  - software
  - minikube
  - k8s
  - Kubernetes
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Microk8s is a more lightweight solution than Minikube
(even thought Microk8s is only for Linux.)

## Installation

1. [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

1. [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

1. Start minikube.

   ```bash
   minikube start --vm-driver=hyperkit
   ```

1. Check status of minikube.

   ```bash
   minikube status
   ```

1. Launch minikube dashboard.

   ```bash
   minikube dashboard
   ```

1. Show minikube IP.

   ```bash
   minikube ip
   ```

## References

- [4 Steps to Install Kubernetes on Ubuntu 16.04 and 18.04](https://matthewpalmer.net/kubernetes-app-developer/articles/install-kubernetes-ubuntu-tutorial.html)
