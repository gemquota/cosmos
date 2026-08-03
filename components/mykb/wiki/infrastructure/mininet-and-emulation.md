---
type: "concept"
title: "Mininet & Emulation"
description: "Emulating full network topologies on one host"
tags: ["mininet", "emulation", "networking", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Mininet & Emulation

## Summary
Mininet emulates complete network topologies — hosts, switches, links, and the protocols running on them — on a single machine, using Linux namespaces and virtual Ethernet pairs to create real network stacks that run real code. It matters because it turns network experimentation from "buy a lab" into "run a script": a researcher or student can instantiate a 100-node topology with custom delays and loss, run real routing daemons and applications on it, and tear it down — all in seconds.

## Details
- The mechanism: each emulated host is a Linux network namespace (its own network stack, interfaces, and routing table), connected by veth pairs to virtual switches — either the kernel's bridge or Open vSwitch (OVS), which supports OpenFlow, so SDN controllers can be tested against emulated switches. Links are emulated by traffic-control (tc) on the veth pairs: delay, loss, bandwidth, and queue disciplines applied per link, giving realistic-enough network behavior. Because the hosts run real Linux stacks and real applications, the emulation exercises the actual protocol implementations — not a model of them — which is the crucial difference from pure simulation.
- The position in the toolkit: emulation vs simulation vs testbeds. Simulators (ns-3, OMNeT++) model protocols mathematically — scalable to thousands of nodes, controllable, but the models can be wrong (a simulator's TCP is not Linux's TCP). Emulation (Mininet) runs real code on virtualized hosts — realism where it matters (application and protocol behavior) with the scalability ceiling of one machine (hundreds of hosts, limited link fidelity at high bandwidths). Testbeds (real hardware, cloud labs) are the ground truth but cost money and setup. The standard workflow uses all three: simulate for scale, emulate for realism, testbed for final validation.
- The sweet spots: teaching (SDN and networking courses run on Mininet), SDN/controller development (OpenFlow switches under test, controller logic against topologies), and protocol research (new congestion control, routing behavior under loss) — anything where the answer must be real code but the environment is not available or is too expensive.
- Failure modes: fidelity gaps — emulated links do not reproduce all hardware behavior (NIC interrupts, ASIC queueing, driver interactions), a single-host resource ceiling (CPU contention between emulated hosts distorts timing-sensitive experiments), and the emulation reality gap: a protocol that works in Mininet can still fail in production because the emulation hid hardware-specific behavior. The discipline: use emulation for logic, not for performance claims.
- For mykb: Mininet anchors the emulation cluster with network simulation tools — the two are the virtualized way to test what the topology-design nodes describe.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
