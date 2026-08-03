---
type: "concept"
title: "Power & Cooling in the Datacenter"
description: "Feeding and cooling racks: PDU, UPS, and airflow design"
tags: ["power", "cooling", "datacenter", "facilities"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Power & Cooling in the Datacenter

## Summary
Power and cooling are the physical substrate of every datacenter: the power chain that feeds the racks (utility → UPS → PDU → PSU) and the cooling system that removes the heat the compute generates. Both are capacity-limited, failure-prone, and unforgiving — a power event or cooling failure takes down hardware in seconds, and their budgets (kilowatts per rack, airflow per kilowatt) are the physical constraints that all other infrastructure decisions must fit inside.

## Details
- The power chain: utility power enters the facility, a UPS (uninterruptible power supply) conditions and buffers it (batteries or flywheels covering the seconds-to-minutes gap until generators start), generators cover extended outages, and PDUs (power distribution units) distribute to the racks — typically with dual feeds (A and B) so that any single component's failure does not kill a rack. The redundancy levels are the famous Tier standards: Tier 1 (single path, no redundancy), Tier 2 (redundant components), Tier 3 (dual paths, one active — maintenance without downtime), Tier 4 (dual active paths, fault-tolerant). The rack-level budget is what the operator actually works with: the rack's rated kilowatts (5-10 kW standard, 20-50+ kW for GPU/HPC) are a contract with the facility, and exceeding them trips breakers or melts infrastructure.
- The cooling chain: servers reject heat to the room; the room's airflow (cold aisle/hot aisle containment — cold air in the front, hot air exhausted to the back, contained so they do not mix) carries it to CRAC/CRAH units; those reject it to chilled water or direct expansion refrigerant; the chiller rejects it to the outside. The design parameters: supply temperature, airflow per kilowatt, and containment discipline (open a containment door and the cooling efficiency collapses). Modern high-density designs add liquid cooling — direct-to-chip or immersion — because air cannot remove 40+ kW per rack without absurd airflow.
- The failure modes: a UPS in bypass (the battery path disabled for maintenance — and a power event during maintenance); generator failure at the moment of transfer (the reason generators are tested under load, not just started); cooling loss on a hot day (heat rises to thermal shutdown in minutes — the datacenter's version of a fire drill); and the silent one: power/cooling capacity that was never actually tested at the deployed density, discovered when the first high-density rack is installed.
- The operational practice: monitor power draw and temperature per rack (PDU metering, sensor arrays), track capacity against budget (a rack at 90% of rated power is a risk, not headroom), and test the failover paths (transfer to UPS, start generators, failover cooling) on a schedule — an untested failover path is a fantasy.
- For mykb: power and cooling anchor the facilities branch of the infrastructure cluster — thermal throttling (the server's reaction), colocation, and rack-and-stack all connect here.

## Related
- [[wiki/os-shell/thermal-throttling-and-power|Thermal Throttling & Power]]
