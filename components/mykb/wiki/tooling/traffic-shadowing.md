---
type: "concept"
title: "Traffic Shadowing"
description: "Sending a copy of production traffic to a new version without affecting users"
tags: ["shadow-traffic", "testing", "deployment", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Traffic Shadowing

## Summary
Traffic shadowing mirrors real requests to a candidate version while the stable version answers users, so the new build is exercised with real traffic and compared. It validates behavior under production load before any user sees it.

## Details
- Shadowed responses are discarded or compared; never returned to users.
- Diffing shadow vs production responses catches behavior drift automatically.
- Shadowing costs double capacity — budget it, and isolate the shadow path's side effects.
- mykb relevance: shadow-run a new curation pipeline against live captures before switching.

## Related
- [[wiki/tooling/dark-launches|Dark Launches]]
- [[wiki/devops-infra/mirroring-and-shadow-traffic|Mirroring and Shadow Traffic]]
- [[wiki/tooling/canary-analysis|Canary Analysis]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
