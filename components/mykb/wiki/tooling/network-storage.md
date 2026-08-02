---
type: "concept"
title: "Network Storage"
description: "Storage accessed over the network as opposed to locally attached"
tags: ["network-storage", "storage", "architecture", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Network Storage

## Summary
Network storage is any storage reached over the network — NAS (file), SAN (block), object stores — that separates data from any single machine. It enables sharing and central management at the cost of network latency and dependence.

## Details
- NAS serves files, SAN serves blocks, object stores serve objects: pick by workload.
- Latency and bandwidth to the network store are the performance determinants.
- Durability and redundancy live in the storage system, not the client.
- mykb relevance: the wiki bundle syncs to network object storage for durability.

## Related
- [[wiki/tooling/file-storage|File Storage]]
- [[wiki/tooling/block-storage|Block Storage]]
- [[wiki/tooling/object-storage-practice|Object Storage Practice]]
- [[wiki/cloud-infra/object-storage|Network Attached Storage]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
