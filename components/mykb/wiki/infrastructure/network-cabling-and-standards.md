---
type: "concept"
title: "Network Cabling & Standards"
description: "Cat5e through Cat8, fiber grades, and structured cabling"
tags: ["ethernet", "cabling", "fiber", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Cabling & Standards

## Summary
Network cabling and standards is the physical-layer discipline: copper categories (Cat5e through Cat8), fiber grades (OM3/OM4/OM5 multimode, OS2 single-mode), connectors, and the structured-cabling rules that turn individual links into a maintainable plant. It matters because the physical layer is where reliability is won or lost — most "mysterious" network failures trace back to cabling that exceeded its standard's reach, was terminated badly, or was installed without the structured-cabling discipline.

## Details
- The copper ladder: Cat5e (1G to 100m), Cat6 (10G to 55m), Cat6a (10G to 100m — the datacenter workhorse for 10G), Cat7 (shielded, 10G to 100m, non-standard connectors), Cat8 (25/40G to 30m — short-reach data center links). The rules that matter: category is a bundle of electrical specs (crosstalk, attenuation, return loss), not a cable color; the installed performance depends on the whole channel (cable + connectors + patch panels + patch cords — a Cat6a channel with a Cat5e patch cord is a Cat5e channel); and reach is a spec, not a suggestion — a 10G link over 70m of Cat6 violates the standard and fails intermittently. The failure mode: "the link is fine most of the time" is the signature of marginal cabling — crosstalk and attenuation issues are intermittent, temperature-dependent, and invisible to switch health checks.
- The fiber grades: multimode (OM3 300m/10G, OM4 400m/10G and 150m/100G, OM5 wideband for SWDM) with VCSEL transceivers — the datacenter short-reach standard — and single-mode (OS2, kilometers at any speed) with longer-wavelength lasers, used for everything beyond multimode's reach and for the highest speeds. The rule: the transceiver and the fiber must match (a single-mode transceiver on multimode fiber fails, and vice versa), and the connector types (LC is the data-center standard; MPO for multi-fiber trunks) must match as well.
- Structured cabling: the discipline of permanent cabling organized in a hierarchy — horizontal runs from the rack to the work area, backbone runs between floors/rooms, and patch panels everywhere — so that moves, adds, and changes happen at the patch panel instead of re-cabling the building. The rules: cable labeling, bend-radius compliance, separation from power, and testing every run with a certifier (the test report is the contract that the run meets its category). The failure mode of unstructured cabling is the "spaghetti" state: an undocumented, unlabeled plant where every change is archaeology.
- For mykb: cabling is the physical foundation of the networking cluster — fiber-vs-copper, transceivers, and topology design all assume a standards-compliant plant.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/infrastructure/network-policy|Network Policy]]
