Status: published
Date: 2020-11-21 11:32:16
Author: Benjamin Du
Slug: tips-on-rust-kernel-via-evcxr-for-jupyterlab
Title: Tips on Rust Kernel Via Evcxr for JupyterLab
Category: Computer Science
Tags: Computer Science, Rust, kernel, Jupyter, JupyterLab, evcxr, dep, dependency
Modified: 2022-05-25 00:20:20

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[Evcxr common usage information](https://github.com/google/evcxr/blob/main/COMMON.md)

## Tips and Traps

1. Manually wrap code into a curly brace block might help 
    if life time issues happen.
    It also help if you use buffered IO.

2. Due to type deduction, 
    valid code in one cell might become invalid 
    if separated into multiple cells. 

## Docker Images

The Docker image
[dclong/jupyterhub-ds:latest](https://github.com/dclong/docker-jupyterhub-ds)
contains a valid Rust kernel for Jupyter/Lab notebooks.

## Dependency 

[Use Custom Source as Dependency](https://github.com/google/evcxr/issues/135)

    :dep serde = { version = "1.0", features = ["derive"] }
Or

    :dep serde_json = "1.0"


## References 

[Evcxr common usage information](https://github.com/google/evcxr/blob/main/COMMON.md)

https://github.com/google/evcxr/issues/135

