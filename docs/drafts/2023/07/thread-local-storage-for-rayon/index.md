---
title: Thread-Local Storage for Rayon
created: 2023-07-05 09:24:27
date: '2026-11-24T22:05:30-08:00'
authors:
  - bendu
label: thread-local-storage-for-rayon
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - thread
  - thread-local
  - TLS
  - storage
  - multi-thread
  - concurrency
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Concerns with `std::thread_local!` in Rayon

1. **Drop timing and resource leaks (`BufWriter`, file handles, large buffers):**
   Rayon's global thread pool keeps worker threads alive for the entire lifetime of the process,
   so `std::thread_local!` values are **not** dropped when a parallel job finishes.
   For example, if you store a `BufWriter` in thread-local storage,
   the last buffered output might not be flushed before the program exits.
   You have to either:
   1. (not recommended) manually flush, or
   2. (recommended) swap out the `BufWriter` from `RefCell<Option<BufWriter<_>>>` (e.g., `bw.borrow_mut().take()` or `bw.replace(None)`) so that you take ownership of it and allow it to be dropped immediately.
      This is good practice anyway because you want to release handles to files as soon as they are no longer used, and free large scratch buffers rather than keeping them allocated on idle worker threads.

2. **Work-stealing and `RefCell` re-entrancy panics:**
   Rayon uses a work-stealing scheduler.
   If code currently holding a `RefCell::borrow_mut()` on a `thread_local!` variable calls back into Rayon
   (nested parallelism such as `rayon::join` or an inner `.par_iter()`),
   the same worker thread may steal another task that tries to `borrow_mut()` the same thread-local `RefCell`,
   causing a runtime `BorrowMutError` panic.

3. **No task affinity and cross-job state leakage:**
   Successive items or chunks are not guaranteed to execute on the same worker thread,
   and thread-local state persists across unrelated parallel jobs on the global pool
   unless you explicitly reset or drain it after each job.

4. **Custom `ThreadPool` vs. the global pool:**
   Unlike the global pool, dropping a custom `rayon::ThreadPool` signals its worker threads to shut down (without blocking to join them),
   so `std::thread_local!` destructors run asynchronously as those worker threads exit rather than synchronously when the `ThreadPool` value is dropped.
   Even then, draining or resetting TLS between jobs on a reused custom pool is still necessary.

## `rayon::broadcast` and `ThreadPool::broadcast`

Can [rayon::broadcast](https://docs.rs/rayon/latest/rayon/fn.broadcast.html)
(or [ThreadPool::broadcast](https://docs.rs/rayon/latest/rayon/struct.ThreadPool.html#method.broadcast))
be used with thread-local storage, and can it return a `Vec<RefCell<T>>` to circumvent Rust's borrow checker?

- **Why returning `Vec<RefCell<T>>` does not circumvent the borrow checker:**
  `rayon::broadcast` executes a closure once on each worker thread in the pool and collects the return values into a `Vec<R>` **after** all threads complete (`R: Send`).
  Although `RefCell<T>` is `Send` (when `T: Send`), `RefCell<T>` is **`!Sync`**.
  Because it is `!Sync`, you **cannot** share `&Vec<RefCell<T>>` across threads in a subsequent `.par_iter()`—Rust's `Sync` bound prevents data races at compile time.
  Furthermore, `broadcast` is synchronous and returns only after every worker thread has finished running the closure;
  it is designed for **per-thread setup, teardown, or draining/collecting TLS results**, not for handing out shared mutable handles across threads.

- **Practical `rayon::broadcast` example (draining TLS accumulators and flushing `BufWriter`s):**
  You can use `rayon::broadcast` after a `par_iter()` to drain each worker thread's `thread_local!` state into a `Vec` on the caller thread and drop any open resources cleanly:

  ```rust
  use rayon::prelude::*;
  use std::cell::RefCell;

  thread_local! {
      static ACCUM: RefCell<Vec<usize>> = const { RefCell::new(Vec::new()) };
  }

  fn main() {
      (0..10_000usize).into_par_iter().for_each(|x| {
          ACCUM.with(|cell| cell.borrow_mut().push(x * x));
      });

      // Drain every worker thread's TLS buffer.
      let per_thread_chunks: Vec<Vec<usize>> = rayon::broadcast(|_| {
          ACCUM.with(|cell| std::mem::take(&mut *cell.borrow_mut()))
      });

      let total_items: usize = per_thread_chunks.iter().map(|c| c.len()).sum();
      println!("Collected {total_items} items across {} worker threads", per_thread_chunks.len());
  }
  ```

  Similarly, for a `thread_local!` `RefCell<Option<BufWriter<File>>>`, calling `rayon::broadcast(|_| TLS_WRITER.with(|w| w.borrow_mut().take()))` drops every worker's `BufWriter` (flushing buffered bytes and closing the file handle) before the program proceeds.

## Idiomatic Alternatives to `std::thread_local!` with Rayon

1. **`map_init`, `for_each_init`, and `fold` + `reduce`:**
   Rayon's built-in combinators create per-job state lazily, pass it as `&mut`, and drop it automatically when the parallel iterator finishes—avoiding `RefCell`, re-entrancy panics, and leaked TLS state.
   Note that `map_init` / `for_each_init` runs its `init` closure once per Rayon split/job rather than strictly once per worker thread; see [](#parallel-rngs-with-rayon-in-rust) for details.

   ```rust
   use rayon::prelude::*;

   let sum: usize = (0..10_000usize)
       .into_par_iter()
       .fold(Vec::new, |mut buf, x| {
           buf.push(x);
           buf
       })
       .map(|buf| buf.into_iter().sum::<usize>())
       .sum();
   ```

2. **The `thread_local` crate (`thread_local::ThreadLocal<T>`):**
   Unlike `std::thread_local!`, `thread_local::ThreadLocal<T>` ties the lifetime of all per-thread values to the `ThreadLocal` object itself rather than to OS thread exit.
   When the `ThreadLocal` instance is dropped (or consumed via `into_iter()`), every thread's value is dropped or collected cleanly—no `rayon::broadcast` teardown required.

## Older `thread_local!` Example in Rayon

```rust
let zip_archive = zip::ZipArchive::new(std::fs::File::open("AllPublicXML.zip")?)?;
let results = (0..zip_archive.len())
    .into_par_iter()
    .map(|i| {
        thread_local!(static ZIP_ARCHIVE: RefCell<Result<zip::ZipArchive<std::fs::File>>> = RefCell::new(std::fs::File::open("AllPublicXML.zip").map_err(failure::Error::from).and_then(|f|zip::ZipArchive::new(f).map_err(|e|e.into()))));
        thread_local!(static CONTENTS: RefCell<String> = RefCell::new(String::new()));
        CONTENTS.with(|contents| {
            let name = ZIP_ARCHIVE.with(|zip_archive| {
                Ok(match &mut *zip_archive.borrow_mut() {
                    &mut Ok(ref mut zip_archive) => {
                        let mut f = zip_archive.by_index(i)?;
                        let name_string = std::path::Path::new(f.name())
                            .file_stem()
                            .unwrap()
                            .to_str()
                            .unwrap()
                            .to_owned();
                        debug!("Processing {}...", name_string);
                        contents.borrow_mut().clear();
                        f.read_to_string(&mut *contents.borrow_mut())?;
                        name_string
                    }
                    &mut Err(ref e) => return Err(format_err!("{:?}", e)),
                })
            })?;
            Ok((
                name,
                phrases
                    .iter()
                    .filter_map(|phrase| {
                        let capture_names = phrase.capture_names();
                        phrase.captures(&*contents.borrow()).map(|captures| {
                            capture_names
                                .filter_map(|name_opt| {
                                    name_opt.and_then(|name| {
                                        captures.name(name).map(|value| {
                                            (name.to_owned(), value.as_str().to_owned())
                                        })
                                    })
                                })
                                .collect::<Vec<(String, String)>>()
                        })
                    })
                    .flat_map(|x| x)
                    .collect::<Vec<(String, String)>>(),
            ))
        })
    })
    .filter_map(|e| match e {
        Ok((_, ref data)) if data.is_empty() => None,
        Ok((name, data)) => Some(Ok((name, data))),
        Err(e) => Some(Err(e)),
    })
    .collect::<Result<HashMap<String, Vec<(String, String)>>>>()?;
```

## `std::thread_local!` with `crossbeam::scope`

The `crossbeam` crate does not provide a `crossbeam::thread_local` macro—it uses `std::thread_local!` with interior mutability (such as `Cell` or `RefCell`) when threads need to mutate their thread-local value (and since Rust 1.63, `std::thread::scope` is available in the standard library for most scoped-thread use cases):

```rust
use std::cell::Cell;

// Define a thread-local variable with interior mutability.
std::thread_local! {
    static MY_VARIABLE: Cell<u32> = const { Cell::new(42) };
}

fn main() {
    crossbeam::scope(|scope| {
        scope.spawn(|_| {
            println!("Thread 1: {}", MY_VARIABLE.with(|v| v.get()));
            MY_VARIABLE.with(|v| v.set(100));
        });

        scope.spawn(|_| {
            println!("Thread 2: {}", MY_VARIABLE.with(|v| v.get()));
            MY_VARIABLE.with(|v| v.set(200));
        });
    })
    .unwrap();

    println!("Main thread: {}", MY_VARIABLE.with(|v| v.get()));
}
```

[Thread lifetime for TLS](https://internals.rust-lang.org/t/thread-lifetime-for-tls/13550/)

## References

- [Example for thread-local variables](https://github.com/rayon-rs/rayon/issues/493)

- [Stack-based thread-local storage](https://github.com/rayon-rs/rayon/issues/941)

- [Strange memory leak (probably) when using rayon::ThreadPool](https://github.com/crossbeam-rs/crossbeam/issues/285)

- [Best practices for using combinators?](https://www.reddit.com/r/rust/comments/7kk49h/best_practices_for_using_combinators/)

- [Per-thread storage patterns & custom reductions](https://users.rust-lang.org/t/per-thread-storage-patterns-custom-reductions/76441)

- [Feature request: easy thread-local resources](https://github.com/rayon-rs/rayon/issues/720)
