---
type: "concept"
title: "Storage Classes & Provisioners"
description: "Dynamic volume provisioning policies in Kubernetes"
tags: ["storage-class", "provisioner", "kubernetes", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Storage Classes & Provisioners

## Summary
Storage classes define the flavors of storage available in a Kubernetes cluster — performance tier, replication, reclaim behavior — and provisioners (drivers) create the actual volumes. A StorageClass maps a user request to an implementation: fast SSD, network volume, local disk, or a cloud product, with parameters like IOPS and disk type.

## Details
- Mechanism: a StorageClass declares a provisioner (the CSI driver), parameters (disk type, IOPS, replication), reclaimPolicy (Delete or Retain), volumeBindingMode (Immediate or WaitForFirstConsumer), and mount options; a PVC referencing the class triggers provisioning; the default class is used when the PVC names none.
- Concrete example: a cluster offers `fast-ssd` (EBS gp3 with high IOPS, WaitForFirstConsumer for correct node placement), `standard` (network volume with replication), and `local-ssd` (node-pinned); a database uses fast-ssd, a cache uses local-ssd, and backups go to object storage outside the class system.
- Failure modes: missing or wrong default class leaving PVCs pending; parameters the provider ignores or rejects, failing provisioning; reclaim policies that delete data when a claim is removed; WaitForFirstConsumer not configured where placement matters, attaching volumes to the wrong node; class proliferation — dozens of subtly different classes that no one understands.
- Tradeoffs: multiple classes let workloads match cost and performance, but every class is an operational surface (quotas, monitoring, troubleshooting); the alternative, one class for everything, is simpler and wasteful; the mature pattern is a small catalog of well-documented classes with explicit default and lifecycle ownership.
- Operational notes: document the class catalog, monitor provisioned capacity and failures, and set quotas per class.
- RSIS3 relevance: the wiki store's storage class choice (speed versus durability) is a cost-and-recovery decision — document which class holds what and why.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]] — related coverage in the same cluster
- [[wiki/cloud-infra/coldline-and-archive-storage-classes|Coldline & Archive Storage Classes]] — related coverage in the same cluster
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
