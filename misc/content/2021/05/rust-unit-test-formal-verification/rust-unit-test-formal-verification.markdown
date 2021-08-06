Status: published
Date: 2021-05-13 09:33:19
Author: Benjamin Du
Slug: unit-testing-formal-verification-rust
Title: Unit Testing and Formal Verification in Rust
Category: Computer Science
Tags: Computer Science, programming, Rust, testing, unit test, verification, analysis, formal verification
Modified: 2021-07-15 23:29:02
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


assert!
assert_eq!
[matches!](https://doc.rust-lang.org/core/macro.matches.html)

assert_eq!(Rank::from_char('2').unwrap(), Rank::_2);
let err = Rank::from_char('z').unwrap_err().downcast().unwrap();
assert_eq!(err, RankError::NotARank('z')));
assert!(matches!(Rank::from_char('Z'), Err(_))


[Rust Design-for-Testability: a survey](https://alastairreid.github.io/rust-testability/)

[Rust Verification Tools](https://project-oak.github.io/rust-verification-tools/)

[Rust testing or verifying: Why not both?](https://alastairreid.github.io/why-not-both/)

[Rust verification tools](https://alastairreid.github.io/rust-verification-tools/#:~:text=Prusti%20is%20a%20really%20interesting,to%20help%20it%20verify%20code.)

[KLEE Symbolic Execution Engine](https://github.com/klee/klee)

[SeaHorn is an automated analysis framework for LLVM-based languages.](https://github.com/seahorn/seahorn)

[Library-ification and analyzing Rust](http://smallcultfollowing.com/babysteps/blog/2020/04/09/libraryification/)

[This is a static simulator for Rust programs. It runs a set of test cases and attempts to prove that all assertions pass on all valid inputs.](https://github.com/GaloisInc/crucible/tree/master/crux-mir)

## References 

- [Issues in asserting Result](https://users.rust-lang.org/t/issues-in-asserting-result/61198/6)

- [Prusti – Deductive Verification for Rust](https://www.youtube.com/watch?v=C9TTioH5JUg)

- [A static verifier for Rust, based on the Viper verification infrastructure.](https://github.com/viperproject/prusti-dev)

- [Verification Competitions](https://alastairreid.github.io/verification-competitions/)
