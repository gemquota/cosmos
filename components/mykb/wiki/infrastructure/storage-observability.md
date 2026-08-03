---
type: "concept"
title: "Storage Observability"
description: "Latency, IOPS, throughput, and capacity metrics for storage systems"
tags: ["storage", "observability", "metrics", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Storage Observability

## Summary
Storage observability is the practice of measuring latency, IOPS, throughput, capacity, and error rates across the storage stack so that slow or failing storage is detectable before users notice. Because storage sits under every workload, its metrics are usually the first place an incident shows up — and the hardest to attribute correctly.

## Details
- Core metrics: latency (p50/p99 and queueing at the device, array, and application layers), IOPS (read/write mix and queue depth), throughput (bytes per second and saturation), capacity (usage, projection, and snapshot overhead), and errors (CRC, SCSI sense codes, SMART attributes).
- Layering: observe at each boundary — application, filesystem, block layer, HBA/controller, and array/cloud volume — because a slow query can be caused by a saturating neighbor on a shared array, not by the application. Without layer attribution, the wrong component gets blamed.
- Concrete example: an IOPS spike on one VM's disk drags down a shared cloud volume's p99 latency for every tenant. Storage observability shows queue depth climbing on the shared volume while per-VM CPU stays flat, pointing to storage contention rather than application code.
- Failure modes: watching averages hides tail latency; capacity alerts that fire too late to resize; snapshots and backups that count against capacity invisibly; and monitoring the array but not the fabric (host path, cables, switches) where many failures actually live.
- Tradeoffs: instrumenting every layer adds agents, cardinality, and cost; but a storage team that only watches the array is blind to host-path issues. Choose a small set of high-signal metrics per layer and correlate them during incidents.
- Operational practice: set latency SLOs with error-budget burn alerts, track capacity with growth projections, run synthetic I/O checks, and keep a runbook that maps common metric signatures (high queue depth, CRC errors, SMART reallocations) to their causes.
- RSIS3/mykb relevance: telemetry coverage is a standing practice requirement in this repo; this node gives loops the metric vocabulary needed to verify that storage state changes actually improved performance.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-of-network-path|Observability of the Network Path]] — related coverage in the same cluster
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
