---
type: "concept"
title: "Root Cause Analysis"
description: "Systematically finding the underlying causes of incidents, beyond the immediate trigger"
tags: ["rca", "incidents", "analysis", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Root Cause Analysis

## Summary
Root cause analysis digs past the immediate trigger to the contributing causes that allowed an incident to happen.

## Details
- Methods: five whys, fishbone diagrams, and timeline analysis converge on contributing factors.
- Distinguish trigger (the final push) from root causes (the conditions that made it possible).
- Every root cause needs a concrete, owned action item to be worth finding.
- Open question: when 'root cause' is the wrong lens and a systems view fits better.

## Related
- [[wiki/devops-infra/incident-response|Incident Response]] — RCA is the follow-up phase
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — evidence for tracing failure paths
- [[wiki/devops-infra/postmortem-culture|Postmortem Culture]] — where RCA findings live
- [[wiki/devops-infra/observability|Observability]] — data that makes RCA possible
