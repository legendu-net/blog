Status: published
Date: 2023-08-29 10:33:58
Modified: 2023-08-29 10:33:58
Author: Benjamin Du
Slug: trait-bound-in-rust
Title: Trait Bound in Rust
Category: Computer Science
Tags: Computer Science, programming

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There has to be a way to bundle up those type declarations. Was it not possible to make driver a trait that contains all of the complicated type declarations?

1. Avoid using complicated type bounds.
    It is better to derive a trait which contains all the complicated type bounds.

First define a trait that has your other traits as super traits. e.g.

`trait Foo : Bar + Baz {} `

Then implement that trait for any type that satisfies the bounds. E.g.:

`impl<T : Bar + Baz> Foo for T`

Now you can use T in place of Bar+ Baz.

You can also pack up lots of bounds / types into a trait:

Rather than

`impl<A,B,C...> where ...`

With a very long list of types and bounds, do:

`trait Pack {

type A where ...

type B where ...

type C where ...

...

}

Now you can just have a single bound to propagate `P : Pack` and one place to update this list. This is the same idea as grouping common arguments together into structs so you can add an argument without leaking details into too many function prototypes.
My last piece of advice on propagating 'where' bounds implicitly is that only super traits are implicitly propagated. `Self : Foo` is a supertrait. 'Self::B : Foo' is not. However, `Self<Indirect = B> { type Indirect : Foo }` is, and means the same thing.

Let's take a look, how HashMap is defined in std

```rust

pub struct HashMap<K, V, S = RandomState> {

base: base::HashMap<K, V, S>,

}

```

As you can see, there are no trait bounds on the generics. They are on impls - you could create HashMap with anything you want, but you cannot do anything useful with if, it K is not Hash.

The good strategy is to not write anything until you have to. So, you could omit where clauses on structs (while types inside the struct does not require any), and specify them only inside impls, when compiler is yelling at you. Here could be useful to split your methods to different impls with less generic bounds.

All types would be type checked in a trait resolution, so if at the end some traits would be missed, compiler will tell you. You specified types ahead of compiler told you, so...

In your code

```rust

#[derive(Clone)]

struct Driver<D>

where

D: Db + Clone + Send + Sync + 'static,

D::Tx: Tx + Send + Sync + 'static,

{

db: D,

}

```

Could become

```rust

struct Driver<D> {

db: D,

}

impl<D: Clone> for Driver {

fn clone(&self) -> Self {

Driver { db: self.db.clone() }

}

}

```

Then, you could remove all where clauses from impls. Compiler starts yelling at you at individual spots, and you should specify trait bounds for individual methods/groups of methods, maybe in separate impls.

Traits are about behavior. You provide behavior, if something has another behavior.


## References

- [A failed experiment with Rust static dispatch](https://jmmv.dev/2023/08/rust-static-dispatch-failed-experiment.html)
