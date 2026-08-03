---
type: "concept"
hub: true
title: "OSPF Protocols"
description: "Link-state routing inside an autonomous system with fast convergence"
tags: ["ospf", "routing", "igp", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc2328",
  "https://www.rfc-editor.org/rfc/rfc5340",
]
---

# OSPF Protocols

## Summary
OSPF is a link-state interior gateway protocol used inside autonomous systems and enterprise networks. Every router floods its link state so all routers compute the same shortest-path map. It is the common alternative to EIGRP and IS-IS in datacenter and campus networks.

## Details
- RFC 2328 defines OSPFv2 for IPv4; OSPFv3 (RFC 5340) adds IPv6 support.
- Link-state advertisements are flooded reliably; each router runs Dijkstra's algorithm on the resulting topology graph to build its routing table.
- Areas partition the network to limit flooding and computation, with area 0 as the backbone.
- Designated routers (DR/BDR) reduce adjacency chatter on broadcast segments such as Ethernet.
- Convergence is fast: link or neighbor failures trigger immediate recalculation rather than timer-based updates.
- OSPF contrast with BGP is instructive: link-state IGP inside the network versus path-vector policy routing between networks, both represented in this cluster.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.

## Related
- [[wiki/infrastructure/scsi-and-sas-protocols|SCSI & SAS Protocols]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]]
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]]
