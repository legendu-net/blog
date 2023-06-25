Status: published
Date: 2022-06-16 15:34:08
Modified: 2023-06-23 16:22:23
Author: Benjamin Du
Slug: unit-test-in-rust
Title: Unit Test in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, test, unit, testing, cargo

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://crates.io/crates/test-with

## Tips and Traps

1. [std::assert!](https://doc.rust-lang.org/std/macro.assert.html)
    and
    [std::assert_eq!](https://doc.rust-lang.org/std/macro.assert_eq.html)
    can be used to assert whether certain conditions are met.
    They are typically used for testing
    but they can also be used in regular code
    to assert certain conditions are met at runtime.

2. [debug_assert!](https://doc.rust-lang.org/std/macro.debug_assert.html)
    is similar to 
    [std::assert!](https://doc.rust-lang.org/std/macro.assert.html)
    but it only takes effect in the debugging version of the compiled binary.

3. [static_assertions](https://crates.io/crates/static_assertions)

4. All assert macros support an optional error message on failure.

## Examples

[matches!](https://doc.rust-lang.org/core/macro.matches.html)

    :::Rust
    assert_eq!(Rank::from_char('2').unwrap(), Rank::_2);
    let err = Rank::from_char('z').unwrap_err().downcast().unwrap();
    assert_eq!(err, RankError::NotARank('z')));
    assert!(matches!(Rank::from_char('Z'), Err(_))

Assert 2 arrays/vectors contain the same values.

    :::Rust
    let a = [3, 4, 5, 6];
    let v = vec![0, 1, 2, 3, 4, 5, 6];
    assert_eq!(&a[..], &v[v.len() - 4..]);

Assert 2 float numbers are the same.

    assert!((x - y).abs() < 1E-6)

Assert an Option value is None.

    assert!(an_option_value.is_none())

Assert an Option value is Some(v).

    assert_eq!(an_option_value.unwrap(), v)

## Setup and Teardown

[How to run setup code before any tests run in Rust?](https://stackoverflow.com/questions/58006033/how-to-run-setup-code-before-any-tests-run-in-rust)

There's nothing built-in that would do this but this should help (you will need to call initialize() in the beginning of every test):

    :::Rust
    use std::sync::Once;

    static INIT: Once = Once::new();

    pub fn initialize() {
        INIT.call_once(|| {
            // initialization code here
        });
    }

[Test setup and teardown in Rust without a framework.](https://medium.com/@ericdreichert/test-setup-and-teardown-in-rust-without-a-framework-ba32d97aa5ab)

    cargo test
    cargo test name_of_test_fun
    cargo test test_mod::inner_mod::name_of_test_fun

    cargo test --release 

Report the execution time of each test case.

    cargo test -- -Zunstable-options --report-time

If building the project with optimization is not too slow, 
it is suggested that your turn on optimization for the test profile 
in your `Cargo.toml` file.

    [profile.test]
    opt-level = 3

https://doc.rust-lang.org/cargo/commands/cargo-test.html

## Passing Command Line Arguments to Test Functions

There are a few approaches to pass arguments to unit test functions.

1. Disable the libtest harness.
    For more discussions,
    please refer to
    [Where do we get started with a custom test harness?](https://www.infinyon.com/blog/2021/04/rust-custom-test-harness/#where-do-we-get-started-with-a-custom-test-harness)
    .

2. Refactor your unit test functions to take parameters using other ways 
    instead of command-line arguments.
    For example,
    you make your unit test functions to read configuration/data files 
    from a specific location.

3. Make the test actually execute a non-cargo-test binary that is for exactly this purpose only.

    - Use a JupyterLab notebook for customized testing, 
        especially occasional long-running tests.
        This is my preference.

    - Create a separate project for testing.
        This is not as convenient as using a JupyterLab notebook.
        However,
        it might be the best solution in certain situations,
        e.g., 
        if you have to leverage Spark/PySpark for large-scale testing.

    - Integrate tests as a command into your main project.
        This is not recommended 
        as you might introduce test-only dependencies into your main project.

## Mocking

https://crates.io/crates/mailtutan

- [Mocking in Rust: Mockall and alternatives](https://blog.logrocket.com/mocking-rust-mockall-alternatives)

- [mockall](https://crates.io/crates/mockall)

- [mockers](https://crates.io/crates/mockers)

- [turmoil](https://crates.io/crates/turmoil)
[Turmoil](https://crates.io/crates/turmoil)
is a framework for testing distributed systems. 
It provides deterministic execution by running multiple concurrent hosts within a single thread. 
It introduces "hardship" into the system via changes in the simulated network. 
The network can be controlled manually or with a seeded rng.

## References

- [Useful Rust Crates for Testing](https://www.legendu.net/misc/blog/useful-rust-crates-for-testing)

- [How to run setup code before any tests run in Rust?](https://stackoverflow.com/questions/58006033/how-to-run-setup-code-before-any-tests-run-in-rust)

- [Test setup and teardown in Rust without a framework.](https://medium.com/@ericdreichert/test-setup-and-teardown-in-rust-without-a-framework-ba32d97aa5ab)

