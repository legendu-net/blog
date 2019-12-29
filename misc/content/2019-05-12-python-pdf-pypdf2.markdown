Status: published
Date: 2019-12-29 11:54:53
Author: Benjamin Du
Title: Extracting PDF pages using the Python Package PyPDF2
Slug: python-pdf-pypdf2
Category: Programming
Tags: programming, Python, PyPDF2, example, PDF, extract pages

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
```Python
from PyPDF2 import PdfFileWriter, PdfFileReader
from typing import List, Mapping, Sequence


def extract_pages(file: str, subfiles: Mapping[str, Sequence[int]]) -> None:
    fin = open(file, 'rb')
    reader = PdfFileReader(fin)
    for file, indexes in subfiles.items():
        _extract_pages(reader, indexes, file)
    fin.close()


def _extract_pages(reader: PdfFileReader, indexes: Sequence[int], output) -> None:
    writer = PdfFileWriter()
    for index in indexes:
        writer.addPage(reader.getPage(index))
    with open(output, 'wb') as fout:
        writer.write(fout)
```

Extract pages 0-3 as `tod.pdf`, page 4 as `loi.pdf` and pages 5-15 as `cia.pdf`.

```Python
subfiles = {
  'tod.pdf': range(4),
  'loi.pdf': [4],
  'cia.pdf': range(5, 16)
}
extract_pages('scan.pdf', subfiles)
```

## References

https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
