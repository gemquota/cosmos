---
type: "concept"
title: "Public Key Infrastructure"
description: "Systems for creating, distributing, validating, and revoking public-key certificates"
tags: ["pki", "certificates", "cryptography", "trust"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Public_key_infrastructure"]
---

# Public Key Infrastructure

## Summary

Public key infrastructure (PKI) is the set of roles, policies, and procedures that manage public-key certificates: certificate authorities (CAs) issue them, relying parties validate them, and revocation mechanisms retire them. It turns raw key pairs into identities others can trust. PKI matters because nearly all encrypted, authenticated traffic — TLS, code signing, email, client certificates — depends on a chain of trust rooted in CAs. RSIS3's security posture stands on PKI decisions: which roots are trusted, which keys sign what, and how quickly bad keys can be revoked.

## Details

- Components: CAs issue certificates, registration authorities verify identity, relying parties validate, and repositories (CRL/OCSP responders) publish revocation.
- Chain of trust: leaf certificates chain up through intermediate CAs to a root CA in a trust store; the browser or OS trust store defines the root set.
- Certificate contents: X.509 fields bind a public key to a subject with validity periods, key usage, and extensions (SANs) — detailed in RFC 5280.
- Key protection: private keys for CAs and TLS live in hardware security modules (HSMs) or secure enclaves to resist theft.
- Lifecycle: issuance, renewal, rotation, and revocation; automation via ACME (Lets Encrypt) collapses the cost of short-lived certificates.
- Failure modes: CA compromise (single point of trust), mis-issued certificates, and revocation gaps when clients ignore CRL/OCSP.
- For mykb, a small internal CA or delegated ACME issuance can give agents machine identities — a PKI pattern that scales better than shared secrets.

## Related

- [[wiki/security-auth/digital-certificates|Digital Certificates]] — the artifacts PKI manages
- [[wiki/identity/key-rotation|Key Rotation]] — lifecycle hygiene for PKI keys
- [[wiki/identity/client-certificates|Client Certificates]] — PKI identities for machines and users
- [[wiki/security/certbot|Certbot]] — automated certificate client
- [[wiki/security/lets-encrypt|Let's Encrypt]] — public CA with ACME automation
- [[wiki/security/tls|TLS]] — the dominant consumer of PKI
- [[wiki/concepts/triad-architecture|Triad Architecture]] — machine identities for triad services
