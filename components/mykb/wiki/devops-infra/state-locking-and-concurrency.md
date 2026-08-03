---
type: "concept"
title: "State Locking & Concurrency"
description: "Preventing conflicting infrastructure mutations with locks"
tags: ["state-locking", "terraform", "concurrency", "iac"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# State Locking & Concurrency

## Summary
State locking and concurrency control prevent two writers from corrupting shared state: infrastructure tools lock state files (Terraform), databases use transactions and advisory locks, and distributed systems use leases and optimistic concurrency. The common requirement is that a conflicting write fails loudly instead of silently overwriting.

## Details
- Mechanism: Terraform/OpenTofu lock the state file during operations (DynamoDB lock, local lock) so two plans cannot race; databases offer transactions with serializable isolation and advisory locks for application-level coordination; optimistic concurrency (version numbers, compare-and-swap) rejects stale writes; distributed locks (etcd, Redis, ZooKeeper) coordinate across processes with leases and fencing.
- Concrete example: two engineers running terraform apply on the same workspace — the state lock makes the second fail with a clear error instead of corrupting state; an inventory service uses a version column so an update based on a stale read is rejected; a background job holds a Redis lease with a TTL and fencing token so a crashed worker cannot keep writing.
- Failure modes: locks held too long blocking legitimate work (stale lock entries need expiry); lock expiry mid-operation letting a second writer in (fencing tokens fix this); optimistic concurrency with no retry loop, failing every conflicting update; distributed locks without fencing, allowing split-brain writes; lock scope too coarse, serializing unrelated operations.
- Tradeoffs: locking guarantees correctness at the cost of availability and throughput — the classic CAP trade; optimistic concurrency keeps availability and fails only conflicting writers, but clients must handle retries; the choice depends on write frequency and the cost of corruption; for state files and databases, correctness almost always wins.
- Operational notes: set lock timeouts, monitor lock contention, implement fencing where writes have real side effects, and test the conflict path.
- RSIS3 relevance: RSIS3's registry and state files need the same protection — concurrent loops writing checkpoints should fail loudly or coordinate, never silently overwrite each other's progress.

## Related
- [[wiki/devops-infra/terraform-state-management|Terraform State Management]] — related coverage in the same cluster
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — related coverage in the same cluster
- [[wiki/infrastructure/query-timeouts-and-concurrency-limits|Query Timeouts And Concurrency Limits]] — related coverage in the same cluster
- [[wiki/os-shell/file-locking|File Locking]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
