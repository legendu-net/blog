---
title: Program Termination in SAS
created: '2015-01-05T09:14:13-08:00'
date: '2026-11-15T12:20:42-08:00'
authors:
  - bendu
label: program-termination-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - termination
  - exit
  - quit
  - stop
  - error
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

To print an error message into the SAS log

```
%put ERROR: error_message;
```

To print a warning message into the SAS log

```
%put WARNING: warning_message;
```

To print a note message into the SAS log

```
%put NOTE: note_message;
```

To terminate an user-defined module in the IML procedure use `stop;`

exit;
quit;
