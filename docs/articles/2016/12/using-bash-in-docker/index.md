---
title: Using Bash in Docker
created: '2016-12-14T13:54:14-08:00'
date: '2026-11-15T12:20:31-08:00'
authors:
  - bendu
label: using-bash-in-docker
license: CC-BY-4.0
tags:
  - software
  - Docker
  - Bash
  - shell
---

If the docker container was started using `/bin/bash`
(you can check using `docker ps`) command you can access it using `attach`.

```bash
docker attach container_name_or_id
```

If the docker container was started but not with `/bin/bash`,
you have to create a bash instance inside the container using `exec`.

```bash
docker exec -it container_name_or_id /bin/bash
```

Notice that `attach` does not create a new instance of bash
but use the already created one in the corresponding docker container.
However,
both `exec` and `run` create new bash instances.

## Examples

```
docker exec -it -u dclong jupyterlab-py jupyter nbconvert --to html --execute --ExecutePreprocessor.timeout=600 /workdir/spend.ipynb 
```
