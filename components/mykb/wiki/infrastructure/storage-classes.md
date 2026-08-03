---
type: "concept"
title: "Storage Classes"
description: "Kubernetes abstractions that map PersistentVolumeClaims to storage backends with specific performance"
tags: ["kubernetes", "storage", "persistent-volumes", "provisioning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Storage Classes

## Summary
A storage class describes a class of storage — SSD, HDD, replicated, local — and how it is dynamically provisioned in Kubernetes. Claims request storage by class name, decoupling workloads from vendor-specific provisioning details so the same manifest can run on different clusters and clouds.

## Details
- Dynamic provisioning: a PersistentVolumeClaim that references a storage class triggers the class's provisioner to create a volume automatically, instead of an admin pre-provisioning PersistentVolumes by hand. The provisioner is usually a cloud or CSI driver: `standard` maps to cloud SSD, `local-path` to node-local storage, `ceph-rbd` to a Ceph pool.
- Key properties: reclaim policy (`Delete` removes the volume with the claim, `Retain` keeps it for manual recovery), volume binding mode (`Immediate` binds at claim time, `WaitForFirstConsumer` delays binding until a pod schedules, which matters for zone-aware or local storage), and allowVolumeExpansion.
- Choose classes by performance and cost: fast replicated storage for databases, cheaper un-replicated classes for logs and caches. Multiple classes let the same application tier request different durability and IOPS profiles without changing code.
- Concrete example: a Postgres pod claims `ssd-replicated` for its data volume while the same namespace's log collector claims `hdd-single`; a cluster admin adds a new `nvme-local` class and workloads opt in by changing one class name.
- Failure modes: misconfigured reclaim policy deletes data when a claim is removed; `Immediate` binding with topology constraints can bind to the wrong zone and fail to schedule; storage classes with incompatible CSI parameters provision volumes that mount with the wrong filesystem or permissions.
- Tradeoffs: dynamic provisioning is convenient but hides backend reality — engineers must understand what each class actually maps to, including snapshot support, backup hooks, and pricing. Over-abstraction leads to "storage doesn't work" incidents that are really class-misconfiguration incidents.
- RSIS3/mykb relevance: for loops that persist state, class choice is a durability and cost decision; this node keeps the mapping rules retrievable so retrievals attach the right failure modes to the right class.

## Related
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]] — what classes provision
- [[wiki/infrastructure/stateful-workloads|Stateful Workloads]] — the consumers of storage
- [[wiki/infrastructure/containerization|Containerization]] — the platform storage plugs into
- [[wiki/devops-infra/kubernetes|Kubernetes]] — storage abstraction in the cluster
