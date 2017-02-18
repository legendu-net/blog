#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "local.sh needs exactly 1 argument."
    exit 1
fi
if [ "$1" == "home" ]; then 
    cp "$1/output/pages/index.html" "$1/output/"
    if [ ! -d "local" ]; then
        mkdir "local"
    fi
    rm -rf "local/!(en|cn|misc)"
    cp -r "$1/output/*" "local/"
elif [ "$1" == "en" ] || [ "$1" == "cn" ] || [ "$1" == "misc" ]; then
    if [ ! -d "local/$1" ]; then
        mkdir -p "local/$1"
    fi
    rm -rf "local/$1/*" 
    cp -r "$1/output/*" "local/$1/"
else
    echo "\"$1\" is not a valid blog directory."
fi
