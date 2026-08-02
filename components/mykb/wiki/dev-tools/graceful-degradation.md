---
type: "concept"
title: "Graceful Degradation"
description: "Continuing to serve a reduced but useful experience when parts of a system fail"
tags: ["resilience", "degradation", "availability", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Graceful Degradation

## Summary
Graceful degradation keeps a system usable when a dependency fails: search falls back to cached results, images drop to text, video lowers quality. The user gets less, but they still get something.

## Details
- Identify which features are critical and which can degrade; design the degraded mode before the outage.
- Communicate the degraded state in the UI so users are not misled by partial data.
- Progressive enhancement is the inverse pattern: build the degraded experience first, then enhance.
- mykb relevance: when a model provider fails, the agent can degrade to rule-based fallbacks for routine tasks.

## Related
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/dev-tools/fail-safe|Fail-Safe]]
- [[wiki/dev-tools/circuit-open-state|Circuit Open State]]
- [[wiki/devops-infra/health-endpoint-contracts|Health Endpoint Contracts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
