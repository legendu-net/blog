---
title: Tips on Network Protocols
created: '2020-10-17T01:00:06-07:00'
date: '2026-11-25T00:30:20-08:00'
authors:
  - bendu
label: tips-on-network-protocols
license: CC-BY-4.0
tags:
  - computer science
  - network
  - internet
  - web
  - protocol
  - transfer
  - HTTP
  - HTTPS
  - FTP
  - TCP
  - IP
  - UDP
  - QUIC
  - SMTP
  - WebSockets
  - RPC
  - ActivityPub
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

TCP/IP and UDP/IP are low-level data transfer protocols.

HTTP, FTP, SMTP, WebSocket are high-level data transfer protocols.

WebSocket persists a connection and use it for bidirectional data transferring.
It is good for real-time applications, e.g., chat and game applications.

WebTransport is a better alternative to WebSocket.

MQTT is a standards-based messaging protocol used for machine-to-machine communication. Smart sensors, wearables, and other Internet of Things (IoT) devices typically have to transmit and receive data over a resource-constrained network with limited bandwidth.

## Protocol Stack & Layering Overview

Protocols such as TCP, UDP, QUIC, HTTP, HTTPS, WebSockets, RPC, and ActivityPub are not all direct competitors—they operate at different layers of the network stack and often build on top of one another:

- **Transport Layer (L4):**
  - **TCP (Transmission Control Protocol):** Connection-oriented, reliable, ordered byte stream.
  - **UDP (User Datagram Protocol):** Connectionless, unreliable, low-overhead datagrams with no ordering or retransmission guarantees.
  - **QUIC (RFC 9000):** Modern multiplexed transport protocol built on top of UDP, integrating TLS 1.3 encryption, independent stream multiplexing, and connection migration.
- **Security Layer (between L4 and L7):**
  - **TLS (Transport Layer Security):** Provides encryption, integrity, and server/client authentication over TCP (or built directly into QUIC), turning HTTP into **HTTPS**.
- **Application / Communication Layer (L7):**
  - **HTTP (Hypertext Transfer Protocol):** Stateless request-response protocol (`HTTP/1.1` and `HTTP/2` run over TCP, with TLS optional in the spec though required by browsers for HTTP/2; `HTTP/3` runs over QUIC).
  - **HTTPS:** HTTP secured with TLS.
  - **WebSockets (RFC 6455):** Persistent, full-duplex, message-framed communication over a single connection, originally initiated via an HTTP/1.1 upgrade handshake and also extensible to HTTP/2 (RFC 8441) and HTTP/3 (RFC 9220). For HTTP/3, **WebTransport** additionally provides multiplexed streams and unreliable datagrams over QUIC.
  - **RPC (Remote Procedure Call):** Action-oriented communication paradigm (e.g., gRPC using Protocol Buffers over HTTP/2, or JSON-RPC over HTTP/WebSockets) for calling remote functions as if they were local.
- **Application / Social Federation Protocol (above HTTP/HTTPS):**
  - **[ActivityPub](https://www.w3.org/TR/activitypub/):** W3C decentralized social networking protocol using ActivityStreams 2.0 JSON-LD payloads over HTTP/HTTPS, powering the Fediverse (e.g., Mastodon, PeerTube, Pixelfed).

## Comparison Table

```{list-table} Network Protocols Comparison
---
header-rows: 1
name: network-protocols-comparison-table
widths: 12 16 16 10 24 22
---
* - Protocol
  - Layer & Transport
  - Communication Model
  - Built-in Encryption
  - Key Strengths & Trade-offs
  - Primary Use Cases
* - **TCP**
  - L4 Transport (over IP)
  - Connection-oriented, reliable ordered byte stream
  - No (pair with TLS)
  - Guaranteed delivery & congestion control; suffers from head-of-line (HoL) blocking and 3-way handshake latency
  - Web traffic (HTTP/1.1, HTTP/2), databases, SSH, email (SMTP)
* - **UDP**
  - L4 Transport (over IP)
  - Connectionless, best-effort datagrams
  - No (pair with DTLS / custom)
  - Minimal overhead and low latency; no built-in ordering, retransmission, or congestion control
  - DNS, VoIP, real-time video calls (RTP/WebRTC), online gaming, foundation for QUIC
* - **QUIC**
  - L4 Transport (over UDP)
  - Connection-oriented, multiplexed independent streams
  - Yes (TLS 1.3 built-in)
  - Eliminates transport-level HoL blocking, supports 0-RTT/1-RTT handshakes and connection migration; UDP blocked on some strict firewalls
  - HTTP/3, mobile/lossy networks, modern real-time transport (WebTransport)
* - **HTTP**
  - L7 Application (TCP or QUIC)
  - Stateless request-response
  - No
  - Universal web semantics, caching, proxies; plaintext traffic is vulnerable to eavesdropping and tampering
  - Local/internal loopback testing, legacy plaintext endpoints
* - **HTTPS**
  - L7 Application (HTTP over TLS / QUIC)
  - Stateless request-response
  - Yes (TLS / TLS 1.3)
  - Confidentiality, integrity, and CA-verified server identity; slight handshake overhead (mitigated by TLS 1.3 & HTTP/3)
  - Public web, REST APIs, browser apps, secure service-to-service calls
* - **WebSockets**
  - L7 Application (TCP via HTTP Upgrade)
  - Persistent, full-duplex bidirectional messages
  - Optional (`wss://` uses TLS)
  - Low-overhead server push and client-to-server streaming; stateful connections complicate horizontal scaling and suffer TCP HoL blocking
  - Live chat, collaborative editing, real-time dashboards, multiplayer games
* - **RPC (e.g., gRPC)**
  - L7 Paradigm (commonly HTTP/2 + Protobuf)
  - Procedure/action invocation & streaming
  - Optional (TLS standard in production)
  - Strongly typed schemas, compact binary payloads, bidirectional streaming (gRPC); tighter coupling and less browser-native than REST
  - Microservices, internal APIs, low-latency polyglot backends
* - **ActivityPub**
  - L7 Social Federation (over HTTP/HTTPS)
  - Asynchronous actor inbox/outbox JSON-LD delivery
  - No (HTTPS used in practice; HTTP Signatures for auth)
  - Decentralized, federated social graph without central lock-in; eventual consistency and cross-instance moderation complexity
  - Fediverse platforms (Mastodon, Lemmy, PeerTube, Pixelfed)
```

## Key Pairwise Comparisons & Takeaways

### TCP vs. UDP vs. QUIC

- **TCP** guarantees that every byte arrives in order, retransmitting lost packets. However, because TCP treats a connection as a single byte stream, one lost packet stalls all multiplexed application streams on that connection (transport-level head-of-line blocking).
- **UDP** sends independent datagrams with no handshake or retransmission. Applications that tolerate minor packet loss (like voice/video calls or fast-paced game state) prefer UDP to avoid retransmission stalls.
- **QUIC** runs over UDP primarily to bypass network middlebox ossification (firewalls, NATs, and proxies that drop or mangle unfamiliar TCP extensions) and to iterate in user space without waiting on OS kernel updates, while implementing reliability, congestion control, and **TLS 1.3** directly. Each QUIC stream is independent, so packet loss on one stream does not block others, and connection IDs let mobile clients switch between Wi-Fi and cellular without dropping the connection.

### HTTP vs. HTTPS

- **HTTP** sends headers and bodies in plaintext, allowing any network intermediary to inspect or modify traffic.
- **HTTPS** wraps HTTP in **TLS** (or runs over QUIC in HTTP/3, which mandates TLS 1.3), providing confidentiality, tamper detection, and server authentication via X.509 certificates. Modern browsers restrict powerful web APIs (such as Service Workers and WebTransport) to HTTPS contexts.

### HTTP vs. WebSockets (and WebTransport)

- Standard **HTTP** is client-initiated request-response. For server-to-client updates alone, **Server-Sent Events (SSE)**—which works over HTTP/1.1, HTTP/2, and HTTP/3 (with HTTP/2+ avoiding HTTP/1.1's per-origin connection limits)—is simpler than WebSockets because it uses plain HTTP semantics and automatic reconnection.
- **WebSockets** (`ws://` / `wss://`) upgrade an HTTP/1.1 connection (or use extended `CONNECT` over HTTP/2 via RFC 8441 and HTTP/3 via RFC 9220) into a long-lived, full-duplex channel where both client and server can push frames at any time.
- **WebTransport** brings WebSocket-like bidirectional messaging *plus* unreliable datagrams and multiple independent streams on top of **HTTP/3 (QUIC)**, avoiding TCP head-of-line blocking.

### HTTP/REST vs. RPC

- **HTTP/REST** models interactions around **resources** (nouns like `/users/42`) manipulated with standard HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`) and typically JSON payloads. It integrates naturally with HTTP caching, CDNs, and browsers.
- **RPC** (such as **gRPC** or JSON-RPC) models interactions around **procedures/actions** (verbs like `GetUser(id)` or `TransferFunds(...)`). gRPC pairs HTTP/2 with binary Protocol Buffers for compact payloads, strict `.proto` contracts, and built-in client/server/bidirectional streaming, making it ideal for internal microservices.

### ActivityPub

- Unlike transport or general-purpose API protocols, **[ActivityPub](https://www.w3.org/TR/activitypub/)** is a decentralized social networking specification built *on top of* HTTP/HTTPS.
- It defines two complementary APIs using ActivityStreams 2.0 JSON-LD:
  - **Client-to-Server (C2S):** How a user's client posts activities (`Create`, `Like`, `Follow`) to their own server's `outbox`.
  - **Server-to-Server (S2S):** How federated servers deliver activities to remote actors' `inbox` endpoints. While the W3C specification does not mandate encryption or a specific signing scheme, Fediverse deployments use HTTPS for transport security and HTTP Signatures by convention to authenticate S2S deliveries.

## Cross-References

- [](#tips-on-http)
- [](#tips-on-websockets)
- [](#grpc-graphql-and-restful-apis)
- [](#tips-on-grpc)

## Video Notes

- [The QUIC Protocol, HTTP3, and How HTTP Has Evolved](https://www.youtube.com/watch?v=VONSx_ftkz8)

- [TCP vs UDP Comparison](https://www.youtube.com/watch?v=uwoD5YsGACg)

- [Networking Protocols Explained | What Are TCP/IP, UDP, HTTP, SMTP, FTP](https://www.youtube.com/watch?v=g_kNTa9y6Is)

- [SSL, TLS, HTTP, HTTPS Explained](https://www.youtube.com/watch?v=hExRDVZHhig)

- [SSL/TLS Termination, TLS Forward Proxy Pros and Cons](https://www.youtube.com/watch?v=H0bkLsUe3no)

## References

- [W3C ActivityPub Specification](https://www.w3.org/TR/activitypub/)

- [RFC 9000: QUIC](https://datatracker.ietf.org/doc/html/rfc9000)

- [WebTransport over HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-webtrans-http3/)

- [What are WebSockets | How is it different from HTTP?](https://www.youtube.com/watch?v=i5OVcTdt_OU)

- [WebSockets in 100 Seconds & Beyond with Socket.io](https://www.youtube.com/watch?v=1BfCnjr_Vjg)
