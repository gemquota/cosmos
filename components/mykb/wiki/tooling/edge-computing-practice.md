---
type: "concept"
title: "Edge Computing Practice"
description: "Running computation and caching close to users at the network edge"
tags: ["edge-computing", "cdn", "latency", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Edge_computing", "https://en.wikipedia.org/wiki/Cloud_computing"]
---

# Edge Computing Practice

## Summary
Edge computing moves computation and caching from central data centers to points of presence near users. Practice covers what belongs at the edge — caching, personalization, routing, and small stateless logic — versus what must stay centralized for consistency and cost.

## Details
- Edge work must be stateless or carefully replicated: state at the edge is a consistency problem.
- Edge functions (Cloudflare Workers, Lambda@Edge) are for fast, bounded logic — not databases or heavy compute.
- Cache correctness is the edge discipline: correct Cache-Control, versioned assets, and purge procedures.
- The edge is part of the system, not magic: it needs the same observability, testing, and rollback discipline.
- Regulatory and data-residency constraints may push processing to specific edges or away from them.
- For the mykb bundle, the edge serves the static wiki and runs lightweight link-preview logic; curation stays centralized.

Worked example — the wiki's edge cache serves immutable article hashes from 300 locations; a worker rewrites a banner and handles A/B headers, while writes still go to the central store.

## Related
- [[wiki/tooling/cdn-practice|CDN Practice]]
- [[wiki/tooling/serverless-architecture|Serverless Architecture]]
- [[wiki/tooling/cache-control-headers|Cache-Control Headers]]
- [[wiki/cloud-infra/edge-computing|Edge Computing]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/tooling/etag-negotiation|ETag Negotiation]]
- [[wiki/cloud-infra/cdns-and-edge-networking|CDNs & Edge Networking]]
