Status: published
Date: 2019-03-09 01:47:48
Author: Benjamin Du
Slug: spacevim-tips
Title: Spacevim Tips
Category: Software
Tags: software, SpaceVim, Vim, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
## Installation
```
curl -sLf https://spacevim.org/install.sh | bash
```

## Uninstallation
```
curl -sLf https://spacevim.org/install.sh | bash -s -- --uninstall
```

https://github.com/SpaceVim/SpaceVim/issues/84

https://github.com/SpaceVim/SpaceVim/issues/78

## Tricks & Traps

1. By default SpaceVim enables GUI colors.
    This makes SpaceVim extremely slow in terminals that does not support 24 bits true colors.
    To resolve the performance issue, 
    simplify disable GUI colors by setting `enable_guicolors = false`
    under `[options]` in your SpaceVim configure file `$HOME/.SpaceVim.d/init.toml`.


## Some Useful Key Bindings

<table style="width:100%">
  <tr>
    <th> Key Binding </th>
    <th> Description </th> 
  </tr>
  <tr>
    <td> SPC b f </td>
    <td> format the buffer </td>
  </tr>
  <tr>
    <td> SPC t 8 </td>
    <td> highlight characters that execeeds 80th column </td>
  </tr>
  <tr>
    <td> SPC t f </td>
    <td> highlight characters that execeeds the fill column </td>
  </tr>
  <tr>
    <td> SPC [1-9] </td>
    <td> jump to the windows with the specific number </td>
  </tr>
</table>

### [Buffers and Files](https://spacevim.org/documentation/#buffers-and-files)

<table style="width:100%">
  <tr>
    <th> Key Binding </th>
    <th> Description </th> 
  </tr>
  <tr>
    <td> :bn </td>
    <td> go to the next buffer </td>
  </tr>
  <tr>
    <td> SPC b n </td>
    <td> go to the next buffer </td>
  </tr>
  <tr>
    <td> :bp </td>
    <td> go to the previous buffer </td>
  </tr>
  <tr>
    <td> :e # </td>
    <td> go to the previous buffer </td>
  </tr>
  <tr>
    <td> SPC b p </td>
    <td> go to the previous buffer </td>
  </tr>
  <tr>
    <td> SPC t f </td>
    <td> highlight characters that execeeds the fill column </td>
  </tr>
  <tr>
    <td> SPC [1-9] </td>
    <td> jump to the windows with the specific number </td>
  </tr>
</table>

## References

https://spacevim.org/documentation/
