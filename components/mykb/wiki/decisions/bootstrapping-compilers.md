---
type: "concept"
title: "Bootstrapping Compilers"
description: "Compilers that compile their own compiler"
tags: ["bootstrapping", "compilers", "self-hosting", "pl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bootstrapping_(compilers)", "https://en.wikipedia.org/wiki/T-diagram"]
---

# Bootstrapping Compilers

## Summary
Bootstrapping a compiler means building a compiler with the language it compiles, using a minimal seed (often a T-diagram: an interpreter or cross-compiler for a subset). It is how real language toolchains become self-hosting and how the recursive improvement cycle starts.

## Details
- **T-diagram** — the standard notation: a compiler written in L for M compiled by a compiler written in L for N.
- **Seed stages** — write minimal compiler in another language, compile the full compiler with it, then rebuild the full compiler with itself.
- **Why it matters** — bootstrapping is the canonical proof that recursive construction is practical, not just theoretical.
- **Risk** — the seed carries trust; a compromised seed propagates (Thompson's hack).
- **RSIS3 parallel** — the wiki's first passes bootstrapped its schema and linking conventions; later passes inherit and extend them.

## Related
- [[wiki/decisions/self-hosting|Self-Hosting]] — the goal state
- [[wiki/concepts/metacircular-evaluators|Metacircular Evaluators]] — the interpreter-side ancestor
- [[wiki/concepts/metacircular-evaluators|metacircular-evaluators]] — the notation
- [[wiki/decisions/self-improving-compilers|Self-Improving Compilers]] — the improvement loop
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — seed trust
- [[wiki/syntheses/acquisition-pass-snapshot-ordering|Acquisition Passes & Snapshot Ordering]] — pass bootstrapping
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
