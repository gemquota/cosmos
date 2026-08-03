---
type: "concept"
title: "Graceful Degradation"
description: "Continuing to serve a reduced but useful experience when parts of a system fail"
tags: ["resilience", "degradation", "availability", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Graceful Degradation

## Summary
Graceful degradation keeps a system usable when a dependency fails: search falls back to cached results, images drop to text, video lowers quality. The user gets less, but they still get something — the system fails in design, not in chaos.

## Details
- Mechanism: identify which features are critical and which can degrade; design the degraded mode before the outage — a fallback source, a reduced feature set, a static stub; communicate the degraded state in the UI so users are not misled by partial data; monitoring flags when the system is running degraded.
- Concrete example: a dashboard serves the last cached snapshot when the live API is down, labeled with its timestamp; an agent uses rule-based fallbacks for routine tasks when the model provider fails; a site drops to text-only when the image CDN is unreachable — each still serves its core purpose.
- Failure modes: degradation designed only at the feature level, missing shared dependencies (a DB outage degrades every feature at once); degraded states that hide errors from monitoring, so the outage persists silently; degraded output that is not clearly labeled, misleading users; degradation logic that is buggier than the happy path, failing when it is most needed.
- Tradeoffs: graceful degradation trades full functionality for continued availability, shifting the decision from binary up/down to a spectrum; the alternative — fail hard — is simpler and clearer but worse for users; progressive enhancement is the inverse pattern: build the degraded experience first, then enhance with capabilities.
- Operational notes: test the degraded modes, alert when they activate, and keep the fallback paths exercised.
- RSIS3 relevance: when a model provider fails, the agent can degrade to rule-based fallbacks for routine tasks — the design-in-advance discipline RSIS3 applies to every loop dependency.

## Practice
- Decide the degraded behavior per dependency tier so losing a non-critical dependency degrades less than losing a core one.
## Related
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/dev-tools/fail-safe|Fail-Safe]]
- [[wiki/dev-tools/circuit-open-state|Circuit Open State]]
- [[wiki/devops-infra/health-endpoint-contracts|Health Endpoint Contracts]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
