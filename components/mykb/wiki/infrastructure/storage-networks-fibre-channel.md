---
type: "concept"
title: "Storage Networks: Fibre Channel"
description: "Dedicated FC fabrics for high-performance block storage"
tags: ["fibre-channel", "san", "storage", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Storage Networks: Fibre Channel

## Summary
Fibre Channel (FC) is a dedicated, lossless network fabric built for high-performance block storage, connecting servers to storage arrays through switches instead of sharing Ethernet with application traffic. It delivers deterministic latency and specialized storage services that general-purpose networks struggle to match, at the cost of separate cabling, hardware, and expertise.

## Details
- Mechanism: FC runs its own protocol stack — FC-0 through FC-4 — over optical or copper links, with the FC-4 layer carrying SCSI commands (FCP). Hosts attach through Host Bus Adapters (HBAs), and switches create a fabric where each device is identified by a World Wide Name (WWN).
- Zoning and LUN masking: fabric zoning restricts which initiators can see which targets at the switch level, while LUN masking controls which logical units a given host may access at the array level. Both are mandatory access controls: get them wrong and hosts see each other's disks.
- Concrete architecture: two redundant FC fabrics (A and B) with separate switches, dual-ported HBAs, and multipathing software on the host, so a switch, cable, or HBA failure does not interrupt I/O. This is the classic dual-fabric design behind enterprise SANs.
- Failure modes: zone misconfiguration exposing wrong LUNs, fabric segmentation when two switches disagree on domain IDs or parameters, CRC errors on marginal optics, flapping ports that trigger SCSI command timeouts, and multipath software split across an inconsistent zoning set.
- Tradeoffs: FC gives predictable latency, lossless delivery, and mature tools, but it is expensive, requires specialized staff, and is a separate network to monitor; FCoE and iSCSI reduce that footprint by reusing Ethernet, trading determinism for convenience.
- Operational practice: monitor fabric events, port login counts, and buffer credits; keep zoning documentation current; and test path failover regularly, because an untested multipath configuration is a failover you have not performed.
- RSIS3/mykb relevance: when self-improvement loops evaluate storage architectures, this node distinguishes the fabric's guarantees from the SCSI command semantics that run over it.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
