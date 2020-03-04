Status: published
Date: 2020-03-03 20:13:43
Author: Benjamin Du
Slug: kubernetes-tips
Title: Tips on Kubernetes
Category: Software
Tags: Software, Kubernetes, k8s, minikube, kubectl

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

https://www.youtube.com/watch?v=ZpbXSdzp_vo


https://github.com/kubernetes/minikube


https://github.com/kubernetes/kubernetes


[Kubertenes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

## Some Kubernetes Distributions

Microk8s seems like a good option.

- k3s - a light-weight Kubernetes distribution ideal for edge and development - compatible with Raspberry Pi & ARM64 (Packet, AWS Graviton)

- k3d - makes k3s available on any computer where Docker is also running

- microk8s - a Kubernetes distribution, specifically for Ubuntu users.

- minikube - a popular, but heavy-weight option that creates a Linux virtual machine your computer using VirtualBox or similar

- Docker for Mac/Windows - Docker's Desktop edition has an option to run a local Kubernetes cluster

## References

- [helm](https://github.com/helm/helm) is the Kubernetes Package Manager

[Multipass and MicroK8s: the Quickest Route to Ubuntu and Kubernetes?](https://dzone.com/articles/-multipass-and-microk8s-the-quickest-route-to-ubun)
