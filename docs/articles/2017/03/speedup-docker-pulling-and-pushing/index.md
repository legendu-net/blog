---
title: Speedup Docker Pulling and Pushing
created: '2017-03-29T01:23:50-07:00'
date: '2026-11-15T09:16:23-08:00'
authors:
  - bendu
label: speedup-docker-pulling-and-pushing
license: CC-BY-4.0
tags:
  - software
  - Docker
  - speedup
  - performance
  - DaoCloud
---

Pulling/pushing Docker images is extremely slow in China.
There are a few ways to speed up docker pulling/pushing in China.

## Using the Official China Mirror

Now the best way is to use the official China mirror.
Please refer to
[Docker 中国官方镜像加速](https://www.docker-cn.com/registry-mirror)
for details.
You have to restart the Docker daemon in order for the configuration to take effect.
If you are Ubuntu,
then you can use the following command to restart the daemon.

```
sudo service docker restart
```

## Use the USTC Mirror

It seems to me that the official China mirror is gone.
However,
there are still other good mirrors that you can use.
For example,
you can usee the USTC mirror
by adding the following option into the file `/etc/docker/daemon.json`.

```
:::json
{
    "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"]
}
```

## Old Way

One way to speedup Docker visiting is to use [DaoCloud](https://www.daocloud.io/) as a proxy.
All you have to do is simply adding the following line into the file `/etc/default/docker`.

```text
DOCKER_OPTS="--registry-mirror='http://a92c904a.m.daocloud.io'"
```

Please refer to <https://www.daocloud.io/mirror#accelerator-doc> for more details.
