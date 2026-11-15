---
title: Number of Observations in a SAS Dataset
created: '2015-05-17T18:57:48-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: number-of-observations-in-a-sas-dataset
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - observation
  - number
  - dataset
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

```SAS
proc sql;
    select count(*) from lib.dataset;
run;
```

Proc sql is not efficient when we have large dataset.
Though using ATTRN is good method but this can accomplish within base sas,
here is the efficient solution that can give number of obs of even billions of rows just by reading one row:

```SAS
data DS1;
    set DS nobs=i;
    if _N_ =2 then stop;
    No_of_obs=i;
run;
```

```SAS
data _null_;
    set yourdataset nobs=number;
    put number= ;
    stop;
run;
```
