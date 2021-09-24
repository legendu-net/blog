Status: published
Date: 2021-09-04 09:56:21
Modified: 2021-09-24 10:54:19
Author: Benjamin Du
Slug: terminal-multiplexers
Title: Terminal Multiplexers
Category: Computer Science
Tags: Computer Science, software, tools, Rust, Zellij, tmux, screen, terminal, SSH



![zellij](https://raw.githubusercontent.com/zellij-org/zellij/main/assets/demo.gif)

1. There are 2 mature popular terminal multiplexer apps: screen and tmux.
    Both of them are very useful if you want to work on multiple tasks over 1 SSH connection.
    Screen is relative simple to use while tmux is much more powerful and more complicated to use.

2. [Zellij](https://github.com/zellij-org/zellij)
    is a new terminal multiplexer implemented in Rust. 
    It is functionally very similar to tmux but with batteries included 
    and is easier to extend via its plugin system back by WASM.
    It is also more intuitive to use.
    Overall,
    I recommend 
    [Zellij](https://github.com/zellij-org/zellij)
    rather than screen or tmux.

## References

- [Good Terminal Apps](http://www.legendu.net/misc/blog/good-terminal-apps/)
