---
type: "concept"
title: "Fuzzing Tools"
description: "Tools that feed malformed, random, or structured inputs to software to discover crashes and bugs"
tags: ["fuzzing", "security", "testing", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fuzzing Tools

## Summary
Fuzzing tools throw unexpected inputs at parsers, APIs, and binaries to trigger crashes, hangs, and memory errors. Coverage-guided fuzzers like libFuzzer and AFL++ mutate inputs toward unexplored code paths.

## Details
- Coverage-guided fuzzing is the default: measure which branches each input hits and keep the interesting ones.
- Structure-aware fuzzing (grammar or dictionary based) reaches deep logic in parsers and protocol handlers.
- Corpus management and minimization make runs reproducible and fast; run fuzzing in CI for short bursts.
- RSIS3 relevance: fuzzing the mykb markdown parser would harden the acquisition pipeline against malformed notes.

## Related
- [[wiki/testing/fuzzing|Fuzzing]]
- [[wiki/testing/security-testing|Security Testing]]
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
