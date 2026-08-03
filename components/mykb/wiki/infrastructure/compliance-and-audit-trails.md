---
type: "concept"
title: "Compliance and Audit Trails"
description: "Recording who did what to data, when, and with what authorization"
tags: ["audit", "compliance", "logging", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Compliance and Audit Trails

## Summary

Audit trails are the records that make systems answerable: who did what, to which data, when, from where, and with what authorization or outcome. They exist for two audiences — internal investigations and access reviews on one side, and regulators and auditors on the other — and a trail that satisfies neither is not really an audit trail.

## Details

- Audit trails capture access, change, and admin events with actor, timestamp, object, and outcome. The essential fields: the actor (which user, service account, or system), the action (read, write, delete, permission change), the object (which file, table, key), the timestamp (in a synchronized clock), the source (IP, session, device), and the outcome (success, failure, denial). The discipline is capturing the four Ws plus outcome — and resisting the temptation to log only "interesting" events, because the events that look boring are often the ones an investigation needs. Access events (who read what) matter as much as changes: for sensitive data, reads are the trail that detects exfiltration.
- They support investigations, access reviews, and regulator evidence for frameworks like SOC 2 and SOX. Investigations need a complete, ordered, searchable record — the trail answers "who touched this data before the leak?" Access reviews need trails that can be aggregated per user — "show me everything this contractor did". Regulatory frameworks require specific controls: SOC 2 needs logging and monitoring of security-relevant events; SOX needs audit trails for financial systems with retention periods; GDPR needs records of data processing. A trail that cannot answer the framework's questions is a compliance gap even if it exists.
- Tamper-evident storage, log retention, and alerting on anomalies make trails trustworthy. An audit trail that an attacker (or an insider) can edit is no trail at all — hence write-once storage (append-only stores, hash chaining, cloud object-lock), strict access control on the log itself, and separation between the systems being logged and the log store. Retention is a policy decision (how long must records survive — years for financial, often indefinite for security events) that must be planned as storage, not discovered during an audit. Alerting closes the loop: trails detect incidents only if someone watches for the anomaly patterns (mass downloads, off-hours admin, failed-then-succeeded access).
- Balancing detail and cost: sample fine-grained access logs, keep policy-relevant events complete. Full-detail logging of every byte access is expensive; the standard design keeps policy-relevant events (admin, permission, security) complete and unconditional, while fine-grained access events can be sampled or aggregated — with the caveat that sampling reduces forensic value, so the sampling decision must be made with the compliance requirements in view.
- For mykb: the node connects audit logging, compliance frameworks, and data lineage — the governance cluster's evidence layer.

## Related

- [[wiki/security-auth/audit-logging|Audit Logging]] — existing note on audit logging
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — frameworks that demand audit trails
- [[wiki/data-storage/data-lineage|Data Lineage]] — data movement history complements access history
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — operational signals around audits
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
