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
- Regulatory and data-residency constraints may push processing to specific edges or away from them; a residency map should be part of the edge rollout so a region change cannot silently move data into a new compliance class.
- Cache invalidation is the failure point: an edge that serves stale assets after a deploy erodes trust, so purge-on-deploy, short TTLs for mutable paths, and a canary that verifies edge freshness after release are the minimum practice.
- For the mykb bundle, the edge would serve the static wiki and run lightweight link-preview logic; curation would stay centralized.

Worked example — the wiki's edge cache would serve immutable article hashes from 300 locations; a worker would rewrite a banner and handle A/B headers, while writes would still go to the central store.
- Failure modes: edge state that diverges from origin (a counter incremented at the edge and never reconciled); edge functions with unbounded runtime or external calls that blow latency budgets; purge failures leaving stale content live; and edges selected purely by geography while ignoring cost per request and egress fees.
- Observability: an edge deployment needs request logs and cache-hit ratios per PoP, error rates per worker version, and a rollback path that flips traffic back to origin or the previous build in minutes, not hours.

## Related
- [[wiki/tooling/cdn-practice|CDN Practice]]
- [[wiki/tooling/serverless-architecture|Serverless Architecture]]
- [[wiki/tooling/cache-control-headers|Cache-Control Headers]]
- [[wiki/cloud-infra/edge-computing|Edge Computing]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/tooling/etag-negotiation|ETag Negotiation]]
- [[wiki/cloud-infra/cdns-and-edge-networking|CDNs & Edge Networking]]
