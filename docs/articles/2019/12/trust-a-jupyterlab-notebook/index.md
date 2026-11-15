---
title: Trust a JupyterLab Notebook
created: '2019-12-29T20:14:09-08:00'
date: '2026-11-15T09:16:29-08:00'
authors:
  - bendu
label: trust-a-jupyterlab-notebook
license: CC-BY-4.0
tags:
  - software
  - tools
  - JupyterLab
  - trust notebook
---

By default,
IPython (kernel of Jupyter/Lab notebook) disables execution of untrusted code without explicit user input.
If you have notebook whose output containing JavaScript (e.g., JS-based visualiation)
and code wasn't run by you (e.g., the notebook is shared by someone else),
the JS-based output won't be shown by default.
For more explanation,
please refer to
[Notebook Security](https://jupyter-notebook.readthedocs.io/en/stable/security.html#notebook-security).

There are currently 2 ways to trust a notebook.
First, you can trust (multiple) notebooks via command-line.

```bash
jupyter trust path_to_notebook.ipynb
jupyter trust notebook1.ipynb notebook2.ipynb
jupyter trust *.ipynb
```

Second,
you can trust a notebook using the `Trust Notebook` command from the command tab in the left panel.

1. Click the on the `Commands` tab in the left panel.

1. Search for `Trust Notebook`.

1. Click the `Trust Notebook` button to trust a notebook.
   You will get a prompt to confirm your action.

![Trust a Notebook](https://user-images.githubusercontent.com/824507/71461881-4ff7aa80-2766-11ea-8c35-0de71284907b.png)

## References

[Notebook Security](https://jupyter-notebook.readthedocs.io/en/stable/security.html#notebook-security)

[Trusting Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#trusting-notebooks)
