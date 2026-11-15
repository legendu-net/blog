---
title: SAS Stored Process and SAS Visual Analytics
created: '2013-07-13T22:11:25-07:00'
date: '2026-11-15T12:20:05-08:00'
authors:
  - bendu
label: sas-stored-process-and-sas-visual-analytics
license: CC-BY-4.0
tags:
  - sas
  - visualization
  - stored process
  - visual analytics
  - software
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

## SAS Stored Process

1. %stpbegin and %stpend initialize the output delivery system (ODS).

They are not needed if you don't have to use ODS.

4. \*ProcessBody; (don't forget the semicolon, this an example of using comment as markup)

1. It seems that SAS 9.2 is messy on this,
   so be aware of the version of SAS that you are using.

1. It it recommended that you begin all stored process
   (regardless of the server types)
   with %global declarations for all of you input parameters
   followed by the \*ProcessBody; comment.
   In SAS 9.3, the \*ProcessBody; is not needed

1. Special characters:
   ampersand (&), apostrophe('), percent sign (%), quotation marks ("),
   and semicolon (;).
   Be care about accepting these characters from user client.

1. accepting multiple values is messy and can result in errors if input values is the same as one of the generated variables ....

1. use masked single line for password entry

1. It's suggested that you always require non-blank input for a textbox.
   Otherwise, the stored process might run without prompt on SVA.

1. it's recommended to store source code in metadata (available in sas 9.3)

1. the header function (stpsrv_header) must be placed before any code that writes results to \_webout.)

1. The stpsrv_header is data step function used to add or modify a header

## SAS Visual Analytics

1. To insert the Stored Process,
   navigate to "Insert->Other->Stored Process".

1. use the original address fix the problem of SAS Visual Analytics

1. SVA is for large data,
   but since we work on servers, we have to upload data.
   How much time do we need to upload, e.g., 10G data in an average corporate network?
