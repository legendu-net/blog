---
title: Television Is a Fast and Portable Fuzzy Finder
created: '2026-09-29T01:21:21.177516-07:00'
date: '2026-09-29T01:21:21.177525-07:00'
authors:
  - bendu
label: television-is-a-fast-and-portable-fuzzy-finder
license: CC-BY-4.0
tags:
  - programming
  - file
  - fuzzy
  - finder
  - television
  - tv
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Usage

ctrl+t to bring up the remote control to switch channels
ctrl+x to bring up commands to run
they are on the status bar

### Change Directory

```
function tv_cd
    # Assuming television has a channel for directories, replace 'directories' with the correct channel name if different
    set -l target (tv directories) 
    
    if test -n "$target"
        # If it's a file, get the parent directory
        if test -f "$target"
            cd (dirname "$target")
        else if test -d "$target"
            cd "$target"
        end
    end
end
```

## Channel

https://alexpasmantier.github.io/television/getting-started/first-channel/

https://alexpasmantier.github.io/television/user-guide/channels/

## fdfind 

ln -s $(which fdfind) ~/.local/bin/fd

