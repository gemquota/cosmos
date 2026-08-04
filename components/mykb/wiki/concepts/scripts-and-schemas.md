---
type: "concept"
title: "Scripts and Schemas"
description: "Structured knowledge about sequences of events and typical situations"
tags: ["schemas", "scripts", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Scripts and Schemas

## Summary

Scripts and schemas are structured knowledge representations that organize expectations about typical situations and event sequences. A schema describes a situation's parts and relations; a script is a schema for a stereotyped sequence, like ordering at a restaurant. They matter because comprehension, memory, and inference all run on these structures, filling in what is implied but not stated.

## Details

- **Definition** — A schema is a generic knowledge structure for a situation; a script is a temporal schema specifying the expected order of events.
- **Role in comprehension** — Activated scripts let readers infer unstated steps: entering a restaurant implies ordering, eating, and paying.
- **Role in memory** — Recall is reconstructed from scripts; people remember script-consistent events and often misremember typical events that never happened.
- **Acquisition** — Scripts form through repeated, varied experience; they become more abstract and robust as examples accumulate.
- **Worked example** — A witness to a checkout interaction confidently reports a payment step that was skipped, because the shopping script filled the gap.
- **Common failure modes** — Scripts cause stereotype-driven errors when applied to atypical cases, and rigid schemas resist updating with new evidence.
- **Practical relevance** — UI flows, documentation, and agent expectations all encode scripts; mismatches between script and reality cause confusion and errors.
- **Variants** — Frames describe situation structure without temporal order; story grammars organize narrative sequences specifically.
- **Limits** — Scripts are culture- and context-specific; assuming universal scripts misleads both humans and systems.
- **Inference generation** — Schemas generate inferences automatically: hearing a restaurant scene implies a menu, a waiter, and payment without any being stated.
- **Scripts in systems** — Agents and automated workflows encode scripts as procedures; when reality deviates, both humans and systems must notice the deviation rather than force the script.
- **Worked example** — A customer service script assumes an order number exists; callers without one break the flow, so the script needs a branch for the missing slot.
- **Update** — Schemas update slowly and unevenly; salient exceptions modify them more than routine confirmations.

## Related

- [[wiki/memory/schema-theory|Schema Theory]] — the broader account
- [[wiki/concepts/frames-and-slots|Frames and Slots]] — situation structure
- [[wiki/concepts/event-segmentation|Event Segmentation]] — parsing event streams
- [[wiki/concepts/story-grammar|Story Grammar]] — narrative script structure
- [[wiki/concepts/episodic-memory|Episodic Memory]] — experience behind scripts
- [[wiki/concepts/semantic-memory|Semantic Memory]] — generalized knowledge
