---
type: "concept"
title: "Security Engineering"
description: "Designing systems that resist attack by construction"
tags: ["security", "engineering", "threat-modeling", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Security_engineering", "https://owasp.org/www-project-top-ten/"]
---

# Security Engineering

## Summary
Security engineering builds security into design rather than bolting it on: threat modeling, least privilege, defense in depth, and secure defaults. It treats attackers as a design constraint and measures success by the cost of compromise.

## Details
- Threat modeling identifies assets, adversaries, and attack paths before code exists; the design responds.
- Least privilege and defense in depth make single failures survivable; secure defaults make mistakes expensive.
- The OWASP Top Ten catalogs the common web risks: injection, broken auth, and misconfiguration lead the list.
- Security is layered: network, host, application, data, and identity controls each slow an attacker.
- The discipline includes incident response: detection, containment, and recovery are engineered, not improvised.
- For the mykb bundle, security engineering covers the sync pipeline, the API, and the integrity of the knowledge corpus.
- Worked example — the wiki API threat model identifies unauthenticated writes as the top risk; the design adds authentication, rate limits, and per-scope authorization before any write path ships.

Worked example — the wiki API threat model identifies unauthenticated writes as the top risk; the design adds authentication, rate limits, and per-scope authorization before any write path ships.

## Related
- [[wiki/compositions/threat-modeling|Threat Modeling]]
- [[wiki/compositions/zero-trust-architecture|Zero-Trust Architecture]]
- [[wiki/tooling/secure-sdlc|Secure SDLC]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
- [[wiki/security/zero-trust|Zero Trust]]
- [[wiki/compositions/identity-management|Identity Management]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
- [[wiki/communities/malicious-packages|Malicious Packages]]
