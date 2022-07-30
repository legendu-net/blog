Status: published
Date: 2020-11-09 11:10:06
Modified: 2022-07-28 10:31:22
Author: Benjamin Du
Slug: the-right-way-to-export-PATH-in-shell
Title: The Right Way to Export Path in Shell
Category: Computer Science
Tags: Computer Science, Shell, Bash, PATH, bashrc, bash_profile

Some people suggest exporting `PATH` only in `.bash_profile` 
instead of in `.bashrc` (for Bash).
The helps but does not resolve the issue of possible duplicated paths in `$PATH`.
The right way is to check for existence of the path in the `$PATH` environment variable first,
and add it only when it does NOT already exist in `$PATH`.
Below is an example snippet of adding paths into the environment variable `$PATH`.

    :::bash
    # set $PATH
    _PATHS=(
        $(ls -d $HOME/*/bin 2> /dev/null)
        $(ls -d $HOME/.*/bin 2> /dev/null)
        $(ls -d $HOME/Library/Python/3.*/bin 2> /dev/null)
    )
    for ((_i=${#_PATHS[@]}-1; _i>=0; _i--)); do
        _PATH=${_PATHS[$_i]}
        if [[ -d $_PATH && ! "$PATH" =~ (^$_PATH:)|(:$_PATH:)|(:$_PATH$) ]]; then
            export PATH=$_PATH:$PATH
        fi
    done

The snippet has the advatage that it works well in both `.bashrc` and `.bash_profile`.
So, 
you can safely add such snippets into `.bashrc`
and keep your `.bash_profile` as simple as the following. 

    :::bash
    if [[ -f ~/.bashrc ]]; then
        . ~/.bashrc
    fi
