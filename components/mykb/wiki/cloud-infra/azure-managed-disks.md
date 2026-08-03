---
type: "concept"
title: "Azure Managed Disks"
description: "Managed SSD/HDD tiers and their redundancy options"
tags: ["azure", "disk", "managed-disks", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Azure Managed Disks

## Summary

Azure managed disks are the IaaS block-storage layer: provisioned SKUs (Standard HDD, Standard SSD, Premium SSD, Ultra) with per-disk IOPS/throughput ceilings and snapshots. Right-sizing means matching SKU and size to workload I/O, not guessing.

## Details
- Mechanism: each managed disk SKU has size-tiered IOPS and throughput (e.g. Premium P30 1TB = 5,000 IOPS / 200 MB/s); Ultra Disk decouples IOPS and throughput from size with per-disk provisioning; snapshots are incremental and can create new disks, region-restore, or cross-region replication. The VM's max IOPS and the disk's ceilings interact — the effective limit is the min, and restore drills should target the region class the recovery plan assumes.
- Concrete example: an OLTP database on a P50-sized Premium disk sized for 7,500 IOPS observed at peak; a scratch analytics store on Standard SSD; a low-I/O boot disk on Standard HDD to save cost; an Ultra disk only where Premium's fixed ratios waste money.
- Failure modes: sizing by capacity instead of I/O (a 32GB P10 can starve a 2,000-IOPS workload); disk-bursting exhaustion on B-series and burstable Premium; host caching misconfiguration (cache-heavy caching writes can corrupt databases — use none for data disks); and ignoring VM size limits so the instance caps the disk's promise.
- Operational tradeoffs: Premium SSD is the default for production data; Standard SSD for moderate I/O; HDD for boot/archive. Plan snapshots into the backup policy (they share storage and cost per GB), and use shared disks/Ultra only when cluster scenarios genuinely require them.
- RSIS3/mykb relevance: VM I/O telemetry is recorded per workload so the loop can right-size disks during scheduled reviews instead of carrying over-provisioned SKUs.
- Performance validation: benchmark the actual workload against the disk SKU's IOPS/throughput caps; a VM can be network- or disk-bound before its CPU is busy. Re-run the benchmark after any VM size change, since the effective ceiling is the intersection of both limits.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/azure-vnet-and-nsg|Azure VNet & NSGs]]
- [[wiki/cloud-infra/parameter-stores-aws-ssm-azure-keyvault-gcp-secretmanager|Cloud Parameter Stores]]
- [[wiki/infrastructure/azure-synapse|Azure Synapse]]
