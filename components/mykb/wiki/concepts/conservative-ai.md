---
type: "concept"
title: "Conservative AI"
description: "AI design that prioritizes safety and reversibility over speed of progress"
tags: ["conservative", "safety", "precaution", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/AI_alignment", "https://en.wikipedia.org/wiki/Precautionary_principle"]
---

# Conservative AI

## Summary
Conservative AI is a design stance that prefers cautious, reversible, well-understood changes over bold capability gains: slow deployment, strong verification, and low blast radius. It is the engineering translation of the precautionary principle into system design.

## Details
- **Design rules** — prefer incremental upgrades, keep kill switches, sandbox experiments, and gate risky capabilities.
- **Tension** — conservatism trades progress for safety; the trade is worth it when failure is irreversible.
- **Related concepts** — mild optimization, bounded agents, and containment strategies all instantiate parts of it.
- **Evidence base** — deployment safety studies and update-regression checks support conservative release practices.
- **RSIS3 relevance** — the triad's test-gated mutations and snapshot-before-change workflow are conservative-AI practices for a self-improving system.

## Related
- [[wiki/concepts/precautionary-principle|Precautionary Principle]] — the ethical root
- [[wiki/concepts/mild-optimization|Mild Optimization]] — objective-level restraint
- [[wiki/syntheses/gradual-deployment|Gradual Deployment]] — release-level restraint
- [[wiki/concepts/conservatism-research|Conservatism Research]] — open research questions
- [[wiki/syntheses/update-regression|Update Regression]] — the conservative concern
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — reversibility primitive
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
