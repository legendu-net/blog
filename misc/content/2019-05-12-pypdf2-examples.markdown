Status: published
Date: 2019-05-12 15:21:22
Author: Benjamin Du
Slug: pypdf2-examples
Title: PyPDF2 Examples
Category: Programming
Tags: programming, Python, PyPDF2, example

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Extract the first 2 pages from `input.pdf` and write them to `output.pdf`.
```
from PyPDF2 import PdfFileWriter, PdfFileReader

output_pdf = PdfFileWriter()
input_pdf = PdfFileReader(open('input.pdf', 'rb'))
for i in [0, 1]:
    output_pdf.addPage(input_pdf.getPage(i))
with open('output.pdf', 'wb') as fout:
    output_pdf.write(fout)
```

## References

https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python