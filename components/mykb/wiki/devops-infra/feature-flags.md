---
type: "concept"
title: "Feature Flags"
description: "Runtime toggles that change behavior without redeploys, enabling gradual rollout and experimentation"
tags: ["feature-flags", "experimentation", "devops", "release-management"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/feature-toggles.html"]
---

# Feature Flags

## Summary
Feature flags (feature toggles) are conditional switches that alter system behavior at runtime without a code deploy. They enable trunk-based development, canary and percentage rollouts, instant kill-switches, and A/B experiments. Martin Fowler's taxonomy — release, experiment, ops, and permission toggles — clarifies their many uses.

## Details
- Types: release toggles (ship dark), experiment toggles (A/B), ops toggles (degrade gracefully), and permission toggles (per-user features).
- Implementation: a flag service (LaunchDarkly, Unleash) or local config with SDKs; decisions at the edge for consistency.
- Flag hygiene: toggles are technical debt — schedule removal, log evaluations, and archive stale flags.
- Risk control: start at 1% of traffic, watch [[wiki/devops-infra/observability|observability]] signals, and roll back by flipping a flag in seconds.
- Versioning interaction: flags decouple deploy from release, complementing [[wiki/api-protocols/api-versioning|API versioning]] for backend changes.
- Worked example: RSIS3's L3 strategy evolution could gate new prompt-spec series behind a flag, letting the pulse engine A/B old vs new prompts on live sessions.
- Relationship: flag evaluation belongs in logs/telemetry so experiments are attributable to outcomes.

## Related
- [[wiki/devops-infra/observability|Observability]] — measuring flag effects
- [[wiki/api-protocols/api-versioning|API Versioning]] — orthogonal change mechanisms
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI deploys code; flags release it
- [[wiki/api-protocols/rest-apis|REST APIs]] — flag endpoints return current state
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — experiment loops in the wiki daemon
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — curation workflow flags
- [[wiki/devops-infra/istio|Istio]] — weighted traffic routing for canary rollouts
- [[wiki/devops-infra/envoy|Envoy]] — proxy-level traffic splitting
