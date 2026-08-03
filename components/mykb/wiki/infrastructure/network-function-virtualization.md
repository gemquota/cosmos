---
type: "concept"
title: "Network Function Virtualization"
description: "Running firewalls, load balancers, and routers as software instances"
tags: ["nfv", "virtualization", "networking", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Function Virtualization

## Summary
Network function virtualization (NFV) runs network functions — firewalls, load balancers, routers, NAT, WAN accelerators — as software instances on commodity servers instead of as dedicated hardware appliances. It is the virtualization movement applied to the middlebox market: the same NFV concept that made compute and storage software-defined, applied to the network functions that used to require a box per function.

## Details
- The problem NFV solves: the appliance model. Every network function historically meant dedicated hardware — a firewall appliance, a load-balancer box, a router chassis — each with its own procurement cycle, capacity ceiling, failure domain, and management interface. Scaling meant buying another box; upgrading meant hardware replacement; and the fleet of appliances was a sprawl of vendor-specific operations. NFV replaces the fleet with software: the functions run as VMs or containers on standard servers (or in the cloud), so they get the entire virtualization benefit — instant deployment, horizontal scaling, hardware independence, and one operational surface.
- The architecture: NFV separates the function (the VNF — virtual network function: firewall, LB, router) from the infrastructure (NFVI — the compute/storage/network it runs on) and adds MANO (management and orchestration — the layer that deploys, scales, and lifecycles VNFs, the NFV counterpart to Kubernetes). In practice, the distinction collapsed into the cloud-native world: modern VNFs are containerized workloads (or cloud functions) deployed by Kubernetes, and the "NFV" label now mostly refers to the telco heritage and the carrier-grade requirements (performance, availability, and the orchestration of virtualized telecom functions like vEPC, vIMS, vRAN).
- The performance question is the historical crux: network functions are packet-heavy, and software data planes historically could not match hardware appliances at line rate. The answer came from the same kernel-bypass and offload toolkits (DPDK, SR-IOV, SmartNICs): a virtual firewall can hit line rate if the data path bypasses the kernel and the NIC offloads the work — which is why NFV performance engineering is really the kernel-bypass/offload story. The tradeoff: software functions are cheaper and more flexible at the cost of CPU consumption and the need for careful data-plane design; hardware appliances win on raw per-box performance and lose on everything else.
- The failure modes: performance surprises (a VNF sharing a host with noisy neighbors), orchestration complexity (MANO/Kubernetes adds a control plane to learn and operate), and the licensing trap (vendors who priced appliances per-box are not automatically cheap as software).
- For mykb: NFV connects the virtualization and networking clusters — it is the application of cloud patterns (function execution lifecycle, network observability) to network functions.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/cloud-infra/function-execution-lifecycle|Function Execution Lifecycle]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
