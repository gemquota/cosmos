---
type: "concept"
title: "RCU & Read-Copy-Update"
description: "Lock-free reads with deferred reclamation for kernel data"
tags: ["rcu", "locking", "kernel", "concurrency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# RCU & Read-Copy-Update

## Summary
RCU (Read-Copy-Update) is a synchronization mechanism that makes reads of shared data completely lock-free: readers never block, never spin, and never contend, while writers publish new versions and defer reclamation of the old one until every reader that might be using it has finished. It is the workhorse of the Linux kernel, protecting everything from the dcache to network protocol tables.

## Details
- Mechanism: the pattern is in the name. A reader enters a read-side critical section (`rcu_read_lock`, often a no-op on non-preemptible kernels) and dereferences a pointer; a writer copies the data structure, modifies the copy, publishes it with an atomic pointer assignment (a store-release), and then — the crucial part — cannot free the old copy until all pre-existing readers have exited their critical sections. The kernel tracks that moment via quiescent states (context switches and idle), and `synchronize_rcu`/`call_rcu` wait for (or defer to) that grace period before reclaiming memory. The key correctness argument: because the old pointer is never freed while a reader may still see it, and readers never write, no locks are needed on the read path.
- Concrete examples: Linux's dentry cache and route tables are read by every syscall and packet; the network stack uses RCU-protected lists for protocol handlers so `tcpdump` can iterate while another CPU unregisters a handler; a module using `list_add_rcu`/`list_del_rcu` lets readers traverse a list lock-free while writers add/remove nodes; user-space flavors (liburcu, and `rcu` in some runtimes) apply the same discipline to hot read paths in databases and message buses.
- Failure modes: the classic failures are freeing too early (a writer frees the old object without waiting for a grace period — a use-after-free that only shows under load), memory leaks from never calling `synchronize_rcu`/`call_rcu` (old versions pile up), and long read-side critical sections that delay grace periods, stalling writers and causing latency spikes or OOM pressure if reclamation backs up. Readers that sleep inside RCU critical sections on preemptible kernels break the guarantee, and misuse of the pointer-exchange ordering (missing the release/acquire semantics) corrupts the shared view.
- Operational tradeoffs: RCU trades writer complexity for reader performance — the read path becomes as cheap as an ordinary dereference with no cache-line bouncing, which is why it scales so well, while writers pay for copying and for grace-period latency (the deferred-free window). It is the right tool for read-mostly data updated rarely (tables, caches, registries); for write-heavy data, locks or per-CPU structures are simpler. The practice rules: keep read-side sections short and non-sleeping, always pair publication with `synchronize_rcu`/`call_rcu` before freeing, and prefer library implementations over hand-rolled ones. RSIS3/mykb relevance: RCU is the canonical read-mostly pattern — the wiki's link graph and the loop registry are read far more than written, and RCU-style "publish new version, defer reclamation" is exactly how MyKB should swap indexes without blocking readers.

## Related
- [[wiki/os-shell/copy-on-write-filesystems|Copy-on-Write Filesystems]]
- [[wiki/os-shell/copy-on-write|Copy-on-Write]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/physics-update|Physics Update]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
