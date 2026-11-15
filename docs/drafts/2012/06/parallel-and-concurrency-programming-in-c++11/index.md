---
title: Parallel and Concurrency Programming in C++11
created: '2012-06-25T17:51:37-07:00'
date: '2026-11-15T09:14:59-08:00'
authors:
  - bendu
label: parallel-and-concurrency-programming-in-c++11
license: CC-BY-4.0
tags:
  - programming
  - C/C++
  - cpp
  - HPC
  - async
  - mutex
  - future
  - concurrency
  - promise
  - parallel
  - multithreading
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

0. If you use g++ to compile your parallel program which uses the thread library,
   you need to use the option `-lpthread`.
   For more information,
   see the post [Tips on C++ Compilers](tips-on-c++-compilers)
   .

1. The `join` method of threads guarantees happen-before relationship between threads.

1. You can pass either a function (can be lambda function) and an object
   which implement the operator `()` to a thread.

1. The `future` class in C++11 is similar to the `future` class in Java.
   The difference is that in C++11 we have another class named `promise`
   which can work together with `future` to return values from threads
   while in Java you do not need a promise and can just let methods (to be called by threads) return values.
   In C++11,
   there is another class `async`
   which is close to what Java does.
   You do not have to use a promise and you can let functions/methods (to be called by threads) return values directly.
   `async` is kind of like thread pool in Java,
   but not exactly the same.
   You do not have much control on what many threads to with `async` in C++11
   while in Java you have better control on that.

1. To protect shared data between threads in C++11,
   you have to use the `mutex` (mutual exclusion) class which is similar to the `ReentrantLock` class in Java.
   Actually the `ReentrantLock` class in Java is essentially mutex.
   There is a common misunderstanding about **lock** in Java.
   The locking/unlocking is a conceptual thing that happens via programmer discipline:
   basically if you make a method synchronized to prevent a read/write conflict on a variable,
   then you have to ensure that every access to that variable is through a synchronized method/block of the same object.
   That forces every threads to acquire mutex of the object and ensures mutual exclusion.
   Directly use of the `lock` and `unlock` methods of mutex is not encouraged in C++11 though,
   this is because if exception occurs between the locked block,
   the resource will never be unlock resulting dead lock.
   In Java this is gracefully addressed by introducing a `finally` block
   in addition to the `try ... catch ...` blocks.
   A commonly used way to protect shared data in C++11 is to use the `lock_guard` class.
   For example you can put the following code in the functions/methods
   that need to be access by thread mutual exclusively

   ```
    :::c++
    std::lock_guard<std::mutex> lck(_mutex);
   ```

   where `_mutex` is a shared object of the `mutex` class among these functions/methods.
   The deconstructor of the `lock_guard` unlocks the lock so this guarantees that no dead lock happens.

1. It seems that parallel code in c++ is as efficient as in java (in the sense of code speedup)?

1. `std::async` together with `std::future` is an alternative to `std::thread`
   and shared variables when implementing parallel algorithms.
   Using `std::async` and `std::future`,
   one avoids to lock/unlock variables and thus avoids false sharing problems,
   so it sometimes a better alternative to `std::thread` and shared variables.

1. When you pass the address of a method to a thread or async,
   you must use the full name of the function,
   i.e.,
   you have to use class name as the prefix.
   Also,
   you have to pass `this` as the second parameter to thread/async if the method is a non-static method.
   This is because a non-static method need a instance to run.
   (I'm not very sure whether this is true for static methods)

1. You'd better not pass overloaded functions to thread or async in a class,
   because it is hard for the thread or async to know which one is the right method to call.
   I'm not sure whether there is way to solve this problem or not ...

1. It seems that object used mutex cannot be copied?
   So if you write a thread safe class using mutex,
   you'd better override the default copy constructor of the class,
   or you can make the mutex static.

1. Parallel program often requires shared variables which should be access by references.
   By default objects are passed by value (i.e. copied) in C++,
   so you have to be careful when you write parallel code in C++,
   otherwise,
   it is easy to make mistakes.

1. Prefer asynchronized buffering when dealing with high-latency operations.
   A good article from Herb Sutter can be found
   [here](http://www.drdobbs.com/architecture-and-design/know-when-to-use-an-active-object-instea/227500074?pgno=1).
