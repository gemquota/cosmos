---
type: "entity"
title: "Cognitive"
description: "Cognitive: cognitive load and mental ergonomics in CLI and IDE tooling"
tags: ["entity", "ast", "bug", "cli", "edge", "ide", "cognitive-load"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Cognitive

## Summary

Cognitive, in this cluster, refers to how development tooling engages the user's mental resources: attention, working memory, and reasoning. CLI and IDE design either reduce or inflate cognitive load. It matters because tool friction is a direct tax on productivity and error rate. Tool design that respects these limits is what separates usable CLIs from scrapes through man pages.

## Details

- **Definition** — Cognitive load is the amount of mental effort a task demands; in tooling it comes from remembering commands, tracking state, and interpreting output.
- **Working memory** — Humans hold only a handful of items in working memory, so tools that expose needed context reduce errors and re-reading.
- **Context engineering** — Surfacing the right context at the right moment, rather than dumping everything, is the core principle of cognitive tool design.
- **Progressive disclosure** — Showing simple options by default and hiding advanced ones keeps beginners unblocked without crippling experts.
- **Feedback loops** — Short, clear feedback after every command lets users build accurate mental models of what the tool did.
- **Failure modes** — Deeply nested help, overloaded flags, and inconsistent naming force users to memorize rather than discover.
- **Worked example** — A CLI that prints the exact file and line for an error, plus the command that caused it, turns a confusing failure into an obvious fix.
- **Practical relevance** — Agents also face load limits: their context windows constrain what they can hold, mirroring human working-memory limits.
- **Consistency** — Predictable flags, naming, and output shapes let users transfer knowledge between tools instead of relearning.
- **Defaults** — Sensible defaults remove decisions; each required choice the tool imposes is cognitive load it adds.
- **Documentation** — Help text written at the point of need, with examples, beats reference manuals that sit outside the flow.

## Related

- [[wiki/development/categories/cli-tools/agentic-context-engineering|Agentic Context Engineering]] — context management for agents
- [[wiki/development/categories/cli-tools/dev|Dev]] — tooling being designed
- [[wiki/development/categories/cli-tools/intent|Intent]] — matching tool behavior to user intent
- [[wiki/development/categories/cli-tools/performance|Performance]] — speed as part of usability
- [[wiki/development/categories/cli-tools/senior-dev|Senior Dev]] — judgment under load
