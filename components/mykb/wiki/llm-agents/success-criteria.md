---
type: "concept"
title: "Success Criteria"
description: "Verifiable conditions that define when a task is done correctly"
tags: ["success-criteria", "evaluation", "goals", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Success Criteria

## Summary

Success criteria are the measurable conditions that define when an agent's task is actually done — verifiable, unambiguous, and decided before the run. They are the contract that makes agent autonomy safe and evaluation honest.

## Details
- Mechanism: good criteria are testable (a test suite, a checklist, a measurable outcome), decided up front (before the run, not after), and complete enough that passing them implies the goal; criteria types include automated checks (tests, schema validation), human verification (review gates), and quantitative targets (accuracy, latency, cost).
- Concrete example: a wiki-writing task's criteria: all links resolve, frontmatter valid, ≥320 words, no stub boilerplate — checked by script; a code task's criteria: tests pass, lint clean, no regressions in the benchmark; a research task's criteria: every claim cited, sources verified. The failure pattern: criteria like "make it better" that no runtime can check.
- Failure modes: criteria that pass while the goal fails (a test that does not test the real requirement); criteria discovered after the run to justify a bad result; ambiguous criteria interpreted differently by agent and reviewer; and gold-plating — criteria so strict that legitimate results are rejected.
- Operational tradeoffs: precise criteria cost definition effort but enable automation, evaluation, and stop conditions; the discipline is writing them like acceptance criteria, making them machine-checkable where possible, and revisiting them when they disagree with human judgment.
- RSIS3/mykb relevance: every wiki promotion pass carries machine-checkable success criteria (word counts, links, schema) so completion is provable, not asserted.
- Criteria review: before each run, a human (or the policy layer) reviews the criteria for completeness; a criteria set nobody can verify is a recipe for fabricated success.
- Partial credit: define what an acceptable partial result looks like for budget-limited runs, so a stopped run still produces usable output and a clear status.

## Related
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — the measurement of success
- [[wiki/llm-agents/stop-conditions|Stop Conditions]] — success as a stop condition
- [[wiki/concepts/agent-benchmarks|Agent Benchmarks]] — criteria at benchmark scale
- [[wiki/llm-agents/traceability|Traceability]] — verifying the evidence
- [[wiki/agent-systems/goal-decomposition|Goal Decomposition]] — criteria per subgoal
