---
type: "decision"
title: "Self-Improving Compilers"
description: "Compilers that use their own output to optimize themselves"
tags: ["compilers", "self-improvement", "bootstrapping", "pl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Meta-circular_evaluator", "https://en.wikipedia.org/wiki/Bootstrapping_(compilers)"]
---

# Self-Improving Compilers

## Summary
A self-improving compiler is a compiler that can be rebuilt with itself and that uses its own generated code to find optimizations — a concrete, centuries-old lineage of recursive self-improvement. Metacircular evaluators and bootstrapping make the pattern formal.

## Details
- **Mechanism** — the compiler is written in its own language; improving the compiler improves every program it builds, including future versions of itself.
- **History** — early Lisp metacircular evaluators (SICP's 'eval' in 'eval') and bootstrapped C compilers (T-diagrams, self-hosting).
- **Why it matters** — it proves recursive self-improvement is real and safe when the improvement is verified by tests and differential compilation.
- **Modern forms** — autotuners and LLVM's self-optimization pipelines.
- **RSIS3 relevance** — the wiki's own pipeline (acquisition → synthesis → checks) is a self-improving 'compiler' for knowledge.

## Related
- [[wiki/concepts/metacircular-evaluators|Metacircular Evaluators]] — the formal ancestor
- [[wiki/decisions/bootstrapping-compilers|Bootstrapping Compilers]] — how the loop starts
- [[wiki/decisions/self-hosting|Self-Hosting]] — the property that enables it
- [[wiki/concepts/autotuning|Autotuning]] — runtime optimization loop
- [[wiki/decisions/kernel-rewriting|Kernel Rewriting]] — system-level sibling
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — loop framing
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
