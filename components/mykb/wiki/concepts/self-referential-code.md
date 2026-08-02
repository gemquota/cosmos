---
type: "concept"
title: "Self-Referential Code"
description: "Programs that refer to, reproduce, or modify themselves"
tags: ["self-reference", "code", "quines", "theory"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Quine_(computing)", "https://en.wikipedia.org/wiki/Self-modifying_code"]
---

# Self-Referential Code

## Summary
Self-referential code is program text that references or reproduces itself — quines (programs that print their own source), self-modifying code, and interpreters that interpret their own semantics. Self-reference is both a theoretical cornerstone (Gödel, fixed points) and an engineering property of self-improving systems.

## Details
- **Quines** — fixed points of the 'print source' function; they demonstrate that self-reproduction is expressible in any general language.
- **Self-modification** — code that rewrites its own instructions at runtime (JIT compilers, kernels, agent scaffolds).
- **Metacircularity** — interpreters written in the language they interpret create a self-referential tower.
- **Safety relevance** — self-reference enables both self-improvement and self-deception; tools must distinguish data from code.
- **RSIS3 relevance** — the practices checker inspects the workspace that contains its own rules — a mild self-referential loop with external enforcement.

## Related
- [[wiki/concepts/quines|Quines]] — self-reproduction
- [[wiki/concepts/metacircular-evaluators|Metacircular Evaluators]] — self-interpretation
- [[wiki/concepts/self-modifying-systems|Self-Modifying Systems]] — self-modification
- [[wiki/decisions/self-hosting|Self-Hosting]] — self-building
- [[wiki/decisions/kernel-rewriting|Kernel Rewriting]] — runtime self-rewrite
- [[wiki/concepts/recursion-guard|Recursion Guard]] — controlling recursion
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
