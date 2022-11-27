Status: published
Date: 2015-05-09 08:43:45
Author: Ben Chuanlong Du
Slug: working-with-spreadsheet-with-python
Title: Working with Spreadsheet in Python
Category: Computer Science
Tags: programming, Python, Spreadsheet, Excel, pandas, xlsxwriter
Modified: 2022-11-27 09:45:57

It is suggested that you avoid using Excel files (or other spreadsheet tools) for storing data.
Parquet file is currently the best format for storing table-like data.
If you do want to interact and manipulate your data using Excel (or other spreadsheet tools),
dump your data into CSV files
and then load them into Excel when needed.
However, 
if you do want to work with spreadsheet in Python,
below are some options.

## [Quadratic](https://app.quadratichq.com/)
[Quadratic](https://app.quadratichq.com/)
is a data science spreadsheet
which has Python (JavaScript and SQL) built-in.

## [Google Spreadsheet](https://www.google.com/sheets/about/)

Please refer to
[Use Python with Google Spreadsheet](https://www.legendu.net/misc/blog/use-python-with-google-spreadsheet/)
for detailed discussions.

## [pandas](https://github.com/pandas-dev/pandas)

If you just want to read an Excel spreadsheet to a pandas DataFrame 
or write a pandas DataFrame to an Excel file, 
it is best to use the pandas library directly.
Notice that 
[openpyxl](https://foss.heptapod.net/openpyxl/openpyxl)
is required if you read/write Excel files using pandas.

## [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl)

[openpyxl](https://foss.heptapod.net/openpyxl/openpyxl)
is the underlying library that pandas leverages for reading/writing Excel files.

## [xlsxwriter](https://github.com/jmcnamara/XlsxWriter)
[xlsxwriter](https://github.com/jmcnamara/XlsxWriter)
is a Python module for writing files in the Excel 2007+ XLSX file format.
XlsxWriter is designed only as a file writer. 
It cannot read or modify an existing Excel file.
However,
if an Excel file is created from data (understandable by Python),
you can create a new Excel file from the same data to overwrite the existing one. 
This sort of gives you a flavor of updating an existing Excel file.

## [xlwings](https://www.xlwings.org/)
xlwings is a commerical software but has a opensource community edition. 
It requires an installation of Excel and therefore only works on Windows and macOS. 
Note that macOS currently does not support UDFs.

## References 

https://xlsxwriter.readthedocs.io/

https://xlsxwriter.readthedocs.io/faq.html

https://xlsxwriter.readthedocs.io/examples.html

https://github.com/xlwings/xlwings