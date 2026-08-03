---
type: "concept"
title: "Certificate Chains"
description: "Hierarchies of CA-signed X.509 certificates that establish server identity in TLS"
tags: ["tls", "certificates", "security", "pkix"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Certificate Chains

## Summary
Certificate chains link a leaf certificate to a trusted root through intermediate certificates. Validation walks the chain checking signatures, validity periods, key usage, and revocation — and every link is a failure point.

## Details
A TLS server presents a chain: the leaf certificate (identifying the host), one or more intermediates, and a pointer to a root. The client validates by walking from the leaf toward a trust anchor in its store, checking each certificate's signature by the issuer above it, validity dates, key usage, and name constraints. The root is trusted out-of-band; intermediates are usually shipped by the server because clients don't have them cached.

The mechanism: for each link, the client verifies the issuer's signature over the child, that the child is within the issuer's validity and name constraints, and that the child's KeyUsage allows what it's used for (TLS serverAuth for the leaf). Path building may try multiple orders. Revocation (OCSP or CRL) is checked per certificate where available, though browsers increasingly treat OCSP as soft-fail. Certificate Transparency logs make misissuance detectable after the fact.

Concrete example: a wiki site uses a Let's Encrypt certificate. The server sends leaf plus an intermediate; the client already trusts the ISRG Root X1 and builds leaf -> intermediate -> root. If the server sends only the leaf, clients missing the intermediate fail with "unable to find valid certification path" — the classic incomplete-chain error that shows up in curl but not browsers (which cache intermediates).

Failure modes: incomplete chains (missing intermediates) break non-browser clients; expired intermediates with long-lived leaves fail validation even though the leaf is fresh; key usage mismatches (a CA cert without CA:TRUE, or a leaf without serverAuth) fail; and misissued or cross-signed chains can build to the wrong root. Clock skew breaks validity windows, and revocation checks that are hard-fail can brick sites when the OCSP responder is down.

Operational tradeoffs: including intermediates costs a few kilobytes per handshake but maximizes compatibility; letting clients fetch missing intermediates (AIA) adds latency and a network dependency; OCSP stapling removes one round trip but requires the server to fetch and refresh the staple. The operational baseline: always serve the full chain, automate renewal with ACME, monitor expiry (expiration alerts), and test with openssl s_client and a fresh client bundle.

RSIS3/mykb relevance: mykb's deployed sites are TLS-terminated; documenting the expected chain and expiry-monitoring rule keeps the ops loop from rediscovering broken-chain failures.

## Related
- [[wiki/api-protocols/tls-https|TLS and HTTPS]] — related coverage in the same cluster
- [[wiki/api-protocols/ocsp-stapling|OCSP Stapling]] — related coverage in the same cluster
- [[wiki/api-protocols/certificate-chains|Certificate Chains]] — related coverage in the same cluster
- [[wiki/api-protocols/ocsp-stapling|OCSP Stapling]] — related coverage in the same cluster
- [[wiki/api-protocols/tls-certificates|TLS Certificates]] — related coverage in the same cluster
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
