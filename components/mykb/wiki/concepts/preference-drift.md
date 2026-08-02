---
type: "concept"
title: "Preference Drift"
description: "Human preferences changing over time, complicating alignment"
tags: ["preference-drift", "alignment", "values", "temporal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1906.01820", "https://en.wikipedia.org/wiki/AI_alignment"]
---

# Preference Drift

## Summary
Preference drift is the change of human preferences over time — generational, contextual, or technology-induced. It complicates alignment because the target itself moves: aligning to today's preferences may misalign with tomorrow's, and preference-learning systems can chase a shifting signal.

## Details
- **Sources** — technology feedback loops (new capabilities create new preferences), context change, and learning effects.
- **Design question** — should AI extrapolate current preferences, adapt to future ones, or preserve a snapshot (value lock-in)?
- **Connection to CEV** — coherent extrapolated volition is an attempt to define the 'right' moving target.
- **Operational issue** — preference data decays; stale datasets train models aligned to the past.
- **RSIS3 relevance** — the wiki's practices are versioned and revised via passes, an explicit answer to preference drift in the workspace.

## Related
- [[wiki/concepts/value-drift|Value Drift]] — system-side analogue
- [[wiki/concepts/preference-updating|Preference Updating]] — the response mechanism
- [[wiki/concepts/coherent-extrapolated-volition|Coherent Extrapolated Volition]] — the extrapolation answer
- [[wiki/concepts/preference-elicitation|Preference Elicitation]] — the measurement being drifted
- [[wiki/decisions/versioning-of-selves|Versioning of Selves]] — versioned targets
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow: Open Threads]] — revision loop
- [[wiki/concepts/utility-functions|Utility Functions]] — objective structure in the existing graph
