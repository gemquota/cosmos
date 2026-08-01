---
type: "concept"
title: "Security Incident Monitoring"
description: "Continuous detection, triage, and response to security events across systems"
tags: ["monitoring", "incident-response", "detection", "soc"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://csrc.nist.gov/pubs/sp/800/61/r2/final"]
---

# Security Incident Monitoring

## Summary

Security incident monitoring is the continuous practice of collecting security-relevant signals, detecting suspicious activity, triaging alerts, and responding through a defined incident-response lifecycle. NIST SP 800-61 is the canonical guide to computer security incident handling. It matters because detection is a race: the shorter the time between compromise and discovery, the smaller the damage; monitoring is what turns logs into action. For RSIS3, monitoring covers the memory system's own boundaries: anomalous access patterns, credential misuse, and unexpected agent behavior.

## Details

- Detection sources: SIEM correlation, endpoint detection (EDR), network telemetry, audit logs, honeypots, and threat-intelligence feeds.
- Triage: alerts are filtered and prioritized by severity and context; most alerts are noise, so tuning and baselining reduce alert fatigue.
- NIST incident response phases: preparation, detection and analysis, containment, eradication, recovery, and post-incident lessons learned.
- Metrics: time to detect (MTTD) and time to respond (MTTR) measure the program; retention of evidence supports forensics.
- Automation: playbooks encode triage and containment steps; SOAR tools orchestrate them, but decisions need human review.
- For mykb, monitoring should cover both infrastructure signals (via the observability stack) and semantic signals (what knowledge was accessed, when, by whom).

## Related

- [[wiki/security-auth/audit-logging|Audit Logging]] — the raw events monitoring consumes
- [[wiki/security-auth/threat-intelligence|Threat Intelligence]] — feeds that sharpen detection
- [[wiki/security-auth/indicators-of-compromise|Indicators of Compromise]] — signatures used to match events
- [[wiki/security-auth/data-breach-response|Data Breach Response]] — the downstream response lifecycle
- [[wiki/devops-infra/observability|Observability]] — shared telemetry infrastructure
- [[wiki/security/zero-trust|Zero Trust Architecture]] — continuous verification feeds monitoring
- [[wiki/concepts/triad-architecture|Triad Architecture]] — monitoring across triad services
