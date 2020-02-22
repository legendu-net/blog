Status: published
Date: 2020-02-21 17:04:44
Author: Benjamin Du
Slug: tips-on-openfaas
Title: Tips on Openfaas
Category: Software
Tags: Software, Kubernetes, k8s, OpenFaaS, serverless, function

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
## Tutorials

https://blog.alexellis.io/quickstart-openfaas-cli/

https://www.youtube.com/watch?time_continue=6&v=LQa8-JvIeWA&feature=emb_logo

## [Deploy OpenFaaS with Kubernetes](https://docs.openfaas.com/deployment/kubernetes/)

Deploy OpenFaaS from static YAML, via helm, or via new YAML files generated with helm template
Find your OpenFaaS gateway address
Log in, deploy a function, and try out the UI.

[Getting started with OpenFaaS on minikube](https://medium.com/faun/getting-started-with-openfaas-on-minikube-634502c7acdf)

[Deploy OpenFaaS Using helm](https://github.com/openfaas/faas-netes/blob/master/HELM.md)

### Install OpenFaaS CLI

	:::bash
	curl -sL https://cli.openfaas.com | sudo sh

You can also use the following command to install faas-cli on macOS.

	:::bash
	brew install faas-cli


faas-cli --help

## References

https://www.youtube.com/watch?time_continue=6&v=LQa8-JvIeWA&feature=emb_logo

[helm](https://github.com/helm/helm)

[OpenFaaS Workshop](https://github.com/openfaas/workshop)
