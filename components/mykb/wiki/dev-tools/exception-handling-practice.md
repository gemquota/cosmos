---
type: "concept"
title: "Exception Handling Practice"
description: "Discipline for catching, wrapping, and reporting exceptions without swallowing them"
tags: ["exceptions", "error-handling", "practice", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Exception Handling Practice

## Summary
Exception handling practice is the set of conventions that keep failures visible and recoverable: catch at boundaries, wrap with context, log with enough detail, and never swallow errors silently. The goal is fail-loudly-but-gracefully — errors become data, not mysteries.

## Details
- Mechanism: catch exceptions where you can act on them, wrap with domain context (what were we doing, with which inputs), and rethrow or convert at boundaries; empty except blocks are the top reliability anti-pattern — at minimum log and re-raise; an error taxonomy (transient versus permanent) lets callers decide retry versus fail.
- Concrete example: an ingestion stage catches a parse error, wraps it as ArticleParseError with the article ID and source line, and logs it; the batch continues with other articles; a transient network error is retried with backoff, a permanent schema error goes to a dead-letter queue; the boundary converts internal exceptions into typed errors for the API response.
- Failure modes: swallowing exceptions, hiding failures until data goes missing; catching too broadly (except Exception) and misclassifying permanent failures as transient, causing infinite retry loops; logging the same error at every layer, creating duplicate noise; exception paths that leak sensitive data into logs; error handling that is more complex than the code it protects.
- Tradeoffs: structured exception handling costs ceremony but makes failures diagnosable and recoverable; the alternative — let everything crash — is simple and loses partial progress; the mature pattern is per-stage policies, typed errors at boundaries, and retry-vs-fail decisions made once.
- Operational notes: define the taxonomy, centralize error reporting, and review exception paths in code review.
- RSIS3 relevance: the acquisition pipeline needs per-stage exception policies so one bad article never halts the batch — the fail-loudly-but-continue discipline RSIS3 applies to its loops.

## Practice
- Handle exceptions at the level with the information to act: low layers wrap, high layers decide policy, and nobody logs without context.
## Related
- [[wiki/dev-tools/error-codes|Error Codes]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/dev-tools/fallback-values|Fallback Values]]
- [[wiki/dev-tools/error-tracking-tools|Error Tracking Tools]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
