---
type: "concept"
title: "East-West vs North-South Traffic"
description: "Internal service traffic versus user-facing traffic"
tags: ["traffic", "east-west", "north-south", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# East-West vs North-South Traffic

## Summary
North-south traffic flows between users and the datacenter (in through the edge, out through the edge); east-west traffic flows between servers inside the datacenter (or between datacenters). The distinction drives network architecture: the two traffic classes have different volumes, different performance requirements, different security postures, and therefore different designs — and the modern datacenter's east-west dominance is why the network was redesigned.

## Details
- North-south is the classic picture of networking: a user's request enters through load balancers/firewalls at the edge, hits the application, and returns. Its characteristics: traffic passes through a small number of chokepoints (the edge), the security perimeter is well-defined (the firewall is the boundary), and volume is bounded by user demand. Design priorities: edge capacity, DDoS protection, and perimeter security. This is the model the traditional three-tier network (core/aggregation/access) was built around — traffic mostly stayed vertical.
- East-west traffic is service-to-service: an API call from a web frontend to an auth service, a query from an analytics job to a database, a replica sync between two instances. Its characteristics: it dwarfs north-south in volume in modern architectures (every request fans out into dozens of internal calls — the "thundering herd" of microservice traffic), it moves horizontally through the fabric, and it carries the system's most sensitive data (databases, caches, internal APIs). Design priorities: fabric capacity and low latency between any pair of nodes, and — the hard part — security, because the perimeter model does not see east-west traffic at all.
- The architectural consequence: east-west dominance killed the tree topology. The traditional three-tier network concentrated east-west traffic in the aggregation/core tiers and became the bottleneck; the response was the spine-and-leaf (Clos) fabric, where every leaf switch connects to every spine switch with equal-cost paths, so any server can reach any server with predictable latency and aggregated bandwidth. This is also why modern designs emphasize horizontal scaling of the fabric (add spines) and why microsegmentation exists — the east-west traffic that the perimeter cannot see needs per-workload isolation instead.
- Failure modes: east-west capacity under-provisioned (internal traffic saturates the fabric while the edge looks fine — the failure is invisible to edge monitoring), east-west traffic invisible to security tooling (an attacker moving laterally between services goes undetected because only north-south was monitored), and topology designs that route east-west traffic through the wrong tier.
- For mykb: the node connects traffic shaping, QoS, and mirroring to the architectural question of what the network is actually carrying — the volume split determines the design.

## Related
- [[wiki/infrastructure/traffic-shaping-and-qos|Traffic Shaping & QoS]]
- [[wiki/devops-infra/traffic-shifting-and-splitting|Traffic Shifting & Splitting]]
- [[wiki/infrastructure/north-star-metrics|North Star Metrics]]
- [[wiki/devops-infra/mirroring-and-shadow-traffic|Mirroring & Shadow Traffic]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
