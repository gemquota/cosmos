---
type: "concept"
title: "Block Device Mapping on GCP"
description: "GCE disks, snapshots, and attachment semantics"
tags: ["gcp", "disk", "block-storage", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Block Device Mapping on GCP

## Summary

GCP block-device mapping connects persistent disks (PDs), local SSDs, and images to instances as /dev devices, with per-disk performance caps and a size-tied IOPS model. Getting the mapping right — which device name, which performance tier, which filesystem — is where GCP storage sharp edges live.

## Details
- Mechanism: persistent disks attach as /dev/disk/by-id/google-* names; each PD has IOPS/throughput tied to size and type (pd-standard, pd-balanced, pd-ssd, pd-extreme), and performance scales per GB up to caps; local SSDs are ephemeral NVMe attached at high IOPS with no persistence; snapshots and images are the backup/portability layer — database snapshot consistency needs a quiesced writer or flush-freeze.
- Concrete example: a database on pd-ssd sized so the GB-based IOPS covers peak (e.g. 8,000 IOPS needs ~1TB in the standard model); a cache tier on local SSD knowing data dies with the instance; a boot disk from a hardened image with pd-balanced for a small, moderate-I/O VM.
- Failure modes: expecting local SSD persistence (data loss on stop); sizing PDs purely for capacity when IOPS come from size (over-paying or starving I/O); device-name confusion when multiple disks attach (use by-id links, not /dev/sd*); and forgetting that live resize requires filesystem grow and possible reboot.
- Operational tradeoffs: PDs give durability and snapshots at a cost and IOPS ceiling; local SSD gives raw speed with ephemerality; pd-extreme (provisioned IOPS) is the escape hatch for high-I/O workloads. Match tier to access pattern and document the device-by-id mapping for automation.
- RSIS3/mykb relevance: experiment runners use a recorded disk recipe (type, size, device path, filesystem) so the loop's provisioning is reproducible and telemetry maps disks correctly.
- Device identity: mount and reference disks by the by-id/google-* names, never /dev/sd*; device letters change across reboots and attachment order. Use this mapping in fstab and systemd units so boot does not depend on discovery order.

## Related
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]]
- [[wiki/devops-infra/dependency-mapping-and-blast-radius|Dependency Mapping & Blast Radius]]
