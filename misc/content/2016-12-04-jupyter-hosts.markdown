Status: published
Date: 2019-12-24 10:29:56
Author: Ben Chuanlong Du
Slug: jupyter-hosts
Title: Public Jupyter/JupyterLab Hosts
Category: JupyterLab
Tags: Data Science, JuptyerLab, Jupyter, notebook

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## [GitPod](https://www.gitpod.io/)

GitPod allows you to expose http services from your workspace.
This means that if you have JupyterLab/Hub installed in your GitPod image,
you can run a JupyterLab/Hub server within your GitPod worksapce and access it from public.
You can use the command `gp url port` to get the public URL to visit the exposed port/service.

## [Kaggle](https://www.kaggle.com/)

1. Terminal supported
1. Jupyter notebooks only, no JupyterLab support.
3. Only Python an R kernels are supported.
4. GPU available for request.

## [Google Colaboratory](https://colab.research.google.com/)

1. JupyterLab is not directly support (even though hacking around is possible).

2. Google Drive can be mounted.

3. Free GPU available.

## [RMOTR Notebooks | notebooks.ai](https://notebooks.ai/)

1. Installed software does not persist.

## [Code Ocean](https://codeocean.com/)

### Pros

1. Very flexible. Seems to be a good choice. 

### Cons

1. The pricing seems to be expensive ...

## [Cocalc](https://cocalc.com/)

1. The free plan is not usable as no internet access is provided for the free plan.

## [Binder](https://mybinder.org/)

### Pros

1. Great for temporary usages. 

2. Customization of Docker iamge is supported!

### Cons

1. No persistent storage at this time.

## [Quantopian](https://www.quantopian.com/)

### Pros

There seems to be lots of good tutorials on Quant Fiance. 

### Cons

1. Jupyter only and too limited features. Not usable. 

## [Gryd](https://gryd.us/)

### Cons

1. Supports only Jupyter but not JupyterLab/Hub.

2. Outdate Docker images and software (Python 3.6 only).

3. `sudo` is not supported currently.

4. Installed software does not persist.

## [DataQuest](https://www.dataquest.io/)

Course learning only.

## [Authorea](https://authorea.com/)

### Cons

1. Jupyter only. 

2. `sudo` not supported

## [YHat ScienceBox](https://aws.amazon.com/marketplace/pp/B00KQY1T32/ref=mkt_wir_yhatsciencebox)

## [Datalore](https://datalore.io/)

Not usable.

## [PythonAnywhere](https://www.pythonanywhere.com/)

### Cons

1. `sudo` is not supported.

## [Microsoft Azure Notebooks](https://notebooks.azure.com/#)

### Cons

1. Supports only Jupyter but not JupyterLab/Hub. 

2. Outdate Docker images and software (Python 3.5 only).

3. `sudo` is not supported currently.

## Amazon SageMath

## [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio)

## Deploy Your Own Public JupyterHub Server
