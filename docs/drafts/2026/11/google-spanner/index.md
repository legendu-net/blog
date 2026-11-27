---
title: Google Spanner
created: '2026-11-25T04:08:36.096845-08:00'
date: '2026-11-25T04:08:36.096853-08:00'
authors:
  - bendu
label: google-spanner
license: CC-BY-4.0
tags:
  - computer science
  - database
  - distributed database
  - Google Spanner
  - NewSQL
  - CAP theorem
  - TrueTime
  - YugabyteDB
  - CockroachDB
  - TiDB
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Overview

[Google Cloud Spanner](https://cloud.google.com/spanner) is a globally distributed, horizontally scalable, strongly consistent relational database (often categorized as **NewSQL**). It combines relational schemas, SQL queries, and full ACID transactions with horizontal sharding and synchronous multi-region replication across datacenters. Spanner supports both its native **GoogleSQL** dialect and a **PostgreSQL** interface (including PGAdapter for standard PostgreSQL drivers and tooling).

## Architecture & TrueTime

In the [OSDI 2012 paper](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf), Google described how Spanner achieves global consistency at scale:

- **Paxos Groups & Two-Phase Commit (2PC)**: Data is sharded into splits (tablets) managed by **Paxos** consensus groups for fault-tolerant replication. Distributed transactions spanning multiple Paxos groups use **two-phase commit (2PC)** layered over Paxos, with two-phase locking for concurrency control.
- **TrueTime API**: Rather than relying on uncalibrated wall clocks (which suffer from drift), Spanner exposes a hardware-backed **TrueTime** API powered by **GPS receivers and atomic clocks** in every datacenter. Instead of returning a single point timestamp, TrueTime returns a bounded time interval `[earliest, latest]` where the true time is guaranteed to lie within an uncertainty window of `2 * epsilon` (typically a few milliseconds).
- **Commit-Wait & External Consistency**: By waiting out the uncertainty window (`commit-wait`) before releasing locks or making a transaction's writes visible, Spanner guarantees **external consistency** (strict serializability)—if transaction $T_2$ starts after $T_1$ commits in real time, $T_2$ receives a strictly greater commit timestamp. This also enables **lock-free read-only transactions** at a chosen timestamp without blocking concurrent writes.

## Spanner and the CAP Theorem

Under the **CAP theorem** (Consistency, Availability, Partition tolerance):

- **Technically CP (and PC/EC in PACELC)**: Because any wide-area distributed database must tolerate network partitions (`P`), Spanner prioritizes **Consistency (`C`)** over **Availability (`A`)** during a true partition—minority-side replicas cannot elect a Paxos leader or accept writes, preserving linearizability. Under the **PACELC** extension, Spanner is **PC/EC**: even during normal operation (`Else`), it chooses consistency (`C`) over minimal latency (`L`) by synchronously replicating writes via Paxos and waiting out TrueTime uncertainty.
- **Why Google describes it as "effectively CA"**: In practice, Spanner runs over Google's private, redundant global fiber WAN rather than the public internet. Combined with multi-region Paxos placement and automated failover, network partitions are rare enough that multi-region Spanner achieves a **99.999% availability SLA**, behaving almost like a CA system for most applications.

## Alternatives & Comparison

If you are already on Google Cloud and want zero-ops global strict serializability with a 99.999% SLA, **Google Cloud Spanner** is the gold standard. If you need multi-cloud portability, self-hosting, or open-source licensing without specialized atomic-clock hardware, **YugabyteDB** (PostgreSQL-compatible, Apache 2.0 core) and **TiDB** (MySQL-compatible, Apache 2.0) are the strongest open-source alternatives, while **CockroachDB** offers a mature PostgreSQL-compatible distributed SQL engine under a source-available license.

```{list-table} Distributed SQL Database Comparison
---
header-rows: 1
name: distributed-sql-comparison-table
widths: 18 8 15 15 9 10 13 12
---
* - Distributed SQL Database
  - Status
  - Clock / Time Sync
  - SQL Dialect
  - Open Source?
  - Language
  - License
  - Popularity (Stars)
* - [Google Cloud Spanner](https://cloud.google.com/spanner)
  - Active
  - TrueTime (GPS + atomic clocks)
  - GoogleSQL, PostgreSQL
  - N
  - C++ (proprietary)
  - Proprietary (Managed)
  - N/A
* - [YugabyteDB](https://github.com/yugabyte/yugabyte-db)
  - Active
  - Hybrid Logical Clocks (HLC)
  - PostgreSQL (YSQL), YCQL
  - Y[^os-yugabyte]
  - C++ / C
  - Apache-2.0 (Core)
  - ~10.7k ★
* - [TiDB](https://github.com/pingcap/tidb)
  - Active
  - Placement Driver TSO
  - MySQL
  - Y
  - Go / Rust[^lang-tidb]
  - Apache-2.0
  - ~40.8k ★
* - [CockroachDB](https://github.com/cockroachdb/cockroach)
  - Active
  - Hybrid Logical Clocks (HLC)
  - PostgreSQL
  - N[^os-cockroach]
  - Go
  - CockroachDB Software License
  - ~32.6k ★
```

## References

- [Inside Cloud Spanner and the CAP Theorem](https://cloud.google.com/blog/products/databases/inside-cloud-spanner-and-the-cap-theorem)
- [Spanner: A relational database for all size applications (FAQs)](https://cloud.google.com/blog/products/databases/spanner-relational-database-for-all-size-applications-faqs)
- [Spanner: Google's Globally-Distributed Database (OSDI 2012)](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
- [Spanning the Globe Without Google Spanner (YugabyteDB)](https://www.yugabyte.com/blog/spanning-the-globe-without-google-spanner/)
- [](#popular-databases)

[^os-yugabyte]: Core database engine (`src/yb/`, `src/postgres/`) is Apache-2.0; enterprise/management components (YugabyteDB Anywhere) are proprietary.

[^lang-tidb]: SQL layer (TiDB) is written in Go; the distributed transactional key-value storage engine (TiKV) is written in Rust.

[^os-cockroach]: Source-available under the CockroachDB Software License (previously BSL), not an OSI-approved open-source license.
