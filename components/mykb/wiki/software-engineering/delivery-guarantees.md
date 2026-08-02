---
type: "concept"
title: "Delivery Guarantees"
description: "The spectrum of message delivery semantics from at-most-once to exactly-once"
tags: ["delivery", "guarantees", "messaging", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Delivery Guarantees

## Summary
Delivery guarantees describe what a messaging system promises: at-most-once (lossy), at-least-once (duplicating), exactly-once (both, via tricks). Choosing a guarantee is choosing which failure you accept and what your consumers must tolerate.

## Details
- Guarantees live at the broker/consumer boundary; end-to-end semantics depend on your whole pipeline.
- Exactly-once is built from at-least-once plus idempotency — name it honestly.
- Document the guarantee per topic or queue; mixed semantics are common and fine.
- mykb relevance: the wiki event bus documents per-topic guarantees so consumers know what to assume.

## Related
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/software-engineering/at-most-once|At-Most-Once]]
- [[wiki/software-engineering/exactly-once-claims|Exactly-Once Claims]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/api-protocols/message-queues|Message Queues]]
