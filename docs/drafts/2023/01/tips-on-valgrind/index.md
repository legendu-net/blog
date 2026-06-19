---
title: Tips on Valgrind
created: '2023-01-08T18:58:25-08:00'
date: '2026-06-18T20:09:23-07:00'
authors:
  - bendu
label: tips-on-valgrind
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Valgrind
  - profiling
  - memory
  - CPU
  - memcheck
  - callgrind
  - dhat
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu

```sh
sudo apt install valgrind
```

## Installation on Fedora

```sh
sudo dnf install valgrind
```

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Valgrind Tool</th>
    <th class="tg-0pky">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"> callgrind </td>
    <td class="tg-0pky"> CPU profiling. </td>
  </tr>
  <tr>
    <td class="tg-0pky">dhat</td>
    <td class="tg-0pky">Dynamic heap analysis. </td>
  </tr>
  <tr>
    <td class="tg-0pky">memcheck</td>
    <td class="tg-0pky">Check for memory errors (leak, invalid access, etc.).</td>
  </tr>
  <tr>
    <td class="tg-0pky">
        <a href="https://valgrind.org/docs/manual/ms-manual.html"> Massif </a>
    </td>
    <td class="tg-0pky"> A heap profiler. </td>
  </tr>
</tbody>
</table>
