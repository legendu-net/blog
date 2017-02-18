UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Some Tips for pdftk
Date: 2015-08-01 13:35:45
Slug: pdftk-tips
Category: Software
Tags: tips, pdftk, Linux, software

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Fill in PD Forms

1. Some PDF forms (e.g., time card, I-9 form, etc.) 
cannot be saved after filled in (only a blank copy can be saved). 
You can use pdftk to help fill in the forms
and the filled forms are saved correctly.
If a PDF form is encrypted/locked, 
you have to decrypt/unlock it first. 
[SmallPDF](http://smallpdf.com/) is a good online service,
which can help you unlock PDF documents.
 

1. pdftk checkbox is tricky: first if group, then every checkbox need a value, (Yes) (Off), /Yes, /Off, /A ...

2. pdftk fill form, fdf, sometimes filed_name[0] and filed_name[1], what's the difference between them?

3. Illustration of filling in an I-9 form 
```bash
# dump fields in the form (optional, for human examination only)
pdftk i9.pdf dump_data_fields > fields.txt 
# generate a FDF data file
pdftk i9.pdf generate_fdf output data.fdf 
# after fill in fileds in the FDF file, run the following command
pdftk i9.pdf fill_form data.fdf output i9_2.pdf
```

2. Extract pages (from 149 to 186) 
from the PDF file "training.pdf" 
as "chap_05.pdf"

```bash
pdftk training.pdf cat 149-186 output chap_05.pdf
```

3. Combine all my i-20s (all PDF files in current directory) into a single file.

```bash
pdftk *.pdf cat output i-20_all.pdf
```

4. Combine scaned pages into the right order.

```bash
pdftk A=20141206171918820.pdf B=20141206171951015.pdf cat A1 B1 A2-3 output i-20.pdf 
```

5. Rotate the first PDF page to 90 degrees clockwise

```bash
pdftk in.pdf cat 1east 2-end output out.pdf
```

6. Rotate all pages in the second PDF file to 180 degrees
```bash
pdftk A=m11.pdf B=m25.pdf cat A Bsouth output comed.pdf
```

5. Rotate an entire PDF document to 180 degrees

```bash
pdftk in.pdf cat 1-endsouth output out.pdf
```
