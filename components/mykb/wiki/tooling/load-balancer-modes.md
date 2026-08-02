---
type: "concept"
title: "Load Balancer Modes"
description: "How load balancers pick a backend: round robin, least connections, IP hash, and more"
tags: ["load-balancing", "algorithms", "traffic", "modes"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Load Balancer Modes

## Summary
Load balancer modes are the backend-selection policies — round robin, least connections, least latency, IP/URL hash, weighted variants. The mode shapes distribution, stickiness, and resilience to slow or failing backends.

## Details
- Least connections suits long-lived requests; round robin suits uniform short requests.
- Hash modes enable sticky sessions and cache affinity but can skew under hot keys.
- Health checks remove dead backends from rotation; the mode picks among the healthy.
- mykb relevance: hash-based routing keeps a wiki request on the node with its cached index.

## Related
- [[wiki/devops-infra/load-balancing|Load Balancing]]
- [[wiki/devops-infra/load-balancing-l4-l7|Load Balancing L4-L7]]
- [[wiki/tooling/hot-key-cache|Hot Key Cache]]
- [[wiki/api-protocols/load-balancing|Load Balancing]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
