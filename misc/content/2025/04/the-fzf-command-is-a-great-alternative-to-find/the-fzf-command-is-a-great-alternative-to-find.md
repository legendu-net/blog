Status: published
Date: 2025-04-29 23:37:05
Modified: 2025-04-30 14:58:55
Author: Benjamin Du
Slug: the-fzf-command-is-a-great-alternative-to-find
Title: The fzf Command Is a Great Alternative to find
Category: Computer Science
Tags: Computer Science, programming, fzf, find, fuzzy, bat, preview

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


```
fzf --preview 'bat --color=always {}'
```

```
# ripgrep->fzf->vim [QUERY]
rfv() (
  RELOAD='reload:rg --column --color=always --smart-case {q} || :'
  OPENER='if [[ $FZF_SELECT_COUNT -eq 0 ]]; then
            vim {1} +{2}     # No selection. Open the current line in Vim.
          else
            vim +cw -q {+f}  # Build quickfix list for the selected items.
          fi'
  fzf --disabled --ansi --multi \
      --bind "start:$RELOAD" --bind "change:$RELOAD" \
      --bind "enter:become:$OPENER" \
      --bind "ctrl-o:execute:$OPENER" \
      --bind 'alt-a:select-all,alt-d:deselect-all,ctrl-/:toggle-preview' \
      --delimiter : \
      --preview 'bat --style=full --color=always --highlight-line {2} {1}' \
      --preview-window '~4,+{2}+4/3,<80(up)' \
      --query "$*"
)
```

## References

- [fzf @ GitHub](https://github.com/junegunn/fzf)

- [FZF Vim integration](https://github.com/junegunn/fzf/blob/master/README-VIM.md)

- [fzf Explained by the Author](https://junegunn.github.io/fzf/)

- [A Practical Guide to fzf: Building a File Explorer](https://thevaluable.dev/practical-guide-fzf-example/)

- [A Practical Guide to fzf: Shell Integration](https://thevaluable.dev/fzf-shell-integration/)

- [A Practical Guide to fzf: Vim Integration](https://thevaluable.dev/fzf-vim-integration/)

- [A Practical Guide to fzf: Building a Git Explorer](https://thevaluable.dev/fzf-git-integration/)

- [Advanced fzf examples](https://sourcegraph.com/github.com/junegunn/fzf/-/blob/ADVANCED.md)

- [4 Useful fzf Tricks for Your Terminal](https://pragmaticpineapple.com/four-useful-fzf-tricks-for-your-terminal/)
