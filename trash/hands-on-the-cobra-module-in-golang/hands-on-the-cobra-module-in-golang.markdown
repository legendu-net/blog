Status: published
Date: 2022-06-26 11:20:34
Modified: 2022-06-26 11:23:22
Author: Benjamin Du
Slug: hands-on-the-cobra-module-in-golang
Title: Hands on the Cobra Module in Golang
Category: Computer Science
Tags: Computer Science, programming, cobra, go, Golang, command-line, terminal

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

    :::bash
    mkdir icon
    cd icon
    go mod init legendu.net/icon
    ls
    cat go.mod 
    go get -u github.com/spf13/cobra@latest
    go install github.com/spf13/cobra-cli@latest
     ~/go/bin/cobra-cli init
    go build


## References

https://www.thorsten-hans.com/lets-build-a-cli-in-go-with-cobra/
