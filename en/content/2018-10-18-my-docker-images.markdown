UUID: 71d67e07-8408-42d5-8e11-0a17c0d79b02
Status: published
Date: 2018-10-18 23:47:12
Author: Ben Chuanlong Du
Slug: my-docker-images
Title: My Docker Images
Category: Software
Tags: software, Docker, Docker image, Ubuntu, JupyterLab, Lubuntu, dclong

## Tips

1. The `dclong/jupyterlab` Docker image is well maintained (which is the base image of `dclong/jupyterhub`), 
    however many of the `dclong/jupyterlab-*` Docker images are not maintained any more.
    Please use the corresponding `dclong/jupyterhub-*`  Docker images instead.

2. There is an issue with the `dclong/xubuntu*` Docker images due to Xfce on Ubuntu 18.04.
    It is suggested that you use the corresponding `dclong/lubuntu*` Docker images instead,
    which are based on LXQt.

- [dclong/ubuntu_b](https://hub.docker.com/r/dclong/ubuntu_b/)  
    - [dclong/python](https://hub.docker.com/r/dclong/python/)  
        - [dclong/jupyter](https://hub.docker.com/r/dclong/jupyter/)  
            - [dclong/jupyter-nodejs](https://hub.docker.com/r/dclong/jupyter-nodejs/)  
                - [dclong/jupyterlab](https://hub.docker.com/r/dclong/jupyterlab)  
                    - [dclong/jupyterlab-js](https://hub.docker.com/r/dclong/jupyterlab-js/)
                    - [dclong/jupyterlab-ts](https://hub.docker.com/r/dclong/jupyterlab-ts/)
                    - [dclong/jupyterlab-tdodbc](https://hub.docker.com/r/dclong/jupyterlab-tdodbc/)
                    - [dclong/jupyterlab-jdk](https://hub.docker.com/r/dclong/jupyterlab-jdk/)
                        - [dclong/jupyterlab-scala](https://hub.docker.com/r/dclong/jupyterlab-scala/)
                            - [dclong/jupyterlab-spark](https://hub.docker.com/r/dclong/jupyterlab-spark/)
                        - [dclong/jupyterlab-antlr4](https://hub.docker.com/r/dclong/jupyterlab-antlr4/)
                        - [dclong/jupyterlab-py](https://hub.docker.com/r/dclong/jupyterlab-py/)
                            - [dclong/jupyterlab-beakerx](https://hub.docker.com/r/dclong/jupyterlab-beakerx/)
                                - [dclong/jupyterlab-ds](https://hub.docker.com/r/dclong/jupyterlab-ds/)
                    - [dclong/jupyterlab-rb](https://hub.docker.com/r/dclong/jupyterlab-rb/)
                        - [dclong/jupyterlab-rp](https://hub.docker.com/r/dclong/jupyterlab-rp/)
                            - [dclong/jupyterlab-rp-py](https://hub.docker.com/r/dclong/jupyterlab-rp-py/)
                            - [dclong/jupyterlab-rstudio](https://hub.docker.com/r/dclong/jupyterlab-rstudio/)
                                - [dclong/jupyterlab-rstudio-py](https://hub.docker.com/r/dclong/jupyterlab-rstudio-py/)
                    - [dclong/jupyterhub](https://hub.docker.com/r/dclong/jupyterhub/)  
                        - [dclong/jupyterhub-jdk](https://hub.docker.com/r/dclong/jupyterhub-jdk/)  
                            - [dclong/jupyterhub-py](https://hub.docker.com/r/dclong/jupyterhub-py/)  
                                - [dclong/jupyterhub-beaker](https://hub.docker.com/r/dclong/jupyterhub-beakerx/)  
                                    - [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/)  
    - [dclong/python:conda3](https://hub.docker.com/r/dclong/python/)  
        - [dclong/jupyter:conda3](https://hub.docker.com/r/dclong/jupyter/)  
            - [dclong/jupyterlab:conda3](https://hub.docker.com/r/dclong/jupyterlab)  
                - [dclong/jupyterhub:conda3](https://hub.docker.com/r/dclong/jupyterhub/)  
                    - [dclong/jupyterhub-py:conda3](https://hub.docker.com/r/dclong/jupyterhub-py/)  
                        - [dclong/holoviews:conda3](https://hub.docker.com/r/dclong/holoviews/)  
                        - [dclong/jupyterhub-ds:conda3](https://hub.docker.com/r/dclong/jupyterhub-ds/)  
    - [dclong/ubuntu_cn](https://hub.docker.com/r/dclong/ubuntu_cn/)  
        - [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)  
            - [dclong/lubuntu-nodejs](https://hub.docker.com/r/dclong/lubuntu-nodejs/)  
                - [dclong/lubuntu-atom](https://hub.docker.com/r/dclong/lubuntu-atom/)  
                - [dclong/lubuntu-vscode](https://hub.docker.com/r/dclong/lubuntu-vscode/)  
            - [dclong/lubuntu-py](https://hub.docker.com/r/dclong/lubuntu-py/)  
                - [dclong/lubuntu-pycharm](https://hub.docker.com/r/dclong/lubuntu-pycharm/)  
            - [dclong/lubuntu-jdk](https://hub.docker.com/r/dclong/lubuntu-jdk/)  
                - [dclong/lubuntu-scala](https://hub.docker.com/r/dclong/lubuntu-scala/)  
                    - [dclong/lubuntu-intellij](https://hub.docker.com/r/dclong/lubuntu-intellij/)  
        - [dclong/xubuntu](https://hub.docker.com/r/dclong/xubuntu/)  
            - [dclong/xubuntu-nodejs](https://hub.docker.com/r/dclong/xubuntu-nodejs/)  
                - [dclong/xubuntu-atom](https://hub.docker.com/r/dclong/xubuntu-atom/)  
                - [dclong/xubuntu-vscode](https://hub.docker.com/r/dclong/xubuntu-vscode/)  
            - [dclong/xubuntu-py](https://hub.docker.com/r/dclong/xubuntu-py/)  
                - [dclong/xubuntu-pycharm](https://hub.docker.com/r/dclong/xubuntu-pycharm/)  
            - [dclong/xubuntu-jdk](https://hub.docker.com/r/dclong/xubuntu-jdk/)  
                - [dclong/xubuntu-scala](https://hub.docker.com/r/dclong/xubuntu-scala/)  
                    - [dclong/xubuntu-intellij](https://hub.docker.com/r/dclong/xubuntu-intellij/)  