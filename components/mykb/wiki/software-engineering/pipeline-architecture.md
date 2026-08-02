---
type: "concept"
title: "Pipeline Architecture"
description: "Processing data through a linear chain of stages"
tags: ["pipeline-architecture", "architecture", "design", "data-processing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pipeline Architecture

## Summary
Pipeline architecture processes data through ordered stages, each transforming input and passing output downstream. Unix pipes, ETL jobs, and compiler passes are pipelines; they are simple, testable, and parallelizable per stage.

## Details
- Stages are independent: each has an interface, and pipelines compose like functions.
- Backpressure and error handling per stage matter: a slow stage must signal upstream.
- Branching and merging (diamonds) complicate pipelines — prefer linear or explicit DAGs.
- mykb relevance: capture → parse → link → verify → publish is the mykb acquisition pipeline.

## Related
- [[wiki/software-engineering/chain-of-responsibility|Chain of Responsibility]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/software-engineering/event-driven-design|Event-Driven Design]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
