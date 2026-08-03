---
type: "concept"
title: "Perception Loop"
description: "Feeding raw observations into an agent's state before reasoning and action"
tags: ["perception", "observation", "agents", "sensing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Perception", "https://en.wikipedia.org/wiki/Perceptual_control_theory"]
---

# Perception Loop

## Summary
The perception loop is the front end of the agent cycle: raw events and tool outputs are parsed, filtered, and turned into structured state that reasoning can use. It matters because garbage observations poison every downstream decision. It pairs with the agent loop's action side.

## Details
- Inputs can be tool stdout, errors, files, web pages, or user messages — each needs a parser and schema.
- Filtering and prioritization decide what reaches the model and what stays out.
- Open questions: how much raw signal to preserve, and how to handle ambiguous or conflicting observations.
- RSIS3 relevance: pulse observations would feed the L1 loop and be logged for replay.
- The perception loop is the cycle in which an agent senses the world, interprets the signal into a state estimate, and acts, with the action's consequences feeding the next sensing pass.
- It is the basic unit of situated intelligence: closed-loop behavior that continuously corrects based on new evidence, rather than open-loop execution of a fixed plan.
- The loop's quality depends on all three stages — a fast action on a bad interpretation is still a bad action.
- Predictive variants use the agent's own model to anticipate sensory feedback and update on the discrepancy, which sharpens both perception and action.
- **Worked example / comparison** — Worked example — an agent would watch the wiki health dashboard, interpret a spike in broken links as a link-fix trigger, run the fix, and re-scan to confirm the metric recovered.
- For mykb, the perception loop is the frame that ties RSIS3's sensing of its own state to the curation actions it takes.

- The loop closes when the action's consequences feed the next sensing pass, so behavior is continuously corrected rather than executed once against a fixed plan.
## Related
- [[wiki/agent-systems/agent-loop|Agent Loop]]
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]]
- [[wiki/concepts/belief-states|Belief States]]
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]]
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
