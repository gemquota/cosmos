---
type: "concept"
title: "Degraded Mode Operations"
description: "Graceful reduction of service quality when resources or dependencies fail"
tags: ["degraded-mode", "reliability", "operations", "fallback"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Degraded Mode Operations

## Summary
Degraded mode operations are the planned reduction of service quality when resources or dependencies fail, such as serving cached answers or using simpler models. They matter because failures are inevitable, and an explicit degraded mode beats uncontrolled failure. Users and operators get predictable behavior instead of an outage. Degraded mode is a design decision, not an accident.

## Details
- **Definition** — degraded mode is a pre-defined operating state with reduced functionality, entered automatically when full service is impossible.
- **Fallback behaviors** — common degradations include cached answers, simpler or cheaper models, read-only access, and reduced concurrency.
- **Why it works** — because degraded behavior is designed in advance, it preserves the most valuable parts of the service under stress.
- **Communication** — users must be told they are seeing degraded output, typically through clear error-messages-llm and status indicators.
- **Governance** — model-fallback-chains define how model degradation steps down capability, while feature-flags enable manual overrides.
- **Worked example** — during an embedding API outage, a search agent serves keyword matches from cache and labels results as reduced-quality instead of failing.
- **Failure modes** — degraded modes that are too complex to enter quickly, stale caches, and silent degradation that hides from users all cause problems.
- **Practical relevance** — degraded mode is the reliability strategy that keeps agent services useful through partial-failure-handling scenarios.
- **Trigger design** — clear, automated triggers decide when degraded mode engages and when it recovers.
- **Testing** — degraded paths should be exercised regularly, since they only run during crises.
- **Priorities** — teams should decide in advance which features matter most when capacity shrinks.
- **Failure example** — a degraded mode that serves stale cache without labeling it misleads users into trusting old data.

## Related
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — stepping down model capability
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — the failure taxonomy
- [[wiki/api-protocols/load-shedding|Load Shedding]] — reducing traffic under overload
- [[wiki/agent-systems/feature-flags-for-agents|Feature Flags for Agents]] — manual control over degraded states
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — telling users about reduced service
