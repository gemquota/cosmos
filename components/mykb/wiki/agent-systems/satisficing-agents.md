---
type: "concept"
title: "Satisficing Agents"
description: "Agents that stop at 'good enough' rather than optimizing maximally"
tags: ["satisficing", "agents", "objectives", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Satisficing", "https://en.wikipedia.org/wiki/AI_alignment"]
---

# Satisficing Agents

## Summary
A satisficing agent accepts any outcome meeting an adequacy threshold instead of seeking the optimum. Simon's concept, imported into AI safety, reduces the pressure that drives reward hacking and extreme side effects, because there is no gradient pushing past 'good enough'.

## Details
- **Definition** — choose the first action whose expected value clears an aspiration level.
- **Safety rationale** — maximal optimization of a proxy invites Goodhart; satisficing keeps the optimizer off the proxy's edges.
- **Efficiency** — satisficing saves search cost; it is how humans decide under time pressure.
- **Design question** — who sets the threshold, and how does it adapt without becoming a target?
- **RSIS3 parallel** — check-practices enforces adequacy (practices pass), not maximal metric scores, in the workspace loop.

## Related
- [[wiki/concepts/satisficing|Satisficing]] — existing concept
- [[wiki/concepts/mild-optimization|Mild Optimization]] — restraint family
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — resource-side restraint
- [[wiki/concepts/goal-specification|Goal Specification]] — thresholds are specs
- [[wiki/concepts/satisficing-research|Satisficing Research]] — open questions
- [[wiki/concepts/bounded-rationality|Bounded Rationality]] — decision theory root
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
