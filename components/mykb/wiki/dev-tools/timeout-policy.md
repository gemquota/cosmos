---
type: "concept"
title: "Timeout Policy"
description: "Rules for how long a call may take before it is abandoned"
tags: ["timeouts", "resilience", "policy", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Timeout Policy

## Summary
A timeout policy fixes the maximum wait for every call — HTTP, DB, lock, model — so one slow dependency cannot hang the system. Timeouts turn unknown delays into bounded failures that retry logic can handle.

## Details
- Mechanism: set per-call-type timeouts (DB calls differ from external APIs; a single global timeout is usually wrong); account for queueing — client timeout plus server processing must sum to less than the caller's budget; propagate deadlines (context deadline, gRPC deadline) so downstream services abort early instead of continuing work nobody will consume.
- Concrete example: a service calls a model API with a 10s deadline, a database with 2s, and an internal service with 5s; each timeout is set from measured percentiles plus headroom; a hung model call cancels at 10s, the client retries within its own budget, and the whole request still returns within 12s.
- Failure modes: no timeouts, so a hung dependency queues requests until connections exhaust; timeouts longer than the caller's patience, so callers retry into a pile-up; timeouts so short they fail legitimate slow responses; deadlines that restart at each hop, so the chain never ends; timeouts that trigger unbounded retries, multiplying load.
- Tradeoffs: tight timeouts protect capacity but cause premature failures; loose timeouts preserve legitimate work but tie up resources; the art is sizing from measured percentiles, making timeouts per dependency, and centralizing the policy so it is tunable.
- Operational notes: monitor timeout-hit rates, size from p99 latency data, and rehearse the behavior when a dependency crosses its timeout.
- RSIS3 relevance: every agent tool call needs a timeout so one hung tool does not stall the whole run — the bounded-failure pattern RSIS3 applies to all its calls.

## Practice
- Review timeouts as part of code review, since a missing or wrong timeout is a reliability bug like any other.
## Related
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/api-protocols/grpc-deadlines|gRPC Deadlines]]
- [[wiki/tooling/client-side-timeouts|Client-Side Timeouts]]
- [[wiki/dev-tools/cancellation-tokens|Cancellation Tokens]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
