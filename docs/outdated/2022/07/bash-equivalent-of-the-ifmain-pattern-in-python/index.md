---
title: Bash Equivalent of the ifmain Pattern in Python
created: '2022-07-28T14:39:20-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: bash-equivalent-of-the-ifmain-pattern-in-python
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - shell
  - Bash
  - ifmain
  - Python
  - module
  - script
  - function
  - import
  - source
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Fish Shell](tips-on-the-fish-shell)
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

```bash
#!/usr/bin/env bash

function install_icon.usage() {
    cat << EOF
NAME
    /scripts/sys/install_icon.sh - Download and install icon to /usr/local/bin/.
SYNTAX
    /scripts/sys/install_icon.sh [-h]
EOF
}

function install_icon() {
    if [[ $1 == "-h" ]]; then
        install_icon.usage
        return 0
    fi
    if [[ $# == 1 && "$1" != "-h" || $# > 1 ]]; then
        install_icon.usage
        return 1
    fi
    local URL=https://github.com/legendu-net/icon/releases
    local VERSION=$(basename $(curl -sL -o /dev/null -w %{url_effective} $URL/latest))
    local ARCH="$(uname -m)"
    case "$ARCH" in
        x86_64 )
            ARCH=amd64
            ;;
        arm64 )
            ARCH=arm64
            ;;
        *)
            echo "The architecture $ARCH is not supported!"
            return 2
            ;;
    esac
    curl -sSL $URL/download/$VERSION/icon-$VERSION-$(uname)-${ARCH}.tar.gz -o /tmp/icon.tar.gz
    tar zxf /tmp/icon.tar.gz -C /usr/local/bin/
    chmod +x /usr/local/bin/icon
}

if [[ "${BASH_SOURCE[0]}" == "" || "${BASH_SOURCE[0]}" == "$0" ]]; then
    install_icon $@
fi
```
