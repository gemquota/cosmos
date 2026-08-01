---
type: "concept"
title: "Data Classification"
description: "Labeling data by sensitivity and value to drive handling, protection, and access decisions"
tags: ["data-classification", "governance", "labels", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/purview/data-classification-overview"]
---

# Data Classification

## Summary

Data classification assigns sensitivity labels to information — public, internal, confidential, restricted — so that handling rules can follow the data. Labels travel with the data (in metadata and content) and drive protection, access control, retention, and DLP decisions. It matters because you cannot protect what you have not labeled: access decisions, breach reporting, and retention all depend on knowing what each item is worth. For RSIS3, classification is the bridge between raw memory and policy: an ABAC policy can only be data-aware if the data carries a label.

## Details

- Label schemes: typical tiers are public / internal / confidential / restricted, with business-specific refinements; each tier implies handling rules.
- Discovery: labels are assigned manually, inferred from templates and patterns, or learned by classifiers scanning content (Microsoft Purview and equivalents).
- Uses: feed access-control policies, trigger encryption, set retention and deletion, drive breach-notification obligations, and scope DLP actions.
- Operationalization: a label taxonomy must be simple enough to apply at scale and precise enough to be useful; over-tagging dilutes the signal.
- Governance: label owners, reclassification workflows, and audits keep the scheme current as data and regulations change.
- For mykb, every knowledge item should carry a classification tag in its frontmatter so retrieval and policy decisions stay consistent.

## Related

- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]] — labels become resource attributes in policies
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — regulatory regimes require classification
- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — minimization depends on knowing sensitivity
- [[wiki/security-auth/audit-logging|Audit Logging]] — access to classified data must be logged
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — carrying labels in mykb files
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — classification as part of curation
- [[wiki/identity/breach-notification|Breach Notification]] — sensitivity drives notification duties
- [[wiki/security-auth/third-party-risk|Third-Party Risk]] — classifying data shared with vendors
- [[wiki/concepts/triad-architecture|Triad Architecture]] — labels enforced at the memory boundary
