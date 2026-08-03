---
type: "concept"
title: "Storage Throughput"
description: "Sequential transfer rates and the bandwidth side of storage"
tags: ["throughput", "storage", "bandwidth", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Storage Throughput

## Summary
Storage throughput is the bandwidth side of storage performance: how many bytes per second a device or system can transfer, usually measured on sequential workloads. It is the sibling of latency and IOPS, and the three metrics describe different bottlenecks — throughput tells you how fast bulk data moves, not how quickly a single request completes.

## Details
- Mechanism: throughput is limited by the narrowest component in the I/O path — the media (disk platters, NAND dies), the interface (SATA, SAS, NVMe, network), the controller, or the filesystem. Sequential reads amortize seek and command overhead, so they reach the media's raw transfer rate, while random I/O trades throughput for IOPS.
- Workloads that care: backups and restores, log shipping, data migration, video streaming, and database scans are sequential and throughput-bound; OLTP transactions are latency- and IOPS-bound. Choosing storage by the wrong metric — buying a fast-latency SSD for a bulk-transfer job — wastes money.
- Concrete example: a 10 TB database dump to a device rated at 2 GB/s takes about 83 minutes at peak; but if the filesystem is fragmented, the array is shared, or checksumming consumes CPU, achieved throughput can drop by an order of magnitude, silently extending every backup window.
- Failure modes: throughput collapse under queue saturation (read-modify-write amplification on parity RAID), throttling by cloud volume burst credits, interference from a noisy neighbor on shared storage, and misconfigured filesystem record sizes that turn sequential writes into read-modify-write churn.
- Tradeoffs: throughput and latency are often opposing goals — deep queues maximize bandwidth but add latency per request; compression raises effective throughput at CPU cost; deduplication saves space but adds a compute stage before writes.
- Operational practice: measure with sequential tools (`dd`, `fio` with a sequential job) at the device, filesystem, and application layers; track achieved versus rated throughput over time; and size backup and replication capacity from peak transfer needs, not average utilization.
- RSIS3/mykb relevance: when loops reason about data movement — snapshots, consolidation, migration — this node supplies the distinction between rated bandwidth and achieved throughput so capacity plans use realistic numbers.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/cloud-infra/bandwidth-vs-throughput|Bandwidth vs Throughput]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
