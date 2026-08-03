---
type: "concept"
title: "VXLAN Overlays"
description: "Encapsulating L2 frames in UDP for scalable overlay networks"
tags: ["vxlan", "overlay", "networking", "virtualization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# VXLAN Overlays

## Summary
VXLAN encapsulates Layer 2 Ethernet frames inside UDP over an existing IP network, extending a virtual L2 segment across racks, buildings, and clouds. It is the standard mechanism behind cloud virtual networks, container overlays, and network virtualization, giving each tenant or workload its own broadcast domain without touching the physical fabric.

## Details
- Mechanism: a 24-bit VXLAN Network Identifier (VNI, up to ~16 million segments) separates tenants; a VTEP (VXLAN tunnel endpoint) — a switch, hypervisor, or software router — encapsulates inner Ethernet frames in UDP (destination port 4789) with the outer IP header addressed to the remote VTEP. The inner MAC addresses are preserved, so the overlay looks like one big switch.
- Control plane: to avoid flooding, VTEPs learn remote MAC-to-VTEP mappings — historically via multicast/BUM flooding, today typically via an EVPN control plane that distributes MAC and IP routes over BGP, which scales and converges far better.
- Concrete examples: Kubernetes clusters where each node runs a VTEP and pods communicate through an overlay independent of the physical IP plan; a cloud VPC implemented as VXLAN segments inside the provider's fabric; and stretched L2 segments for VM migration between buildings (with the caveat that stretched failure domains inherit ARP/broadcast storms).
- Failure modes: MTU mismatch — the 50-byte VXLAN overhead on a 1500-byte network silently fragments or drops large frames; BUM flooding storms when the control plane is misconfigured; VTEP state drift after a VM migrates; and tunnel health issues that are invisible to tools that only see the physical network.
- Tradeoffs: overlays decouple the virtual network from the physical one (huge flexibility) at the cost of encapsulation overhead, another layer to debug, and a dependency on the underlay's health; performance depends on offload (NIC checksum/TSO offload) because software encapsulation burns CPU.
- Operational practice: set the underlay MTU to accommodate the header (typically 9000 or at least +50), monitor VTEP and tunnel counters, prefer EVPN control planes at scale, and always test jumbo frames end to end before rollout.
- RSIS3/mykb relevance: overlay-versus-underlay reasoning is the network analogue of separating logical from physical state in the knowledge store; this node keeps the encapsulation tradeoffs retrievable for multi-node deployments.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
