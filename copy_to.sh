#!/usr/bin/env bash

function copy_to.usage() {
    cat << EOF
Copy compiled HTML to a directory for HTTP serving. 
Syntax: copy_to dir
EOF
}

function copy_to() {
    if [[ "$1" == "-h" ]]; then
        copy_to.usage
        return 0
    fi
    cp -ir home/output/* $1
    cp -ir en/output $1/en
    cp -ir cn/output $1/cn
    cp -ir misc/output $1/misc
}

if [[ "$0" == ${BASH_SOURCE[0]} ]]; then
    copy_to $@
fi
