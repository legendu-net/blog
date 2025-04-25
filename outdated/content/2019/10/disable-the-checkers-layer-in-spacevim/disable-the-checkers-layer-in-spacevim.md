Status: published
Date: 2019-10-20 21:35:44
Author: Benjamin Du
Slug: disable-the-checkers-layer-in-spacevim
Title: Disable the Checkers Layer in SpaceVim
Category: Software
Tags: Software, SpaceVim, Vim, checkers, layer, LSP, language server protocol
Modified: 2025-04-25 03:42:52

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

The SpaceVim project has been abandoned.
Check AstroVim instead.

You can use the following command in SpaceVim to disable the `checkers` layer temporarily.

    :::vim
    let g:spacevim_lint_on_save = 0

If you want to disable the `checkers` layer permanently,
add the following lines into your `init.toml` file.

    [[layers]]
    name = "checkers"
    enable = false

It is suggested that you disable the `checkers` layer permanently 
and use language server protocol (LSP) plugins instead
as LSP plugins are better alternatives to the `checkers` layer.

## References

- https://spacevim.org/layers/checkers/

- https://github.com/SpaceVim/SpaceVim/issues/399

- https://github.com/SpaceVim/SpaceVim/issues/3163
