---
type: "concept"
title: "EVPN & BGP-EVPN"
description: "Using BGP to distribute MAC and IP reachability for VXLAN fabrics"
tags: ["evpn", "bgp", "vxlan", "fabric"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# EVPN & BGP-EVPN

## Summary
EVPN (Ethernet VPN) uses BGP as the control plane to distribute MAC and IP reachability across a VXLAN fabric, replacing the flood-and-learn behavior of traditional Ethernet with explicit, protocol-driven learning. It matters because it solves the scaling and stability problems of large layer-2 fabrics: every switch knows where every address lives, without flooding or MAC-table explosion.

## Details
- The problem it solves: traditional Ethernet learns MAC addresses by flooding — an unknown destination is flooded to every port until the switch learns the answer. In a large or heavily virtualized fabric, flooding wastes bandwidth and the MAC tables of edge switches bloat with addresses that live elsewhere. EVPN replaces flooding with advertisement: each VTEP (VXLAN tunnel endpoint) advertises the MAC and IP addresses learned on its local segment to all other VTEPs via BGP, and every switch builds a complete reachability map — traffic is forwarded directly to the right VTEP, and unknown unicast flooding largely disappears.
- The mechanics: BGP carries the reachability in new address families (the EVPN NLRI) over an MP-BGP session between the fabric's route reflectors or spines; the routes carry the MAC address, its IP, the VNI (VXLAN network identifier — the tenant/L2 segment), and the advertising VTEP. On receipt, each VTEP programs its VXLAN forwarding so that traffic for that MAC goes to the advertising VTEP's tunnel. Multi-homing (a host connected to two VTEPs), mobility (a VM moving between hosts), and ARP suppression (the fabric answers ARP from its control-plane knowledge instead of flooding ARP requests) all fall out of the control-plane model — which is why EVPN is the standard control plane for VXLAN fabrics.
- The operational gains: deterministic learning (no flooding surprises), fast convergence (BGP withdraws routes on failure instead of relying on MAC timeouts), scale (control-plane learning scales beyond what flooding can), and unified L2/L3 (EVPN can carry both MAC routes and IP prefixes, so the same protocol handles bridging and routing — EVPN-VXLAN with symmetric IRB).
- Failure modes: BGP session failures between the fabric and the route reflector (the fabric stops learning — hence redundant route reflectors), route churn from flapping hosts, and the classic misconfiguration class: VNI/route-target mismatches that silently isolate segments.
- For mykb: EVPN is the meeting point of the overlay cluster — VXLAN overlays, BGP, and SDN all converge on this control-plane design.

## Related
- [[wiki/cloud-infra/bgp-routing|BGP Routing]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
