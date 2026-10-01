---
title: Handling Sign in Modulo
created: '2026-09-30T16:58:26.336344-07:00'
date: '2026-09-30T16:58:26.336353-07:00'
authors:
  - bendu
label: handling-sign-in-modulo
license: CC-BY-4.0
tags:
  - programming
  - math
  - mathematics
  - modulo
  - integer
  - sign
  - signed
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

When implementing hash tables, round-robin schedulers, circular buffers, or data partitions, developers frequently rely on the modulo / remainder operator `%` to map integers into a fixed range of buckets $[0, Y - 1]$. However, handling negative inputs ($X < 0$) introduces subtle traps involving language semantics, frequency distribution, integer overflow, and low-level bit representations.

## Modulo Semantics Across Languages

The behavior of `X % Y` with negative numbers depends on how the programming language defines integer division:

1. **Truncated Division (Truncation toward Zero):**

   - Implemented in C, C++, Java, Rust, Go, C#, JavaScript, etc.
   - The quotient is rounded toward zero: $q = \text{trunc}(X / Y)$.
   - The remainder satisfies $r = X - q \times Y$ and preserves the sign of the dividend $X$.
   - For a positive divisor $Y = 3$, $X \pmod 3$ yields values in $\{-2, -1, 0, 1, 2\}$.

1. **Floored Division (Rounding toward $-\infty$):**

   - Implemented in Python, Ruby, etc.
   - The quotient is rounded toward negative infinity: $q = \lfloor X / Y \rfloor$.
   - The remainder takes the sign of the divisor $Y$.
   - For $Y = 3$, $X \pmod 3$ always yields non-negative values in $\{0, 1, 2\}$, naturally forming valid bucket indices.

In languages with truncated division, developers must explicitly handle negative remainders to map them into $[0, Y - 1]$.

## The "Zero Frequency Trap" in Signed Modulo

Consider truncated modulo with $Y = 3$, producing signed remainders in $\{-2, -1, 0, 1, 2\}$.

If you directly observe the frequencies of these five values across a symmetric range of inputs (e.g., $X \in [-N, N]$):

- `0` is produced by all multiples of $3$ on **both the positive and negative sides**: $\dots, -6, -3, 0, 3, 6, \dots$.
- `1` and `2` come **only from positive numbers**: $1, 2, 4, 5, \dots$.
- `-1` and `-2` come **only from negative numbers**: $-1, -2, -4, -5, \dots$.

Consequently, among the 5 distinct raw remainder values, `0` occurs with roughly **twice the frequency** of each individual nonzero signed value (`-2`, `-1`, `1`, `2`).

## Mapping to Non-Negative Buckets

To map remainders into $[0, Y - 1]$, two common approaches are:

1. `abs(X % Y)`
1. `abs(X) % Y`

### Why `abs` Balances Bucket Frequencies

Taking the absolute value collapses symmetric positive and negative non-zero remainders together:

- Both $+1$ and $-1$ map to bucket $1$.
- Both $+2$ and $-2$ map to bucket $2$.

Now, bucket $0$ receives multiples of $Y$ from both sides, while buckets $1, \dots, Y - 1$ also receive inputs from both positive and negative sides. This merges the split cases and balances the bucket frequencies uniformly.

### The `INT_MIN` Overflow Trap

Between `abs(X % Y)` and `abs(X) % Y`, **`abs(X % Y)` is significantly safer**.

In two's-complement arithmetic, an $N$-bit signed integer represents values in the range $[-2^{N-1}, 2^{N-1}-1]$. Because the negative range is asymmetric, `INT_MIN` has no positive equivalent:

- For a 32-bit signed integer, `INT_MIN = -2147483648`, whereas `INT_MAX = 2147483647`.
- Calling `abs(INT_MIN)` cannot represent $+2147483648$ as a signed integer, causing signed integer overflow (undefined behavior in C/C++, or returning `INT_MIN` in Java/Rust wrapping operations).

Evaluating `abs(X) % Y` first encounters this overflow whenever $X = \text{INT\_MIN}$.

A classic real-world bug in Java demonstrates this trap:

```java
// BUG: If key.hashCode() is Integer.MIN_VALUE,
// Math.abs(Integer.MIN_VALUE) returns Integer.MIN_VALUE!
// The result is negative, causing an ArrayIndexOutOfBoundsException:
int bucket = Math.abs(key.hashCode()) % numBuckets;
```

In contrast, `abs(X % Y)` computes the modulo first. Since $|X \% Y| < Y$, for any practical divisor $Y \ll \text{INT\_MAX}$, the intermediate remainder is well within the representable signed range. Its absolute value will never overflow.

*(Note: In C and C++, `INT_MIN % -1` can overflow because the quotient exceeds `INT_MAX`, but for positive divisors $Y > 0$, `X % Y` is completely well-defined.)*

### `abs(X % Y)` vs Canonical Modulo

While `abs(X % Y)` works well for hashing and random bucketing, note that it does **not** equal mathematical (floored) modulo:

- For $X = -1$ and $Y = 3$:
  - `abs(-1 % 3) = abs(-1) = 1`
  - Mathematical modulo (congruence) defines $-1 \equiv 2 \pmod 3$.

If your use case requires cyclic continuity (such as ring buffers, array rotation, or clock arithmetic where $-1$ should wrap around to the end $Y - 1$):

- Assuming a positive divisor $Y > 0$, use the canonical formula:
  ```c
  int mod = (X % Y + Y) % Y;
  ```

### Bonus: Power-of-Two Bitmasking (Hash Tables)

When the bucket count is a power of two ($Y = 2^k$), standard hash tables (such as Java's `HashMap`) avoid modulo division altogether by using bitwise AND:

```c
int bucket = hash & (capacity - 1);
```

In two's-complement representation, this bitmask naturally and branchlessly extracts the lowest $k$ bits for any integer—including `INT_MIN`—always yielding a valid non-negative index in $[0, Y - 1]$ without overflow concerns.

## Can We Erase the Sign Bit with Bit Operations?

It is tempting to wonder if clearing the sign bit using bit manipulation is a faster way to obtain `abs(X)`. The answer depends on data representation:

### 1. Two's-Complement Integers: Do NOT Simply Clear the Sign Bit

Two's-complement negative numbers are **not** represented as "sign bit + magnitude".

For example, in 8-bit integers:

- $+8 = 00001000_2$
- $-8 = 11111000_2$

If you clear the most significant bit (MSB) of $-8$:

```text
  11111000  (-8)
↓ clear MSB
  01111000  (120 in decimal, NOT 8!)
```

To compute `abs(X)` branchlessly on two's-complement integers using bitwise operations:

```c
int mask = x >> 31;                 // 0 for x >= 0; -1 (0xFFFFFFFF) for x < 0
int abs_x = (x ^ mask) - mask;      // Inverts bits and adds 1 if negative
```

Even with this branchless trick, the `INT_MIN` overflow limitation remains.

### 2. IEEE-754 Floating-Point: Clearing the Sign Bit Works

Unlike integers, IEEE-754 floating-point numbers explicitly store the sign in the most significant bit (1 sign bit, followed by exponent and mantissa).

For floating-point numbers, clearing the sign bit directly calculates `fabs`:

```c
// Conceptually:
uint64_t bits = *(uint64_t*)&double_val;
bits &= ~(1ULL << 63);              // Clear sign bit
double abs_val = *(double*)&bits;
```

*(In production C/C++, use `std::bit_cast` in C++20 or `memcpy` in C to avoid strict aliasing violations).*

## Summary

| Goal                                                | Recommended Approach                       | Note                                                       |
| --------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------- |
| Hash bucketing / partitioning ($X$ may be negative) | `abs(X % Y)`                               | Avoids `INT_MIN` overflow; balances bucket frequencies.    |
| Power-of-two hash bucketing ($Y = 2^k$)             | `X & (Y - 1)`                              | Branchless, avoids division, handles `INT_MIN` safely.     |
| Cyclic wrapping / modular arithmetic ($Y > 0$)      | `(X % Y + Y) % Y`                          | Preserves mathematical congruence: $-1 \pmod Y \to Y - 1$. |
| Branchless absolute value (two's complement)        | `(x ^ mask) - mask` where `mask = x >> 31` | Never clear MSB directly; still watch for `INT_MIN`.       |
| Float absolute value                                | Clear MSB (`bits & ~SIGN_BIT`)             | Valid for IEEE-754 sign-magnitude encoding.                |
