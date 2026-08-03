---
type: "concept"
title: "io_uring & Async I/O"
description: "The high-performance asynchronous I/O interface on Linux"
tags: ["io-uring", "async-io", "kernel", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# io_uring & Async I/O

## Summary
io_uring is Linux's modern asynchronous I/O interface, designed to minimize the per-operation cost of syscalls: applications submit batches of requests to a shared ring buffer (`io_uring_submit`) and reap completions from another ring (`io_uring_wait_cqe`), with the kernel performing the actual I/O asynchronously. It supersedes both the older libaio interface and much of the epoll-based readiness model for high-performance storage and networking.

## Details
- Mechanism: two memory-mapped ring buffers shared between the application and kernel carry submissions (SQE, submission queue entries) and completions (CQE). The app fills an SQE describing an operation (read, write, fsync, accept, send, recv, or even `openat` and `splice`), advances the tail, and rings a doorbell; the kernel processes the entries and posts CQEs, which the app reaps without a syscall per operation in the common case. Features include `IORING_SETUP_IOPOLL` for polling drives, registered buffers and files (`IORING_REGISTER_BUFFERS`, `io_uring_register_files`) that skip per-op setup, linked requests, and multishot accept/receive for server workloads.
- Concrete examples: a storage engine batches thousands of preads with registered buffers and reaps completions in one wait — the pattern behind RocksDB's and ScyllaDB's io_uring backends; a proxy uses multishot accept to handle new connections without a syscall per connection; databases use `IORING_FEAT_FAST_POLL` and io_uring-provided registered files to reduce per-request overhead; `fio` benchmarks with `ioengine=io_uring` show substantially higher IOPS than libaio on modern kernels.
- Failure modes: the classic failures are assuming it works everywhere — older kernels (pre-5.1) lack it, containers and seccomp profiles may block `io_uring_setup`, and some filesystems/backing devices do not support every operation (the kernel falls back or returns `EOPNOTSUPP`); ring-buffer misuse (submitting entries past the capacity, forgetting to advance indices, or sharing rings across threads without locking) corrupts submissions; and memory-registration misuse (registering a buffer then freeing it) causes use-after-free bugs that are notoriously hard to debug.
- Operational tradeoffs: io_uring's wins are real — fewer syscalls, true async completion for both storage and sockets, and features (registered files, fixed buffers, poll) that reduce per-I/O overhead — but they come with complexity: ring management, feature probing, kernel-version checks, and a programming model that is easy to get subtly wrong. The pragmatic path: use high-level libraries (liburing, `tokio-uring`, RocksDB's wrapper) rather than the raw interface, probe kernel support at runtime with fallbacks to epoll/thread pools, and measure before adopting. RSIS3/mykb relevance: the daemon's graph rebuilds and telemetry writes are batch I/O; adopting io_uring-style batched, completion-driven I/O where it is available mirrors RSIS3's principle of amortizing fixed costs across batch work.

## Related
- [[wiki/infrastructure/io-latency-and-iops|IO Latency & IOPS]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
