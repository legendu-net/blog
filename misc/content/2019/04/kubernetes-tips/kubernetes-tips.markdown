Status: published
Date: 2019-04-10 09:39:25
Author: Benjamin Du
Slug: kubernetes-tips
Title: Tips on Kubernetes
Category: Software
Tags: Software, Kubernetes, k8s, minikube, kubectl, Microk8s
Modified: 2021-09-08 14:27:46

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tutorials

https://www.youtube.com/watch?v=ZpbXSdzp_vo

## Some Kubernetes Distributions

Microk8s seems like a good option.

- k3s - a light-weight Kubernetes distribution ideal for edge and development - compatible with Raspberry Pi & ARM64 (Packet, AWS Graviton)

- k3d - makes k3s available on any computer where Docker is also running

- microk8s - a Kubernetes distribution, specifically for Ubuntu users.

- minikube - a popular, but heavy-weight option that creates a Linux virtual machine your computer using VirtualBox or similar

- Docker for Mac/Windows - Docker's Desktop edition has an option to run a local Kubernetes cluster

## Tips and Traps

1. https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/
  Define a Command and Arguments for a Container

## Request Resource 

https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits

https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/

https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/

[Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)




## Kubertenes Deployment

[Kubertenes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

Below is an example YAML configuration file.
```
---
apiVersion: v1
kind: Service
metadata:
  name: helloworldserivce
spec:
  selector:
    app: hello-world
  ports:
    - protocol: "TCP"
      port: 8080
      targetPort: 80
      nodePort: 30001
  type: LoadBalancer


---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  replicas: 5
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world
        image: tutum/hello-world
        ports:
        - containerPort: 80

```
Another good example is to 
[Deploy Apache Ray on Kubernetes](https://ray.readthedocs.io/en/latest/deploy-on-kubernetes.html)
.


in you namespace, you can run `kubectl get resourcequota` to check your quota



kubectl version list

kubectl get namespace

kubectl get namespace -l account.kubernetes.io/name=your_account

kubectl config get-contexts

kubectl get account chdu -o yaml

kubectl get application jupyterhub -o yaml

kubectl get namespace your_namespace -o yaml

kubectl get rc,pod,svc -n your_namespace

Run command in a pod.

  kubectl exec -it pod_name -n your_namespace -- /bin/bash

Delete a pod.
Notice that a new pod will be created to replace the deleted pod
if there's no enough replicas.
If you want to delete a pod completely (without replacement),
you have to delete the corresponding deployment instead.

  kubectl -n your_namespace delete pods pod_name

List deployments in a namespace.

  kubectl -n ms get deployments

Delete a deployment.

  kubectl -n your_namespace delete deployment deployment_name 

## References

- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

- [helm](https://github.com/helm/helm) is the Kubernetes Package Manager

- [Multipass and MicroK8s: the Quickest Route to Ubuntu and Kubernetes?](https://dzone.com/articles/-multipass-and-microk8s-the-quickest-route-to-ubun)

- [minikube @ GitHub](https://github.com/kubernetes/minikube)

- [kubernetes @ GitHub](https://github.com/kubernetes/kubernetes)

- [Kubertenes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)