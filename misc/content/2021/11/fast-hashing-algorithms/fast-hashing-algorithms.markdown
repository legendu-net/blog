Status: published
Date: 2021-11-21 00:36:07
Modified: 2021-11-21 00:36:07
Author: Benjamin Du
Slug: fast-hashing-algorithms
Title: Fast Hashing Algorithms
Category: Computer Science
Tags: Computer Science, programming, hash, hashing, HashMap, modulus, modulo, multiplicative, FNV, Swiss Table

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. For simple integer hashing functions, 
    integer modulo is a very BAD (in terms of speed) hashing function
    while the multiplicative hashing is a much better alternative.

## References 

- [What integer hash function are good that accepts an integer hash key?](https://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key)

- [Signed Division and Remainder by Non-Powers of 2](https://doc.lagout.org/security/Hackers%20Delight.pdf)

- [A fast alternative to the modulo reduction](https://lemire.me/blog/2016/06/27/a-fast-alternative-to-the-modulo-reduction/)

- [Fibonacci Hashing: The Optimization that the World Forgot (or: a Better Alternative to Integer Modulo)](https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/)

- [FNV Hash](http://www.isthe.com/chongo/tech/comp/fnv/index.html)

- [Swiss Tables and absl::Hash](https://abseil.io/blog/20180927-swisstables)

- [OPTIMIZING HASHMAPS EVEN MORE](https://blog.yoshuawuyts.com/optimizing-hashmaps-even-more/)

- [HashMap in Rust](http://www.legendu.net/misc/blog/rust-hashmap/)
