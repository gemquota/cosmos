---
type: "concept"
title: "Storage Classes"
description: "Kubernetes abstractions that map PersistentVolumeClaims to storage backends with specific performance"
tags: ["kubernetes", "storage", "persistent-volumes", "provisioning"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Storage Classes

## Summary
A storage class describes a class of storage — SSD, HDD, replicated, local — and how it is dynamically provisioned. Claims request storage by class, decoupling workloads from vendor specifics.

## Details
- Dynamic provisioning: a claim with a storage class creates the volume automatically.
- Properties: reclaim policy (delete/retain), volume binding mode (immediate/wait-for-first-consumer), and provisioner.
- Choose classes by performance and cost: fast for databases, cheap for logs.
- Open question: how to map storage classes to cloud tiers and backups.

## Related
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]] — what classes provision
- [[wiki/infrastructure/stateful-workloads|Stateful Workloads]] — the consumers of storage
- [[wiki/infrastructure/containerization|Containerization]] — the platform storage plugs into
- [[wiki/devops-infra/kubernetes|Kubernetes]] — storage abstraction in the cluster
