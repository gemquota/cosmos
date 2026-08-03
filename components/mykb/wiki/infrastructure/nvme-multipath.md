---
type: "concept"
title: "NVMe Multipath"
description: "Multiple paths to one NVMe namespace for failover and load"
tags: ["nvme", "multipath", "storage", "failover"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# NVMe Multipath

## Summary
NVMe multipath gives a host multiple physical paths to the same NVMe namespace — through multiple ports, controllers, or fabric connections — and uses them for both failover and load distribution. It is the NVMe-era replacement for the SCSI multipath pattern: a failed path must not mean lost storage, and with NVMe the multiple paths are not just redundancy but a performance feature, because I/O can be spread across them.

## Details
- The topology: an NVMe device (or a namespace on a shared NVMe-oF target) is reachable through multiple controllers — a local NVMe drive exposes multiple PCIe ports; an NVMe-over-Fabrics target exposes multiple controller addresses (TCP or RDMA endpoints). The host sees the same namespace through each path, and the multipath layer (Linux's nvme-multipath, device-mapper-based) presents them as one block device, distributing I/O across the paths and failing over on path loss.
- The mechanism: NVMe native multipath (the standard — ANA, Asymmetric Namespace Access) lets the storage system declare path states: a namespace accessed through multiple controllers can be "active/optimized" on some paths (the ones the host should use) and "active/non-optimized" or "inaccessible" on others. The host's multipath driver routes I/O to the optimized paths, keeps the others as failover, and re-evaluates when the target changes the states (e.g., a controller fails and the target marks the namespace non-optimized on the dead path, optimized on a live one). ANA turns multipath from a host-side hack into a first-class protocol feature — the target tells the host which path to use.
- The tradeoffs: multipath with active/active I/O distribution multiplies aggregate throughput (two 25G paths → up to 50G to one namespace) but the gains depend on the workload (single-queue sequential I/O may not parallelize across paths well); failover requires the fabric to be genuinely redundant (two paths through the same switch or the same NIC are not redundancy); and the complexity is real — path state, ANA transitions, and I/O retry behavior all need monitoring. The failure mode: a "redundant" setup where both paths share a single failure domain, discovered when the shared component fails.
- The operational practice: configure multipath with proper path policy (round-robin or queue-depth-based), monitor path states (nvme list, multipath -l), and test failover deliberately — a failover path that has never been exercised is a failover path that will fail when needed.
- For mykb: NVMe multipath is the reliability layer over the NVMe cluster — it connects NVMe & NVMe-oF, NVMe-oF TCP, and storage systems.

## Related
- [[wiki/infrastructure/nvme-and-nvme-of|NVMe & NVMe-oF]]
- [[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
