---
title: Public Jupyter/JupyterLab Hosts
created: '2016-12-14T18:35:33-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: public-jupyter-jupyterlab-hosts
license: CC-BY-4.0
tags:
  - data science
  - JuptyerLab
  - Jupyter
  - notebook
  - deepnote
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [Google Firebase Studio](tips-on-google-firebase-studio)

You can use notebooks after installing the jupyter extension
and the programming lanuage that you want to use in Jupyter notebook.

## [Google Cloud Shell](https://cloud.google.com/shell/docs)

Technically speaking,
[Google Cloud Shell](https://cloud.google.com/shell/docs)
isn't Jupyter/JupyterLab service.
It is a always free small VM with 5GB persistent storage
that Google Cloud Platform offers to its customers
to experiment with Google Cloud and manage projects and resources from web browsers.
However,
the Google Cloud Shell can be used to run Jupyter/JupyterLab notebooks in 2 ways.

1. Google Cloud Shell comes with Cloud Shell Editor
   which is a cloud IDE based on Theia
   (which a cloud & desktop IDE framework implemented in TypeScript and is partly VSCode compatible)
   .
   With Cloud Shell Editor,
   Jupyter/JupyterLab notebooks can be run
   (if the required notebook kernel is installed).

1. You can manually install JupyterLab and launch a service.

A Cloud Shell VM is ephemeral and no system-wide change will persist beyond session end.
There are 3 ways to circumvent this problem.

1. Use a custom Docker image (recommended).
   Please refer to
   [container image customization](https://cloud.google.com/shell/docs/configuring-cloud-shell#container_image_customization)
   for detailed instructions.

1. Use a
   [environment customization script](https://cloud.google.com/shell/docs/configuring-cloud-shell#environment_customization_script)
   .

1. Install tools to your local directories which are persistent (not recommended).

## [GitPod](https://www.gitpod.io/)

GitPod allows users to use their customized Docker images
and allow users to expose HTTP services from your workspace.
This means that if you have JupyterLab/Hub installed in your GitPod image,
you can run a JupyterLab/Hub server within your GitPod worksapce and access it from public.
Once you start a new services listing on a port,
a prompt will show up at the right-bottom corner and you can click it to visit the service.
The prompt will disappear after a few seconds or after being clicked.
You can always use command `gp url port` to find the public URL of an exposed port/service.

Note that GitPod has a timeout of 30 minutes (unless you have the Unlimited Plan)
if there's no activity on the GitPod IDE page.
This seriously limit the usability of the JupyterLab server launched from a GitPod workspace.
You will have to go back to the IDE page once for a while
to make sure that your workspace won't timeout and get killed.
I typically use JupyterLab launched from GitPod for ad hoc short-time tasks,
e.g., writing a notebook-based article for my blog.

## [Noteable](https://app.noteable.io)

### Pros

1. support filesystem navigation
1. support different kernels in different cells in the same notebook

### Cons

1. no terminal support

## [Google Colaboratory](https://colab.research.google.com/)

1. No terminal unless you
   [hack it to run JupyterLab](https://numba.pydata.org/numba-doc/dev/reference/jit-compilation.html?highlight=target%20cuda)

1. Support root user.

1. Google Drive can be mounted.

1. **Free GPU available!**

## [Kaggle](https://www.kaggle.com/)

1. Jupyter notebooks only, no JupyterLab support.
1. Only Python an R kernels are supported.
1. GPU available for request.

## [DeepNote](https://deepnote.com/)

### Pros

1. Allow customized Docker images.

### Cons

1. DeepNote uses a customized interface instead of Jupyter/Lab interface
   causing
   - no easy way to navigate through the file system
   - no easy way to switch among different kernels

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

1. Customization of Docker iamge is supported!

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

1. Outdate Docker images and software (Python 3.6 only).

1. `sudo` is not supported currently.

1. Installed software does not persist.

## [DataQuest](https://www.dataquest.io/)

Course learning only.

## [Authorea](https://authorea.com/)

### Cons

1. Jupyter only.

1. `sudo` not supported

## [YHat ScienceBox](https://aws.amazon.com/marketplace/pp/B00KQY1T32/ref=mkt_wir_yhatsciencebox)

## [Datalore](https://datalore.io/)

Not usable.

## [PythonAnywhere](https://www.pythonanywhere.com/)

### Cons

1. `sudo` is not supported.

## [Microsoft Azure Notebooks](https://notebooks.azure.com/#)

### Cons

1. Supports only Jupyter but not JupyterLab/Hub.

1. Outdate Docker images and software (Python 3.5 only).

1. `sudo` is not supported currently.

## Amazon SageMath

## [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio)

## Deploy Your Own Public JupyterHub Server

It is very easy to deploy a Jupyter/Hub/Lab server.
The difficult part is how to make your Jupyter/Hub/Lab secure.
Please refer to
[Running a notebook server](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html)
and
[Installing and Running Jupyter Notebooks on a Server](https://janakiev.com/blog/jupyter-notebook-server/)
on how to set up SSL encryption to enable HTTPS for your Jupyter/Hub/Lab server.
