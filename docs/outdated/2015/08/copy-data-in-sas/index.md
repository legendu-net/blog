---
title: Copy Data in SAS
created: '2015-08-28T12:50:40-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: copy-data-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - copy
  - dataset
  - datasets
  - data step
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

```SAS
/* copy data using the datasets procedure */
proc datasets;
    copy in=src_lib out=des_lib index=yes;
	select data_set_1 data_set_2;
quit;

/* copy data using the copy procedure */
proc copy in=source out=xptout memtype=data;
    select bonus budget salary;
run;

/* copy using a data step */
data copy;
    set raw;
run;

/* copy data using a SQL procedure */
proc sql;
    create table t as
    select * from s;
quit;

/* copying directly using command line */
x cp src_file des_file;
```

1. datasets and copy are essentially the same
1. datasets and copy can copy the index as well
1. generally speaking, the datasets procedure is preferred
   actually datasets is recommended for not only copying but also deleting, renaming datasets, etc.
