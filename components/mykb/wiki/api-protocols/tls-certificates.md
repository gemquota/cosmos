---
type: "concept"
title: "TLS Certificates"
description: "X.509 certificates, CAs, chains, and validation"
tags: ["tls", "certificates", "x509", "pki", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc5280", "https://letsencrypt.org/how-it-works/"]
---

# TLS Certificates

## Summary
TLS certificates are X.509 documents binding a public key to an identity (a domain or client). A certificate chain runs from the leaf through intermediate CAs to a root in the client's trust store, and validation checks signatures, validity dates, revocation, and hostname — the machinery that makes TLS authentication trustworthy.

## Details
- X.509 structure: version, serial, issuer, subject, validity period, public key, extensions (SAN, key usage, EKU), and the issuer's signature.
- Subject Alternative Name (SAN): holds the domains or identities the certificate is valid for; browsers ignore the legacy CN field.
- Chains: leaf signed by intermediate, intermediate signed by root; servers must send the full chain (minus root) so clients can build a path to a trusted root.
- Validation steps: verify each signature, check expiry and notBefore, confirm hostname against SAN, honor key usage, and check revocation (OCSP/CRL).
- Automation: ACME (Let's Encrypt) issues and renews certificates automatically via HTTP-01, DNS-01, or TLS-ALPN challenges.
- PKI trust: the system's security rests on root CA compromise, so pinning (rare), transparency logs (CT), and short-lived certs reduce blast radius.
- Private keys: guard them — a leaked private key lets attackers impersonate the identity until the cert expires or is revoked.

## Related
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — certificates authenticate the handshake
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — the PKI that issues and validates certs
- [[wiki/api-protocols/mtls|mTLS]] — client-side certificates
- [[wiki/security-auth/digital-certificates|Digital Certificates]] — the broader certificate landscape
- [[wiki/api-protocols/dns-srv-records|DNS SRV Records]] — service discovery still needs certs for TLS
