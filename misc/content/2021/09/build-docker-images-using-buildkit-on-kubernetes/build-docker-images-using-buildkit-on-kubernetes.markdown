Status: published
Date: 2021-09-15 16:43:40
Modified: 2021-09-15 22:02:15
Author: Benjamin Du
Slug: build-docker-images-using-buildkit-on-kubernetes
Title: Build Docker Images Using BuildKit on Kubernetes
Category: Computer Science
Tags: Computer Science, software, tools, Kubernetes, k8s, BuildKit, Docker, image, build, container

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


According to
[Build Docker Images on Kubernetes](http://www.legendu.net/misc/blog/build-docker-images-on-kubernetes)
,
BuildKit is the most promissing tool to build Docker images on Kubernetes.
[buildkit-cli-for-kubectl](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl)
is a plugin for kubectl 
which provides a similar experience building Docker images on Kubernetes
as building Docker images locally using `docker build`.
[buildkit-cli-for-kubectl](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl)
works perfectly in a personal/development Kubernetes cluster (e.g., minikube running locally),
however,
it needs to resolve issues
[#68](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl/issues/68),
[#24](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl/issues/24)
and
[#25](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl/issues/25)
to make itself really usable in an enterprise production environment.

## References

- [BuildKit](https://github.com/moby/buildkit)

- [Support custom DNS from dockerd config #734](https://github.com/moby/buildkit/issues/734)