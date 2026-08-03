---
type: "synthesis"
title: "Tripwires"
description: "Triggers that halt a system when thresholds are crossed"
tags: ["tripwires", "monitoring", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tripwires

## Summary
Tripwires are automated triggers that pause, alert, or roll back a system when monitored signals cross thresholds.

## Details
- Tripwires are automated triggers that pause, alert, or roll back a system when monitored signals cross thresholds.
- They convert continuous risk into discrete decision points.
- Tripwire design needs calibrated thresholds and non-gamed signals.
- RSIS3 relevance: check-failure thresholds are tripwires for the knowledge loop.

## Related
- [[wiki/syntheses/monitored-deployment|Monitored Deployment]] — the context
- [[wiki/syntheses/fallback-plans|Fallback Plans]] — the response
- [[wiki/concepts/kill-switch-design|Kill Switch Design]] — the last resort
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — the signal source
- [[wiki/concepts/control-protocols|Control Protocols]] — the full treatment of this theme
- [[wiki/agent-systems/telemetry-for-agents|Telemetry for Agents]] — existing graph context
