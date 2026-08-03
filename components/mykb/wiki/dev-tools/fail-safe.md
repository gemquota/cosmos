---
type: "concept"
title: "Fail-Safe"
description: "Designing so that when something fails, the outcome is the safe option"
tags: ["fail-safe", "safety", "design", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fail-Safe

## Summary
A fail-safe system defaults to a safe state when it cannot determine the correct action: traffic lights go red, doors unlock, valves close. In software, fail-safe means denying by default when verification is impossible — the default action is chosen for safety, not for convenience.

## Details
- Mechanism: each guard defines its failure default explicitly — access denied when the identity provider is unreachable, writes rejected when quorum is lost, links flagged when they cannot be verified; the default is chosen per domain by asking what an outage should do.
- Concrete example: a zero-trust proxy denies requests when policy cannot be evaluated; a write path refuses to proceed when the state lock is uncertain; the wiki link-checker marks an unverifiable source link as flagged rather than silently keeping it — fail-safe on correctness.
- Failure modes: fail-safe defaults that over-protect — a denial on every identity-provider blip takes down the service, so fail-safe needs graceful fallbacks where the safety stakes are low; defaults chosen without domain thought (deny for a system where availability is the safety property); operators unaware of the default, so an outage surprises everyone; fail-safe implemented inconsistently across guards, so behavior differs per component.
- Tradeoffs: fail-safe (deny by default) protects correctness and security at the cost of availability; fail-open keeps service flowing but risks incorrect or insecure results; the right default is a per-domain judgment — authentication and data-integrity checks fail-safe, read paths may fail-open to cached data.
- Operational notes: document the default action of every guard, test outage behavior, and make the failure mode visible to operators.
- RSIS3 relevance: link-checking should fail-safe — an unverifiable source link is flagged, not silently kept — the same default-to-safety RSIS3 wants for its guardrails.

- Verify fail-safe behavior in tests: inject the failure condition and assert the safe default actually engages, before an outage does it for you.
## Related
- [[wiki/dev-tools/fail-fast|Fail-Fast]]
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/security/zero-trust|Zero Trust]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]]
