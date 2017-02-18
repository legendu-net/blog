UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: File Name of Bash Script
Date: 2015-02-03 19:54:45
Slug: file-name-of-bash-script
Author: Ben Chuanlong Du
Category: Linux
Tags: $0, BASH_SOURCE, bash, Linux

This post discusses the behavior of `$0` and `BASH_SOURCE` in bash using examples.
I created 3 executable bash files `a.sh`, `b.sh` and `c.sh`.

Content of `a.sh`:

    echo $0
    echo $(readlink -f $0)
    echo ${BASH_SOURCE[0]}
    echo $(readlink -f ${BASH_SOURCE[0]})

`b.sh` is a symbolic of `a.sh`

Content of `c.sh`:

    source a.sh
    ./a.sh
    echo ${BASH_SOURCE[0]}

```bash
./a.sh # run a.sh
```

```
## ./a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
```


```bash
source a.sh # source in a.sh
```

```
## bash
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/bash
## a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
```


```bash
./b.sh # run b.sh
```

```
## ./b.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./b.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
```


```bash
source b.sh # source in b.sh
```

```
## bash
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/bash
## b.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
```


```bash
./c.sh # run c.sh
```

```
## ./c.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/c.sh
## a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./c.sh
```


```bash
source c.sh # source in c.sh
```

```
## bash
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/bash
## a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## ./a.sh
## /home/dclong/btsync/dclong/blog/en/knitr/13-09-13/a.sh
## c.sh
```

