---
type: "concept"
title: "Certificate Transparency"
description: "Append-only public logs that audit issued TLS certificates"
tags: ["certificates", "security", "tls", "audit"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Certificate Transparency

## Summary

Certificate Transparency (CT) is the public, append-only log of issued TLS certificates, making misissuance visible and auditable. It is mandatory in practice — browsers require SCTs — and is the monitoring layer that turns CA mistakes into incidents instead of silent breaches.

## Details
- Mechanism: CAs submit certificates to CT logs; logs return SCTs (signed timestamps) embedded in the certificate or delivered via TLS; browsers require a valid SCT for trust in Chrome; monitors and auditors watch logs for suspicious issuance (a certificate for your domain you did not request).
- Concrete example: a security team subscribes to CT streams filtered by their domains; the moment an attacker or misconfigured CA issues a certificate for example.com, an alert fires and the cert is preemptively distrusted or investigated — long before the browser trusts it for interception.
- Failure modes: certificates issued without SCTs (older or misconfigured CAs) failing browser trust; CT logs being append-only means misissuance cannot be deleted, only flagged — so monitoring is the actual control; log split-brain and inclusion delays causing transient validation failures; and ignoring CT for internal/non-public PKIs, where the model does not apply.
- Operational tradeoffs: CT shifts CA oversight from trust-by-fiat to audit-by-log; the cost is monitoring infrastructure and false-positive triage. Run continuous CT monitoring for every public domain, integrate alerts with your incident pipeline, and treat unsigned or SCT-less issuance as a red flag.
- RSIS3/mykb relevance: the cosmos domains are watched through CT monitors; this note records the alerting policy so the loop's certificate automation inherits the same visibility.
- Response plan: predefine what a suspicious issuance alert triggers (verify, revoke, contact CA); an alert without a runbook is just noise.
- Monitoring scope: monitor all public domains and wildcards, not just apex names; the subdomain certificate is the one attackers actually use.

## Related
- [[wiki/cloud-infra/certificate-pinning-infra|Certificate Pinning in Infrastructure]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
