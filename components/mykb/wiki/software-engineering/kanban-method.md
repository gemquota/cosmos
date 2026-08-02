---
type: "concept"
title: "Kanban Method"
description: "The pull-based flow system of visual boards and work-in-progress limits"
tags: ["kanban", "flow", "wip-limits", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Kanban_(development)", "https://en.wikipedia.org/wiki/Lean_software_development"]
---

# Kanban Method

## Summary
Kanban is a pull-based method: work is visualized on a board, limited in progress (WIP limits), and pulled only when capacity frees up. It optimizes flow and lead time rather than sprint commitments, making it a natural fit for continuous, interrupt-driven work.

## Details
- Core practices: visualize work, limit WIP, manage flow, make policies explicit, and improve collaboratively.
- WIP limits are the engine: they surface bottlenecks, expose overload, and force finishing before starting.
- Kanban needs no fixed iterations or roles — it layers onto existing processes and changes them incrementally.
- Lead time and cycle time are the key metrics; cumulative flow diagrams show where work accumulates.
- It suits support queues, maintenance streams, and knowledge work where arrival is unpredictable.
- For the mykb bundle, curation flows through a Kanban lane — captured, verified, drafted, published — with a WIP cap on verification.

Worked example — the wiki curation board has columns Captured, Verified, Drafted, Published with WIP limits 5-3-3-0. When verification is full, no captures enter verification, so the bottleneck is visible and gets the next improvement.

## Related
- [[wiki/software-engineering/lean-software-development|Lean Software Development]]
- [[wiki/software-engineering/agile-methodology|Agile Methodology]]
- [[wiki/software-engineering/backlog-grooming|Backlog Grooming]]
- [[wiki/software-engineering/velocity-metrics|Velocity Metrics]]
- [[wiki/software-engineering/sprint-planning|Sprint Planning]]
- [[wiki/communities/standup-practices|Standup Practices]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
- [[wiki/tooling/load-shaping|Load Shaping]]
- [[wiki/software-engineering/agile-ceremonies|Agile Ceremonies]]
- [[wiki/software-engineering/developer-experience|Developer Experience]]
