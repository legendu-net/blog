Status: published
Author: Ben Chuanlong Du
Title: Tips on pdftk
Date: 2019-05-12 15:12:58
Slug: pdftk-tips
Category: Software
Tags: tips, pdftk, Linux, software

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Even though `pdftk` is a great command-line tool,
it is suggested that you use Python libraries to manipulating PDFs.


1. Fill in forms in an I-9 doc. 

        # dump fields in the form (optional, for human examination only)
        pdftk i9.pdf dump_data_fields > fields.txt 
        # generate a FDF data file
        pdftk i9.pdf generate_fdf output data.fdf 
        # after fill in fileds in the FDF file, run the following command
        pdftk i9.pdf fill_form data.fdf output i9_2.pdf

    If the PDF form to fill in using `pdftk` is encrypted, 
    you have to decrypt it first. 
    [SmallPDF](http://smallpdf.com/) is a good online service,
    which can help you unlock PDF documents if you don't have the encryption password.
 
    Notice that some PDF forms (e.g., time card, I-9 form, etc.) 
    cannot be saved (only a blank copy can be saved). 
    after filled in using Adobe Reader.
    `pdftk` provides a solution to this problem.

2. Extract pages (from 149 to 186) 
    from the PDF file "training.pdf" 
    as "chap_05.pdf"

        pdftk training.pdf cat 149-186 output chap_05.pdf

3. Combine all my i-20s (all PDF files in current directory) into a single file.

        pdftk *.pdf cat output i-20_all.pdf

4. Combine scaned pages into the right order.

        pdftk A=20141206171918820.pdf B=20141206171951015.pdf cat A1 B1 A2-3 output i-20.pdf 

5. Rotate the first PDF page to 90 degrees clockwise

        pdftk in.pdf cat 1east 2-end output out.pdf

6. Rotate all pages in the second PDF file to 180 degrees

        pdftk A=m11.pdf B=m25.pdf cat A Bsouth output comed.pdf


7. Rotate an entire PDF document to 180 degrees

        pdftk in.pdf cat 1-endsouth output out.pdf
