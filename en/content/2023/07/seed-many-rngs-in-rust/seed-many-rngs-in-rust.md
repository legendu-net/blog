Status: published
Date: 2023-07-05 22:39:36
Modified: 2023-07-06 22:33:26
Author: Benjamin Du
Slug: seed-many-rngs-in-rust
Title: Seed Many RNGs in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, RNG, random number generator, seed



There are different ways to seed many RNGs (for parallel RNGs).
Below summarizes 3 popular ways.
Seeding RNGs using 
`std::collections::hash_map::RandomState`
or `rand::thread_rng`
is preferred.

## Seed Using System Time

```
use std::time::{SystemTime, UNIX_EPOCH};
use rand::SmallRng;

fn main () {
    let seed = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_nanos()
        & ((1 << 65) - 1);
    let mut rng = SmallRng::seed_from_u64(seed);
}
```

## Seed Using `std::collections::hash_map::RandomState`

`std::collections::hash_map::RandomState` gets true (or close to true) random bytes using entropy
as the base random state 
which is cached using thread-local storage.
Subsequent instantiations increment the random state to ensure different states.
```
use std::collections::hash_map::RandomState;
use std::hash::{BuildHasher, Hasher};
use rand::SmallRng;

fn main() {
    let seed = RandomState::new().build_hasher().finish();
    let mut rng = Xoshiro256PlusPlus::seed_from_u64(seed);
}
```

## Seed Using a Master RNG

```
use rand::{SmallRng, thread_rng};

fn main() {
    let mut rng = SmallRng::from_rng(thread_rng()).unwrap();
}
```

## References

- [Seedablerng::from_entropy](https://docs.rs/rand/latest/rand/trait.SeedableRng.html#method.from_entropy)

- [Zero-dependency random number generation in Rust](https://blog.orhun.dev/zero-deps-random-in-rust/)
