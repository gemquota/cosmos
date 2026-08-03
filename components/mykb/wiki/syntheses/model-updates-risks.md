---
type: "synthesis"
title: "Model Update Risks"
description: "Risks introduced when models are updated"
tags: ["model-updates", "risks", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Model Update Risks

## Summary
Model update risks arise when a new model version changes behavior in unexpected ways: regressions on previously working inputs, new failure modes, or policy drift where the model's decisions quietly diverge from the governing policy. Because a model update changes a distribution, not a binary flag, it needs pre-release evaluation and post-release monitoring — an update is a deployment of new behavior, not a patch.

## Details
- Model update risks arise when a new model version changes behavior in unexpected ways: regressions, new failure modes, or policy drift. A regression is a previously correct output that becomes wrong; a new failure mode is a class of input the old model handled that the new one mishandles (or a novel input class entirely); policy drift is the gradual change in how the model applies the rules it was given.
- Updates need pre-release evals and post-release monitoring. Pre-release: regression suites over known-good and known-bad examples, distribution comparisons on representative traffic, and adversarial probes for the failure classes the change targets. Post-release: canary deployment with metric comparison (accuracy, refusal rate, latency, error distribution) against the previous version, with the ability to revert.
- Concrete example: a chatbot's new model version improves open-ended answers but silently stops refusing a class of disallowed requests that the eval suite did not cover; a canary with per-category refusal-rate monitoring catches the drop before full rollout, and the deployment reverts while the gap is fixed.
- Rollback plans bound the damage of bad updates. Every update should carry a tested rollback: the previous version available, the ability to switch traffic instantly, and state compatibility handled (conversations, caches, and fine-tuned artifacts that assume one version).
- Failure modes: eval suites that only test improvements, so regressions ship silently; monitoring that compares averages, hiding degradation in a small but critical slice; updates shipped with no rollback because "the new version is better"; and drift that is invisible because no one tracks how decisions change over time.
- Tradeoffs: aggressive evaluation slows the update cadence and costs infrastructure; lax evaluation ships faster but externalizes the cost to incidents. The balance is risk-tiered — high-impact models get full pre-release batteries and canaries; low-impact internal models get lighter gates.
- RSIS3 relevance: pass updates to the graph carry the same risks — a changed embedding model or graph format can regress retrieval for old queries, so the same eval-before, monitor-after, rollback-available discipline applies to knowledge-layer updates.

## Related
- [[wiki/syntheses/update-regression|Update Regression]] — the failure
- [[wiki/syntheses/deployment-safety|Deployment Safety]] — the discipline
- [[wiki/syntheses/monitored-deployment|Monitored Deployment]] — the watch
- [[wiki/syntheses/fallback-plans|Fallback Plans]] — the safety net
- [[wiki/decisions/auto-update-mechanisms|Auto-Update Mechanisms]]
- [[wiki/devops-infra/patch-management-revisited|Patch Management Revisited]]
