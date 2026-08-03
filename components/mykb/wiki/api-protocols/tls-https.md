---
type: "concept"
title: "TLS and HTTPS"
description: "Transport Layer Security providing confidentiality, integrity, and authentication for HTTP"
tags: ["tls", "https", "security", "crypto", "certificates"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc8446", "https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security"]
---
# TLS and HTTPS

## Summary
TLS encrypts traffic between clients and servers, authenticates the server (and optionally the client) with certificates, and detects tampering. HTTPS is HTTP over TLS and is mandatory for cookies, credentials, and modern web APIs. TLS 1.3 is the current standard; 1.2 still appears in legacy stacks.

## Details
- **Handshake** — the client sends supported ciphers and keyshares; the server picks a suite, sends its certificate chain, and the two derive session keys; TLS 1.3 cut this to one round trip (0-RTT with caveats).
- **Certificate trust** — servers present a chain from leaf to a CA root; clients validate signatures, validity, hostname, and revocation.
- **Forward secrecy** — ephemeral Diffie-Hellman keys mean past traffic stays secret if long-term keys leak.
- **Operational musts** — HSTS forces HTTPS, certificate transparency deters misissuance, and short-lived certs shrink compromise windows.
- **Worked example** — the mykb bundle would be served over HTTPS with Let's Encrypt certificates; the wiki would track TLS handshakes and certificate chains for ops.
- **Relevance** — every curl-verified source fetch and every API call in RSIS3 rides on TLS assumptions.

## Related
- [[wiki/api-protocols/certificate-chains|Certificate Chains]] — adjacent concept in this wiki
- [[wiki/api-protocols/ocsp-stapling|OCSP Stapling]] — adjacent concept in this wiki
- [[wiki/api-protocols/tls-certificates|TLS Certificates]] — existing coverage
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — existing coverage
- [[wiki/api-protocols/mtls|mTLS]] — existing coverage
