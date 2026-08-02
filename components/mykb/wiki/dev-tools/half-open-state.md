---
type: "concept"
title: "Half-Open State"
description: "The probe state a circuit breaker enters to test whether a dependency recovered"
tags: ["circuit-breaker", "resilience", "recovery", "states"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Half-Open State

## Summary
The half-open state lets a circuit breaker send a small probe of traffic to a recovering dependency. Success closes the circuit; failure reopens it. It is the recovery mechanism that keeps outages from being permanent.

## Details
- Limit probe concurrency to avoid overwhelming a just-recovered dependency.
- Base the close decision on a sample (one or a few probes), not on a flood of traffic.
- Log transitions between states — open-to-half-open-to-closed is the heartbeat of a recovery.
- mykb relevance: half-open probing fits agent health checks of model endpoints after failures.

## Related
- [[wiki/dev-tools/circuit-open-state|Circuit Open State]]
- [[wiki/software-engineering/circuit-breaker-libs|Circuit Breaker Libraries]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/devops-infra/health-endpoint-contracts|Health Endpoint Contracts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
