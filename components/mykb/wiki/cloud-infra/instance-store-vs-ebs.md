---
type: "concept"
title: "Instance Store vs EBS"
description: "Ephemeral local disks versus networked durable volumes"
tags: ["instance-store", "ebs", "aws", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Instance Store vs EBS

## Summary

Instance store is ephemeral, directly attached storage with enormous I/O; EBS is durable, network-attached block storage. The choice is durability vs speed: instance store for caches, scratch, and replicated services; EBS for anything that must survive instance replacement.

## Details
- Mechanism: instance store (AWS, GCP local SSD, Azure temp disk) lives on the physical host — no network hop, up to millions of IOPS — but is lost on stop/termination/host failure; EBS/PD persists independently and reattaches, with snapshots, at network-attached latency and per-volume IOPS ceilings. Instance store capacity and performance vary by instance size.
- Concrete example: a Redis cache on instance store accepts data loss because it is rebuilt from the source of truth; a Spark shuffle writes instance store for speed; a database on EBS with snapshots survives host replacement. The failure pattern is storing the only copy of something on instance store and losing it to a host maintenance event.
- Failure modes: treating instance store as persistent (no replication) and losing data; instance store sizes that cannot back up conveniently (backup from the network path instead); EBS latency surprises for high-IOPS workloads that instance store would handle; and forgetting that some instance families force a storage choice (NVMe vs EBS-only).
- Operational tradeoffs: the pattern is stateful data on durable storage, stateless/temp data on instance store; a hybrid (instance store cache + EBS truth) captures both. Design for instance store loss from the start — it is a maintenance event away.
- RSIS3/mykb relevance: the wiki's experiment runners would place scratch and caches on instance store and durable artifacts on EBS; this note records the split so the loop's jobs never write critical data to ephemeral disks.
- Backup design: if the durable copy lives on EBS, snapshot it; if the fast copy lives on instance store, treat it as rebuildable and verify the rebuild path actually works.

## Related
- [[wiki/cloud-infra/amazon-ebs-provisioning|Amazon EBS Provisioning]]
