Status: published
Date: 2022-10-16 16:12:18
Modified: 2022-10-17 13:48:56
Author: Benjamin Du
Slug: binary-serialization-format
Title: Binary Serialization Format
Category: Computer Science
Tags: Computer Science, programming, binary, serialization, protobuf, Protocol Buffer, FlatBuffers, messagepack

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Summary 

1. Protobuf is best for message serialization.
    Some companies (e.g., Google) also use it extensively for disk serialization.

2. FlatBuffers has better CPU performance.

3. [Apache Parquet](https://github.com/apache/parquet-format)
    is the most popular binary serialization format for data frames.
    
4. For text serialization format,
    please refer to
    [Serialization and deserialization in Python](https://www.legendu.net/misc/blog/serialization-and-deserialization-in-python/)
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
