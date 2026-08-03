---
type: "concept"
title: "OCSP Stapling"
description: "Serving a signed OCSP response with the handshake to skip the revocation round trip"
tags: ["tls", "certificates", "security", "pkix"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# OCSP Stapling

## Summary
OCSP stapling lets a TLS server fetch a signed, fresh certificate-revocation response from the CA and attach it to its own handshake. Clients get revocation status without an extra connection to the OCSP responder, removing latency and a privacy leak.

## Details
Online Certificate Status Protocol (OCSP) answers "is this certificate revoked?" The client-side check normally means a second connection to the CA's responder after the handshake — extra latency, and it leaks the site's identity to the responder. With stapling (RFC 6066), the server periodically fetches an OCSP response for its own certificate and includes it in the Certificate message of the handshake; the client verifies the staple's signature and freshness instead of making its own query.

The mechanism: the server queries the responder (often with a must-staple certificate that signals the intent), caches the response until near its nextUpdate, and presents it in every handshake. Clients that receive a valid staple skip their own OCSP call; clients that don't (or get an expired staple) fall back to a normal OCSP query or, in must-staple enforcement, refuse the connection. Revocation timing is bounded by the staple's freshness, so a recently revoked certificate can still be presented until the next staple refresh.

Concrete example: a high-traffic wiki site enables OCSP stapling. Browsers complete handshakes in one round trip instead of two, and the CA's responder sees almost no traffic from site visitors — only the server's periodic staple fetches. If the server stops stapling (config change, responder outage), clients quietly fall back to direct OCSP, so the failure mode is degraded latency, not broken TLS.

Failure modes: a must-staple certificate without stapling configured makes clients hard-fail, so the feature must be enabled before deploying must-staple; staples that are cached past nextUpdate are rejected, and clock skew on either side breaks freshness checks; and misconfigured servers that staple an unrelated certificate fail validation. Revocation latency is inherently higher than a live check — stapling trades immediacy for performance.

Operational tradeoffs: stapling is free performance and should be on for every TLS service; the configuration cost is a scheduled staple fetch and cache refresh. For revocation-critical decisions, pair stapling with short certificate lifetimes (automated renewal shrinks the revocation window) and, where supported, CRLite-style compact CRLs. Monitoring should alert when stapling stops being served.

RSIS3/mykb relevance: the deployed dashboards terminate TLS via their host; documenting the stapling configuration and must-staple choice gives RSIS3's ops checks a concrete TLS assertion.

## Related
- [[wiki/api-protocols/tls-https|TLS and HTTPS]]
- [[wiki/api-protocols/certificate-chains|Certificate Chains]]
- [[wiki/api-protocols/tls-certificates|TLS Certificates]]
- [[wiki/api-protocols/tls-handshake|TLS Handshake]]
- [[wiki/api-protocols/mtls|mTLS]]
