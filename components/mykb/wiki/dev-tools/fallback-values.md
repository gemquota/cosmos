---
type: "concept"
title: "Fallback Values"
description: "Safe defaults returned when a primary value or operation is unavailable"
tags: ["resilience", "fallbacks", "defaults", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fallback Values

## Summary
A fallback value is a safe, degraded answer used when the real one is unavailable — a cached copy, a default config, a stub response. Fallbacks keep systems usable during partial failures, as long as they are honest about staleness.

## Details
- Fallbacks must be visibly degraded: stamp results as fallback so callers and users know they are stale.
- Cache-as-fallback (serve last-known-good) beats failing when the primary store is down.
- A wrong silent fallback is worse than a loud error — choose defaults that cannot cause data corruption.
- mykb relevance: agent tool calls can fall back to cached summaries when the network or model is down.

## Related
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
- [[wiki/dev-tools/fail-safe|Fail-Safe]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
