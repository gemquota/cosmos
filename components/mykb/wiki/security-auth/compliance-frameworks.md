---
type: "concept"
title: "Compliance Frameworks"
description: "Structured control sets and practices used to meet regulatory and security obligations"
tags: ["compliance", "frameworks", "governance", "nist", "gdpr"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.nist.gov/cyberframework"]
---

# Compliance Frameworks

## Summary

Compliance frameworks are organized sets of controls, practices, and reporting obligations that organizations adopt to satisfy regulations, contracts, and security expectations. NIST CSF 2.0 organizes cybersecurity by functions — Govern, Identify, Protect, Detect, Respond, Recover — while ISO 27001, SOC 2, and GDPR impose auditable requirements. They matter because they turn security from an engineering taste into a measurable, auditable program, and because breaches now carry legal penalties under regimes like GDPR. For RSIS3, frameworks are the vocabulary for justifying and documenting why mykb holds data the way it does.

## Details

- NIST CSF 2.0: the risk-based framework with six functions and thousands of mapped controls; free and widely used as a baseline.
- ISO/IEC 27001: certifiable ISMS standard with Annex A controls; compliance is proven through audits.
- SOC 2: trust services criteria (security, availability, confidentiality, processing integrity, privacy) assessed by CPAs — the default for SaaS vendors.
- Regulatory regimes: GDPR (EU data protection), HIPAA (healthcare), PCI-DSS (card data), and sector rules impose specific obligations with fines.
- Mapping: frameworks overlap; many organizations map controls to multiple frameworks and use a control register as the single source of truth.
- Compliance is not security: passing an audit does not stop attackers — frameworks set a floor, not a ceiling.
- For mykb, the practical output is a control register that ties data-classification labels, audit logs, and privacy decisions to framework controls.

## Related

- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — GDPR's engineering principle
- [[wiki/security-auth/data-classification|Data Classification]] — labeling that feeds compliance reporting
- [[wiki/security-auth/audit-logging|Audit Logging]] — evidence for compliance audits
- [[wiki/identity/breach-notification|Breach Notification]] — regulatory duty to report incidents
- [[wiki/security/sbom|SBOM]] — software supply chain transparency
- [[wiki/security-auth/third-party-risk|Third-Party Risk]] — vendor obligations under frameworks
- [[wiki/ops/gap-report|Gap Analysis Report]] — tracking compliance coverage gaps
- [[wiki/concepts/triad-architecture|Triad Architecture]] — governance across the triad
