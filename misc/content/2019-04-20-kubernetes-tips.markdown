Status: published
Date: 2020-02-21 15:02:06
Author: Benjamin Du
Slug: kubernetes-tips
Title: Kubernetes Tips
Category: Software
Tags: Software, Kubernetes, k8s, minikube, kubectl

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

https://www.youtube.com/watch?v=ZpbXSdzp_vo


https://github.com/kubernetes/minikube


https://github.com/kubernetes/kubernetes


[4 Steps to Install Kubernetes on Ubuntu 16.04 and 18.04](https://matthewpalmer.net/kubernetes-app-developer/articles/install-kubernetes-ubuntu-tutorial.html)


1. [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

2. Install VirtualBox

3. [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

4. Start minikube. 
	
		:::bash
		minikube start --vm-driver=virtualbox

5. Check status of minikube.

		:::bash
		minikube status


minikube dashboard

minikube ip

[Kubertenes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
