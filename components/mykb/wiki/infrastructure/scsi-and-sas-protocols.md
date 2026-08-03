---
type: "concept"
title: "SCSI & SAS Protocols"
description: "The command sets behind disks and enterprise storage"
tags: ["scsi", "sas", "storage", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SCSI & SAS Protocols

## Summary
SCSI is a command/response architecture that defines how hosts issue I/O to storage devices, and SAS is a serial, point-to-point transport that carries SCSI commands to enterprise disks and enclosures. Together they underpin most spinning disk and tape deployments, with SATA and NVMe sitting alongside for consumer and flash workloads.

## Details
- Mechanism: SCSI commands (INQUIRY, READ, WRITE, TEST UNIT READY) travel inside Command Descriptor Blocks (CDBs) over a transport — historically parallel SCSI, today SAS, iSCSI, or USB-attached SCSI. The SCSI Architecture Model (SAM) separates command semantics from the transport so the same command set works over many media.
- SAS specifics: point-to-point serial links at 12 Gbit/s per lane, expanders fan out to dozens of drives, and dual-port drives can attach to two controllers for path failover. SAS natively uses SCSI commands, so no translation layer is needed.
- SATA contrast: SATA disks speak ATA commands and are typically single-ported, cheaper, and lower-performing; HBAs and RAID controllers bridge ATA onto the SCSI world through translation.
- Failure modes: link CRC errors, command timeouts that trigger SCSI error recovery and device resets, reservations held by a dead initiator, and expander topology loops. Misconfigured multipath can double-issue writes when failover is not set to active/passive correctly.
- Tradeoffs: SAS drives cost more but offer dual-porting, better error handling, and longer service life; SATA wins on price. Choose by workload: streaming and archival data tolerate SATA, while transactional and shared storage favor SAS.
- Operational practice: dm-multipath over dual SAS ports, enclosure management (SES) for slot LEDs and power control, and predictable rebuild pacing to avoid RAID resync storms.
- RSIS3/mykb relevance: self-improvement cycles that tune storage subsystems need this node to distinguish command semantics from transport, avoiding confusion between SCSI-level errors and fabric-level problems.

## Related
- [[wiki/cloud-infra/http-protocols|HTTP Protocols]] — related coverage in the same cluster
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]] — related coverage in the same cluster
- [[wiki/cloud-infra/object-storage-protocols|Object Storage Protocols]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
