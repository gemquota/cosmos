---
type: "concept"
title: "Cipher Suites"
description: "Named combinations of key exchange, authentication, encryption, and MAC algorithms in TLS"
tags: ["cipher-suites", "tls", "cryptography", "security", "config"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Cipher Suites

## Summary
A cipher suite names the algorithm set a TLS connection uses: key exchange, authentication, bulk encryption, and message authentication. Weak suites caused famous breaks like POODLE and BEAST.

## Details
- Modern preference: TLS 1.3 suites (AES-128/256-GCM, ChaCha20) with ECDHE key exchange.
- Servers configure allowed suites; clients pick from the intersection.
- Scan configs (SSL Labs, `openssl ciphers`) to avoid deprecated suites.

## Related
- [[wiki/security/tls|TLS]] — where suites apply
- [[wiki/security/https|HTTPS]] — suite negotiation in browsers
- [[wiki/security/zero-trust|Zero Trust Architecture]] — strong crypto baseline
- [[wiki/devops-infra/nginx|Nginx]] — suite configuration
- [[wiki/devops-infra/caddy|Caddy]] — secure defaults
