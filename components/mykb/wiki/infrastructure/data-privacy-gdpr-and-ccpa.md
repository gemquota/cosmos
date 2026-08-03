---
type: "concept"
title: "Data Privacy: GDPR and CCPA"
description: "Regulatory regimes governing collection, use, and deletion of personal data"
tags: ["privacy", "gdpr", "ccpa", "compliance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Privacy: GDPR and CCPA

## Summary

GDPR (EU) and CCPA/CPRA (California) are the two most influential privacy regimes, both built on the idea that individuals hold rights over their personal data — what is collected, how it is used, and whether it persists. They differ in mechanism and reach, but their engineering demands converge: you must know what personal data you hold, why you hold it, and how to act on it when a person asks.

## Details

- GDPR (EU) grants rights: access, rectification, erasure ('right to be forgotten'), portability, and consent controls. The rights translate directly into operations: access requires retrieving everything you hold about a person; rectification requires updating it; erasure requires deleting it (including from backups, within reason); portability requires exporting it in a machine-readable format; consent controls require honoring granular, revocable consent. GDPR's reach is extraterritorial — it applies to any organization processing EU residents' data, regardless of where the organization sits — and its enforcement teeth (fines up to 4% of global revenue) make it the regime most organizations design to first.
- CCPA/CPRA (California) focuses on disclosure, opt-out of sale/sharing, and deletion rights for consumers. CCPA is disclosure-heavy: businesses must say what they collect and why, and consumers may opt out of the "sale" or "sharing" of their data (with CPRA expanding "sharing" to cross-context behavioral advertising). Deletion and access rights exist but with a narrower scope than GDPR (no general rectification or portability), and there is no consent-first baseline — instead, notice-and-opt-out for sale/sharing. California's size makes CCPA a de facto national standard in the US.
- Both require inventory of personal data, lawful basis or purpose tracking, and documented retention limits. You cannot answer "what do you hold about me?" without an inventory; you cannot justify collection without recording the lawful basis (GDPR: consent, contract, legal obligation, legitimate interest) or purpose (CCPA); you cannot honor deletion without knowing where the data lives. These requirements turn privacy compliance into a data-management project: the inventory, lineage, and retention policy are the deliverables.
- Engineering impact: PII tagging, lineage for erasure, masking in dev, and contracts with processors. Tag data as PII at the schema level (classification labels), build lineage so erasure can trace a person's data through copies and derivatives, mask PII in development environments so the raw data does not spread, and contract with processors (cloud vendors, analytics tools) to bind them to the same obligations — since a breach or violation at a processor is your violation.
- For mykb: the node is the legal floor under privacy-by-design and responsible use, and the engineering patterns (classification, lineage, retention) are the governance cluster's core.

## Related

- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — design principle behind compliance
- [[wiki/security-auth/data-classification|Data Classification]] — finding personal data to govern
- [[wiki/infrastructure/data-classification-labels|Data Classification Labels]] — labels that mark personal data
- [[wiki/infrastructure/compliance-and-audit-trails|Compliance and Audit Trails]] — evidence for regulators
- [[wiki/data-storage/data-retention-and-lifecycle|Data Retention And Lifecycle]] — retention limits required by law
