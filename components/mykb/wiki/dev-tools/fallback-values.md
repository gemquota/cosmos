---
type: "concept"
title: "Fallback Values"
description: "Safe defaults returned when a primary value or operation is unavailable"
tags: ["resilience", "fallbacks", "defaults", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fallback Values

## Summary
A fallback value is a safe, degraded answer used when the real one is unavailable — a cached copy, a default config, a stub response. Fallbacks keep systems usable during partial failures, as long as they are honest about staleness and cannot cause corruption.

## Details
- Mechanism: the primary lookup is attempted; on failure or timeout, a fallback source is consulted (last-known-good cache, default config, static stub); the result is stamped as a fallback so callers and users know it may be stale; fallbacks are chosen to be safe under the failure conditions, never values that could corrupt state.
- Concrete example: a dashboard shows the last cached telemetry snapshot stamped with its timestamp when the live API fails; an agent tool call returns a cached summary when the model provider is down; a config loader uses a documented default when the remote store is unreachable — all visibly marked as degraded.
- Failure modes: silent fallbacks — users acting on stale data without knowing, making wrong decisions; fallback values that are wrong under the failure (a default config that assumes the failed system is up); fallback chains that mask the primary outage, so nobody fixes it; fallbacks that hide the error from monitoring, defeating alerting.
- Tradeoffs: fallbacks trade freshness and correctness for availability — the cached copy is better than nothing only if its staleness is visible and tolerable; the alternative, loud failure, is safer for correctness-critical paths; the mature pattern is fallback-plus-stamp, with the fallback path itself monitored.
- Operational notes: stamp fallback results, alert when fallbacks are serving, and size fallback caches for the outage duration.
- RSIS3 relevance: agent tool calls can fall back to cached summaries when the network or model is down — degraded but honest, exactly the tradeoff RSIS3 wants in its loops.

## Related
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
- [[wiki/dev-tools/fail-safe|Fail-Safe]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
