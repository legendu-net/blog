#!/bin/bash

# clear temporary files in blog
function rmopt(){
    echo "Removing contents in \"$1/output/\" ..."
    rm -rf $1/output/*
}

rmopt home
rmopt en
rmopt cn
rmopt misc
