---
type: "concept"
title: "Quines"
description: "Programs that output their own source code"
tags: ["quines", "self-reference", "theory", "programs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Quine_(computing)", "https://en.wikipedia.org/wiki/Fixed-point_combinator"]
---

# Quines

## Summary
A quine is a program that prints a copy of its own source, with no input. Quines are fixed points of the 'output source' computation and are constructible in every general-purpose language; they matter as the cleanest demonstration of self-reproduction in computation.

## Details
- **Construction** — the classic trick stores the source as a data string and prints it twice: once literally, once as code.
- **Theory** — quines connect to recursion and fixed-point combinators (Y combinator) and to Gödel's self-referential sentences.
- **Why relevant** — self-reproducing programs are the logical substrate of self-replicating agents and of self-improvement loops.
- **Safety note** — self-replication without bounds (quine chains, fork bombs) is a containment concern for agent code.
- **RSIS3 angle** — the triad's generators reproduce and extend the workspace structure each pass, a knowledge-graph 'quine' with checks.

## Related
- [[wiki/concepts/self-referential-code|Self-Referential Code]] — the general property
- [[wiki/concepts/self-referential-code|self-referential-code]] — the theoretical root
- [[wiki/concepts/self-replication-evals|Self-Replication Evals]] — agent replication checks
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — self-reproduction in action
- [[wiki/syntheses/containment-strategies|Containment Strategies]] — bounding replication
- [[wiki/concepts/recursion-guard|Recursion Guard]] — loop guard
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
