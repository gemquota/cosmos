---
type: "concept"
title: "OCSP Stapling"
description: "Serving certificate revocation status inside the TLS handshake to reduce round trips"
tags: ["tls", "certificates", "security", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# OCSP Stapling

## Summary
Serving certificate revocation status inside the TLS handshake to reduce round trips. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Stapling lets servers attach revocation status to the TLS handshake
- Staples are signed by the CA and reduce client-side OCSP round trips
- Open question — will AIA fetching fully replace OCSP checking?

## Related
- [[wiki/api-protocols/tls-https|TLS and HTTPS]] — related coverage in the same cluster
- [[wiki/api-protocols/certificate-chains|Certificate Chains]] — related coverage in the same cluster
- [[wiki/api-protocols/ocsp-stapling|OCSP Stapling]] — related coverage in the same cluster
- [[wiki/api-protocols/certificate-chains|Certificate Chains]] — related coverage in the same cluster
- [[wiki/api-protocols/tls-certificates|TLS Certificates]] — related coverage in the same cluster
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
