---
type: "concept"
title: "Dark Launches"
description: "Shipping a feature that runs invisibly behind the scenes before it is exposed"
tags: ["dark-launch", "feature-flags", "deployment", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dark Launches

## Summary
A dark launch deploys a feature in production where it executes — collecting data, exercising paths — without users seeing or being affected by it. When the evidence is good, the feature flips on for real users.

## Details
- Dark code must be side-effect-isolated: log its behavior, never let it affect responses.
- Compare dark results against the current implementation to validate correctness.
- Dark launches pair with feature flags: the flag keeps it hidden until the flip.
- mykb relevance: a dark link-checker could score existing links before it starts reporting.

## Related
- [[wiki/tooling/traffic-shadowing|Traffic Shadowing]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/tooling/traffic-shadowing|Dark Launches]]
- [[wiki/devops-infra/dark-launch-techniques|Dark Launch Techniques]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
