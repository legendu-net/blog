Status: published
Date: 2017-06-29 21:22:04
Author: Ben Chuanlong Du
Slug: tips-on-creating-docker-images
Title: Tips on Creating Docker Images
Category: Software
Tags: software, Docker, image, build, create
Modified: 2021-09-13 14:23:53

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. The `COPY` command copies a file or directory to the Docker image to be built.
    In addition to copying the file/directory, 
    the `ADD` command also untars the file if it is a `tar` file.
    It is suggested that you avoid use the `ADD` command unless you are clear about the side effect.

2. Docker caches building operations. 
    When cache for an operation is available, 
    Docker use the cache layer directly and avoid building the layer again.

3. The command `ARG` creates environment variables for build-time 
    while the command `ENV` creates environment variables for run-time.
    Notice that substring does not work with environment variables created by `ARG`!
    For example, 
    if you have a variable created as `ARG version=6.7.6_11`. 
    `${version:0:3}` won't work in a Dockerfile.

4. When install packages using `apt-get`,
    it is suggested that you use the option `--no-install-recommends` 
    to avoid installing non necessary packages to reduce the size of the built Docker image. 
    After installing Linux packages using `apt-get`,
    run the comamnd `apt-get autoremove && apt-get autoclean` 
    to remove local caches to reduce the size of the built Docker image.

5. When install Python packages using `pip`, 
    it is suggested that you use the option `--no-cache-dir` 
    to avoid caching downloaded packages locally 
    to reduce the size of the built Docker image.

6. After installing NodeJS packages using `npm`,
    run the comamnd `npm cache clean --force` to remove local caches 
    to reduce the size of built Docker images.

7. You have to tag an image into a Docker repository 
    so that you can push the image into the repository. 

8. It is a good idea to expose additional ports to a Docker container
    just in case you might need to start other services later in the Docker container.

9. The `docker build` command does not support symbolic links 
    to files outside the root directory of `docker build`.

10. By default the `ubuntu` Docker image does not include the multiverse repository.
    You can include it manually if you need it.

## Git + SSH to Avoid Two-way Authentication Behind Corporate Firewall

Sometimes, 
you need to access an enterprise GitHub or private Git repositories to build Docker images,
which requires SSH key authentication during the building process.
Docker has built-in support of SSH key forwarding. 
For more details,
please refer to
[Build secrets and SSH forwarding in Docker 18.09](https://medium.com/@tonistiigi/build-secrets-and-ssh-forwarding-in-docker-18-09-ae8161d066)
,
[Kaniko, How to Build Container Image with SSH](https://medium.com/hiredscore-engineering/kaniko-builds-with-private-repository-634d5e7fa4a5)
and
[Using SSH to access private data in builds](https://docs.docker.com/develop/develop-images/build_enhancements/#using-ssh-to-access-private-data-in-builds)
.
However, 
I wasn't able to make it work following the instructions.

Another possible way to enable SSH key authentication when building a Docker image
is to copy your SSH private key into the directory `/root/.ssh/` inside the Docker container
and remove it after the Docker image building is complete.
In order to make SSH work without human intervention,
you have to disable strict checking of SSH. 
This can be done by having the following lines into the file `/root/.ssh/config` inside the Docker container.

    :::bash
    Host *
    StrictHostKeyChecking no
