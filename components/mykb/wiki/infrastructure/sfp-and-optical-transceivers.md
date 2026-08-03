---
type: "concept"
title: "SFP & Optical Transceivers"
description: "Hot-swappable modules that adapt switches to fiber or copper"
tags: ["sfp", "optics", "transceiver", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SFP & Optical Transceivers

## Summary
SFP and its higher-speed relatives (SFP+, SFP28, QSFP, QSFP-DD, OSFP) are hot-swappable modules that adapt switches, NICs, and routers to fiber or copper media. They package the speed, reach, and media decision into a small field-replaceable component, which is why datacenters stock spares rather than rip out line cards when optics fail.

## Details
- Mechanism: the module contains a laser and photodiode (optical) or a copper PHY, plus an EEPROM carrying identity, serial number, and digital optical monitoring (DOM) data. The host reads DOM telemetry — TX/RX power, temperature, and voltage — to detect degradation before hard failure.
- Variants and reach: SFP for 1G, SFP+ for 10G, SFP28 for 25G, QSFP28 for 100G (4x25), and QSFP-DD/OSFP for 400G (8x50). Optics are named by reach: SR for short multimode runs, LR for long single-mode runs, and ER/ZR for metro and longer spans, each with different power budgets.
- Concrete examples: a 40G QSFP+ to 4x10G SFP+ breakout cable fanning out to four servers, DAC cables for short rack-internal links where cost and power beat reach, and a 10G LR module crossing a building backbone on single-mode fiber.
- Failure modes: dirty or damaged fiber connectors (the leading cause of flapping links), laser aging that shows up as rising TX power or falling RX margin, counterfeit or vendor-locked modules rejected by the switch, DOM threshold alerts ignored until the link drops, and heat build-up in dense 400G ports.
- Tradeoffs: DAC and AOC cables cost less than optical modules but are fixed-length and heavier; optics give flexibility and reach at higher cost per port; single-mode fiber costs more up front but supports future speeds, while multimode is cheaper for short runs.
- RSIS3/mykb relevance: when self-improvement cycles tune the physical layer, this node reminds retrievals that the module and the fiber are separate failure domains and that DOM telemetry is the observability signal to track.

## Related
- [[wiki/infrastructure/optical-storage-tape|Optical Storage & Tape]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
