---
type: "concept"
title: "SIEM"
description: "Centralizing logs and alerts for security investigation"
tags: ["splunk", "siem", "security", "logs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SIEM

## Summary
A SIEM centralizes logs, events, and alerts from across the estate and turns them into searchable, correlatable evidence for security investigation. It is the aggregation layer that converts "did anything happen?" into "what happened, in what order, and is it still happening?" — the backbone of modern security operations centers.

## Details
- Pipeline: agents and forwarders collect logs, normalize them into a common schema, and ship them to the indexer; correlation rules and analytics then turn indexed events into alerts, and case management tracks them to resolution.
- Core features: full-text and structured search (SPL in Splunk, KQL in Elastic), correlation of events across sources and time windows, alert rules with thresholds and suppression, dashboards, and retention tiers that balance cost against compliance requirements.
- Concrete examples: correlating failed logins followed by a successful one from a new geolocation, detecting credential dumping by matching unusual process spawns against a baseline, and replaying the full kill chain from firewall, EDR, and authentication logs during an incident.
- Failure modes: alert fatigue from noisy rules that trains analysts to ignore everything; log-source gaps that leave blind spots; timestamp and timezone skew across appliances; ingestion lag that breaks time-window correlations; rules that silently reference removed fields; and retention policies driven by license cost rather than investigation need.
- Tradeoffs: centralizing everything simplifies correlation but concentrates cost and privacy risk; edge analytics reduce egress but fragment the view. Signature rules are cheap and precise but miss novel attacks, while anomaly detection finds outliers but generates more false positives.
- Rule tuning: treat every alert as a candidate for tuning — track true/false positive rates per rule, suppress noisy rules with windows, and re-baseline after infrastructure changes.
- RSIS3/mykb relevance: the SIEM's triage loop — collect, correlate, alert, investigate, tune rules — is a direct analogue of RSIS3's L1 action loop, and this node keeps that analogy retrievable for telemetry design.

## Related
- [[wiki/os-shell/logical-volume-management|Logical Volume Management]]
- [[wiki/devops-infra/helm-and-chart-management|Helm & Chart Management]]
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]
