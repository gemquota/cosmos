---
type: "concept"
title: "Exception Handling Practice"
description: "Discipline for catching, wrapping, and reporting exceptions without swallowing them"
tags: ["exceptions", "error-handling", "practice", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exception Handling Practice

## Summary
Exception handling practice is the set of conventions that keep failures visible and recoverable: catch at boundaries, wrap with context, log with enough detail, and never swallow errors silently. The goal is fail-loudly-but-gracefully.

## Details
- Catch exceptions where you can act on them, wrap with domain context (what were we doing?), and rethrow.
- Empty except blocks are the top reliability anti-pattern; at minimum log and re-raise at a boundary.
- Define an error taxonomy — transient vs permanent — so callers can decide retry vs fail.
- mykb relevance: the acquisition pipeline needs per-stage exception policies so one bad article never halts the batch.

## Related
- [[wiki/dev-tools/error-codes|Error Codes]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/dev-tools/error-tracking-tools|Error Tracking Tools]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
