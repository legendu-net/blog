UUID: 236e93b3-5eb1-47f0-a006-4ba28ed6546c
Status: published
Date: 2017-06-11 18:33:18
Author: Ben Chuanlong Du
Slug: tips-for-creating-docker-images
Title: Tips for Creating Docker Images
Category: Software
Tags: software, docker, image, build, create

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. ADD vs COPY: ADD auto untar which is tricky.
It is suggested that you avoid use ADD unless you are clear about the side effect.

5. Docker caches building operations. 
When cache for an operation is available, 
Docker use the cache layer directly and avoiding building the layer again.

7. docker `ARG` for build-time and `ENV` for run-time

4. You have to tag an image into a docker repository 
so that you can push the image into the repository. 

1. it might be a good idea to expose an additional port in docker, if not sure how many services will be used ...

2. to avoid duplicate of files, use different branches instead of directories seems like a good idea

3. does not support symbolic links

4. by default ubuntu docker image does not include the multiverse repository ..., manually include it if you need it ...

