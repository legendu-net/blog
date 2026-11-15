---
title: Operators in Different Programming Languages
created: '2012-06-14T16:08:55-07:00'
date: '2026-11-15T12:20:32-08:00'
authors:
  - bendu
label: operators-in-different-programming-languages
license: CC-BY-4.0
tags:
  - Python
  - Julia
  - programming
  - C/C++
  - Java
  - operator
  - Bash
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

<table border="1" align="center">
    <tr>
        <th> </th>
        <th>Python</th>
        <th>Bash</th>
        <th>C/C++</th>
        <th>Java</th>
        <th>Julia</th>
    </tr>   

```
<tr>
    <td> and </td>
    <td> and </td>
    <td> -a </td>
    <td> && </td>
    <td> && </td>
    <td> && </td>
</tr>

<tr>
    <td> or </td>
    <td> or </td>
    <td> -o </td>
    <td> || </td>
    <td> || </td>
    <td> || </td>
</tr>

<tr>
    <td> not </td>
    <td> not </td>
    <td> ! </td>
    <td> ! </td>
    <td> ! </td>
    <td> ! </td>
</tr>

<tr>
    <td> bit and </td>
    <td> & </td>
    <td> & </td>
    <td> & </td>
    <td> & </td>
    <td> & </td>
</tr>

<tr>
    <td> bit or </td>
    <td> | </td>
    <td> | </td>
    <td> | </td>
    <td> | </td>
    <td> | </td>
</tr>

<tr>
    <td> bit not </td>
    <td> ~ </td>
    <td> ~ </td>
    <td> ~ </td>
    <td> ~ </td>
    <td> ~ </td>
</tr>

<tr>
    <td> bit xor </td>
    <td> ^ </td>
    <td> ^ </td>
    <td> ^ </td>
    <td> ^ </td>
    <td> ^ </td>
</tr>

<tr>
    <td> vector and </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
</tr>

<tr>
    <td> vector or </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
</tr>

<tr>
    <td> vector not </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td> </td>
</tr>

<tr>
    <td> equals </td>
    <td> == </td>
    <td> -eq </td>
    <td> == </td>
    <td> == </td>
    <td> == </td>
</tr>

<tr>
    <td> not equal </td>
    <td> != </td>
    <td> -ne </td>
    <td> != </td>
    <td> != </td>
    <td> != </td>
</tr>

<tr>
    <td> greater than </td>
    <td> > </td>
    <td> -gt </td>
    <td> > </td>
    <td> > </td>
    <td> > </td>
</tr>

<tr>
    <td> less than </td>
    <td> < </td>
    <td> -lt </td>
    <td> < </td>
    <td> < </td>
    <td> < </td>
</tr>

<tr>
    <td> greater than or equal to </td>
    <td> >= </td>
    <td> -ge </td>
    <td> >= </td>
    <td> >= </td>
    <td> >= </td>
</tr>

<tr>
    <td> less than or equal to </td>
    <td> <= </td>
    <td> -le </td>
    <td> <= </td>
    <td> <= </td>
    <td> <= </td>
</tr>   

<tr>
    <td> next loop </td>
    <td> continue </td>
    <td> continue </td>
    <td> continue </td>
    <td> continue </td>
    <td> continue </td>
</tr>

<tr> 
    <td> stop loop </td>
    <td> break </td>
    <td> break </td>
    <td> break </td>
    <td> break </td>
    <td> break </td>
</tr>
<tr>
    <td> print </td>
    <td>  </td>
    <td> echo </td>
    <td> printf/std::cout </td>
    <td> System.out.print, System.out.println </td>
    <td> print, println </td>
</tr>
```

</table>

Python supports `1 <= x < 3`
which is equivalent to `x >= 1 and x <3`.
