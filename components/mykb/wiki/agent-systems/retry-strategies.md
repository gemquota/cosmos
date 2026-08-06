---
type: "concept"
title: "Retry Strategies"
description: "Policies for recovering from transient failures without masking real errors"
tags: ["retries", "reliability", "error-handling", "agents", "telemetry"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/error-codes"]
---

# Retry Strategies

## Summary
Retry strategies govern what an agent does when a step fails: how many times to retry, how long to wait, and when to escalate. They matter because transient failures (rate limits, network blips, busy tools) are normal in agent systems, while blind retrying wastes budget and can hide genuine bugs. RSIS3 wraps every tool call in bounded retries with backoff and telemetry.

## Details
- **Classify first**: transient errors (429, 5xx, timeouts) are retryable; permanent errors (bad schema, permission denied) must not be retried blindly.
- **Exponential backoff with jitter** prevents thundering herds on shared services.
- **Retry budgets**: a max attempts and max elapsed time, after which the agent escalates to a different strategy or reports failure.
- **Idempotency**: retries must be safe to repeat, which is why pure tools and versioned patches matter.
- RSIS3's L1 loop treats tool failure as an observation, feeds it to retry logic, and logs the full sequence for traceability.
- Worked example: a rate-limited API call retries with backoff three times, then the agent switches to a cached result.

- **Escalation ladder** — the strategy is a ladder: retry with backoff, fall back to a cached or alternative result, degrade scope, then fail with a precise report; each rung has its own trigger.
- **Error classification** — the policy table maps error classes (transient, permanent, unknown) to actions; misclassifying permanent errors as transient is how retry loops burn budget.
- **Concurrency discipline** — do not retry the same call from multiple threads in parallel; serialized retries preserve ordering and prevent duplicate side effects.
- **Policy as code** — retry strategies belong in the runtime configuration, versioned and observable, not scattered through prompts where they cannot be tested.

## Related

- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — re-running failed steps for debugging
- [[wiki/llm-agents/agent-logs|Agent Logs]] — the record retry decisions write to
- [[wiki/llm-agents/traceability|Traceability]] — linking retries back to causes
- [[wiki/ops/gap-report|Gap Analysis Report]] — identifies retry policy gaps
