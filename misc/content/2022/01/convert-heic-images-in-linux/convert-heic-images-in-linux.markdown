Status: published
Date: 2022-01-01 13:41:55
Modified: 2022-12-07 22:11:36
Author: Benjamin Du
Slug: convert-heic-images-in-linux
Title: Convert HEIC Images in Linux
Category: Computer Science
Tags: Computer Science, programming, iOS, HEIC, image, photo, Linux, convert, HEIF

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu

    :::bash
    wajig install heif-gdk-pixbuf libheif-examples

## Usage

    :::bash
    heif-convert input.HEIC output.jpg
    
## Batch Convert Using IPython / JupyterLab
If you have multiple HIEC images 
and you want to convert all of them to JPG images,
then you use the following code in IPython or a JupyterLab notebook.

    :::bash
    for p in Path().glob("*.HEIC"):
        !heif-convert {p} {p.with_suffix(".jpg")}

## References

- https://ubuntuhandbook.org/index.php/2021/06/open-heic-convert-jpg-png-ubuntu-20-04/
