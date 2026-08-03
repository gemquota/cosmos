---
type: "concept"
title: "Amazon EBS Provisioning"
description: "EBS volume types, sizing, and IOPS provisioning"
tags: ["ebs", "aws", "block-storage", "provisioning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Amazon EBS Provisioning

## Summary

Amazon EBS provisioning is the discipline of choosing volume type, size, IOPS, and throughput to match a workload without overpaying or starving it. It is a capacity-planning exercise, not a storage purchase.

## Details
- Mechanism: EBS offers general-purpose gp3/gp2, provisioned IOPS io2/io1, throughput-optimized st1, and cold hdd sc1; each has independent IOPS and throughput ceilings, and gp3 lets you provision IOPS/throughput separately from size. IOPS matter for random small I/O (databases), throughput for sequential large I/O (logs, analytics).
- Concrete example: a PostgreSQL primary on io2 with 10,000 provisioned IOPS sized for peak write volume; a web app boot volume on gp3 with 3,000 IOPS baseline and 125 MB/s throughput; a data lake archive on sc1 where cold reads are acceptable. Right-sizing uses observed P99 IOPS and throughput, not instance type defaults.
- Failure modes: over-provisioning IOPS that burst patterns never use (cost); under-provisioning causing queueing and latency spikes at peak; choosing size as the IOPS lever on gp2 (every GB adds IOPS, inflating cost); and ignoring multi-attach, snapshot throughput, and instance EBS-optimization limits when sizing.
- Operational tradeoffs: gp3's decoupled IOPS is the default; io2 is for guaranteed, durable high IOPS; st1/sc1 only for sequential workloads. Snapshots are volume-level and count toward restore time and cost — keep snapshots on a lifecycle policy and test restore RTOs.
- RSIS3/mykb relevance: instance telemetry (queue depth, IOPS utilization) feeds the rack; this note records the sizing decision rules the loop uses when provisioning storage for experiments.
- Monitoring: track EBS metrics (VolumeQueueLength, VolumeRead/WriteBytes, BurstBalance) per volume; sustained queue length is the signal that IOPS are exhausted, not a failed disk. Base alarm thresholds on steady-state P99 rather than averages so queue buildup surfaces early.
- Cost review: compare gp3 with custom IOPS vs io2 at each workload's P99; most workloads can save 30-50% by moving from io1/io2 to tuned gp3. Multi-attach and fast snapshot restore change the sizing math for clustered databases and DR drills.

## Related
- [[wiki/cloud-infra/instance-store-vs-ebs|Instance Store vs EBS]]
