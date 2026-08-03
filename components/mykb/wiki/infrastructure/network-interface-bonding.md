---
type: "concept"
title: "Network Interface Bonding"
description: "Combining multiple NICs into one logical interface for redundancy or throughput"
tags: ["nic", "bonding", "networking", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Interface Bonding

## Summary
Network interface bonding combines multiple physical NICs into one logical interface (bond0) for redundancy, throughput, or both. The server sees one interface with the aggregate's IP; the kernel distributes traffic across the member NICs according to a bonding mode, and a failed member is removed from service without breaking the logical interface. It is the host-level answer to "the NIC is a single point of failure" and "one NIC's bandwidth is not enough".

## Details
- The bonding modes, which decide everything: mode 1 (active-backup) — one NIC carries traffic, the others stand ready; on failure, the backup takes over in milliseconds (link detection via MII or ARP monitoring). Mode 4 (802.3ad/LACP) — all NICs carry traffic in parallel, negotiated with the switch via Link Aggregation Control Protocol, giving both throughput and redundancy; the switch must support LACP and the member links must land in the same aggregation group. Mode 0 (round-robin), mode 2 (xor), and mode 5/6 (adaptive transmit load balancing) spread traffic without LACP but with limitations (mode 0/2 require the switch to accept multiple links — usually meaning they act as separate paths, not one faster link, unless the switch aggregates them). The practical choice: LACP (mode 4) for everything the switch supports, active-backup (mode 1) for simple redundancy.
- The throughput math: LACP aggregation does not multiply per-connection throughput — a single TCP flow is pinned to one member NIC by the hashing (LACP hashes on L2/L3/L4 fields), so a server with 2x25G bonded has 50G aggregate but individual flows still get 25G. The benefit is aggregate capacity across many flows, plus redundancy. The common misunderstanding — "bonding makes my single transfer twice as fast" — is the classic disappointment, and the fix when per-flow speed matters is a faster single NIC, not a bond.
- The failure modes: mismatched LACP configuration (one side expects LACP, the other does not — the link flaps or fails), member links that land on different switches without proper stacking (the aggregation breaks), and the bonding monitor's blind spot (a NIC that is up but silently dropping traffic — MII detection misses it, which is why ARP monitoring exists).
- The modern context: in the virtualized world, bonding moved down a layer — the hypervisor bonds the physical NICs and VMs get virtual NICs on top; and in the cloud, the provider's virtual NIC (ENA, gVNIC) already provides multi-queue and redundancy, so host-level bonding is mostly a bare-metal/homelab pattern.
- For mykb: bonding is the host-level reliability link — it connects to network observability (what to watch on a bond), interface policy, and the physical cabling it aggregates.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/infrastructure/network-function-virtualization|Network Function Virtualization]]
- [[wiki/infrastructure/network-policy|Network Policy]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
