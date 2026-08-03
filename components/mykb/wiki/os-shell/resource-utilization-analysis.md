---
type: "concept"
title: "Resource Utilization Analysis"
description: "Reading CPU, memory, disk, and network counters to find the bottleneck"
tags: ["resource", "utilization", "performance", "monitoring"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Resource Utilization Analysis

## Summary
Resource utilization analysis is the practice of reading CPU, memory, disk, and network counters to find the actual bottleneck of a workload: which resource is saturated, which is merely busy, and what the utilization numbers imply about headroom. It is the difference between guessing "add more CPU" and knowing that the real constraint is a 100%-utilized disk queue or a saturated network link.

## Details
- Mechanism: the starting point is a set of counters per resource. CPU: `top`/`htop` show per-core utilization, `mpstat -P ALL` per-CPU, and `sar` history; the key subtlety is that 100% CPU is not automatically bad — a busy system doing real work is fine, while a system at 100% with a blocked pipeline is stalled. Memory: `free -m`, `vmstat`, and `/proc/meminfo` distinguish used, buffered/cached (reclaimable!), and swapped; the classic mistake is treating cached memory as "used". Disk: `iostat -x` shows `%util`, queue depth (`avgqu-sz`), and await; high `%util` with deep queues means saturated, while high latency with low utilization points elsewhere (contention, remote storage). Network: `sar -n DEV`, `nload`, and `ss -s` show throughput and errors; the bottleneck is often the link, not the server.
- Concrete examples: a web server at 90% CPU with disk at 5% needs more CPU or fewer requests per request (optimization); a database at 5% CPU with `%util` 99% and `avgqu-sz` 50 on its data disk is I/O-bound — the fix is caching, indexing, or faster storage, not more cores; a host with 64GB RAM showing 60GB "used" is often fine because 50GB is page cache that the kernel will reclaim; a CI worker with network `sar` showing 0.9 Gbps on a 1 Gbps link is network-bound. `pidstat`, `perf top`, and `strace` then zoom into the process level.
- Failure modes: the classic failures are reading single snapshots instead of trends (a momentary spike is not a bottleneck), measuring utilization while ignoring saturation and queues (a disk at 50% with a deep queue is already the bottleneck), and misreading cache as used memory. Instrumentation itself distorts: `top` samples can miss short CPU bursts, and monitoring agents add their own load. Correlating one resource's counter with the wrong symptom (blaming CPU when lock contention shows as high CPU but the real issue is serialization) is the subtlest failure.
- Operational tradeoffs: analysis tools range from instant (`top`, `vmstat 1`) to deep (`perf`, eBPF), and the tradeoff is speed versus precision: the USE method (utilization, saturation, errors) gets you to the bottleneck in minutes; deeper profiling confirms it. The practice rules: start with USE per resource, watch trends not snapshots, always ask "saturated or just busy?", and collect baseline numbers so "unusual" is measurable, not vibes.
- RSIS3/mykb relevance: RSIS3's batch loops (graph rebuilds, TF-IDF indexing) are exactly the workloads that benefit: check CPU vs. I/O saturation before scaling, and record utilization baselines with telemetry so loop regression is visible in the dashboard — the same counters, tracked over time.

## Related
- [[wiki/infrastructure/packet-analysis-with-tcpdump|Packet Analysis with tcpdump]]
- [[wiki/devops-infra/custom-resource-definitions|Custom Resource Definitions]]
- [[wiki/cloud-infra/flow-logs-and-analysis|Flow Logs & Analysis]]
- [[wiki/cloud-infra/resource-tagging|Resource Tagging]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
