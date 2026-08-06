---
type: "concept"
title: "Agent Bootstrapping"
description: "Starting with a minimal capable agent and growing it through its own operation"
tags: ["bootstrapping", "agents", "self-improvement", "scaffold"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Recursive_self-improvement", "https://arxiv.org/abs/2210.03629"]
---

# Agent Bootstrapping

## Summary
Agent bootstrapping grows a small, imperfect agent into a stronger one by letting it use its own experience, tools, and improvements — rather than waiting for a fully capable model. It is the practical, bounded version of seed AI, and scaffolds are its main vehicle.

## Details
- **Mechanism** — the agent records failures, adds tools, refines prompts and practices, and delegates subtasks, compounding capability.
- **Contrast with seed AI** — bootstrapping improves the scaffold and knowledge, not the model weights.
- **Risk management** — capability grows faster than verification if bootstrap steps are not gated.
- **Worked example** — a coding agent that writes helper scripts, caches solutions, and builds a personal knowledge base accelerates on repeated tasks.
- **RSIS3/mykb relevance** — acquisition passes are knowledge bootstrapping: each pass makes the graph dense enough for the next pass to go deeper.

- **Scaffold-first growth** — most bootstrapping happens at the scaffold level: prompts, tools, checklists, and memory get better even when the underlying model is frozen, so each improvement is verifiable per component.
- **Verification gates** — a new tool or practice only persists if it measurably helps on a held-out task set; ungated bootstrapping drifts capability without evidence.
- **Failure modes** — premature delegation, tool sprawl, and overfitting to past tasks all look like progress while compounding debt, so the bootstrapping loop needs the same hygiene as any codebase.
- **Measure the loop** — track time-to-task, tool success rate, and knowledge reuse across bootstrapping iterations; flat metrics mean the loop is adding machinery without compounding capability.
## Related
- [[wiki/concepts/seed-ai|Seed AI]] — the strong hypothesis
- [[wiki/agent-systems/scaffold-loops|Scaffold Loops]] — vehicle of bootstrapping
- [[wiki/concepts/bootstrap-problem|Bootstrap Problem]] — epistemic barrier
- [[wiki/decisions/self-hosting|Self-Hosting]] — infrastructure-level bootstrap
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — the loop being bootstrapped
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — evidence it works
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
