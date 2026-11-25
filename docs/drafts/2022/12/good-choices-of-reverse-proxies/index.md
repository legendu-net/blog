---
title: Good Choices of Reverse Proxies
created: '2022-12-09T10:57:00-08:00'
date: '2026-11-25T04:55:00-08:00'
authors:
  - bendu
label: good-choices-of-reverse-proxies
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - proxy
  - reverse proxy
  - tunneling
  - nginx
  - caddy
  - traefik
  - haproxy
  - envoy
  - Sozu
  - pingora
  - tinyproxy
  - frp
  - rathole
  - cloudflared
  - tailscale
  - ngrok
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

"Reverse proxy" is an overloaded term that covers two distinct architectures.
Understanding this split explains why tools like [frp](https://github.com/fatedier/frp) and [TinyProxy](https://github.com/tinyproxy/tinyproxy) look out of place next to [Nginx](https://github.com/nginx/nginx):

1. **Edge / Web Reverse Proxies**:
   Sit in front of public-facing servers (with a public IP and open ports 80/443)
   to terminate TLS, route HTTP/HTTPS/gRPC traffic, and load-balance across backends.
   Examples: Caddy, Nginx, Traefik, HAProxy, Envoy, Sozu, and Cloudflare Pingora (a Rust framework for building custom proxies).
2. **NAT-Traversal / Tunneling Reverse Proxies**:
   Expose local services running behind a NAT or firewall without opening inbound router ports,
   by maintaining an outbound connection from the local machine to a public relay server.
   Examples: frp, rathole, Cloudflare Tunnel (`cloudflared`), Tailscale Funnel, and ngrok.
   See also [](#expose-local-service-to-public) and [](#proxy-reverse-proxy-load-balancer-vpn-and-dns).

> **Note on TinyProxy:** [TinyProxy](https://github.com/tinyproxy/tinyproxy) (see [](#tips-on-tinyproxy))
> is primarily a lightweight HTTP/HTTPS *forward* proxy,
> though it supports a basic reverse-proxy mode via `ReversePath`.
> For dedicated reverse-proxying or TLS termination, prefer Caddy or Nginx.

## Verdict

- **Default self-hosted web reverse proxy:** Use **[Caddy](https://github.com/caddyserver/caddy)** for automatic HTTPS out of the box and minimal configuration (see [](#tips-on-caddy)). Use **[Nginx](https://github.com/nginx/nginx)** when you need maximum ecosystem familiarity, static-file throughput, or fine-grained tuning.
- **Containers & Kubernetes ingress:** Use **[Traefik](https://github.com/traefik/traefik)** for dynamic service discovery (Docker labels, Kubernetes CRDs) or **[Envoy](https://github.com/envoyproxy/envoy)** for service-mesh / L7 observability.
- **High-throughput TCP/HTTP load balancing:** Use **[HAProxy](https://github.com/haproxy/haproxy)**, or **[Pingora](https://github.com/cloudflare/pingora)** if you want to embed a memory-safe Rust proxy library.
- **Self-hosted NAT traversal (no open local ports):** Use **[frp](https://github.com/fatedier/frp)** when you have a cheap VPS and want rich protocol support (TCP/UDP/HTTP/HTTPS/STCP) and dashboarding. Use **[rathole](https://github.com/rathole-org/rathole)** for a minimal, high-performance Rust alternative.
- **Zero-VPS managed NAT traversal:** Use **[Cloudflare Tunnel](https://github.com/cloudflare/cloudflared)** for production-grade public web apps behind Cloudflare's edge, **[Tailscale Funnel](https://github.com/tailscale/tailscale)** if you already use Tailscale, or **[ngrok](https://ngrok.com/)** for quick ephemeral developer demos.

## Comparison

```{list-table} Reverse Proxy and Tunneling Tools Comparison
---
header-rows: 1
name: reverse-proxy-comparison-table
widths: 12 8 10 6 6 12 16 14 7 8 8
---
* - Reverse Proxy
  - Status
  - Category
  - Self-Hosted
  - Auto-TLS
  - Protocols
  - Best For
  - Caveats
  - Language
  - License
  - Popularity (Stars)
* - [Caddy](https://github.com/caddyserver/caddy)
  - Active
  - Edge / Web
  - Y
  - Y[^at-caddy]
  - HTTP/1-3, gRPC, WebSocket
  - Default self-hosted web proxy
  - Slightly higher memory than Nginx
  - Go
  - Apache-2.0
  - ~79.5k ★
* - [Nginx](https://github.com/nginx/nginx)
  - Active
  - Edge / Web
  - Y
  - N[^at-nginx]
  - HTTP/1-3, gRPC, TCP/UDP
  - Static files & battle-tested edge
  - Requires Certbot/ACME for TLS; reload on config change
  - C
  - BSD-2-Clause
  - ~33.3k ★
* - [Traefik](https://github.com/traefik/traefik)
  - Active
  - Edge / Web
  - Y
  - Y[^at-traefik]
  - HTTP/1-3, gRPC, TCP/UDP
  - Docker / Kubernetes auto-discovery
  - Dynamic config can be verbose for static hosts
  - Go
  - MIT
  - ~65.7k ★
* - [HAProxy](https://github.com/haproxy/haproxy)
  - Active
  - Edge / Web
  - Y
  - N[^at-haproxy]
  - TCP, HTTP/1-3, gRPC
  - High-throughput L4/L7 load balancing
  - Manual TLS cert management; steeper config
  - C
  - GPL-2.0 / LGPL-2.1
  - ~7.0k ★
* - [Envoy](https://github.com/envoyproxy/envoy)
  - Active
  - Edge / Web
  - Y
  - N[^at-envoy]
  - HTTP/1-3, gRPC, TCP
  - Service mesh & cloud-native L7
  - Complex YAML/xDS config for simple setups
  - C++
  - Apache-2.0
  - ~29.3k ★
* - [Pingora](https://github.com/cloudflare/pingora)
  - Active
  - Edge Framework
  - Y
  - N[^at-pingora]
  - HTTP/1-2, TLS, TCP
  - Building custom Rust proxies
  - Library/framework, not a turnkey binary
  - Rust
  - Apache-2.0
  - ~28.0k ★
* - [Sozu](https://github.com/sozu-proxy/sozu)
  - Active
  - Edge / Web
  - Y
  - N[^at-sozu]
  - HTTP/1-2, WebSocket, TCP
  - Hot-reconfigurable Rust edge proxy
  - Smaller ecosystem than Nginx/Caddy
  - Rust
  - AGPL-3.0
  - ~3.8k ★
* - [frp](https://github.com/fatedier/frp)
  - Active
  - NAT Tunnel
  - Y
  - N[^at-frp]
  - TCP, UDP, HTTP, HTTPS, STCP
  - Feature-rich self-hosted NAT traversal
  - Requires a public VPS for `frps`
  - Go
  - Apache-2.0
  - ~110.8k ★
* - [rathole](https://github.com/rathole-org/rathole)
  - Active
  - NAT Tunnel
  - Y
  - N[^at-rathole]
  - TCP, UDP
  - Lightweight, fast `frp` alternative
  - Requires a public VPS; no built-in HTTP routing
  - Rust
  - Apache-2.0
  - ~14.5k ★
* - [cloudflared](https://github.com/cloudflare/cloudflared)
  - Active
  - NAT Tunnel
  - N[^sh-cloudflared]
  - Y[^at-cloudflared]
  - HTTP, HTTPS, SSH, TCP, UDP
  - Zero-VPS public web exposure
  - Tied to Cloudflare DNS and edge limits
  - Go
  - Apache-2.0
  - ~16.7k ★
* - [Tailscale Funnel](https://github.com/tailscale/tailscale)
  - Active
  - NAT Tunnel
  - N[^sh-tailscale]
  - Y[^at-tailscale]
  - HTTPS, TCP
  - Sharing services on an existing tailnet
  - Public Funnel relay is managed; limited ports
  - Go
  - BSD-3-Clause
  - ~39.6k ★
* - [ngrok](https://ngrok.com/)
  - Active
  - NAT Tunnel
  - N[^sh-ngrok]
  - Y[^at-ngrok]
  - HTTP, HTTPS, TLS, TCP
  - Instant ephemeral dev webhooks/demos
  - Proprietary v3 service; free-tier limits
  - Go
  - Proprietary
  - N/A[^pop-ngrok]
```

## Notes by Category

### Edge / Web Reverse Proxies

- **[Caddy](https://github.com/caddyserver/caddy)**: Written in Go with automatic Let's Encrypt / ZeroSSL provisioning and renewal out of the box, plus a concise `Caddyfile` syntax.
- **[Nginx](https://github.com/nginx/nginx)**: The industry workhorse for static content and reverse proxying, with vast documentation and third-party modules.
- **[Traefik](https://github.com/traefik/traefik)**: Excels in dynamic container environments by watching Docker, Swarm, or Kubernetes APIs directly.
- **[HAProxy](https://github.com/haproxy/haproxy)**: Optimized for high-concurrency L4 TCP and L7 HTTP load balancing with rich health checks and stick tables.
- **[Envoy](https://github.com/envoyproxy/envoy)**: Designed for large microservice architectures and service meshes (e.g., Istio) with dynamic xDS configuration and deep telemetry.
- **[Pingora](https://github.com/cloudflare/pingora)**: Cloudflare's async Rust proxy framework powering massive edge traffic; ideal when you need programmatic control rather than a static config file.
- **[Sozu](https://github.com/sozu-proxy/sozu)**: A Rust reverse proxy designed for runtime hot-reconfiguration without dropping connections.

### NAT-Traversal / Tunneling Reverse Proxies

- **[frp](https://github.com/fatedier/frp)**: Consists of a server (`frps`) on a public VPS and a client (`frpc`) behind NAT. Supports HTTP/HTTPS virtual hosts, raw TCP/UDP port forwarding, P2P/STCP encrypted tunnels, and a web dashboard.
- **[rathole](https://github.com/rathole-org/rathole)**: A Rust alternative to `frp` focused on low memory footprint and high throughput over Noise/TLS encrypted TCP/UDP tunnels.
- **[cloudflared](https://github.com/cloudflare/cloudflared)**: Connects local origins to Cloudflare's global edge via outbound tunnels, eliminating the need to maintain a public VPS or open firewall ports.
- **[Tailscale Funnel](https://github.com/tailscale/tailscale)**: Exposes a local port on a Tailscale node to the public internet over `*.ts.net` with automatic TLS.
- **[ngrok](https://ngrok.com/)**: Managed developer tunneling service with request inspection and replay; convenient for quick webhook testing.

[^at-caddy]: Built-in automatic ACME (Let's Encrypt / ZeroSSL) provisioning and renewal.
[^at-nginx]: Requires external ACME tooling such as `certbot` or `acme.sh`.
[^at-traefik]: Built-in `certificatesResolvers` ACME support.
[^at-haproxy]: Requires external ACME tooling (e.g., `acme.sh` + reload/socket update).
[^at-envoy]: Typically delegated to the control plane / SDS (e.g., cert-manager + Istio).
[^at-pingora]: Framework only; TLS certificate management must be wired in Rust code.
[^at-sozu]: Certificates are supplied via configuration/socket commands rather than built-in ACME.
[^at-frp]: Supports TLS between `frpc`/`frps` and `https2http` plugins, but does not auto-provision public ACME certs.
[^at-rathole]: Supports Noise/TLS transport encryption, not public ACME web certs.
[^sh-cloudflared]: The `cloudflared` daemon is open-source, but the Cloudflare Tunnel edge relay is managed.
[^at-cloudflared]: Automatic TLS termination on Cloudflare's edge.
[^sh-tailscale]: The Tailscale client is open-source, but the Funnel ingress relay and coordination plane are managed.
[^at-tailscale]: Automatic TLS certificates for `*.ts.net` domains.
[^sh-ngrok]: Managed SaaS; the legacy open-source v1 repository (`inconshreveable/ngrok`) is archived.
[^at-ngrok]: Automatic TLS termination on ngrok's edge.
[^pop-ngrok]: Closed-source v3 agent/service; the archived v1 repository has ~24.4k ★.
