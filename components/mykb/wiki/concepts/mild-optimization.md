---
type: "concept"
title: "Mild Optimization"
description: "Restricting an optimizer's pursuit so it cannot drive the world to extremes"
tags: ["mild-optimization", "safety", "optimization", "bounded"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Instrumental_convergence", "https://en.wikipedia.org/wiki/AI_alignment"]
---

# Mild Optimization

## Summary
Mild optimization is the design stance that an AI should improve outcomes without optimizing them to the extreme, because extreme optimization of any proxy produces catastrophic side effects. Soares and Fallenstein's analysis treats mildness as a property of the objective design, not the optimizer.

## Details
- **Why extremes are bad** — aggressive optimization of a proxy (even a good one) invites Goodhart, wireheading, and world-model fragility.
- **Forms** — quantilization (randomize among top-actions), conservative satisficing, and bounded optimization.
- **Not the same as weakness** — a mild optimizer can be highly capable while refusing to chase the last unit of expected value.
- **Implementation** — indifference to small gains, flat utility plateaus, and explicit caps on impact.
- **RSIS3 link** — check-practices and scope discipline are mild-optimization for the knowledge loop: improve the wiki without overfitting any single metric.

## Related
- [[wiki/concepts/quantilizers|Quantilizers]] — formal mild optimizer
- [[wiki/concepts/conservatism-ai|Conservatism in AI Design]] — sibling stance
- [[wiki/agent-systems/satisficing-agents|Satisficing Agents]] — stop-at-good-enough
- [[wiki/concepts/impact-measures|Impact Measures]] — measuring world impact
- [[wiki/concepts/wireheading|Wireheading]] — the extreme to avoid
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — capacity bounds
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
