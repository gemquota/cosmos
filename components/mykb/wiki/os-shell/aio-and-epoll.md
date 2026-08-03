---
type: "concept"
title: "AIO & epoll"
description: "Kernel async I/O and event notification side by side"
tags: ["aio", "epoll", "io", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# AIO & epoll

## Summary
epoll and AIO are the Linux kernel's two answers to the same problem — keeping a process busy while I/O completes — from opposite directions. epoll notifies you when a file descriptor becomes ready (readiness-based event notification), while kernel AIO (io_submit/io_getevents) performs the I/O for you and delivers completion events (completion-based async I/O). Understanding the difference is the key to choosing the right I/O model for servers, databases, and storage engines.

## Details
- Mechanism: epoll is an event-ready interface: you register file descriptors with `epoll_ctl`, block on `epoll_wait`, and the kernel returns the subset that can be read or written without blocking. The actual read/write still happens in your process via regular syscalls. Linux native AIO (`io_submit` with `IOCB_CMD_PREAD`/`PWRITE`) instead queues an I/O request that the kernel carries out asynchronously, delivering completion events through `io_getevents`; because the syscall returns before the data is in your buffer, the I/O overlaps with computation in a way that even non-blocking syscalls cannot provide for regular files.
- Concrete examples: an HTTP server uses epoll to track thousands of idle connections with one thread, waking only when sockets have data (this is how nginx and most modern servers scale); a database or search engine issues a batch of pread requests on a file via `io_submit`, then continues computing while the disk (or NVMe) works, collecting completions later — the pattern that makes io_uring's predecessor attractive for high-IOPS workloads.
- Failure modes: the classic epoll failure is the thundering herd and starvation: many threads waking on one event, or level-triggered notifications re-firing because data was not fully drained; edge-triggered mode fixes the re-fire but demands that you read until `EAGAIN`. Native AIO's failures are worse: the classic implementation only works on O_DIRECT files and some block devices (buffered files fall back to a synchronous wait), and misaligned buffers or sizes (must be sector-aligned) fail with `EINVAL`; there is also no default timeout semantics without an eventfd, and the API is notoriously easy to misuse.
- Operational tradeoffs: epoll is the right tool for network I/O and mixed workloads — simple, robust, and universally applicable — while native AIO only pays off for high-throughput, aligned, O_DIRECT storage workloads where the synchronous syscall cost and cache behavior dominate. Modern guidance: prefer io_uring, which unifies both models (readiness and completion, buffered and direct), or use epoll for sockets and libaio only where benchmarks justify it. RSIS3/mykb relevance: the daemon's telemetry ingestion and graph rebuilds are I/O-bound; choosing completion-based I/O with proper alignment mirrors the loop hygiene rule that batch work should overlap with compute rather than block it.

## Related
- [[wiki/os-shell/select-poll-epoll-comparison|select, poll & epoll]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
