---
type: "concept"
title: "iSCSI & SAN"
description: "Block storage delivered over IP networks"
tags: ["iscsi", "san", "block-storage", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc7143",
  "https://en.wikipedia.org/wiki/ISCSI",
]
---

# iSCSI & SAN

## Summary
iSCSI delivers block storage over IP networks, emulating a local SCSI disk for remote clients. It is the standard protocol for IP-based SANs. iSCSI makes shared block storage possible without specialized fibre-channel hardware.

## Details
- iSCSI encapsulates SCSI commands in TCP/IP packets, letting initiators (servers) address targets (storage arrays) as if they were local disks.
- RFC 7143 defines the iSCSI protocol, including login, session management, and error recovery.
- Multipathing and jumbo frames are common tuning levers for throughput and redundancy.
- CHAP and IPsec protect iSCSI sessions, since block traffic is sensitive and latency-sensitive.
- The Linux kernel ships an iSCSI initiator; cloud block storage and SAN arrays both present iSCSI or its successors.
- In mykb, iSCSI connects to SAN, block storage, and fibre-channel articles to map the shared-storage landscape and its protocol choices.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.
- Capacity and redundancy tradeoffs for this topic are covered in the datacenter redundancy and power articles.

## Related
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/infrastructure/vxlan-overlays|VXLAN Overlays]]
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]]
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]]
