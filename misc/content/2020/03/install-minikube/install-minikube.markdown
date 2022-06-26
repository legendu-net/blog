Status: published
Date: 2020-03-10 09:39:25
Author: Benjamin Du
Slug: tips-minikube
Title: Tips on Minikube
Category: Software
Tags: Software, Minikube, k8s, Kubernetes
Modified: 2021-09-15 16:39:23

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Microk8s is a more lightweight solution than Minikube 
(even thought Microk8s is only for Linux.)


## Installation

1. [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

3. [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

4. Start minikube. 
	
		:::bash
		minikube start --vm-driver=hyperkit

5. Check status of minikube.

		:::bash
		minikube status

6. Launch minikube dashboard.

		:::bash
		minikube dashboard

7. Show minikube IP.

		:::bash
		minikube ip

## References

- [4 Steps to Install Kubernetes on Ubuntu 16.04 and 18.04](https://matthewpalmer.net/kubernetes-app-developer/articles/install-kubernetes-ubuntu-tutorial.html)