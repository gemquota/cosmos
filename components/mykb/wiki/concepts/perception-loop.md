---
type: "concept"
title: "Perception Loop"
description: "Feeding raw observations into an agent's state before reasoning and action"
tags: ["perception", "observation", "agents", "sensing"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Perception Loop

## Summary
The perception loop is the front end of the agent cycle: raw events and tool outputs are parsed, filtered, and turned into structured state that reasoning can use. It matters because garbage observations poison every downstream decision. It pairs with the agent loop's action side.

## Details
- Inputs can be tool stdout, errors, files, web pages, or user messages — each needs a parser and schema.
- Filtering and prioritization decide what reaches the model and what stays out.
- Open questions: how much raw signal to preserve, and how to handle ambiguous or conflicting observations.
- RSIS3 relevance: pulse observations feed the L1 loop and are logged for replay.

## Related

- [[wiki/agent-systems/agent-loop|Agent Loop]] — the cycle this loop feeds
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the pattern that consumes perceptions
- [[wiki/concepts/belief-states|Belief States]] — what perceptions update
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]] — deciding what to perceive
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — perceptions become wiki knowledge