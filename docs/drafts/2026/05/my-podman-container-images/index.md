---
title: My Podman Container Images
created: '2026-05-16T16:22:55.500335-07:00'
date: '2026-11-15T09:30:07-08:00'
authors:
  - bendu
label: my-podman-container-images
license: CC-BY-4.0
tags:
  - software
  - podman
  - container
  - image
  - Fedora
  - JupyterLab
  - JupyterHub
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Why Migrate from Docker Images to Podman Images

1. Podman is a better alternative to Docker

   - rootless
   - no daemon

1. Toolbx + Podman is an awesome combination.

   - I had a similar effort in [My Docker Images](my-docker-images) as what Toolbx/Distrobox tries to achieve.
     Migrating to Toolbx + Podman makes it much easier to maintainer those container images.

1. Switch from `ubuntu` to `fedora-toolbox` as the very base image.

   - Fedora adopts new versions of tools faster than Ubuntu.

## Recommended Container Images and Tags

Most of my container images have different variants
(corresponding to tags `latest`, `next`, etc)
for different use cases.
And each tag might have histocial versions
with the pattern `mmddhh`
(`mm`, `dd` and `hh` stand for the month, day and hour)
for fallback if a tag is broken.
Please refer to the following tag table for more details.

```{list-table}
---
header-rows: 1
---
- - Tag
  - Base Image OS
  - Comment
- - latest
  - fedora-toolbox:latest
  - The most recent stable version of the container image. 
    <span style="color:green">
        The latest tag is what most users should use.
    </span>
    It cares more about user friendliness rather than container image size or load speed.
- - next
  - fedora-toolbox:latest (or newer if necessary and well tested)
  - The most recent testing version of the container image.
    New features/tools will be added into the next tag 
    before entering other tags.
- - mmddhh
  - Histoical versions corresponding to the latest tag.
  - Fallback tags (for latest) if the latest tag is broken.
- - next_mmddhh
  - Histoical versions corresponding to the next tag.
  - Fallback tags (for next) if the next tag is broken.
```

```{list-table}
---
header-rows: 1
---
- - Container Image
  - Comment
- - [quay.io/legendu/vscode-server](https://github.com/legendu-net/docker-vscode-server)
  - Cloud IDE [code-server](https://github.com/coder/code-server) (based on VSCode)
- - [quay.io/legendu/jupyterhub-ds](https://github.com/legendu-net/docker-jupyterhub-ds)
  - For data science, machine learning and AI.
- - [quay.io/legendu/python-portable](https://github.com/legendu-net/docker-python-portable)
  - Build portable Python using [python-build-standalone](https://github.com/indygreg/python-build-standalone)
- - [quay.io/legendu/jupyterhub-kotlin](https://github.com/legendu-net/docker-jupyterhub-kotlin)
  - JupyterHub with Kotlin
```

## Usage

Those podman images can be used the regular way.
However,
they work specially well with [Toolbx](tips-on-toolbx)
.
The following documentation takes `quay.io/legendu/jupyterhub-ds` as an example.

### Create a Podman Container Using Toolbx

you can create a container using the following command.

```sh
toolbox create -c jupyterhub-ds -i quay.io/legendu/jupyterhub-ds
```

Notice that toolbx maps the user on the host into the container
to have a seamless integration.
Then you can launch the default service (JupyterHub in this case) in the container using

```sh
toolbox run /scripts/init.sh
```

### Use the JupyterHub Server

1. Open your browser and and visit `your_host_ip:8000`
   where `your_host_ip` is the URL/ip address of your server.
   If you've started the container and service on your local host,
   just visit `localhost:8000` in your browser.

1. Login to the JupyterHub server
   using your user name (on the host machine)
   and no password is required.

1. Enjoy JupyterLab notebook!

## Easy Install of Other Kernels

Install and configure PySpark for use with the Python kernel.

```bash
icon spark -ic && icon pyspark -ic
```

Install the evcxr Rust kernel.

```bash
icon evcxr -ic
```

Install the Almond Scala kernel.

```bash
icon almond -ic
```

Many other software/tools can be easily install by
[icon](https://github.com/legendu-net/icon)
.

## Build Container Images

Those podman images are auto built leveraging GitHub Actions workflow
.

## Tips for Maintaining Container Images (for My own Reference)

1. Do NOT update the `latest` tag
   until you have fully tested the corresponding `next` tag.

1. Do NOT add new features or tools unless you really need them.

1. It generally a good idea to restrict versions of non-stable packages to be a specific (working) version
   or a range of versions that is unlikely to break.

## On Failure of GitHub Actions Workflow for Building Container Images

1. If the Docker image building workflow fails due to network issues,
   it might not work to rerun failed pipelines in GitHub Actions
   (as the network issue is like due to probalematic network nodes
   and retrying failed pipelines sending jobs to the same nodes).
   In such situtions,
   it is better to trigger a new run of the workflow.
