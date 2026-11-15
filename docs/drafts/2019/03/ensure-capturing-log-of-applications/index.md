---
title: Ensure Capturing Log of Applications
created: '2019-03-11T08:26:52-07:00'
date: '2026-11-15T09:22:20-08:00'
authors:
  - bendu
label: ensure-capturing-log-of-applications
license: CC-BY-4.0
tags:
  - programming
  - logging
  - log
  - redirect
  - redirection
  - exception
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Logging is critical for debugging applications.
For production applications,
it is best to send log information into a file instead of the standard output
so that the log information is persisted.
One command way to keep log into a file is to redirect standard output into a file.

```Bash
some_command arg1 arg2 > log_file
```

There is some issue with this approach.
If an exception throws in `some_command arg1 arg2`,
no log is redirected into the log file
as the redirection happens after `some_command` runs successfully.
One way to fix the issue is to let the underlying application log into files. directly
instead of relying on shell redirection.
However,
this is not always feasible.
Another even simple way is to wrap `some_command` into a `try ... catch ...` block
to ensure that `some_command` runs without throwing exceptions
so that the log redirection will always happen.

## References

https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels
