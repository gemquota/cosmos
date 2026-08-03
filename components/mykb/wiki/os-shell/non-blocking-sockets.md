---
type: "concept"
title: "Non-Blocking Sockets"
description: "Socket modes that return immediately instead of blocking"
tags: ["non-blocking", "sockets", "io", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Non-Blocking Sockets

## Summary
A non-blocking socket returns immediately from `read`, `write`, `accept`, and `connect` instead of waiting: when no data is available, `read` returns `EAGAIN`/`EWOULDBLOCK`; when the send buffer is full, `write` does the same. This is the primitive under event-driven servers — epoll tells you when a socket is ready, and non-blocking mode ensures the handler never stalls the event loop.

## Details
- Mechanism: setting `O_NONBLOCK` via `fcntl(sock, F_SETFL, O_NONBLOCK)` (or the `SOCK_NONBLOCK` flag at creation) changes every blocking syscall's behavior: `read`/`recv` return -1 with `EAGAIN` when no data, `write`/`send` return `EAGAIN` when the send buffer has no room, `accept` returns `EAGAIN` when no connection is pending, and `connect` returns `EINPROGRESS` instead of waiting for the handshake (completion is detected via `POLLOUT`/`getsockopt(SO_ERROR)`). The standard architecture pairs non-blocking sockets with a readiness interface — select, poll, epoll — so a thread can manage thousands of connections: wait for readiness, then perform the operation knowing it will not block.
- Concrete examples: nginx and most high-performance servers set every listening and accepted socket non-blocking and drive them with epoll; a chat server's send path checks `EAGAIN` and queues pending bytes per connection rather than blocking the loop; an HTTP client does an asynchronous `connect` and waits on `POLLOUT`; `python`'s asyncio and Node.js do this implicitly — user code rarely sees `EAGAIN` because the runtime handles it, but the underlying sockets are non-blocking.
- Failure modes: the classic failure is treating `EAGAIN` as an error: naive code aborts the connection or spins in a busy loop retrying immediately, burning CPU; the correct response is to return to the event loop and retry when the socket becomes ready. The partial-write problem is the second classic: a `write` on a non-blocking socket can accept part of the buffer and return a short count, so senders must track unsent bytes across multiple `POLLOUT` wakeups. `accept` loops need care under load (accept until `EAGAIN` to avoid thundering wakeups), and mixing blocking and non-blocking sockets in one event loop stalls the whole loop.
- Operational tradeoffs: non-blocking sockets trade programmer convenience for scalability: the code becomes stateful (partial writes, in-flight connects, queue per connection), but a single thread can serve tens of thousands of connections. The alternatives — a thread per connection or io_uring — shift the tradeoff differently: threads simplify code but burn memory and context switches; io_uring moves the completion model into the kernel. The practice rules: always handle `EAGAIN` by returning to the event loop, track partial writes explicitly, and prefer higher-level event frameworks unless you are building the server yourself. RSIS3/mykb relevance: the daemon's API and telemetry sockets should be non-blocking under an event loop so one slow client cannot stall graph rebuilds — the same backpressure discipline RSIS3 applies to loop queues.

## Related
- [[wiki/infrastructure/non-production-data-refresh|Non Production Data Refresh]] — related coverage in the same cluster
- [[wiki/os-shell/netcat-and-raw-sockets|netcat & Raw Sockets]] — related coverage in the same cluster
- [[wiki/os-shell/network-sockets|Network Sockets]] — related coverage in the same cluster
- [[wiki/os-shell/unix-domain-sockets|Unix Domain Sockets]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
