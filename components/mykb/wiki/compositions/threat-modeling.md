---
type: "concept"
title: "Threat Modeling"
description: "Systematically finding and addressing attack paths in a design"
tags: ["threat-modeling", "security", "risk", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.owasp.org/www-community/Threat_Modeling", "https://en.wikipedia.org/wiki/Threat_model"]
---

# Threat Modeling

## Summary
Threat modeling is the structured process of identifying what to protect, who might attack, and how — then deciding what to do about it. It turns security from a checklist into a design conversation repeated as the system changes.

## Details
- The core questions: what are we building, what can go wrong, what are we going to do about it, and did we do it?
- Common methods: STRIDE (spoofing, tampering, repudiation, information disclosure, DoS, elevation) and attack trees.
- Model early and often: the design phase is where mitigations are cheap; every architecture change re-runs the model.
- Outputs are ranked risks with owners and mitigations, plus the accepted risks made explicit.
- Tools help (drawing, data-flow diagrams) but the conversation is the product.
- For the mykb bundle, threat modeling covers the capture pipeline, the API, and the integrity of linked content.
- Worked example — STRIDE on the wiki sync: spoofing (unauthenticated capture injection), tampering (link poisoning), and DoS (fetch storms) rank highest; mitigations are auth, checksums, and rate limits.

Worked example — STRIDE on the wiki sync: spoofing (unauthenticated capture injection), tampering (link poisoning), and DoS (fetch storms) rank highest; mitigations are auth, checksums, and rate limits.

## Related
- [[wiki/compositions/security-engineering|Security Engineering]]
- [[wiki/tooling/secure-sdlc|Secure SDLC]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
- [[wiki/compositions/security-engineering|Threat Modeling]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/compositions/zero-trust-architecture|Zero-Trust Architecture]]
- [[wiki/communities/supply-chain-attacks|Supply-Chain Attacks]]
- [[wiki/communities/typosquatting|Typosquatting]]
- [[wiki/security/container-hardening|Container Hardening]]
