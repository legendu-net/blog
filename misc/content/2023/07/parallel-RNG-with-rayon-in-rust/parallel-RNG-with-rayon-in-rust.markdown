Status: published
Date: 2023-07-05 08:42:27
Modified: 2023-07-06 22:32:57
Author: Benjamin Du
Slug: parallel-RNGs-with-rayon-in-rust
Title: Parallel RNGs With Rayon in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, parallel, concurrency, thread, multi-thread, RNG, PRNG, random number generator

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[The Rust Rand Book - Parallel RNGs](https://rust-random.github.io/book/guide-parallel.html)
has a very good summary aboutparallel RNGs.
It also gives code examples using the rayon library.
However,
a few things to notice.

1. `rand::thread_rng` is often used in code examples of parallel RNGs
    as it uses thread-local storage and seeded automatically (lazily and uniquely) on each thread where it is used. 
    However,
    [rand::ThreadRng](https://docs.rs/rand/latest/rand/rngs/struct.ThreadRng.html)
    uses the same PRNG as 
    [StdRng](https://docs.rs/rand/latest/rand/rngs/struct.StdRng.html)
    (currently, ChaCha block cipher with 12 rounds 
    and might change if new evidence of cipher security and performance becomes available
    )
    for security and performance and is automatically seeded from OsRng.


[map_init](https://docs.rs/rayon/latest/rayon/iter/trait.ParallelIterator.html#method.map_init)

Note that the init closure is called once for each rayon job – a worker thread will typically execute many jobs. You can easily check this by incrementing an AtomicU64 in the init closure and printing it afterwards.

Try using 
[with_min_len](https://docs.rs/rayon/latest/rayon/iter/trait.IndexedParallelIterator.html#method.with_min_len)
to set the minimum number of items processed per job, play with the parameter a little, and see whether it's faster.

```
use rand::Rng;
use rayon::prelude::*;

let a: Vec<_> = (1i32..1_000_000)
    .into_par_iter()
    .map_init(
        || rand::thread_rng(),  // get the thread-local RNG
        |rng, x| if rng.gen() { // randomly negate items
            -x
        } else {
            x
        },
    ).collect();
```

## Customized RNGs with Thread-local Storage

Please refer to
[Thread-Local Storage for Rayon]( https://www.legendu.net/misc/blog/thread-local-storage-for-rayon ) 
for detailed discussions.

## References

[The Rust Rand Book - Parallel RNGs](https://rust-random.github.io/book/guide-parallel.html)

- [What is the best practice for initializing variables for use in parallelized rayon iterators?](https://www.reddit.com/r/rust/comments/ya5m3r/what_is_the_best_practice_for_initializing/)

