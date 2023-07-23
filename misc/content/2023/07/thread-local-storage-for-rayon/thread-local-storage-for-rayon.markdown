Status: published
Date: 2023-07-05 09:24:27
Modified: 2023-07-22 22:29:15
Author: Benjamin Du
Slug: thread-local-storage-for-rayon
Title: Thread-Local Storage for Rayon
Category: Computer Science
Tags: Computer Science, programming, Rust, thread, thread-local, TLS, storage, multi-thread, concurrency

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There might be issue if the code relies on Drop of the struct.
For example,
if you create a BufWriter in thread-local storage,
last buffered output might not flush.
You have to 
1. (not recommended) manually flush 
2. (recommended) swap out the `BufWrite` from RefCell to allow it to be dropped.

Have to manually call bw.replace(None) so own the struct so that it can be dropped.
This is good practice anyway as you want to lease handle to files so soon as they are no longer used.

## rayon
1. Can  
    [ThreadPool.broadcast](https://docs.rs/rayon/latest/rayon/struct.ThreadPool.html#method.broadcast)
    be used?
    No good example of using it for thread-local storage ...

```
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

## crossbeam

```
use crossbeam::thread_local;

// Define a thread-local variable.
thread_local! {
    static MY_VARIABLE: u32 = 42;
}

fn main() {
    // Access the thread-local variable from multiple threads.
    crossbeam::scope(|scope| {
        scope.spawn(|_| {
            // Get the value of the thread-local variable.
            println!("Thread 1: {}", MY_VARIABLE.with(|&v| v));

            // Set a new value for the thread-local variable.
            MY_VARIABLE.with(|v| *v = 100);
        });

        scope.spawn(|_| {
            // Get the value of the thread-local variable.
            println!("Thread 2: {}", MY_VARIABLE.with(|&v| v));

            // Set a new value for the thread-local variable.
            MY_VARIABLE.with(|v| *v = 200);
        });
    })
    .unwrap();

    // Get the value of the thread-local variable in the main thread.
    println!("Main thread: {}", MY_VARIABLE.with(|&v| v));
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
