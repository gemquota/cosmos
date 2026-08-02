---
type: "concept"
title: "Metacircular Evaluators"
description: "Interpreters that interpret the language they are written in"
tags: ["metacircular", "interpreters", "lisp", "self-reference"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Meta-circular_evaluator", "https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs"]
---

# Metacircular Evaluators

## Summary
A metacircular evaluator is an interpreter written in the language it interprets — most famously the Lisp evaluator 'eval' defined in Lisp, canonicalized in SICP. It shows that a language's semantics can be described in itself, a foundational trick for bootstrapping and self-improvement.

## Details
- **SICP classic** — chapter 4 builds 'eval'/'apply' in Scheme, exposing the interpreter's own structure.
- **Why it matters** — metacircularity proves semantic self-description is possible and makes a language its own meta-language.
- **Engineering use** — language hosts (like Python's Python, or Rust's rustc) use the pattern for tooling and bootstrapping.
- **Safety angle** — a metacircular system can reason about and modify its own semantics; that power needs external checks.
- **RSIS3 relevance** — the wiki describes its own acquisition workflow in wiki files (a metacircular documentation loop).

## Related
- [[wiki/concepts/self-referential-code|Self-Referential Code]] — the property
- [[wiki/decisions/bootstrapping-compilers|Bootstrapping Compilers]] — engineering application
- [[wiki/decisions/self-improving-compilers|Self-Improving Compilers]] — improving the self-interpreter
- [[wiki/concepts/quines|Quines]] — the reproduction cousin
- [[wiki/decisions/kernel-rewriting|Kernel Rewriting]] — system-level self-description
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — self-describing knowledge system
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
