---
type: "concept"
title: "Timeouts & Deadlines"
description: "Bounding operation duration to fail fast and stay responsive"
tags: ["timeouts", "deadlines", "resilience", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Timeouts & Deadlines

## Summary
Timeouts and deadlines bound how long an operation may take: a timeout limits a single operation, while a deadline bounds the whole chain of work (request plus its retries and downstream calls). Without them, a slow dependency makes every caller wait forever, and queueing amplifies the delay into an outage.

## Details
- Mechanism: timeouts are set per call (connection, read, total), per layer (client, proxy, service), and per context (gRPC deadlines propagate through the call graph); deadlines should be shorter than the caller's own timeout so failures surface at the boundary; jittered, bounded retries live inside the deadline budget.
- Concrete example: a service calls a downstream API with a 2s connect and 5s read timeout and a 10s total deadline; the caller above has a 12s timeout, so the failure propagates before the caller gives up; a gRPC deadline of 5s is passed to downstream calls, which cancel when it expires.
- Failure modes: no timeouts, so a hung dependency queues requests until memory or connections exhaust; timeouts longer than the caller's patience, so callers retry into a pile-up; timeouts so short they fail on legitimate slow responses; deadlines that do not propagate, so each hop restarts the clock and the chain never ends; timeouts that trigger retries without budget, multiplying load.
- Tradeoffs: tight timeouts protect capacity but cause premature failures and retry noise; loose timeouts preserve legitimate work but let slow dependencies tie up resources; the art is sizing from measured percentiles with headroom and making timeouts configurable per dependency.
- Operational notes: measure and monitor timeout-hit rates, size from p99 latency data, and centralize timeout policy.
- RSIS3 relevance: RSIS3's calls to the daemon and LLM providers need explicit timeouts and deadlines — a hung provider should cancel the loop step, not stall the whole loop.

## Related
- [[wiki/infrastructure/query-timeouts-and-concurrency-limits|Query Timeouts And Concurrency Limits]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
