---
title: Convert HEIC Images in Linux
created: '2022-01-01T13:41:55-08:00'
date: '2026-11-15T12:20:38-08:00'
authors:
  - bendu
label: convert-heic-images-in-linux
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - iOS
  - HEIC
  - image
  - photo
  - Linux
  - convert
  - HEIF
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu

```bash
sudo apt install heif-gdk-pixbuf libheif-examples
```

## Usage

```bash
heif-convert input.HEIC output.jpg
```

## Batch Convert Using IPython / JupyterLab

If you have multiple HIEC images
and you want to convert all of them to JPG images,
then you use the following code in IPython or a JupyterLab notebook.

```bash
for p in Path().glob("*.HEIC"):
!heif-convert {p} {p.with_suffix(".jpg")}
```

## References

- [How to Open iOS HEIC Photos or Convert to JPG/PNG in Ubuntu 20.04 | 22.04](https://ubuntuhandbook.org/index.php/2021/06/open-heic-convert-jpg-png-ubuntu-20-04/)
