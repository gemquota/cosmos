---
type: "concept"
title: "Timeout Policy"
description: "Rules for how long a call may take before it is abandoned"
tags: ["timeouts", "resilience", "policy", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Timeout Policy

## Summary
A timeout policy fixes the maximum wait for every call — HTTP, DB, lock, model — so one slow dependency cannot hang the system. Timeouts turn unknown delays into bounded failures that retry logic can handle.

## Details
- Set per-call-type timeouts: DB calls differ from external APIs; a single global timeout is usually wrong.
- Account for queueing: timeout-at-client plus timeout-at-server must sum to less than the client budget.
- Deadlines that propagate (context deadline, grpc deadline) let downstream services abort early.
- mykb relevance: every agent tool call needs a timeout so one hung tool does not stall the whole run.

## Related
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/api-protocols/grpc-deadlines|gRPC Deadlines]]
- [[wiki/tooling/client-side-timeouts|Client-Side Timeouts]]
- [[wiki/dev-tools/cancellation-tokens|Cancellation Tokens]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
