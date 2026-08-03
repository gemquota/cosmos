---
type: "concept"
title: "Automated Rollbacks"
description: "Reverting releases automatically when health signals degrade"
tags: ["rollback", "deployment", "automation", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Automated Rollbacks

## Summary
Automated rollbacks revert a release to its previous known-good revision when health signals degrade after deploy. The trigger is a pre-agreed condition — error-rate threshold, latency budget, or repeated readiness failure over N seconds — evaluated during a rollout window, not a human watching a dashboard.

## Details
- Mechanism: progressive delivery tools (Argo Rollouts, Flagger) watch a canary or blue-green deployment; when metrics exceed the threshold, the controller aborts analysis and routes traffic back to the stable revision. On plain Kubernetes, a health-check loop or operator watches Deployment status and runs `kubectl rollout undo`.
- Concrete example: Flagger promotes a canary in steps (10/25/50/100% traffic) while querying Prometheus for error rate; three consecutive failed checks pause the rollout and revert automatically, marking the canary degraded. The GitOps equivalent is reverting the commit and letting the sync loop re-apply the old manifest.
- Failure modes: thresholds too tight cause flapping (roll out, roll back, roll out again); thresholds too loose let bad releases reach everyone. Rolling back a stateful release after a schema migration is not a pure image revert — code and data versions now mismatch, so pair automated rollback with forward-fix or reversible migrations.
- Tradeoffs: full automation removes human judgment — a traffic spike or downstream outage can look like a bad release and trigger mass rollbacks, so keep a manual override and an abort path. Rollback is also a re-deploy of an old artifact that can fail for new reasons (registry GC removed the old image, config has changed).
- Operational notes: define rollback as code (thresholds, windows, post-rollback verification), exercise the rollback path in game days, and log every automated action with the metric evidence that triggered it.
- RSIS3 relevance: RSIS3's L2 improvement loop is itself a rollout of new behaviors; automated rollback gives it the same safety — if a new strategy degrades pulse telemetry, revert to the previous parameter set instead of compounding the damage.

## Related
