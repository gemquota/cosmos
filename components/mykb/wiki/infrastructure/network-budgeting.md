---
type: "concept"
title: "Network Budgeting"
description: "Planning capacity, growth, and cost for network infrastructure"
tags: ["networking", "budgeting", "capacity", "cost"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Network Budgeting

## Summary
Network budgeting is planning capacity, growth, and cost for the network: forecasting how much traffic the network must carry, when it will need to carry it, and what that costs — then turning the forecasts into procurement, sizing, and monitoring commitments. It is the network team's version of capacity planning, and it exists because the network is both mission-critical and expensive: under-budgeted, it fails at the worst moment; over-budgeted, it wastes capital on idle capacity.

## Details
- The capacity model: the network's demand is not one number but a distribution — baseline traffic plus peaks (business hours, batch windows, marketing events), plus growth (new services, more users, bigger payloads), plus headroom (failover: one path must carry the traffic of the failed path). The budgeting practice is to track utilization per link and per tier over time, project growth from trends (and from known future workloads — a new service that will add X Gbps), and size for the peak-with-failover case, not the average. The classic failure is budgeting for the mean: the network looks healthy at 40% average utilization and saturates during a peak that the average hid.
- The cost model has three components: capital (switches, optics, cabling, and their lifecycle — hardware is refreshed every 5-7 years), operating (power, cooling, and space per port — often the larger cost over the hardware's life), and cloud/metro/transit (bandwidth purchases, egress fees, circuit costs — recurring and often the least predictable). Budgeting reconciles the three: a 400G port costs more to buy but less per bit than four 100G ports, and a link's total cost of ownership includes the power and the rack space it consumes. Cloud egress is its own budget line — the "cost of bandwidth" node covers the pricing dynamics that make egress unpredictable.
- The monitoring loop closes the budget: actual utilization against forecast, with alarms when a link crosses its planning threshold (typically 60-70% of capacity — the point where a failover or a spike saturates). The budget is a living model, updated from the measurements; the failure mode is the static budget — a plan written once and never reconciled with the network's actual growth.
- The governance dimension: budget requests compete with other infrastructure spend, so the network team must justify capacity in the language of the business (what workload needs it, what failure it prevents), and the budget must reserve explicit headroom for the surprises that always come.
- For mykb: network budgeting connects observability (the measurement input), bandwidth costs, and topology design — the planning layer over the physical network.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]]
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]]
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]]
- [[wiki/infrastructure/network-policy|Network Policy]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
