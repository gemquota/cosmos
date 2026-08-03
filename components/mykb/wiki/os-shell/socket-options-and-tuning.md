---
type: "concept"
title: "Socket Options & Tuning"
description: "SO_* knobs for buffers, timeouts, and reuse across sockets"
tags: ["sockets", "tuning", "networking", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Socket Options & Tuning

## Summary
Socket options are the per-socket knobs that tune how the kernel handles a connection: buffer sizes, timeouts, reuse, keepalive, and delivery semantics. `SO_RCVBUF`/`SO_SNDBUF` control buffering, `SO_REUSEADDR`/`SO_REUSEPORT` manage bind and load distribution, `SO_KEEPALIVE` detects dead peers, and `TCP_NODELAY` disables Nagle — each one a lever for latency, throughput, or reliability on a specific connection class.

## Details
- Mechanism: `setsockopt(fd, SOL_SOCKET, optname, ...)` sets a per-socket attribute at creation or any time; TCP-specific options use `IPPROTO_TCP`. `SO_RCVBUF`/`SO_SNDBUF` bound how much the kernel buffers before the app (or the peer) — larger buffers smooth bursts and improve throughput on lossy links but increase latency and memory; note the kernel doubles the requested receive buffer (`rmem_max` caps it). `SO_REUSEADDR` lets a server rebind while old TIME_WAIT sockets linger; `SO_REUSEPORT` lets several sockets bind the same port, with the kernel load-balancing across them — the standard multi-worker trick. `TCP_NODELAY` disables Nagle's algorithm so small writes flush immediately (essential for request/response protocols); `TCP_QUICKACK` and `TCP_CORK` tune acknowledgment and batching in the other direction.
- Concrete examples: a Redis server sets large `SO_RCVBUF`/`SO_SNDBUF` and `TCP_NODELAY` on client connections; nginx uses `SO_REUSEPORT` so each worker accepts directly; a gaming or RPC server disables Nagle to cut per-request latency; `SO_KEEPALIVE` with tuned `TCP_KEEPIDLE`/`TCP_KEEPINTVL` detects half-open connections after idle; a database sets `SO_LINGER` carefully so `close()` flushes or aborts as intended (a zero linger forces RST, which loses unsent data); `ss -o state established` shows keepalive timers.
- Failure modes: the classic failures are buffer mis-sizing (a huge `SO_SNDBUF` on many sockets exhausts kernel memory — `vm.max_map_count`/memory pressure; tiny buffers collapse throughput), forgetting `SO_REUSEADDR` so restarts fail with "address already in use" during TIME_WAIT, and `TCP_NODELAY` misuse — disabling Nagle without disabling delayed ACKs can actually *increase* latency by causing ACK delays, so both must be considered. `SO_REUSEPORT` without careful hashing can skew connections to one worker, and keepalive defaults (2 hours idle) are useless for dead-peer detection unless tuned.
- Operational tradeoffs: the knobs are cheap to set and powerful, but every option is a tradeoff — bigger buffers buy throughput at latency/memory cost, aggressive ACK/NO_DELAY buys latency at packet-count cost, and reuse options buy bind flexibility at fairness cost. The practice rules: set the few options that match your protocol (NO_DELAY for request/response, reuseport for multi-worker, keepalive tuned for your idle tolerance), verify with `ss -o`/`netstat -s`, and treat sysctl-wide tuning (`net.core.rmem_max`, `net.ipv4.tcp_*`) as capacity work, not per-connection fixes. RSIS3/mykb relevance: the daemon's API sockets should set `TCP_NODELAY` and tuned keepalive so dashboard requests and agent callbacks never wait on Nagle or die silently on dead connections — the transport-level mirror of loop timeout discipline.

## Related
- [[wiki/os-shell/errexit-and-shell-options|Errexit & Shell Options]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
