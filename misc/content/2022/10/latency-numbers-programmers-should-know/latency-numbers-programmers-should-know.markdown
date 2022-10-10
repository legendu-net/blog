Status: published
Date: 2022-10-08 16:59:59
Modified: 2022-10-09 17:57:17
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
    <td class="tg-0pky">
      <ul>
        <li>accessing CPU registers</li>
        <li>CPU clock cycle</li>
        <li>L1 cache</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">1-10ns</td>
    <td class="tg-0pky">
      <ul>
        <li>L2 cache</li>
        <li>branch mispredict</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">10-100ns</td>
    <td class="tg-0pky">
      <ul>
        <li>L3 cache</li>
        <li>mutex lock/unlock</li>
        <li>main memory referencing</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">100-1000ns</td>
    <td class="tg-0pky">
      <ul>
        <li>trapping of system call</li>
        <li>md5 hash of an u64</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">1-10us</td>
    <td class="tg-0pky">
      <ul>
        <li>process context switching</li>
        <li>compress 1k with zippy</li>
        <li>memory copy of 64k</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">10-100us</td>
    <td class="tg-0pky">
      <ul>
        <li>network proxy / http request</li>
        <li>read 1M from memory</li>
        <li>SSD latency (read a 8k page)</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">100-1000us</td>
    <td class="tg-0pky">
      <ul>
        <li>SSD write latency / write a page</li>
        <li>intra-zone networking round trip</li>
        <li>memcache/redis get operation <br>
          (measured by client including network round trip)</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">1-10ms</td>
    <td class="tg-0pky">
      <ul>
        <li>inter-zone networking latency</li>
        <li>hard drive latency</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">10-100ms</td>
    <td class="tg-0pky">
      <ul>
        <li>network round trip between US coasts</li>
        <li>network round trip between US east coast and Europe</li>
        <li>read 1G from memory</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">100-1000ms</td>
    <td class="tg-0pky">
      <ul>
        <li>bcypt a password</li>
        <li>TLS handshae (250-500ms)</li>
        <li>network round trip from US west coast to Singapore</li>
        <li>read 1G from SSD</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="tg-0pky">&gt;=1s</td>
    <td class="tg-0pky">
      <ul>
        <li>transfer 1G over a network in the same region</li>
      </ul>
    </td>
  </tr>
</tbody>
</table>

## References

- [Latency Numbers Programmer Should Know - 2020's](https://www.youtube.com/watch?v=FqR5vESuKe0)

- [Visualizing Latency Numbers Every Programmer Should Know](https://blog.nahurst.com/visualizing-latency-numbers-every-programmer)

- [Latency Numbers Every Programmer Should Know - 2012](https://gist.github.com/jboner/2841832)
