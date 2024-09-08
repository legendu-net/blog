Status: published
Date: 2023-07-05 08:42:27
Modified: 2023-07-24 15:45:49
Author: Benjamin Du
Slug: parallel-RNGs-with-rayon-in-rust
Title: Parallel RNGs With Rayon in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, parallel, concurrency, thread, multi-thread, RNG, PRNG, random number generator



[The Rust Rand Book - Parallel RNGs](https://rust-random.github.io/book/guide-parallel.html)
has a very good summary about parallel RNGs.
It also gives code examples using the rayon library.
However,
a few things to notice.

1. [rand::ThreadRng](https://docs.rs/rand/latest/rand/rngs/struct.ThreadRng.html)
    (obtained by calling [rand::thread_rng](https://docs.rs/rand/latest/rand/fn.thread_rng.html))
    is often used in code examples of parallel RNGs
    as it uses thread-local storage and is seeded automatically (lazily and uniquely) on each thread. 

        :::Rust
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

    While [rand::ThreadRng](https://docs.rs/rand/latest/rand/rngs/struct.ThreadRng.html)
    is convenient to use as parallel RNGs,
    it is based on
    [StdRng](https://docs.rs/rand/latest/rand/rngs/struct.StdRng.html)
    (currently, ChaCha block cipher with 12 rounds)
    which might be too slow for statistical simulations.
    If that's the case,
    you can use a faster RNG (e.g., SmallRng) with thread-local storage as parallel RNGs.
    Please refer to 
    [Customized RNGs with Thread-local Storage](https://www.legendu.net/misc/blog/parallel-RNGs-with-rayon-in-rust/#customized-rngs-with-thread-local-storage)
    for details.

2. [rayon::iter::ParallelIterator::map_init](https://docs.rs/rayon/latest/rayon/iter/trait.ParallelIterator.html#method.map_init)
    allows you do some initializing work before running each job.
    Note that the `init` closure passed to `map_init` is called once per rayon job
    NOT per rayon worker thead.
    A rayon worker thread typically executes many jobs. 
    If you need to ensure some intializing work per rayon worker thread
    (e.g., if you want to use the same RNG for jobs executed by the same worker thread),
    you have to leverage thread-local storage in the `init` closure.
    For more discussions,
    please refer to
    [Thread-Local Storage for Rayon]( https://www.legendu.net/misc/blog/thread-local-storage-for-rayon ) 
    .

3. [rayon::iter::ParallelIterator::with_min_len](https://docs.rs/rayon/latest/rayon/iter/trait.IndexedParallelIterator.html#method.with_min_len)
    can be used to set the minimum number of items processed per job.
    When necessary,
    its parameter can be tuned to improve performance.

## Customized RNGs with Thread-local Storage

Please refer to
[Thread-Local Storage for Rayon]( https://www.legendu.net/misc/blog/thread-local-storage-for-rayon ) 
for detailed discussions.

## References

- [The Rust Rand Book - Parallel RNGs](https://rust-random.github.io/book/guide-parallel.html)

- [What is the best practice for initializing variables for use in parallelized rayon iterators?](https://www.reddit.com/r/rust/comments/ya5m3r/what_is_the_best_practice_for_initializing/)

