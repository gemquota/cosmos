---
type: "concept"
title: "Container Network Interfaces"
description: "How CNI plugins attach pods to networks and assign addresses"
tags: ["cni", "containers", "networking", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Container Network Interfaces

## Summary
The Container Network Interface (CNI) defines how Kubernetes and other container runtimes attach containers to a network: plugins allocate IPs, create virtual interfaces, and enforce policy. Each pod gets a network namespace with an interface, and CNI plugins — bridge, Calico, Cilium, Weave — implement the topology from flat L2 to full eBPF-backed L3 policy.

## Details
- Mechanism: the runtime calls the plugin with ADD/DEL commands and a JSON spec: allocate an IP (IPAM), create a veth pair between pod and host, connect to a bridge or overlay, and optionally attach policy. The pod's single interface is the base case; multi-homed setups need a meta-plugin like Multus.
- Concrete example: Cilium with an overlay — each pod gets an IP, traffic is encapsulated (VXLAN) or natively routed, and eBPF programs enforce NetworkPolicy without iptables; Calico uses BGP to route pod IPs without an overlay in cloud-native environments.
- Failure modes: IP exhaustion when IPAM leaks addresses from deleted pods; MTU mismatches where overlay headers reduce effective MTU, causing fragmentation and latency; plugin version skew between kubelet and plugin; a CNI outage taking down all pod networking — making upgrades cluster-wide, high-risk operations; duplicate IPs when a crashed node's leases expire slowly.
- Tradeoffs: overlay networks (VXLAN) are portable and need no cloud routing integration but add overhead and MTU constraints; direct routing (BGP, native) is faster but needs network integration; policy enforcement moves from iptables, which is slow at scale, to eBPF and IP sets.
- Operational notes: pin CNI versions, run vendor diagnostics (cilium status, calicoctl), monitor IPAM usage, and test network policy in staging.
- IPAM hygiene: confirm that address reservations are released on pod deletion — leaked leases are the leading cause of address exhaustion.
- RSIS3 relevance: if RSIS3's services (wiki daemon, dashboard) run on Kubernetes, understanding CNI explains where latency, MTU, and policy failures come from when retrieval or sync calls slow down.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/devops-infra/container-runtimes|Container Runtimes]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
