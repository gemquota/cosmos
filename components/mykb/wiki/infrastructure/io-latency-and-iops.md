---
type: "concept"
title: "IO Latency & IOPS"
description: "Queue depth, latency percentiles, and IO operations per second"
tags: ["io", "latency", "iops", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# IO Latency & IOPS

## Summary
IO latency and IOPS are the two numbers that describe storage performance: IOPS (input/output operations per second) measures how many operations the storage can complete, and latency measures how long each operation takes. The relationship between them — queue depth — is the key that makes both numbers legible, and the latency percentile distribution (not the average) is what actually predicts whether applications will be happy.

## Details
- The arithmetic: throughput = IOPS × transfer size, and the relationship between IOPS and latency is governed by queue depth: latency ≈ queue depth ÷ IOPS (Little's law). A storage device with 10ms latency can deliver 100 IOPS at queue depth 1 (one request in flight) — or, if the system issues 100 concurrent requests, 10,000 IOPS at the same 10ms latency. This is why "the disk can do 100K IOPS" and "the disk has 10ms latency" are both true: the numbers describe different operating points, and applications drive queue depth by how many concurrent I/Os they issue. Random access is latency-bound (each operation is a seek/access — IOPS matters), sequential access is bandwidth-bound (large transfers — throughput matters).
- The hardware ladder: HDDs deliver ~100-200 random IOPS with 5-15ms latency (mechanical seek dominates); SATA SSDs deliver tens of thousands of IOPS with ~100µs latency; NVMe drives deliver hundreds of thousands to millions of IOPS with ~10-50µs latency. The order-of-magnitude jumps are why the storage stack changed: database designs that minimized random I/O (because disks were slow) became unnecessary on NVMe, and queue depth (which software had to maximize for disks) became something the drives themselves handle with deep native queues.
- The measurement discipline: latency must be reported as percentiles, not averages. An average hides the tail — a database with 1ms average latency and 500ms p99 is failing its interactive users while looking healthy in the average. The standard set is p50/p95/p99 (and p99.9 for critical paths), and the failure mode this catches is exactly the noisy-neighbor and garbage-collection class: storage that is mostly fast but periodically stalls. The alerting rule: watch p99 against a budget; the average is a dashboard decoration.
- The operational reality: the measured latency of a cloud volume is not the device's latency — it includes the network (iSCSI/EBS), the hypervisor, the queueing at every layer, and the tenant's own contention; "provisioned IOPS" on a cloud volume is a billing contract with a performance expectation attached, and the only way to verify it is to measure it under load.
- Failure modes: queue-depth saturation (one noisy workload starves the device's queues — everyone's latency climbs), tail latency from background tasks (snapshots, scrubs, garbage collection), and the measurement trap: benchmarking a device at the wrong queue depth or wrong block size produces numbers that describe the benchmark, not the workload.
- For mykb: the node anchors the storage-performance cluster — IO sizing, latency budgets, and async I/O all connect here.

## Related
- [[wiki/os-shell/io-uring-and-async-io|io_uring & Async I/O]]
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]]
- [[wiki/infrastructure/pipeline-sla-and-latency-budgets|Pipeline Sla And Latency Budgets]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
