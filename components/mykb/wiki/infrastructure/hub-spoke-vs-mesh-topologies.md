---
type: "concept"
title: "Hub-Spoke vs Mesh Topologies"
description: "Centralized versus direct interconnects and their tradeoffs"
tags: ["topology", "hub-spoke", "mesh", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Hub-Spoke vs Mesh Topologies

## Summary
Hub-spoke and mesh are the two poles of interconnect design: hub-spoke routes all traffic through a central hub (or hierarchy of hubs), while mesh connects nodes directly (or through a full/partial fabric). The choice appears at every layer — network topology, service communication, cluster federation, and API integration — and the tradeoff is always the same: centralized control and simplicity versus direct paths and resilience.

## Details
- Hub-spoke: every node connects to a hub, and all inter-node traffic transits the hub. The wins: centralized control (policy, security, and monitoring all live in one place — the hub is the natural chokepoint for firewalls and inspection), simpler node configuration (each node needs one connection, not N), and easier management (the hub knows the whole picture). The costs: the hub is a bottleneck (all traffic through one point — capacity must be provisioned for the aggregate) and a single point of failure (hub down, everyone down), and every inter-node path pays an extra hop (latency and bandwidth tax). Hierarchical hub-spoke (spokes that are themselves hubs) scales the model and is how WAN/VPN designs typically work — regional hubs aggregating to a core.
- Mesh: nodes connect directly (full mesh: every node to every other — N² connections; partial mesh: direct links where traffic warrants, routing elsewhere). The wins: direct low-latency paths (no hub hop), resilience (no central chokepoint; failures degrade only the affected links), and bandwidth (parallel paths). The costs: N² scaling (full mesh does not scale past a handful of nodes), distributed management (policy must be enforced everywhere or via a control plane), and a harder security story (no natural chokepoint — hence microsegmentation and distributed policy). The network version of mesh is the Clos/spine-leaf fabric: a partial mesh with enough paths to behave like full connectivity at any scale.
- The decision framework: hub-spoke when control and simplicity dominate — small numbers of nodes, centralized policy needs, security inspection required — and mesh/fabric when traffic volume, latency, and resilience dominate — datacenter fabrics, microservice east-west traffic, distributed teams. The common pattern is hybrid: a mesh fabric for the high-volume east-west traffic plus hubs at the edges for north-south control.
- Failure modes: hub-spoke under-provisioned (the hub saturates and everyone slows — invisible until the traffic pattern changes), mesh with unmanaged N² growth (connection count explodes, operational complexity overwhelms), and the hybrid failure: control-plane policy applied inconsistently across mesh paths.
- For mykb: the topology question recurs across the wiki's networking and service clusters — this node is the general lens for hub-spoke/federation and mesh/service-mesh decisions.

## Related
- [[wiki/devops-infra/service-mesh-sidecars|Service Mesh Sidecars]]
- [[wiki/devops-infra/cluster-federation-vs-hub-spoke|Federation vs Hub-Spoke]]
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/infrastructure/service-mesh|Service Mesh]]
