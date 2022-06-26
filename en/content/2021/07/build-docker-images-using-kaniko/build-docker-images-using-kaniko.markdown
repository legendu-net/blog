Status: published
Date: 2021-07-20 17:09:59
Modified: 2021-09-24 11:47:55
Author: Benjamin Du
Slug: build-docker-images-using-kaniko
Title: Build Docker Images Using Kaniko
Category: Computer Science
Tags: Computer Science, programming, Kaniko, Docker, build, image, buildah



1. Kaniko works differently from Docker. 
    It runs inside a Docker container and detect and extract new layers to build Docker images. 
    Since Kaniko manipulates the filesystem (layers) inside the Docker container,
    it can have unexpected side effect if not used carefully. 
    For this reason,
    the developer team suggests users to use Kaniko only via official Docker images.
    The official Docker image
    `gcr.io/kaniko-project/executor` 
    limits itself to run the command `/kaniko/executor` only
    so that users won't screw up things accidentally.
    The official Docker image
    `gcr.io/kaniko-project/executor:debug`
    adds a shell (`/busybox/sh`) in addition to to the command `/kaniko/executor`.
    However,
    `/busybox/sh` in `gcr.io/kaniko-project/executor:debug`
    is minimal and limited too.
    For example,
    the `cd` command is not provided 
    and users can work in the directory `/workspace` only.
    Even if some users have tried customizing their own Kaniko Docker images 
    and reported successful experiences,
    it is NOT guranteed that customized Kaniko Docker images will always work.
    Any additional tool (besides `/kaniko/executor` and `/busybox/sh`) 
    might fail to work due to changed filesystems (layers) during the building of a Docker image,
    and even worse, might intervent the building of Docker images.

2. Even if you use an official Kaniko Docker image, 
    it doesn't mean that it will always work 
    even if your Docker image can be built successfull using Docker.
    Various issues can make the image building fail to work.

    i. If your Docker image intervent with critial Kaniko filesystem/layers,
        it might fail to work.
        For example, 
        `/workspace` is the work directory of Kaniko.
        If you Docker image create a directory `/workspace` 
        or make it a symbolic link to another directory,
        Kaniko might fail to build your Docker image.

    2. Network issues.

2. It might be helpful to keep a Kaniko pod running 
    for testing, debugging and possibly for building multiple Docker images (even if this is not a good idea).
    You couldn't do this with the Docker image 
    `gcr.io/kaniko-project/executor`,
    however, 
    it is doable with the Docker image
    `gcr.io/kaniko-project/executor:debug`.
    Basically,
    you have to define a Kubernetes command (entrypoint in Docker) 
    which runs forever for the container.
    A simple shell command that runs forever is `tail -f /dev/null`,
    so you can define the command as 
    `["tail", "-f", "/dev/null"]`
    .
    The above command implicity invokes `/busybox/sh`.
    If you'd like to invoke `/busybox/sh` directly,
    make sure to use
    `["/busybox/sh", "-c", "tail -f /dev/null"]`
    instead of
    `["/busybox/sh", "-c", "tail", "-f", "/dev/null"]`
    as the latter one won't work with Kubernetes
    even if `docker run --entrypoint /busybox/sh gcr.io/kaniko-project/executor:debug -c tail -f /dev/null` runs OK locally.

2. The credential file `config.json` for authentication 
    should be mounted to `/kaniko/.docker/config.json` 
    when running an official Kaniko Docker image.
    Some users customize their own Kaniko Docker images,
    in which situations, 
    the credential file `config.json` might need to be mounted/placed at `$HOME/.docker/config.json`,
    where `$HOME` is the home directory of the user that is used to run `/kaniko/executor`.
    In most situations, 
    customized Kaniko Docker images use the root user 
    whose home directory is `/root`.
    However, 
    be aware that the directory `/root` might not survive during the building of Docker images 
    and thus can make authentication to fail.

3. It is suggested that you always pass the option `--log-timestamp` 
    when building Docker images using `/kaniko/executor`.
    It adds timestamps into logs 
    which is useful for debugging and measuring performancing of pulling, pushing and building.

4. The option `--cleanup` (of `/kaniko/executor`) cleans up the filesystem/layers
    after building a Docker image 
    so that you can use the same Kaniko Docker container to build multiple Docker images.
    However,
    Kaniko won't recover the filesystem/layers if it fails to build or push a Docker image
    even if the option `--cleanup` is specified.
    It is suggested that you build **only 1 image in a Kaniko pod/container**.
    When you need to build another Docker image, 
    start a new Kaniko pod/container.

5. Always, specify `--push-try` (e.g., `--push-retry=2`)
    and `--image-fs-extract-retry` when Kaniko > 1.6.0 is released.

## Kaniko Build Contexts

1. Kaniko supports varying context locations.
    Specifically, 
    Git repositories are supported as context locations.
    For more details, 
    please refer to
    [Kaniko Build Contexts](https://github.com/GoogleContainerTools/kaniko#kaniko-build-contexts)
    .
    However, 
    private Git repositories might not work at this time (Sep 2021).
    Please refer to the issue
    [build context in private gitlab repository #719](https://github.com/GoogleContainerTools/kaniko/issues/719)
    for more discussions.

## Connection Reset by Peer

`--image-fs-extract-retry=2` (need a version > 1.6.0)

`--push-retry=2`

What seems to help is the following annotations for the registry Nginx Ingress (taken from the Gitlab Helm chart):

    :::json
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "900"
    nginx.ingress.kubernetes.io/proxy-request-buffering: "off"
    nginx.ingress.kubernetes.io/proxy-buffering: "off"

[Connection reset by peer #797](https://github.com/GoogleContainerTools/kaniko/issues/797)

[error building image: error building stage connection reset by peer #1377](https://github.com/GoogleContainerTools/kaniko/issues/1377)

[Improve retry logic for downloading base image - Implement a --pull-retry flag #1627](https://github.com/GoogleContainerTools/kaniko/issues/1627)

[failed to get filesystem from image: connection reset by peer #1717](https://github.com/GoogleContainerTools/kaniko/issues/1717)

## References

- [Introducing kaniko: Build container images in Kubernetes and Google Container Builder without privileges](https://cloud.google.com/blog/products/containers-kubernetes/introducing-kaniko-build-container-images-in-kubernetes-and-google-container-builder-even-without-root-access)

- [Official Kaniko Dockerfile](https://github.com/GoogleContainerTools/kaniko/blob/master/deploy/Dockerfile)

- [A quick look at Google's Kaniko project](https://blog.alexellis.io/quick-look-at-google-kaniko/)

- [Use kaniko to build Docker images](https://docs.gitlab.com/ee/ci/docker/using_kaniko.html)

- [Best practices for running Buildah in a container](https://developers.redhat.com/blog/2019/08/14/best-practices-for-running-buildah-in-a-container)

- [Building Container Image inside Container using Buildah](https://insujang.github.io/2020-11-09/building-container-image-inside-container-using-buildah/)
