Status: published
Date: 2020-09-02 09:22:34
Author: Benjamin Du
Slug: shell-equivalent-in-different-operating-systems
Title: Shell Equivalent in Different Operating Systems
Category: Computer Science
Tags: Computer Science, OS, Linux, macOS, Windows, Shell, PowerShell
Modified: 2021-09-04 10:31:04
PowerShell examples are used for Windows in the table below.

<div style="overflow-x:auto;">
<style>
    tr:nth-child(even) {background-color: #f2f2f2}
</style>
<table style="width:100%">
  <tr>
    <th> </th>
    <th> OS </th>
    <th> Command </th>
  </tr>

  <tr>
    <td rowspan="2"> Set PATH </td>
    <td> Linux/Unix </td>
    <td> <code> 
    export PATH=/new/path:$PATH
    </code> </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> <code> 
    $env:Path += ";.\swigwin-4.0.1";
    </code> </td>
  </tr>

  <tr>
    <td rowspan="3"> Get location <br> of a command </td>
    <td> Linux/Unix </td>
    <td> <code> 
    which command_name
    </code> </td>
  </tr>
  <tr>
    <td> Windows CMD </td>
    <td> <code> 
    where command_name
    </code> </td>
  </tr>
  <tr>
    <td> Windows PowerShell </td>
    <td> <code> 
    Get-command command_name
    </code> </td>
  </tr>

  <tr>
    <td rowspan="3"> Add user <br> to a group </td>
    <td> Linux </td>
    <td> <code> 
    sudo gpasswd -a user_name group_name
    </code> </td>
  </tr>
  <tr>
    <td> macOS </td>
    <td> <code> 
    sudo dseditgroup -o edit -a $username_to_add -t user admin
    </code> </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> <code> 
    NA
    </code> </td>
  </tr>

  <tr>
    <td rowspan="2"> Compress/Decompress Archives </td>
    <td> Linux/Unix </td>
    <td> <code> 
    <a href="http://www.legendu.net/en/blog/compress-and-decompress-in-linux/">
    Compress and Decompressing Archives in Linux
    </a>
    </code> </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> <code> 
    Expand-Archive .\swigwin-4.0.1.zip .;
    </code> </td>
  </tr>

  <tr>
    <td rowspan="3"> Download a file </td>
    <td rowspan="2"> Linux/Unix </td>
    <td> <code> 
    curl -sSL http://file.example.com -o output
    </code> </td>
  </tr>
  <tr>
    <td> <code> 
    wget http://file.example.com -O output
    </code> </td>
  </tr>
  <tr>
    <td> Windows </td>
    <td> <code> 
    (New-Object System.Net.WebClient).DownloadFile("http://prdownloads.sourceforge.net/swig/swigwin-4.0.1.zip","swigwin-4.0.1.zip");
    </code> </td>
  </tr>

    
</table>
</div>