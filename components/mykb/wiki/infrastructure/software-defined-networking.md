---
type: "concept"
title: "Software-Defined Networking"
description: "Decoupling the control plane from the data plane with centralized controllers"
tags: ["sdn", "control-plane", "networking", "openflow"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Software-Defined Networking

## Summary
Software-defined networking (SDN) decouples the control plane — the logic that decides where traffic goes — from the data plane, the switches and routers that actually forward packets. A centralized controller computes policy and pushes forwarding rules down to devices, replacing per-box configuration with a programmatic, network-wide view.

## Details
- Mechanism: control and data planes are separated by a well-defined southbound interface, historically OpenFlow, which lets the controller install flow rules (match fields, actions, priorities) into switch forwarding tables. Applications consume a northbound API, so intent — "segment these tenants," "route around this link" — is expressed once instead of per device.
- Concrete examples: a controller that recomputes paths when a link fails and pre-installs failover entries; a campus network where a controller enforces per-user access policies across dozens of access switches; and cloud overlay fabrics where SDN controllers program VXLAN tunnels between virtual switches.
- Failure modes: controller loss can leave switches with stale rules or unable to install new flows; clustered controllers risk split-brain if partitioning is mishandled; flow-table capacity is finite, so a flood of new flows can overflow TCAM; and bugs in the centralized logic become network-wide incidents instead of box-local ones.
- Tradeoffs: SDN buys programmability, global visibility, and consistent policy at the price of a new control-plane dependency, higher operational skill requirements, and debugging complexity when data-plane behavior diverges from controller intent. Fail-open versus fail-closed behavior must be chosen deliberately for every critical path.
- Operational practice: run controllers as an odd-numbered cluster, monitor southbound session counts and flow-table utilization, test controller failover with network faults injected into production-like labs, and keep fallback forwarding rules for management and emergency traffic.
- RSIS3/mykb relevance: SDN's separation of decision-making from execution mirrors RSIS3's loop architecture, and this node keeps that structural analogy retrievable when the system reasons about its own control flow.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/devops-infra/grpc-and-protobuf-networking|gRPC & Protobuf Networking]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
