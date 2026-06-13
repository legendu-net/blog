---
title: Binary Serialization Format
created: '2022-10-16T16:12:18-07:00'
date: '2026-06-12T22:15:55-07:00'
authors:
  - bendu
label: binary-serialization-format
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - binary
  - serialization
  - protobuf
  - Protocol Buffer
  - FlatBuffers
  - messagepack
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Summary

1. Protobuf is best for message serialization.
   Some companies (e.g., Google) also use it extensively for disk serialization.

1. FlatBuffers has better CPU performance.

1. [Apache Parquet](https://github.com/apache/parquet-format)
   is the most popular binary serialization format for data frames.

1. For text serialization format,
   please refer to
   [Serialization and deserialization in Python](serialization-and-deserialization-in-python)
   .

## Protobuf vs FlatBuffers

Flatbuffers are mmap-able and don't have any parsing overhead compared to protos.
Large protos not only have CPU overhead but cause a memory usage spike
when proto is parsed during the resource loading phase.
The memory usage spike can lead to more page faults and increased end user latency.
Flatbuffers have none of these disadvantages.

## [messagepack](https://msgpack.org/index.html)

## [Apache Parquet](https://github.com/apache/parquet-format)

## References

- [FlatBuffers vs Protocol Buffer](https://www.reddit.com/r/cpp/comments/l4viq3/flatbuffers_vs_protocol_buffer/)

- [Protobuf vs flatbuffer vs messagepack](https://news.ycombinator.com/item?id=18189437)

- [The need for speed — Experimenting with message serialization](https://medium.com/@hugovs/the-need-for-speed-experimenting-with-message-serialization-93d7562b16e4#:~:text=MessagePack%20is%20known%20for%20its,any%20message%20can%20be%20serialized.)
