---
title: Parallel Computing in Fish
created: '2026-08-04T08:30:22.663046-07:00'
date: '2026-08-04T08:30:22.663054-07:00'
authors:
  - bendu
label: parallel-computing-in-fish
license: CC-BY-4.0
tags:
  - fish
  - shell
  - parallel
  - computing
  - xargs
  - background
  - process
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Fork Background Processes

The simplest way is to do parallel computing in fish 
is to fork a background process using `&` (in a for loop).
```
for val in $some_var
    run_some_cmd & 
end 
```

1. You can use the `wait` function to wait for a specific or all background processes to finish.

2. Forking background processes in a for loop might spawn too many subprocesses. 
  Fish has a built-in command `jobs` for managing background jobs.
  You can leverage it to control the number of background jobs if needed.

## Using xargs / parallel

Taking `xargs` as an example,
```
command_producing_lines | xargs -P 10 -I {} fish --no-config -c "..."
# or
command_producing_lines | xargs -P 10 -I {} fish -c "..."
```
but it does has a drawback.
A fish function might not be discoverable by `fish --no-config -c` or `fish -c`.
For example,
if the function is only available in interactive mode.
You can use `fish -ic` to run the function but at the cost of performance.
If performance is critical 
and the fish function is defined in a script which is sourced in by `config.fish` 
with an `if status is-interactive` guard,
you can hack it by `fish -c source /path/to/script.fish && cmd_to_run`.

```{list-table} Fish Command Execution Comparison
:header-rows: 1
:widths: 25 20 20 35

* - Command
  - Reads `config.fish` & `conf.d`?
  - `status is-interactive`
  - Best Used For
* - **`fish --no-config -c`**
  - **No**
  - **False**
  - CI/CD pipelines, cron jobs, or scripts requiring maximum speed and absolute isolation.
* - **`fish -c`**
  - Yes
  - **False**
  - General scripts where you need your custom paths and environment variables.
* - **`fish -ic`**
  - Yes
  - **True**
  - Terminal emulator keybinds or wrappers where you need your aliases and UI elements.
```

### Comparison of xargs vs parallel 

The main purpose of xargs in Linux is to read streams of data from standard input (stdin) 
and convert them into command-line arguments for another command.
GNU parallel was built from the ground up specifically to run jobs concurrently. 
It behaves much like a for loop, but executes in parallel.

```{list-table} Feature Comparison
:header-rows: 1
:name: xargs-vs-parallel

* - Feature
  - `xargs -P`
  - GNU `parallel`
* - **Output Handling**
  - Interleaved (mixed up)
  - Buffered (cleanly grouped per job)
* - **Default Cores**
  - Must specify `-P` manually
  - Auto-detects and uses all cores
* - **Argument Placement**
  - End of command only (mostly)
  - Anywhere using `{}`
* - **String Manipulation**
  - Difficult (needs `sh -c` or `sed`)
  - Built-in (`{.}`, `{/}`, `{//}`)
* - **Progress Tracking**
  - None
  - Built-in (`--bar`, `--eta`)
* - **Remote Execution**
  - None
  - Built-in (`--sshlogin`)
* - **Job Resuming**
  - None
  - Built-in (`--joblog` and `--resume`)
```
