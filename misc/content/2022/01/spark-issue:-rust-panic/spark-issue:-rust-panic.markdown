Status: published
Date: 2022-01-07 11:12:24
Modified: 2022-01-07 11:41:08
Author: Benjamin Du
Slug: spark-issue:-rust-panic
Title: Spark Issue: Rust Panic
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, big data, panic, panicked at, Rust

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

If use Rust with Spark/PySpark,
you might get Rust panic error messages. 

## Symptom 

Error: b"thread 'main' panicked at 'index out of bounds: the len is 15 but the index is 15', src/game.rs:131:39\nnote: run with RUST_BACKTRACE=1 environment variable to display a backtrace\n"

## Cause 

Bug in the Rust code.

## Solution

Fix the bug in the Rust code.


