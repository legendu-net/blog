---
title: Use pdftk to Manipulating PDF Files
created: '2013-10-06T11:44:58-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: use-pdftk-to-manipulating-pdf-files
license: CC-BY-4.0
tags:
  - pdftk
  - software
  - examples
  - PDF
---

1. It is suggested that
   you use Python modules or [Stirling-PDF](editing-pdf-files-using-stirling-pdf)
   instead of `pdftk` to manipulating PDFs for several reasons.
   First,
   even though `pdftk` is a great command-line tool,
   it is hard to remember its syntax.
   On the contratry,
   Python code is easy to read and understand (even though it is more verbose).
   Second,
   it is not easy to have `pdftk` installed and configured on macOS.
   If you prefer a GUI-based application for manipulating PDF files,
   [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
   is is a robust, locally hosted web-based PDF manipulation tool using Docker.

1. Please refer to
   [PyPDF2 Examples](extracting-pdf-pages-using-the-python-package-pypdf)
   for a simple example of extracting PDF pages using the Python package `PyPDF2`.
   If you need to edit PDF pages,
   please refer to
   [Editing PDF Files](editing-pdf-files)
   for possible tools.
   If you do have to stick with `pdftk`,
   below are concrete examples on how to use it.

## Install pdftk on Ubuntu / Debian

```
sudo apt install pdftk-java
```

## Examples of Using pdftk

1. Fill in forms in an I-9 doc.

   ```
    :::bash
    # dump fields in the form (optional, for human examination only)
    pdftk i9.pdf dump_data_fields > fields.txt 
    # generate a FDF data file
    pdftk i9.pdf generate_fdf output data.fdf 
    # after fill in fileds in the FDF file, run the following command
    pdftk i9.pdf fill_form data.fdf output i9_2.pdf
   ```

   If the PDF form to fill in using `pdftk` is encrypted,
   you have to decrypt it first.
   [SmallPDF](http://smallpdf.com/) is a good online service,
   which can help you unlock PDF documents if you don't have the encryption password.

   Notice that some PDF forms (e.g., time card, I-9 form, etc.)
   cannot be saved (only a blank copy can be saved).
   after filled in using Adobe Reader.
   `pdftk` provides a solution to this problem.

1. Extract pages (from 149 to 186)
   from the PDF file "training.pdf"
   as "chap_05.pdf"

   ```
    :::bash
    pdftk training.pdf cat 149-186 output chap_05.pdf
   ```

1. Combine all my i-20s (all PDF files in current directory) into a single file.

   ```
    :::bash
    pdftk *.pdf cat output i-20_all.pdf
   ```

1. Combine scaned pages into the right order.

   ```
    :::bash
    pdftk A=20141206171918820.pdf B=20141206171951015.pdf cat A1 B1 A2-3 output i-20.pdf 
   ```

1. Rotate the first PDF page to 90 degrees clockwise

   ```
    :::bash
    pdftk in.pdf cat 1east 2-end output out.pdf
   ```

1. Rotate all pages in the second PDF file to 180 degrees

   ```
    :::bash
    pdftk A=m11.pdf B=m25.pdf cat A Bsouth output comed.pdf
   ```

1. Rotate an entire PDF document to 180 degrees

   ```
    :::bash
    pdftk in.pdf cat 1-endsouth output out.pdf
   ```

## References

- [Editing PDF Files](editing-pdf-files)
