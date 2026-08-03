---
type: "concept"
title: "Multicast Networking"
description: "One-to-many delivery using group membership protocols like IGMP"
tags: ["multicast", "igmp", "networking", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Multicast Networking

## Summary

Multicast delivers one stream to many receivers efficiently — video distribution, financial market data, cluster membership (VXLAN, etcd-style discovery). Cloud platforms generally do not support multicast in VPCs, which forces architectures to emulate it (unicast fan-out, overlay multicast) or avoid it.

## Details
- Mechanism: senders send once to a group address (224.0.0.0/4, ff00::/8); routers replicate along a tree to subscribers (IGMP for host membership, PIM for routing). Efficiency is the payoff — one packet per link instead of per receiver; the cost is protocol complexity (group management, tree state, timing) and limited cloud support.
- Concrete example: a trading floor fans market data to hundreds of terminals with multicast at wire speed; a datacenter uses multicast for VM-to-VM discovery (VXLAN head-end replication is the unicast emulation); a video platform uses multicast only on campus networks and unicast/CDN elsewhere because the internet does not route multicast.
- Failure modes: cloud VPCs silently dropping multicast (design for unicast or overlay); IGMP snooping misconfigs on switches causing intermittent drops; group addresses colliding or leaking across tenants; and multicast storms from misconfigured sources saturating links.
- Operational tradeoffs: where multicast is unavailable (most cloud), replicate with unicast fan-out (list distribution, pub/sub brokers) and accept the bandwidth cost; overlay multicast (a broker or mesh) restores efficiency at latency and complexity cost. Choose based on group size and scale — small groups are cheaper with unicast.
- RSIS3/mykb relevance: the wiki's distributed-cache experiments document unicast fan-out designs, since cloud environments in this deployment do not support multicast.
- Broker alternative: where multicast is unavailable, a pub/sub broker with topic filtering replicates the fan-out pattern at predictable cost; choose it when group membership is dynamic.
- Group hygiene: document every multicast group address and its purpose; address collisions across applications are invisible until traffic mixes.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/devops-infra/grpc-and-protobuf-networking|gRPC & Protobuf Networking]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
