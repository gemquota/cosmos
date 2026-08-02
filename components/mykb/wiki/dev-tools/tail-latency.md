---
type: "concept"
title: "Tail Latency"
description: "The slowest few percent of requests and the strategies that control them"
tags: ["latency", "performance", "distributed-systems", "tail-latency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tail Latency

## Summary
Tail latency is the delay experienced by the slowest requests — p99 and beyond. In distributed systems, a single slow backend makes many user requests slow because fan-out multiplies the worst case.

## Details
- Fan-out amplification: with 100 parallel calls, even 1% slow backends give nearly every request a slow leg.
- Hedged requests, short timeouts, and replicated work cut tail latency; so does reducing queue buildup.
- Long tails often come from garbage collection, noisy neighbors, or hot keys rather than average load.
- mykb relevance: multi-agent fan-out has the same tail problem — one slow model call delays the whole article.

## Related
- [[wiki/dev-tools/latency-percentiles|Latency Percentiles]]
- [[wiki/devops-infra/load-balancing|Load Balancing]]
- [[wiki/tooling/client-side-timeouts|Client-Side Timeouts]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/devops-infra/observability|Observability]]
