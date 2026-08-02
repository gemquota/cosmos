---
type: "concept"
title: "Fail-Safe"
description: "Designing so that when something fails, the outcome is the safe option"
tags: ["fail-safe", "safety", "design", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fail-Safe

## Summary
A fail-safe system defaults to a safe state when it cannot determine the correct action: traffic lights go red, doors unlock, valves close. In software, fail-safe means denying by default when verification is impossible.

## Details
- Fail-safe defaults matter for security (deny access) and physical safety; choose the failure mode per domain.
- Contrast with fail-open: fail-open keeps service flowing but risks incorrect or insecure results.
- Document the default action of every guard so operators know what an outage will do.
- mykb relevance: link-checking should fail-safe — an unverifiable source link is flagged, not silently kept.

## Related
- [[wiki/dev-tools/fail-fast|Fail-Fast]]
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/security/zero-trust|Zero Trust]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]]
