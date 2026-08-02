---
type: "concept"
title: "Zero-Trust Architecture"
description: "Never trust, always verify: securing every request regardless of origin"
tags: ["zero-trust", "security", "architecture", "identity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://csrc.nist.gov/pubs/sp/800/207/final", "https://en.wikipedia.org/wiki/Zero_trust_security_model"]
---

# Zero-Trust Architecture

## Summary
Zero-trust architecture removes implicit trust: every request — inside or outside the network — is authenticated, authorized, and continuously verified. NIST SP 800-207 frames it as identity-based access control with micro-segmentation, least privilege, and continuous monitoring.

## Details
- The core: no network location implies trust; every access decision uses identity, device state, and policy.
- Pillars: identity-centric access, micro-segmentation, least privilege, and continuous verification.
- Implementation: identity-aware proxies, mTLS, short-lived credentials, and policy engines that re-check continuously.
- The journey is incremental: start with crown-jewel assets and expand the perimeter of verification.
- Zero trust is a model, not a product — it changes how access decisions are made everywhere.
- For the mykb bundle, zero trust means the wiki API authenticates every request and grants scoped, short-lived access.
- Worked example — the wiki sync uses mTLS between nodes, short-lived tokens for the API, and a policy engine that denies any request lacking current proof of identity and device health.

Worked example — the wiki sync uses mTLS between nodes, short-lived tokens for the API, and a policy engine that denies any request lacking current proof of identity and device health.

## Related
- [[wiki/compositions/identity-management|Identity Management]]
- [[wiki/compositions/authentication-patterns|Authentication Patterns]]
- [[wiki/compositions/authorization-models|Authorization Models]]
- [[wiki/security/zero-trust|Zero Trust]]
- [[wiki/api-protocols/mtls|mTLS]]
- [[wiki/compositions/security-engineering|Security Engineering]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/security/tls|TLS]]
