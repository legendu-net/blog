---
title: Query and Monitor OS Information using osquery
created: '2019-02-22T15:27:24-08:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: query-and-monitor-os-information-using-osquery
license: CC-BY-4.0
tags:
  - software
  - osquery
  - tips
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. List all tables.

   .\\osqueryi .tables

1. Check the schema of a table (e.g., "process").

   .\\osqueryi ".schema processes"

## Querying System Information

```
.\osqueryi.exe "select * from system_info"
```

## Querying Docker

Please refer to
[Manage Docker Images and Containers](manage-docker-images-and-containers)
for more details.

## Information About Network Cards

```
osqueryi 'select * from interface_details'
```

`friendly_name`, `description` and `manufacturer` information are not populated yet.

```
osqueryi 'select interface, friendly_name, description, manufacturer from interface_details'
```

## Find/Locate Files

There are currently some bugs ...

1. Find all files with the extension ".out" in the current directory and its subdirectory,
   and then make them executable.

   ```
    :::bash
    osqueryi "select * from file where directory = '$(pwd)' and filename like '%.json'"
    find . -type f -iname *.out -exec chmod +x '{}' \;
    # or you can use 
    find . -type f -iname *.out -print0 | xargs -0 chmod +x
   ```

1. Find files whose names contain "conflicted" and remove them.

   ```
    :::bash
    find . -iname '*conflicted*' -print0 | xargs -0 rm
   ```

## Size Related Finding

1. Find files with 0 size and delete them.

   ```
    :::bash
    find /path/to/files -size 0 -ok -exec rm {} \;
    # or you can use
    find /path/to/files -size 0 -ok | xargs rm 
   ```

1. Find empty directories.

   ```
    :::bash
    find / -type d -empty
   ```

1. Find files greater than 1G.

   ```
    :::bash
    find . -xdev -type f -size +1G
   ```

1. First find files and then pass them to other commands is a very useful trick.
   For example,
   you can use the following command to find all R scripts containing the word `paste`.

   ```
    :::bash
    find . -type f -iname '*.r' | grep --color=auto paste
   ```

## Time Related Finding

1. Find files created with in 60 minutes.

   ```
    :::bash
    find . -cmin 60
   ```

1. Find files more than 30 days ago

   ```
    :::bash
    find . -ctime +30
   ```

1. Find file less than 30 days ago.

   ```
    :::bash
    find . -ctime -30
   ```

1. Find files that are exactly 30 days ago.

   ```
    :::bash
    find . -ctime 30
   ```

1. Find all files modified on the June 7, 2007 in the current directory.

   ```
    :::bash
    find . -type f -newermt 2007-06-07 ! -newermt 2007-06-08
   ```

1. Find all files accessed on the Sep 29, 2008 in the current directory.

   ```
    :::bash
    find . -type f -newerat 2008-09-29 ! -newerat 2008-09-30
   ```

1. Find files which had their permission changed on the same day.

   ```
    :::bash
    find . -type f -newerct 2008-09-29 ! -newerct 2008-09-30
   ```

## File Type Related Finding

1. Find broken symbolic links.

   ```
    :::bash
    find . -xtype l
    # or
    find -L . -type l
   ```

1. Find executable files in current directory

   ```
    :::bash
    find .  -maxdepth 1 -type f -executable
   ```

## User Related Finding

10. Find files that belong to a user but writable by its group or other people.

    ```
    :::bash
    find /path/to/file -user user1 -perm /022
    ```

01. Check file type of all files under the current directory.

    ```
    :::bash
    find . -type f | xargs file
    ```

-perm mode: File's permission bits are exactly mode (octal or symbolic).
-perm -mode: All of the permission bits mode are set for the file.
-perm /mode: Any of the permission bits mode are set for the file.
a little bit trick about how to understand the last 2 permission criterias.
as suggested, think in terms of permission BITs (0/1)

The following command finds all files that readable or writable by the group or (readable or writable) by others.

```
:::bash
find /path/to/file -user user1 -perm /066
```

The following command find all files that readable and writable by the group and (readable and writable) by others.

```
:::bash
find /path/to/file -user user1 -perm -066
```

The following command find all files that readable or writable by the group and (readable or writable) by others.

```
:::bash
find /path/to/file -user user1 -perm /060 -perm /006
```

Find Python scripts in the current directory recursively
but ignore those under directories with the name `.ipynb_checkpoints`.

```
:::bash
find . -type f -iname '*.py' -not -path '*/.ipynb_checkpoints/*'
```

## References

- https://holdmybeersecurity.com/2020/02/11/creating-my-first-osquery-extension-to-generate-communityids-with-osquery-python-on-windows/

- [osquery-python](https://github.com/osquery/osquery-python)
