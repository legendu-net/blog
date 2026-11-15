---
title: Limiting/Filtering Results in SAS
created: '2015-05-28T12:54:45-07:00'
date: '2026-11-15T12:20:43-08:00'
authors:
  - bendu
label: limiting-filtering-results-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - limiting
  - filtering
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

In the data step you can use the hidden variable `_n_` to select records based on observation id.

In `proc sql`,
you can use the `outobs` option.
In other procedures,
you can use `firstobs` together with `obs` to limit records based observation id.
Again, this is ugly as you have to much to remember when using SAS.

```SAS
proc sql;
	select *
	from sasHelp.cars
	where monotonic() <= 10;
quit;
```

The `monotonic` function is similar to the `row_number` function in Oracle SQL.

```SAS
proc sql outobs=10;
	select
		*
	from 
		ia.ia_lgd_final_macro_mdl_v2
	;
quit;
```

For other steps, you can use firstObs and obs to limit the number of observations.

```SAS
proc print data=s (obs=5);
run;
```
