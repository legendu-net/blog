---
title: Tips on nbconvert
created: '2021-01-08T13:59:41-08:00'
date: '2026-11-15T09:25:49-08:00'
authors:
  - bendu
label: tips-on-nbconvert
license: CC-BY-4.0
tags:
  - computer science
  - Jupyter
  - JupyterLab
  - notebook
  - nbconvert
  - template
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Converting too many notebooks at the same (multiprocessing) causes `zmq.error.ZMQError: Address already in use`.
   The simple way to fix this issue is to limit the number of processes converting notebooks.
   It is suggested that you keep in within 3.

1. Convert a Jupyter notebook to markdown format.

   ```bash
   jupyter nbconvert --to markdown notebook.ipynb
   ```

1. It is recommended that you use the template
   provided by the Python library
   [pretty-jupyter](https://github.com/JanPalasek/pretty-jupyter)
   when converting a notebook to HTML
   .
   [pretty-jupyter](https://github.com/JanPalasek/pretty-jupyter)
   is currently the best template for Jupyter/Lab notebooks
   which provides beautiful and dynamic reports.

   ```bash
   pip3 install pretty_jupyter
   jupyter nbconvert --to HTML --template pj notebook.ipynb
   ```

1. You can execute a notebook without converting it to a different format using the following command.

   ```bash
   jupyter nbconvert --to notebook --execute mynotebook.ipynb
   ```

   This will generate another notebook with the output inlined.
   You can use the option `--inplace` to overwrite the file inplace.

   ```bash
   jupyter nbconvert --to notebook --inplace --execute mynotebook.ipynb
   ```

1. There is no way to control the work directory of `jupyter nbconvert` at this time.
   A recommended alternative is to manually change the directory in the notebook.
   It is possible to specify the output directory where things will be deployed.
   For more discussions,
   please refer to [this issue](https://github.com/jupyter/nbconvert/issues/1343).

## Template

```bash
jupyter nbconvert --template=nbextensions mynotebook.ipynb
```

http://nbconvert.readthedocs.io/en/latest/customizing.html#Custom-Templates

```bash
jupyter nbconvert --to python 'example.ipynb' --stdout --template=simplepython.tpl
```

## Line Number in Code Blocks

```bash
jupyter nbconvert a.ipynb --to html --Highlight2HTML.extra_formatter_options linenos=table
```

## References

https://nbconvert.readthedocs.io/en/latest/usage.html

https://nbconvert.readthedocs.io/en/latest/usage.html#default-output-format-html

http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/exporting.html#nbextensions-tpl
