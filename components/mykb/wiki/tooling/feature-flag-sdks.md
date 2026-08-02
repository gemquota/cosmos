---
type: "concept"
title: "Feature Flag SDKs"
description: "Libraries and services for evaluating feature flags at runtime"
tags: ["feature-flags", "sdks", "tooling", "delivery"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Feature Flag SDKs

## Summary
Feature flag SDKs (LaunchDarkly, Unleash, Flagsmith, open-feature) evaluate flags in your app: server-side targeting, local evaluation, and SDK-level caching. They standardize how flags are read and who controls them.

## Details
- Local evaluation caches flag rules and avoids a network call per check.
- Standardize with OpenFeature for vendor portability.
- SDK defaults matter: what happens when the flag service is down?
- mykb relevance: flags gate new curation behaviors per worker without redeploys.

## Related
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/tooling/flag-debt|Flag Debt]]
- [[wiki/tooling/rollout-plans|Rollout Plans]]
- [[wiki/devops-infra/feature-flags|Feature Flags]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
