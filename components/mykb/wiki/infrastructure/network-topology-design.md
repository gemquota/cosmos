---
type: "concept"
title: "Network Topology Design"
description: "Structuring leaf-spine, rings, and tree designs for scale"
tags: ["topology", "design", "leaf-spine", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Topology Design

## Summary
Network topology design structures how switches and links connect: the classic tree (core/aggregation/access), the modern leaf-spine (Clos), and the specialized ring and mesh forms. The design choices — how many layers, how many paths, how much capacity where — determine the network's latency, bandwidth, resilience, and cost, and the modern datacenter's answer has converged on leaf-spine because of the east-west traffic pattern.

## Details
- The tree (three-tier) topology: access switches connect servers, aggregation switches connect access switches, core switches connect everything. It is simple and cheap, but it has two structural problems at scale: east-west traffic (server-to-server) traverses the aggregation and core tiers, so those tiers become the bottleneck as internal traffic grows; and the higher tiers are the failure domain — one core switch or link failure partitions large parts of the network. The tree is the legacy design; it survives in small and campus networks, not in modern datacenters.
- The leaf-spine (Clos) topology: every leaf switch connects to every spine switch, and servers connect to leaves. Every path is exactly two hops (leaf → spine → leaf), and with equal-cost multipath routing (ECMP), traffic load-balances across all spines — so bandwidth between any two leaves scales by adding spines, and a spine failure just reduces capacity by one path rather than partitioning the network. The design rules: leaves should be identical (uniform uplink count), spines should be redundant (at least 2, N+1 in practice), and the oversubscription ratio (leaf uplink capacity ÷ server-facing capacity) is the capacity knob — 1:1 for lossless fabrics, 2:1 to 4:1 for typical workloads. This is the design behind virtually every hyperscale and enterprise datacenter fabric.
- The specialized forms: rings (each node connects to two neighbors — cheap and simple, but a link failure splits the ring and hops grow with node count; used in WAN/metro and storage topologies like Fibre Channel), mesh (direct links where traffic warrants — the resilience benchmark), and the hub-spoke WAN pattern (regional sites to a core — the management and security chokepoint).
- The failure modes of topology design: oversubscription misjudged (the fabric's aggregate capacity looks fine; the actual traffic matrix saturates specific paths — the reason traffic matrices matter more than peak numbers), ECMP hash polarization (all flows hash to the same spine under poor hashing), and the upgrade trap: a topology that cannot grow without rewiring (fixed spine count, no room to add leaves).
- For mykb: topology design is the synthesis node of the networking cluster — it applies the ASIC, cabling, bonding, and traffic-pattern knowledge into one coherent design discipline.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/os-shell/filesystem-design|Filesystem Design]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
