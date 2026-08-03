---
type: "concept"
title: "Network Simulation Tools"
description: "Simulating topologies and protocols before building them"
tags: ["simulation", "networking", "modeling", "tools"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Simulation Tools

## Summary
Network simulation tools model topologies and protocols in software before anything is built — the network's version of "test in production later, plan in the simulator now". A simulator lets you instantiate hundreds or thousands of nodes, define links with delay, loss, and bandwidth, run protocol implementations (or models of them), and observe the behavior — with full visibility and perfect reproducibility, at the cost of the models being models.

## Details
- The simulator spectrum: ns-3 is the academic/research standard — a discrete-event simulator with detailed models of TCP, routing (OSPF, BGP in extensions), WiFi, and 5G, scriptable in C++/Python, the tool for protocol research and paper-grade experiments. OMNeT++ is the component-based framework (INET model library) — strong for modeling complex protocol stacks and distributed algorithms. GNS3 and EVE-NG are the practitioners' tools — they run real network operating systems (Cisco IOS, Arista, Juniper images) as VMs/containers connected in emulated topologies, giving configuration-level fidelity (you configure them like real devices) without the hardware. And the cloud providers' network simulators/modelers (AWS's network reachability analyzer, GCP's topology simulations) analyze existing deployments rather than design new ones.
- The fidelity ladder: mathematical models (fast, scalable, approximate — a flow-level model cannot show TCP's behavior), discrete-event protocol models (detailed, slower — ns-3's TCP is a model of TCP, not Linux's TCP), emulation (real code, bounded scale — Mininet's hosts run real stacks), and testbeds (ground truth, expensive). The tool choice is a fidelity-vs-scale tradeoff, and the discipline is to know which layer each tool occupies — a configuration error found in GNS3 is a real configuration error, while a performance number from ns-3 is a model prediction.
- What simulation is for: validating topology designs (will this leaf-spine handle the traffic matrix?), testing protocol behavior under failure (what happens to convergence when a link dies — before it dies in production), teaching (students build and break networks safely), and automating experiments (a simulation harness that runs thousands of scenarios and reports the aggregate behavior).
- Failure modes: the simulator-is-not-the-network gap (the model's TCP, the model's radio channel, the model's queueing — each a place where reality diverges), simulation scale delusions (a 1000-node simulation runs on models, not on the behavior of 1000 real devices), and the config-drift trap: a topology validated in simulation that is not what was built, because the build process drifted from the design.
- For mykb: the node pairs with Mininet (emulation) — together they are the virtual testbed for the topology-design and protocol nodes.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/shell-environment/unix-text-processing-tools|Unix Text Processing Tools]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/cloud-infra/categories/aws-cloud/particle-simulation-2|Particle Simulation]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
