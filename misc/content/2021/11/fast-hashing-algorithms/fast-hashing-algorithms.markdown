Status: published
Date: 2021-11-21 00:36:07
Modified: 2022-07-23 21:30:03
Author: Benjamin Du
Slug: fast-hashing-algorithms
Title: Fast Hashing Algorithms
Category: Computer Science
Tags: Computer Science, programming, hash, hashing, HashMap, modulus, modulo, multiplicative, FNV, Swiss Table

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. For simple integer hashing functions, 
    integer modulo is a very BAD (in terms of speed) hashing function
    while the multiplicative hashing is a much better alternative.

2. By default, 
  Rust hash tables use Siphash 1-3, a hash function that is high quality but fairly slow. 
  In contrast, 
  the Rust compiler uses as hash function called FxHasher, which is surprisingly simple yet effective.

## References 

- [A brutally effective hash function in Rust](https://nnethercote.github.io/2021/12/08/a-brutally-effective-hash-function-in-rust.html)

- [What integer hash function are good that accepts an integer hash key?](https://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key)

- [Signed Division and Remainder by Non-Powers of 2](https://doc.lagout.org/security/Hackers%20Delight.pdf)

- [A fast alternative to the modulo reduction](https://lemire.me/blog/2016/06/27/a-fast-alternative-to-the-modulo-reduction/)

- [Fibonacci Hashing: The Optimization that the World Forgot (or: a Better Alternative to Integer Modulo)](https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/)

- [Fastest Lookup Time Map for Short Keys](https://users.rust-lang.org/t/fastest-lookup-time-map-for-short-keys/2028)

- [FNV Hash](http://www.isthe.com/chongo/tech/comp/fnv/index.html)

- [Swiss Tables and absl::Hash](https://abseil.io/blog/20180927-swisstables)

- [OPTIMIZING HASHMAPS EVEN MORE](https://blog.yoshuawuyts.com/optimizing-hashmaps-even-more/)

- [HashMap in Rust](http://www.legendu.net/misc/blog/rust-hashmap/)

