---
type: "concept"
title: "Feature Flag Systems"
description: "Runtime toggles that separate deploy from release"
tags: ["feature-flags", "releases", "experimentation", "deploy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Feature Flag Systems

## Summary
Feature flags decouple deployment from release: code ships behind a flag, and the flag decides who sees the feature. "Revisited" reflects current practice — flags are now full systems with SDKs, targeting rules, kill switches, and experimentation integration, not just boolean toggles in config files.

## Details
- Mechanism: the application calls a flag-evaluation SDK; the flag service (LaunchDarkly, Unleash, Flagsmith, OpenFeature) evaluates targeting rules — user segment, rollout percentage, environment — and streams updates so flag changes propagate without redeploys; kill switches reuse the same path for instant rollback.
- Concrete example: a new checkout flow ships behind `checkout-v2` at 5% rollout; support engineers escalate, and the flag is set to 0% instantly; after stability, it ramps to 100% and the dead code is removed in a later cleanup PR.
- Failure modes: flag sprawl — hundreds of stale flags accumulate, and code paths are never cleaned up (schedule flag TTLs and audits); SDK outages blocking flag evaluation can crash the app unless the SDK caches defaults and fails open; targeting rules that leak test flags into production traffic; flags that change behavior at runtime making incidents hard to reproduce — log flag state with requests.
- Tradeoffs: flags give instant release control and progressive delivery but add an external dependency and two code paths per feature; the maintenance cost is real — each flag is a branch in the codebase; the alternative (only deploy-gated releases) is simpler but turns every release into a high-risk event.
- Operational notes: treat flags as configuration with review and audit, remove flags on a schedule, test both flag states in CI, and ensure the kill switch path is exercised.
- RSIS3 relevance: RSIS3's experimental strategies are natural feature flags — evaluate a new L2 behavior for a fraction of tasks, compare telemetry, and kill-switch it if pulses degrade.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/os-shell/systemd-and-init-systems|systemd & Init Systems]]
- [[wiki/infrastructure/intrusion-detection-systems|Intrusion Detection Systems]]
- [[wiki/devops-infra/dotenv-vs-config-systems|dotenv vs Config Systems]]
