---
type: "concept"
title: "Colocation & Racks"
description: "Housing your servers in third-party datacenter cages and racks"
tags: ["colocation", "racks", "datacenter", "hosting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Colocation & Racks

## Summary
Colocation means housing your servers in a third-party datacenter: you own (or lease) the hardware, and the facility provides the physical environment — power, cooling, space, physical security, and connectivity. It sits between bare metal in your own building and renting cloud capacity: you keep control of the hardware and the operational model, while outsourcing the physical plant that makes hardware reliable.

## Details
- What the facility provides: conditioned power (utility feeds with UPS and generator backup — the A/B power paths), cooling (the datacenter's job is removing heat at the designed density), physical security (cages, badges, cameras, biometrics), and carrier connectivity (fiber from multiple providers into meet-me rooms). Your responsibility starts at the rack: the servers, their configuration, patching, monitoring, and every operational action — "remotely, if you're lucky" is the colo operator's life.
- The unit of purchase is the rack or cage, and the key technical spec is power density: how many kilowatts can the rack deliver, and does the cooling match? A rack spec of 5 kW per cabinet supports a handful of standard servers; AI/GPU workloads need 20–50+ kW per rack with liquid or high-density cooling, which changes both the facility choice and the physical design (how you distribute power, where heat goes). The practical failure mode is under-budgeting: a facility that cannot deliver the power density or the cooling the hardware needs turns into throttled, hot, unreliable gear.
- The tradeoffs vs cloud: colo gives predictable cost at high utilization (the hardware cost amortizes, the power bill is stable), data control (your hardware, your compliance surface), and low latency (your gear, your network). It costs in operations (you are the SRE team for hardware — failures, spares, remote hands), in agility (capacity changes mean buying and shipping hardware, not an API call), and in physical logistics (hardware failures need remote hands or travel). The typical path is cloud → colo once a workload's utilization is high and predictable.
- Failure modes: single-site risk (one facility is one blast radius — a power event, a network outage, or a facility bankruptcy affects everything), under-provisioned power/cooling, and the remote-hands trap (operations that require physical access become slow and expensive).
- For mykb: colocation connects to rack-and-stack layout, power and cooling, and the hosting decision tree that includes bare metal and cloud.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
