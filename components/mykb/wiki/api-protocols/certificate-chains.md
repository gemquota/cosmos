---
type: "concept"
title: "Certificate Chains"
description: "Hierarchies of CA-signed X.509 certificates that establish server identity in TLS"
tags: ["tls", "certificates", "security", "pkix"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Certificate Chains

## Summary
Hierarchies of CA-signed X.509 certificates that establish server identity in TLS. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Leaf, intermediate, and root certificates form the TLS trust path
- Chain completeness matters: servers should send intermediates, not roots
- Open question — how do short-lived certs change chain caching?

## Related
- [[wiki/api-protocols/tls-https|TLS and HTTPS]] — related coverage in the same cluster
- [[wiki/api-protocols/ocsp-stapling|OCSP Stapling]] — related coverage in the same cluster
- [[wiki/api-protocols/certificate-chains|Certificate Chains]] — related coverage in the same cluster
- [[wiki/api-protocols/ocsp-stapling|OCSP Stapling]] — related coverage in the same cluster
- [[wiki/api-protocols/tls-certificates|TLS Certificates]] — related coverage in the same cluster
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
