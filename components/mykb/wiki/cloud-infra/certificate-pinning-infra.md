---
type: "concept"
title: "Certificate Pinning in Infrastructure"
description: "Storing and rotating pinned leaf or intermediate certificates for internal TLS"
tags: ["certificates", "pinning", "tls", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Certificate Pinning in Infrastructure

## Summary

Certificate pinning binds a client to a specific certificate or public key, rejecting anything else — even from a trusted CA. It defends against CA compromise and some MITM setups, but its revocation problems make it a high-risk, mostly-discontinued practice for public clients.

## Details
- Mechanism: the client stores a hash of the expected leaf or intermediate public key (or the SPKI) and validates it alongside the chain; any certificate change that does not match breaks the connection. Chrome removed support for public key pinning (HPKP) in 2018; mobile apps still use pins (via network security config or libraries) where the app can ship updates.
- Concrete example: a banking app pins its API's intermediate CA so a fraudulent certificate from any other CA is rejected; an internal service mesh pins its own CA, making compromised public CAs irrelevant. The failure mode: when the pinned key rotates (cert renewal, provider change) without a client update, every connection fails — a self-inflicted outage.
- Failure modes: pinning the leaf instead of the SPKI (leaf renewals break the pin); pin expiry scenarios without a release pipeline fast enough to update clients; long-lived IoT devices that cannot be updated; and pinning third-party endpoints you do not control, guaranteeing breakage on their rotation.
- Operational tradeoffs: pinning buys CA-independence for high-value, updateable clients; for everything else, standard PKI plus certificate transparency monitoring and short-lived certs is the accepted defense. Prefer pinning the CA/SPKI over leaf pins and design a dual-pin rollout (new pin shipped before old pin expires).
- RSIS3/mykb relevance: the wiki's internal tooling would pin its private CA for API clients, with a rotation runbook recorded here so the loop never pins a leaf certificate.
- Rollout design: ship the new pin alongside the old (dual-pin) before rotation; a single-pin cutover is an outage scheduled around the cert's expiry. Monitor pin-verification failures as an early warning when a rotation goes wrong.

## Related
- [[wiki/cloud-infra/certificate-transparency|Certificate Transparency]]
