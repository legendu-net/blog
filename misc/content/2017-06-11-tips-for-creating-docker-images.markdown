Status: published
Date: 2020-01-30 19:11:29
Author: Ben Chuanlong Du
Slug: tips-on-creating-docker-images
Title: Tips on Creating Docker Images
Category: Software
Tags: software, Docker, image, build, create

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. The `COPY` command copies a file or directory to the Docker image to be built.
    In addition to copying the file/directory, 
    the `ADD` command also untars the file if it is a `tar` file.
    It is suggested that you avoid use the `ADD` command unless you are clear about the side effect.

5. Docker caches building operations. 
    When cache for an operation is available, 
    Docker use the cache layer directly and avoid building the layer again.

7. The command `ARG` creates environment variables for build-time 
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

4. You have to tag an image into a Docker repository 
    so that you can push the image into the repository. 

1. it might be a good idea to expose an additional port in Docker, if not sure how many services will be used ...

2. to avoid duplicate of files, use different branches instead of directories seems like a good idea

3. does not support symbolic links

4. by default ubuntu Docker image does not include the multiverse repository ..., manually include it if you need it ...

