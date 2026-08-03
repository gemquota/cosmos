---
type: "concept"
title: "NFV & MANO"
description: "Virtualizing network functions with management and orchestration"
tags: ["nfv", "mano", "orchestration", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# NFV & MANO

## Summary
NFV (network function virtualization) runs network functions — firewalls, load balancers, routers, telecom core functions — as software on commodity hardware, and MANO is the management and orchestration layer that operates them: deployment, scaling, lifecycle, and assurance. Together they answer the question "how do you run a carrier-grade network as software, and who keeps it running?"

## Details
- The NFV architectural model (ETSI NFV): the VNF (virtual network function) is the software function; the NFVI (NFV infrastructure) is the compute/storage/network fabric it runs on; and MANO sits above, managing both. MANO has three layers: the NFVO (orchestrator — end-to-end service lifecycle: instantiate, scale, terminate, chain VNFs into network services), the VNFM (VNF manager — per-function lifecycle and configuration), and the VIM (virtualized infrastructure manager — the compute/storage/network resource layer, in practice Kubernetes or OpenStack). The reference model is the vocabulary the whole field uses, even where products have collapsed the layers.
- The service-chaining idea is the operational heart: a network service is not one function but a chain — traffic passes through firewall → load balancer → NAT → WAN optimizer in sequence. MANO's job is to instantiate the chain, wire the traffic path through it (the VNF forwarding graph), and scale/repair each element independently. The chaining is where NFV meets SDN: the SDN controller programs the network to steer traffic through the chain, and the NFVO decides what the chain should be.
- The modern collapse: in cloud-native practice, VNFs are containers and MANO's roles are largely absorbed by Kubernetes — the VIM is the cluster, the VNFM is a Helm/operator, and the NFVO is the platform orchestration (or a telco-specific layer like OSM, ONAP, or commercial suites) on top. The tradeoff: the ETSI architecture was designed for carrier requirements (hardware-agnostic, multi-vendor, lifecycle-managed), and Kubernetes gives most of that with a far larger ecosystem — but telco-grade functions (vRAN with hard real-time requirements, deep packet inspection at line rate) still need the performance tooling (DPDK, SR-IOV) and the carrier-grade operations that pure Kubernetes does not provide out of the box.
- The failure modes: performance surprises (software data planes on shared hosts), orchestration sprawl (the management layer becomes more complex than the functions), and the vendor trap (MANO products that only orchestrate their own vendor's VNFs).
- For mykb: NFV & MANO connect the virtualization and networking clusters — the orchestration view of the network-function story, complementing the NFV node's function view.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
