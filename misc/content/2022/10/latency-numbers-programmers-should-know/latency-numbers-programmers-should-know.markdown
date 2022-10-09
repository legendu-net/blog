Status: published
Date: 2022-10-08 16:59:59
Modified: 2022-10-08 16:59:59
Author: Benjamin Du
Slug: latency-numbers-programmers-should-know
Title: Latency Numbers Programmers Should Know
Category: Computer Science
Tags: Computer Science, programming, latency, number, time, system design

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Latency</th>
    <th class="tg-0pky">Operations</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">&lt;=1ns</td>
    <td class="tg-0pky">CPU registers; CPU clock cycle; L1 cache</td>
  </tr>
  <tr>
    <td class="tg-0pky">1 - 10ns</td>
    <td class="tg-0pky">L2 cache; branch mispredict</td>
  </tr>
  <tr>
    <td class="tg-0pky">10 - 100ns</td>
    <td class="tg-0pky">L3 cache; mutex lock/unlock; main memory referencing; </td>
  </tr>
  <tr>
    <td class="tg-0pky">100 - 1000ns</td>
    <td class="tg-0pky">trapping of system call; md5 hash of an u64;</td>
  </tr>
  <tr>
    <td class="tg-0pky">1 - 10us</td>
    <td class="tg-0pky">
        process context switching; <br>
        compress 1kb with zippy; <br> 
        memory copy of 64kb 
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">10-100us</td>
    <td class="tg-0pky">
        network proxy / http request; <br>
        read 1M from memory; <br>
        SSD latency / read a 8k-page; 
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">100-1000us</td>
    <td class="tg-0pky">
        SSD write latency / write a page; <br>
        intra-zone networking round trip; <br>
        redis get operation / memcache (measured by client including network round trip) 
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">1-10ms</td>
    <td class="tg-0pky">inter-zone networking latency; hard drive latency; </td>
  </tr>
  <tr>
    <td class="tg-0pky">10-100ms</td>
    <td class="tg-0pky">
        network round trip between US coasts; <br>
        network round trip between US east coast to Europe; <br>
        read 1GB from memory
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">100-1000ms</td>
    <td class="tg-0pky">
        bcypt a password; <br> 
        TLS handshake (250-500ms); <br>
        network round trip from US west coast to Singapore; <br>
        read 1G from SSD
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">&gt;=1s</td>
    <td class="tg-0pky">transfer 1G over the network in the same region (10S)</td>
  </tr>
</tbody>
</table>

## References

- [Latency Numbers Programmer Should Know - 2020's](https://www.youtube.com/watch?v=FqR5vESuKe0)

- [Visualizing Latency Numbers Every Programmer Should Know](https://blog.nahurst.com/visualizing-latency-numbers-every-programmer)

- [Latency Numbers Every Programmer Should Know - 2012](https://gist.github.com/jboner/2841832)
