---
type: "concept"
title: "Delay-Tolerant Networking"
description: "Protocols that survive long delays and frequent disconnection"
tags: ["dtn", "networking", "resilience", "space"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Delay-Tolerant Networking

## Summary
Delay-tolerant networking (DTN) is the protocol family for networks where the assumptions of the internet break down: end-to-end paths that do not exist, round-trip times of minutes to hours, and links that disconnect as a matter of course. It is the networking of space missions, deep-sea sensors, and any environment where "the network" is a store-and-forward chain rather than a connected fabric.

## Details
- The core problem with TCP/IP in challenged environments: TCP assumes an end-to-end path, measures timeouts in seconds, and treats disconnection as an error. When a Mars rover's link to Earth disappears for 20 minutes (occultation), TCP gives up and retransmits wastefully; when a sensor network's links only exist intermittently, there is no path at all for most of the time. DTN inverts the design: the network does not promise connectivity, it promises delivery — messages are stored at each hop until the next hop is available, then forwarded.
- The mechanism is store-and-forward with the bundle protocol: a DTN "bundle" is a message with custody and lifetime metadata, passed hop by hop. Each node stores bundles until a forwarding opportunity exists, accepts custody (taking responsibility for delivery), and retransmits on failure — so delivery is achieved across a chain of intermittently connected links, with each hop making progress toward the destination even when no end-to-end path ever exists. The Contact Graph Routing (CGR) layer plans forwarding using predicted contact windows (when will Mars be visible?), treating the schedule of connectivity as the routing input.
- The design choices trade latency and storage against resilience: DTN nodes must be able to buffer arbitrarily long (a bundle can wait hours for a contact), so storage sizing is a first-class design problem; custody transfer creates delivery guarantees but requires retransmission state; and the protocol gives up TCP's congestion feedback entirely, so flow control is replaced by careful scheduling of what is sent in each contact window.
- Failure modes: buffer exhaustion (bundles accumulate faster than contacts drain them), custody loss (a node holding custody dies), and routing tables based on contact predictions that turn out wrong (a contact missed means bundles wait for the next window).
- For mykb: DTN is the extreme case that clarifies the internet's assumptions — the sibling networking nodes (fundamentals, VLANs, SDN) all assume the connected, low-delay regime DTN abandons, and the contrast is the lesson.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
