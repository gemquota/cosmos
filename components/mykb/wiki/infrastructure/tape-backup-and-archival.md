---
type: "concept"
title: "Tape Backup & Archival"
description: "Linear tape for long-term, low-cost retention"
tags: ["tape", "backup", "archival", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Tape Backup & Archival

## Summary
Linear tape remains the workhorse for long-term, low-cost retention: data written once and read rarely, where the cost per terabyte and the energy footprint beat spinning disk and cloud object storage at scale. Tape's economics are offset by its mechanics — sequential access and slow random seeks — which shape exactly which workloads belong on it.

## Details
- Mechanism: tape records data sequentially on removable cartridges (LTO generations, currently reaching 18 TB native per cartridge), read and written by tape drives in libraries with robotic pickers. Files are laid out in sequential streams, so restores are fast when reading a whole stream and slow for random single files.
- Use cases: backup archives and retention tiers (7-year compliance data), cold storage for media masters and datasets, air-gapped ransomware protection (offline cartridges cannot be encrypted in place), and disaster-recovery copies shipped offsite.
- Concrete example: the 3-2-1 backup rule — three copies, two media types, one offsite — is often implemented as primary disk plus a replicated tape copy stored in a vault, giving ransomware resilience because the tape copy is physically offline.
- Failure modes: media degradation and bit rot over decades (mitigated by checksums and periodic verification reads), drive head cleaning needs, robotics failures in libraries, tape read errors from handling damage, and restore speed surprises when a backup tool stored small files in a layout that requires many repositioning operations.
- Tradeoffs: tape is cheap per byte and very durable, but it needs specialized infrastructure (drives, libraries, management software), has slow random access, and cannot be scaled with a click — the operational cost is real even though the media cost is low.
- Operational practice: verify restores on a schedule, rotate media with generations, store a catalog that maps logical files to tape positions, and treat tape capacity as finite — monitor library slots as you would disk capacity.
- RSIS3/mykb relevance: for loops that decide what to persist and how long to keep it, tape is the canonical "cold tier" pattern; this node keeps the access-pattern tradeoffs retrievable so archival decisions are not made by price per GB alone.

## Related
- [[wiki/devops-infra/backup-strategies-3-2-1|Backup Strategies: 3-2-1]]
- [[wiki/devops-infra/backup-tools-restic-borg|Backup Tools: restic & Borg]]
- [[wiki/infrastructure/optical-storage-tape|Optical Storage & Tape]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
