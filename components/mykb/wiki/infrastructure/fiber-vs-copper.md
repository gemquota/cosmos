---
type: "concept"
title: "Fiber vs Copper"
description: "Choosing between optical and copper links for reach and speed"
tags: ["fiber", "copper", "networking", "cabling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fiber vs Copper

## Summary
Fiber vs copper is the physical-layer choice for network links: electrical signals over twisted-pair copper, or light over glass optical fiber. The decision is driven by reach, speed, cost, and environment — copper dominates the last meters (desktops, racks, short interconnects), while fiber owns every distance beyond a few dozen meters and every speed beyond 10G in practice.

## Details
- The physics decides the division. Copper carries electrical signals that attenuate and pick up interference with distance; the practical ceiling is roughly 100 meters for twisted-pair Ethernet (the standard's limit), with speed inversely related to reach. Fiber carries light that attenuates far more slowly (kilometers for multimode, tens of kilometers for single-mode), is immune to electromagnetic interference, and has a bandwidth ceiling orders of magnitude higher — the reason every high-speed link beyond the rack is optical. The tradeoff is cost and handling: fiber transceivers are more expensive than copper PHYs, fiber is fragile (no sharp bends, careful termination), and fiber needs power-free but exacting connector hygiene (dust on a connector face is a real failure mode).
- The speed ladder: within the datacenter, copper holds the short-reach positions — 10GBASE-T over Cat6a/Cat7 (30-55m), and Direct Attach Copper (DAC) cables for top-of-rack to server links at 10/25/100G over 1-7 meters, where DAC's low cost and low latency make it the default. Beyond DAC range and beyond 100G, the medium is fiber: multimode (OM3/OM4/OM5) for 100-300m with VCSEL transceivers, single-mode for everything longer and all long-haul. The modern fabric rule of thumb: DAC for the shortest links, multimode fiber for intra-rack/row, single-mode for everything else.
- The physical plant implications: fiber cabling (panels, patch cords, polarity, cleaning) is a discipline — a dirty connector is the most common cause of mysterious optical link failures, and bend-radius violations cause latent attenuation that surfaces as intermittent errors. Copper has its own traps: cable-grade confusion (Cat5e vs Cat6 vs Cat6a matters at 10G), and alien crosstalk in dense bundles.
- The failure modes: exceeding the medium's reach (a 10G link over 60m of Cat6a is a reliability gamble), mixing multimode and single-mode components (transceivers and fibers must match), and environmental mismatch (fiber near vibration or sharp bends; copper near high-interference sources).
- For mykb: the node anchors the physical-layer cluster — cabling standards, transceivers, and network-topology design all build on the fiber-vs-copper choice.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
