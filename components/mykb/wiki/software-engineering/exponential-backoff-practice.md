---
type: "concept"
title: "Exponential Backoff Practice"
description: "Doubling the wait between retries so load on a failing system decreases"
tags: ["backoff", "retry", "reliability", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exponential Backoff Practice

## Summary
Exponential backoff multiplies the delay between attempts — 1s, 2s, 4s, 8s — so retry storms do not pile onto an already failing system. Adding jitter prevents synchronized retry waves across many clients.

## Details
- Cap the exponent (max delay) and add full or equal jitter to break synchronization.
- Reset backoff after success; track attempts to bound total time.
- Backoff is for transient failures — permanent errors should fail fast instead.
- mykb relevance: the wiki link-checker backs off on 429/503 sources automatically.

## Related
- [[wiki/software-engineering/jitter-practice|Jitter Practice]]
- [[wiki/software-engineering/backoff-cap|Backoff Cap]]
- [[wiki/software-engineering/retry-queues|Retry Queues]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]]
