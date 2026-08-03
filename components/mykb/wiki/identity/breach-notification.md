---
type: "concept"
title: "Breach Notification"
description: "Legal and ethical duty to inform affected parties and authorities after a data breach"
tags: ["breach", "notification", "gdpr", "compliance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://gdpr-info.eu/art-33-gdpr/"]
---

# Breach Notification

## Summary
Breach notification is the legal and ethical duty to inform regulators and affected individuals after a data breach that puts personal data at risk. It is not a single email — it is the endpoint of a prepared response chain that starts with detection, proceeds through classification and containment, and ends with timely, accurate notice that lets affected people protect themselves.

## Details
- Legal framework: GDPR Article 33 requires reporting personal-data breaches to the supervisory authority within 72 hours of becoming aware; Article 34 requires notifying affected individuals when the risk is high. Other regimes (state laws such as the California Consumer Privacy Act, sector rules like HIPAA) impose similar duties with varying timelines and thresholds.
- Concrete example: a database with customer email addresses and hashed passwords is exfiltrated. The response chain: detect the exfiltration via monitoring, classify the data involved (emails and password hashes — a "confidentiality breach" of personal data), contain and preserve evidence, notify the regulator within 72 hours with the known facts, and notify customers because the risk to them is high.
- Preparedness matters: notification is only possible if detection, classification, and data mapping already exist. The 72-hour clock cannot be met if the first task is discovering what data was stored where — data mapping, an inventory of processing, and pre-drafted notification templates are what make the deadline achievable.
- Failure modes: notifying too early with wrong facts, then having to correct (or retract) the notice; not notifying at all because the breach was "only" encrypted data or test data, when the letter of the law still requires assessment; and the notification paradox, where a fast but wrong notification erodes trust more than a slower accurate one.
- Tradeoffs: early notification limits damage to users but risks incomplete information and public confusion; delayed notification allows a complete picture but breaches the legal duty and gives attackers time to monetize the data. The resolution is staged notification: regulator first with what is known, users as soon as facts stabilize.
- Operational practice: maintain a breach-response runbook, pre-draft templates with placeholders, assign notification owners, test the 72-hour drill regularly, and record every decision (why notified, why not) so the analysis is defensible.
- For mykb: knowing what data is stored, where, and how sensitive (data classification) is the prerequisite for any notification obligation; the wiki's data inventory is exactly the mapping a response needs.

## Related
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — GDPR and other regimes define the duty
- [[wiki/security-auth/data-breach-response|Data Breach Response]] — notification is one phase of response
- [[wiki/security-auth/data-classification|Data Classification]] — sensitivity drives notification thresholds
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detection enables timely notice
