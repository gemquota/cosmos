---
type: "concept"
title: "Reaction Threshold"
resource: ""
---
description: "The trigger point at which a system or agent changes behavior in response to a signal"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "thresholds", "monitoring"]
timestamp: "2026-07-19T22:41:43Z"

# Reaction Threshold

## Summary
A reaction threshold is the point at which a system or agent changes behavior in response to a measured signal, such as alerting when latency crosses a limit or fleeing when an enemy gets close. It matters because thresholds decide when nothing happens versus when something does. Poorly set thresholds cause either deafening silence or constant noise, so calibration deserves real effort.

## Details
- **Definition** — a reaction threshold compares a monitored value against a boundary and triggers a defined response when the boundary is crossed.
- **Signal selection** — the measured signal must actually reflect the condition of interest; a wrong signal makes any threshold meaningless.
- **Hysteresis** — separate entry and exit thresholds prevent rapid oscillation at the boundary, a classic failure of naive thresholds.
- **Sensitivity** — low thresholds react early but fire often; high thresholds stay calm but miss problems; the right level depends on cost and context.
- **Time windows** — reacting to sustained conditions over a window filters transient spikes that should not trigger action.
- **Tuning** — thresholds should be derived from observed baselines and revisited as behavior changes.
- **Common failure modes** — thresholds set by guesswork, alert fatigue from over-firing, and thresholds that never fire because they drift stale.
- **Worked example** — a monitoring rule alerts when p95 latency exceeds 300 ms for five consecutive minutes, and clears when it drops below 250 ms.
- **Practical relevance** — well-designed reaction thresholds make automation, alerting, and agent behavior predictable.

- **Alert routing** — a threshold crossing should map to a specific response path, such as paging, scaling, or fallback, not a generic alarm.
- **Multi-signal** — combining thresholds across signals, such as latency and error rate, reduces false triggers that single signals cause.
- **Review** — threshold changes deserve review and versioning, since a tweak can silence a genuine problem.
## Related
- [[wiki/data-storage/anomaly-detection-in-metrics|Anomaly Detection in Metrics]] — finding signal
- [[wiki/software-engineering/metrics-and-monitoring|Metrics and Monitoring]] — the measured values
- [[wiki/testing/response-time-percentiles|Response Time Percentiles]] — latency signals
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — time-based triggers
- [[wiki/testing/load-testing|Load Testing]] — exercising thresholds
- [[wiki/agent-systems/backpressure-agents|Backpressure for Agents]] — load reaction
