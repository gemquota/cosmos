---
type: "concept"
title: "Fuzzing Tools"
description: "Tools that feed malformed, random, or structured inputs to software to discover crashes and bugs"
tags: ["fuzzing", "security", "testing", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fuzzing Tools

## Summary
Fuzzing tools throw unexpected inputs at parsers, APIs, and binaries to trigger crashes, hangs, and memory errors. Coverage-guided fuzzers like libFuzzer and AFL++ mutate inputs toward unexplored code paths, turning random testing into systematic exploration.

## Details
- Mechanism: a harness feeds generated inputs to the target; coverage-guided fuzzers instrument the target, measure which branches each input reaches, and keep mutations that explore new paths; the corpus grows with interesting inputs and is minimized for reproducibility; crashes and hangs are saved as regression cases.
- Concrete example: libFuzzer fuzzing a markdown parser with byte-mutated documents finds a crash on a crafted frontmatter block; AFL++ fuzzing a binary parser with a seed corpus of valid files reaches deep state-machine logic; structure-aware fuzzing using a grammar generates syntactically valid-but-hostile inputs for protocol handlers.
- Failure modes: fuzzing without coverage guidance, degenerating into random noise; targets that allocate unboundedly on hostile input, so the fuzzer finds OOMs instead of logic bugs; a harness that checks nothing, so crashes in swallowed exceptions never surface; fuzzing runs that are never integrated into CI, so regressions reappear; corpora bloating and slowing every run.
- Tradeoffs: fuzzing finds real bugs cheaply after setup, but setup is real work — harnesses, corpus, and crash triage; the alternative, manual and unit testing, misses the hostile-input class; the mature pattern is coverage-guided fuzzing in CI for parsers and boundary-heavy code, with crashes minimized into the test suite.
- Operational notes: run short CI fuzz bursts, keep a minimized corpus, and triage every crash into a regression test.
- RSIS3 relevance: fuzzing the mykb markdown parser would harden the acquisition pipeline against malformed notes — hostile input handling is exactly what a growing wiki needs.

- Start with the highest-risk parsers (markdown, YAML, JSON) and add fuzzing where input crosses trust boundaries.
## Related
- [[wiki/testing/fuzzing|Fuzzing]]
- [[wiki/testing/security-testing|Security Testing]]
- [[wiki/testing/boundary-value-analysis|Boundary Value Analysis]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
