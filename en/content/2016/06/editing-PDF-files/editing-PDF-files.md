Status: published
Date: 2016-06-30 10:21:47
Author: Ben Chuanlong Du
Slug: editing-PDF-files
Title: Editing PDF Files
Category: Software
Tags: software, PDF, tools, edit, convert, PDFfiller
Modified: 2024-12-04 19:19:24

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

<div style="overflow-x:auto;">
<style>
    tr:nth-child(even) {background-color: #f2f2f2}
</style>
<table style="width:100%">
  <tr>
    <th> Type </th>
    <th> Name </th>
    <th> Comments </th>
  </tr>

  <tr>
    <td rowspan="5"> Web Tools </td>
    <td> <a href="https://app.parseur.com/">Parseur</a> </td>
    <td>  
      - AI-based PDF parser
    </td>
  </tr>
  <tr>
    <td> <a href="https://www.docusign.com/">DocuSign</a>  </td>
    <td> 
        - Great for convert PDF files to MS Office files, etc. <br>
        - non-free: 1 file per 30 minutes <br>
    </td>
  </tr>
  <tr>
    <td> <a href="https://www.freepdfconvert.com/">Free PDF Convert</a> </td>
    <td> 
        - Great for convert PDF files to MS Office files, etc. <br>
        - non-free: 1 file per 30 minutes <br>
    </td>
  </tr>
  <tr>
    <td> <a href="https://www.adobe.com/acrobat/online/rearrange-pdf.html">Adobe Rearrage PDF</a> </td>
    <td>  
      - Sign in needed <br>
      - Paid service but free trial available <br>
    </td>
  </tr>
  <tr>
    <td> <a href="https://www.ilovepdf.com/">I Love PDF</a> </td>
    <td>  
      - No need to sign in <br>
      - Paid service but free trial available <br>
    </td>
  </tr>

  <tr>
    <td rowspan="4"> Linux Desktop </td>
    <td> 
      <a href="https://github.com/pdfarranger/pdfarranger">PDFArranger</a> 
    </td>
    <td>  
        - Opensource and free <br>
        - Easy to use <br>
    </td>
  </tr>
  <tr>
    <td>  
    Okular
    </td>
    <td>  
        - support annotating PDFs <br>
        - does NOT support removing/adding PDF pages <br>
    </td>
  </tr>
  <tr>
    <td> 
      <a href="https://help.gnome.org/users/evince/stable/">Evince</a> </td>
    <td>  
        - most popular PDF viewer in Linux <br>
        - does NOT support editing PDF files in any way <br>
    </td>
  </tr>
  <tr>
    <td> 
      <a href="https://code-industry.net/masterpdfeditor/">Master PDF Editor</a> 
    </td>
    <td>  
        - Free version available but with very limited features. <br>
        - Not recommended.  <br>
    </td>
  </tr>

  <tr>
    <td> macOS Desktop </td>
    <td>Preview</td>
    <td>  
        - Default PDF viewer on macOS <br>
        - Support rotating, adding and removing pages <br>
    </td>
  </tr>

  <tr>
    <td rowspan="4"> Windows Desktop </td>
    <td> 
      <a href="https://code-industry.net/masterpdfeditor/">Master PDF Editor</a> 
    </td>  
    <td>  
        - Free version available but with very limited features. <br>
        - Not recommended. <br>
    </td>
  </tr>
  <tr>
    <td> Wondershare PDFelement </td>
    <td>  
      - Great one <br>
      - support Chinese font when filling forms <br>
      - need to purchase a licence <br>
    </td>
  </tr>
  <tr>
    <td> <a href="https://www.pdffiller.com/">PDFfiller</a> </td>
    <td>  
        - good one <br>
        - does NOT support Chinese font when filling forms <br>
    </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.pdffiller.com/">Bluebeam Revue eXtreme</a> 
    </td>
    <td>  
      - Great one <br>
      - support Chinese fonts when filling forms <br>
      - need to purchase a license but 30 days free trial available <br>
    </td>
  </tr>
    
  <tr>
    <td rowspan="7"> Python Libraries </td>
    <td> 
    <a href="https://github.com/py-pdf/pypdf">PyPDF</a>
    </td>
    <td>  
      A utility to read and write PDFs with Python.
    </td>
  </tr>
  <tr>
    <td> 
      <a href="https://github.com/jsvine/pdfplumber">pdfplumber</a>
    </td>
    <td>  
    Plumbs a PDF for detailed information about each char, rectangle, line, et cetera,
    and easily extract text and tables.
    </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/jalan/pdftotext">pdftotext</a> </td>
    <td>  
    Great at parsing text from PDFs which also keeps the original layout as much as possible.
    </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/pdfminer/pdfminer.six">pdfminer.six</a> </td>
    <td>  
    A Python library for parsing PDF.
    It is good for manipulating PDF files 
    but weak at parsing text from PDF files.
    </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/socialcopsdev/camelot/">camelot</a> </td>
    <td>  
    A Python library for extracting data tables in PDF files.
    </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/chezou/tabula-py">tabula-py</a> </td>
    <td>  
    A Python binding for [tabulapdf/tabula](https://github.com/tabulapdf/tabula).
    </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/chrismattmann/tika-python">tika-python</a> </td>
    <td>  
    </td>
  </tr>
</table>
</div>

## Java Libraries

### [tabulapdf/tabula](https://github.com/tabulapdf/tabula)

A Java library for liberating data tables trapped inside PDF files.

### [apache/tika](https://github.com/apache/tika)
The Apache Tika™ toolkit detects and extracts metadata and text from over a thousand different file types (such as PPT, XLS, and PDF). 
All of these file types can be parsed through a single interface, making Tika useful for search engine indexing, content analysis, translation, and much more. 

## Command-line Tools

### pdftk

A command-line tool for filling fileds in PDF docs.

## References

- [Extracting Data from PDF Files](https://misc.legendu.net/blog/extracting-data-from-pdf-files/)

- [Python for PDF](https://towardsdatascience.com/python-for-pdf-ef0fac2808b0)

- [Hands on the Python Library pdfplumber](http://www.legendu.net/misc/blog/hands-on-the-python-library-pdfplumber)

- [Extracting PDF pages using the Python Package PyPDF2](http://www.legendu.net/en/blog/python-pdf-pypdf2)

- [Use pdftk to Manipulating PDF Files](http://www.legendu.net/en/blog/pdftk-examples)

- [View and Edit PDF Documents Using Okular](http://www.legendu.net/misc/blog/okular-tips)

- [Hands on the Python Library Pdfplumber](http://www.legendu.net/misc/blog/hands-on-the-python-library-pdfplumber)

