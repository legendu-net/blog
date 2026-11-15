---
title: Generating YYYYMM Formatted Dates Using Python
created: '2015-05-17T17:05:55-07:00'
date: '2026-11-15T09:20:32-08:00'
authors:
  - bendu
label: generating-yyyymm-formatted-dates-using-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - credit risk
  - risk capital
  - stress testing
  - YYYYMM
  - YYYYQQ
---

```Python

import monthdelta as md
import datetime as dt
import math as math

def quarter(month):
    return int(math.ceil(month/3.0))
#end def

d0 = md.date.today()
dates = [d0 + md.monthdelta(i) for i in range(1, 20)]
yyyymms = [d.year*100 + d.month for d in dates]
yymms = [d.year%100 * 100 + d.month for d in dates]
print(", ".join(map(str, yyyymms)))
print(", ".join(map(str, yymms)))
```

The between ... and clause is also convenient to work with YYYYMM numbers
I saw people use

```SAS
where m in &months.;
```

to check ..
while a much more convenient way is to use

```SAS
where m between 200201 and 201212;
```

if you are sure `m` contains only YYYYMM formatted numbers.
