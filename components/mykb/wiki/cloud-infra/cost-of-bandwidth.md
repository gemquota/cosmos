---
type: "concept"
title: "Cost of Bandwidth"
description: "Egress pricing and how bandwidth shapes cloud architecture"
tags: ["bandwidth", "cost", "egress", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cost of Bandwidth

## Summary

Bandwidth costs are the hidden budget-buster of cloud: egress is priced per GB (often 5-10x ingress), inter-AZ traffic bills, and data transfer around services (NAT, load balancers) multiplies. Architecting for egress is a first-class cost control.

## Details
- Mechanism: providers charge egress from the cloud to the internet per GB (AWS ~$0.09/GB first tier, GCP similar, Azure ~$0.087), while ingress is typically free; inter-AZ and inter-region traffic bills per GB; NAT gateways and load balancers add per-GB processing fees; CDN egress is far cheaper than origin egress, and free tiers exist within regions.
- Concrete example: streaming 10TB/month from an origin instead of a CDN costs ~$900 vs ~$100-300 via CDN; a chatty API sending 100KB of redundant JSON per call bills silently at scale; putting a NAT gateway in the path of high-volume egress adds both per-GB and per-hour costs.
- Failure modes: ignoring egress in architecture reviews until the bill arrives; chatty protocols and uncompressed payloads inflating per-GB costs; cross-region replication of data that only needs to exist once; and free-tier confusion (same-region transfer is not free everywhere).
- Operational tradeoffs: cache at the edge, compress payloads, co-locate compute and data (same-region, same-AZ where possible), and choose providers by egress pricing for data-heavy workloads; the trade is vendor stickiness and capability differences. Instrument egress per route to catch spikes early.
- RSIS3/mykb relevance: the wiki's deployment would monitor egress per service; this note records the egress pricing rules so the loop's architecture proposals include bandwidth cost as a design constraint.
- Protocol efficiency: gzip/brotli and binary payloads cut egress linearly; a chatty JSON API is a bandwidth bill that compression and batching can halve without architecture changes.
- Egress budget: set per-service egress budgets and alert at 80%; the first sign of a bandwidth leak is a bill, unless the budget exists first.

## Related
- [[wiki/cloud-infra/bandwidth-vs-throughput|Bandwidth vs Throughput]]
- [[wiki/infrastructure/bandwidth-allocation|Bandwidth Allocation]]
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]]
