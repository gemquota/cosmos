---
type: "concept"
title: "Self-Modifying Systems"
description: "Systems that alter their own code, weights, or structure during operation"
tags: ["self-modification", "RSI", "agent-systems", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Self-modifying_code", "https://en.wikipedia.org/wiki/Recursive_self-improvement"]
---

# Self-Modifying Systems

## Summary
A self-modifying system changes its own implementation while running: patching source, updating weights, or re-architecting components. It is the substrate on which recursive self-improvement happens, and it concentrates both capability gain and failure risk in one loop.

## Details
- **Kinds of modification** — parameter updates (training), architectural edits (neural architecture search), and code-level changes (self-hosting compilers, kernel rewriting) form a spectrum of invasiveness.
- **Why it matters** — each modification is a hypothesis about the system's own future; unverified hypotheses compound into drift.
- **Safety property** — modification should be gated by tests, rollback, and an immutable evaluator so a bad change cannot persist.
- **Worked example** — RSIS3's check-practices gate: no mutation is accepted unless all tests pass, and git rollback restores a prior self on failure.
- **Risk** — a system that can edit its own evaluator can wirehead its own reward; self-modification safety requires separating the evaluator from the optimizable substrate.

## Related
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — the loop self-modification enables
- [[wiki/concepts/self-modification-safety|Self-Modification Safety]] — safety constraints on edits
- [[wiki/decisions/versioning-of-selves|Versioning of Selves]] — tracking identity across edits
- [[wiki/decisions/kernel-rewriting|Kernel Rewriting]] — deepest-level code modification
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — rollback primitive that makes edits reversible
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — parent concept
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — measuring loop gains
