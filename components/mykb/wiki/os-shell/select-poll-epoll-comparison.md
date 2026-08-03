---
type: "concept"
title: "select, poll & epoll"
description: "Scaling event notification from fd arrays to readiness sets"
tags: ["select", "poll", "epoll", "io"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Select, Poll & epoll

## Summary
select, poll, and epoll are the Linux APIs for waiting on many file descriptors at once — the readiness layer under every event-driven server. select and poll rescan the full descriptor set on every call, which limits them to a few thousand fds; epoll registers interest once and reports only the descriptors that became ready, scaling to hundreds of thousands of connections with O(1) wakeups.

## Details
- Mechanism: `select(nfds, rfds, wfds, xfds, timeout)` takes three fixed-size fd bitmaps and returns which fds are ready, with an `FD_SETSIZE` limit (typically 1024) and no way to register interest once — the kernel rescans everything each call, and the caller must rebuild the sets between calls. `poll(struct pollfd[], nfds, timeout)` removes the bitmap limit (arbitrary fd arrays) and reports per-fd events with `revents`, but still rescans the full array per call — O(n) work and memory copying per wakeup. `epoll` inverts the model: `epoll_ctl` registers fds with interest flags once, and `epoll_wait` returns only the ready fds; the kernel maintains a ready list, so wakeups cost O(number of ready fds), and edge-triggered mode (`EPOLLET`) notifies once per state change rather than while data remains.
- Concrete examples: a chat server registering 50,000 connections: select would fail at 1024; poll would copy 50,000 pollfds on every call; epoll handles it with one registration each and small wait results. nginx, Redis, and Node.js's libuv all use epoll on Linux for this reason. Level-triggered epoll behaves like poll (notify while readable), edge-triggered requires reading until `EAGAIN`; `epoll_ctl` supports modifying interest (e.g., toggling `EPOLLOUT` for backpressure) and `EPOLLONESHOT` for one-shot wakeups used with thread pools.
- Failure modes: the classic failures are fd leaks (an unclosed fd registered in epoll grows the watch set until `EMFILE`/`ENFILE` — "too many open files" while the app believes it cleaned up), missed events in edge-triggered mode when code stops reading before `EAGAIN` (the event never re-fires, the connection stalls), and thundering-herd wakeups when multiple threads call `epoll_wait` on the same set (mitigated with `EPOLLEXCLUSIVE` or per-thread sets). select's 1024-fd limit and fd-set corruption from writing past `FD_SETSIZE` are legacy footguns that still bite ported code.
- Operational tradeoffs: epoll's scaling wins come with complexity: registration state, edge-trigger semantics, and readiness-vs-completion confusion (epoll tells you "ready", not "done" — that is io_uring's job). The practice rules: use epoll (or a library built on it) for any server with more than a few hundred connections, prefer level-triggered unless you understand edge semantics, set `RLIMIT_NOFILE` deliberately, and audit fd usage under load. RSIS3/mykb relevance: the daemon's many client connections (dashboard, agents, CLI) are an epoll-class workload; choosing the right readiness model keeps one slow client from blocking the loop, mirroring RSIS3's backpressure discipline.

## Related
- [[wiki/os-shell/aio-and-epoll|AIO & epoll]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
