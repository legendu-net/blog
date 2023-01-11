Status: published
Date: 2023-01-08 18:58:25
Modified: 2023-01-10 21:12:32
Author: Benjamin Du
Slug: tips-on-valgrind
Title: Tips on Valgrind
Category: Computer Science
Tags: Computer Science, programming, Valgrind, profiling, memory, cpu, memcheck, callgrind, dhat

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

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

