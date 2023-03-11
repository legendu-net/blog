Status: published
Date: 2023-01-13 15:46:22
Modified: 2023-03-06 10:42:48
Author: Benjamin Du
Slug: useful-rust-crates-for-database
Title: Useful Rust Crates for Database
Category: Computer Science
Tags: Computer Science, programming, Rust, database, crate, SQL

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [surrealdb](https://github.com/surrealdb/surrealdb)
[SurrealDB](https://github.com/surrealdb/surrealdb)
is an end-to-end cloud native database for web, mobile, serverless, Jamstack, backend, and traditional applications. 
SurrealDB reduces the development time of modern applications by simplifying your database and API stack, 
removing the need for most server-side components, 
and allowing you to build secure, performant apps quicker and cheaper. 
SurrealDB acts as both a database and a modern, real-time, collaborative API backend layer. 
SurrealDB can run as a single server or in a highly-available, 
highly-scalable distributed mode, 
with support for SQL querying from client devices, GraphQL, ACID transactions, WebSocket connections, structured 
and unstructured data, graph querying, full-text indexing, geospatial querying, and row-by-row permissions-based access.

## [rusqlite](https://crates.io/crates/rusqlite)
[rusqlite](https://crates.io/crates/rusqlite)
is an ergonomic wrapper for SQLite.

## [serde](https://crates.io/crates/serde)
[serde](https://crates.io/crates/serde)
is a framework for serializing and deserializing Rust data structures efficiently and generically.

## [sled](https://github.com/spacejam/sled)
[sled](https://github.com/spacejam/sled)
is an embedded key-value pair databases written in Rust.

## [indradb](https://github.com/indradb/indradb)
[indradb](https://github.com/indradb/indradb)
is a graph database written in rust.

## [oxigraph/](https://github.com/oxigraph/oxigraph/)
[oxigraph/](https://github.com/oxigraph/oxigraph/)
Oxigraph is a graph database implementing the SPARQL standard.
Its goal is to provide a compliant, safe, 
and fast graph database based on the RocksDB and Sled key-value stores. 
It is written in Rust. 
It also provides a set of utility functions for reading, writing, and processing RDF files.
Oxigraph is in heavy development and SPARQL query evaluation has not been optimized yet.

### [skytable](https://github.com/skytable/skytable)
[Skytable](https://github.com/skytable/skytable)
is a free and open-source NoSQL database 
that aims to provide flexible data modeling at scale. 
Simplicity, performance and flexibility are the guiding design principles.

### [bolt-rs](https://github.com/lucis-fluxum/bolt-rs)
[bolt-rs](https://github.com/lucis-fluxum/bolt-rs)
aims to provide a comprehensive set of libraries 
that allow for interaction with graph database servers 
that support the Bolt protocol, namely, Neo4j. 
This set of libraries allows interacting with servers 
supporting versions 1 through 4.1 of the protocol, 
which includes Neo4j 3.1 through 4.2.

### [neo4rs](https://github.com/yehohanan7/neo4rs)
[Neo4rs](https://github.com/yehohanan7/neo4rs)
is a Neo4j rust driver implemented using bolt specification.
This driver is compatible with neo4j 4.x versions

## [qdrant](https://github.com/qdrant/qdrant)
[Qdrant](https://github.com/qdrant/qdrant)
is a vector similarity search engine and vector database. 
It provides a production-ready service with a convenient API 
to store, search, and manage points - vectors with an additional payload. 
Qdrant is tailored to extended filtering support. 
It makes it useful for all sorts of neural-network or semantic-based matching, faceted search, and other applications.





