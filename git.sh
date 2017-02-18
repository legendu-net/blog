#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "git.sh needs exactly 1 argument."
    exit 1
fi
if [ "$1" == "home" ]; then
    mkdir -p "$1/output"
    cd "$1/output"
    cp pages/index.html .
    if [[ ! -d ".git" ]]; then
        git init 
        git add --all .
        git commit -a -m ... 
        git remote add origin git@github.com:dclong/dclong.github.io.git
        git push origin master --force
    fi
    git add --all . 
    git commit -a -m ... 
    git push origin master --force
elif [ "$1" == "en" ] || [ "$1" == "cn" ] || [ "$1" == "misc" ]; then
    mkdir -p "$1/output"
    cd "$1/output"
    if [[ ! -d ".git" ]]; then
        git init 
        git add --all .  
        git commit -a -m ... 
        git branch gh-pages
        git checkout gh-pages
        git branch -d master
        git remote add origin git@github.com:dclong/$1.git
        git push origin gh-pages --force
    else
        if [ "$(git branch)" == "* master" ]; then
            git branch gh-pages
            git checkout gh-pages
            git branch -d master
        fi
        git add --all .  
        git commit -a -m ... 
        git push origin gh-pages --force
    fi
else
    echo "\"$1\" is not a valid blog directory."
fi
