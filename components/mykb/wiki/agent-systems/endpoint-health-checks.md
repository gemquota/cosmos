---
type: "concept"
title: "Endpoint Health Checks"
description: "Monitoring API and model endpoints for availability and correctness"
tags: ["health-checks", "monitoring", "endpoints", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Endpoint Health Checks

## Summary
Endpoint health checks continuously probe API and model endpoints for availability and correctness, feeding routing and failover decisions. They matter because agents depend on external services, and a silent degradation is worse than an explicit failure. Health state is the signal that lets traffic move away from trouble before users notice. Health checks are only useful if they fail loudly and recover cleanly.

## Details
- **Definition** — a health check is a lightweight, repeated probe that verifies an endpoint is reachable, responsive, and returning sane results.
- **Probe types** — checks range from TCP pings and HTTP status probes to semantic checks that validate response shape or content.
- **Realism** — the best probes mirror real request patterns, including payloads and authentication, because synthetic probes can pass while real traffic fails.
- **Signal use** — health state drives provider-failover, model-fallback-chains, and routing weight adjustments in llm-gateway-and-routing.
- **Worked example** — a gateway checks an embedding endpoint every thirty seconds; after two consecutive timeouts it marks the endpoint unhealthy and routes traffic to a replica.
- **Failure modes** — flapping endpoints cause routing thrash, too-coarse checks miss subtle regressions, and check traffic itself can distort load.
- **Layers** — health checks complement model-monitoring and drift-detection, which catch behavioral degradation that liveness probes cannot.
- **Practical relevance** — health checks are the cheapest reliability investment an agent platform can make and a prerequisite for automatic failover.
- **Frequency** — check intervals should be fast enough to catch failures but light enough not to add load.
- **State transitions** — unhealthy and healthy transitions need debouncing to avoid flapping.
- **Readiness vs liveness** — liveness probes say the process is up; readiness probes say it can serve traffic.
- **Failure example** — a check that only pings TCP misses an endpoint returning server errors to every real request.

## Related
- [[wiki/agent-systems/provider-failover|Provider Failover]] — the failover logic health checks trigger
- [[wiki/ai-ml/model-monitoring|Model Monitoring]] — the metrics layer around health
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — where health state is consumed
- [[wiki/testing/drift-detection-for-models|Drift Detection for Models]] — catching behavioral drift
- [[wiki/agent-systems/exponential-backoff-llm|Exponential Backoff for LLMs]] — client retry behavior around outages
