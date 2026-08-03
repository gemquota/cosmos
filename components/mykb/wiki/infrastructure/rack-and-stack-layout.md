---
type: "concept"
title: "Rack & Stack Layout"
description: "Physical arrangement of servers, switches, and cabling in racks"
tags: ["rack", "cabling", "datacenter", "hardware"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Rack & Stack Layout

## Summary
Rack and stack layout is the physical arrangement of servers, switches, and cabling inside racks: where each component sits, how power is fed, how cabling runs, and how airflow flows. It looks like housekeeping and behaves like architecture — a bad layout costs capacity (power and cooling mismatches), reliability (cable failures, hot spots), and operations (every change becomes a wrestling match), while a disciplined layout makes the rack a predictable, serviceable unit.

## Details
- The vertical arrangement: switches sit at the top (or middle) of the rack — top-of-rack (ToR) is the modern standard, putting the switch close to the servers' NICs with short cable runs — and servers fill the rest, with power distribution (PDUs) on the sides and cable management between units. The layout rules: balance the power draw across the rack's feeds (a rack with all high-power servers on one PDU trips it; spreading them keeps both feeds within limits), match server depth to the rack (a too-deep server blocks the rear cable tray), and leave serviceability space — a rack packed to the last U is a rack where nothing can be replaced without moving everything.
- The airflow design: front-to-back cooling means cold air enters the front, hot air exits the rear, and the rack's layout must preserve that path — blanking panels fill empty U-spaces (without them, hot air recirculates forward and the rack's cooling collapses), cable bundles avoid blocking the rear exhaust, and high-power gear (GPU servers, storage) is placed where the cooling can actually reach it. The failure mode is the hot spot: one rack region running 20°C above the rest because airflow was blocked by cabling or missing blanking panels — invisible until the servers throttle or fail.
- The cabling discipline: structured cabling — patch panels at the top, labeled cables, organized bundles, and lengths that reach — so the "rats nest" never forms. The rules: label every cable at both ends, use the correct cable type for the distance (DAC for short, fiber for long), and keep the cabling plan documented (a rack diagram that says where every cable goes). The failure mode of unstructured cabling: a cable fault becomes an archaeology project — every change risks pulling the wrong cable.
- The documentation loop: the rack's physical reality must match its records (rack diagrams, asset tags, power draws, cable maps); the failure is the undocumented change — a server moved, a cable re-routed, a PDU re-fed — that makes the diagram fiction, and every future decision based on it wrong.
- For mykb: rack and stack connects the physical layer — power/cooling (the rack's budgets), colocation (where racks live), and cabling standards (what runs between them).

## Related
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
