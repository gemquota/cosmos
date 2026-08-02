---
type: "concept"
title: "Self-Hosting"
description: "A system that can build and run itself"
tags: ["self-hosting", "bootstrapping", "compilers", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Self-hosting_(compilers)", "https://en.wikipedia.org/wiki/Dogfooding"]
---

# Self-Hosting

## Summary
Self-hosting is the property of a tool that can compile or run its own source — a compiler written in the language it compiles, an OS that builds itself, or a service that runs its own stack. It is the operational precondition for recursive self-improvement.

## Details
- **Classic case** — a C compiler compiled by C; self-hosting proves the toolchain is complete and exercises its own code.
- **Why it matters** — a self-hosted system can improve itself directly: patch source, rebuild, test.
- **Trust problem** — Ken Thompson's 1984 Turing-award lecture showed a self-hosting compiler can hide a backdoor in its descendants; provenance and reproducible builds are the defense.
- **RSIS3 relevance** — the workspace builds and checks itself (scripts, checkers, generators), and its VERSION files track the self-hosted stack.
- **Modern forms** — dogfooding and eating your own dog food are self-hosting culture.

## Related
- [[wiki/decisions/bootstrapping-compilers|Bootstrapping Compilers]] — the technique
- [[wiki/concepts/dogfooding|Dogfooding]] — using your own product
- [[wiki/concepts/self-referential-code|Self-Referential Code]] — the code property
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the trust risk
- [[wiki/decisions/auto-update-mechanisms|Auto-Update Mechanisms]] — self-hosted updates
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — the payoff
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
