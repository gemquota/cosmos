---
type: "concept"
title: "HTTPS & TLS"
description: "How TLS authenticates servers and encrypts web traffic"
tags: ["https", "tls", "security", "encryption"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc8446",
  "https://www.rfc-editor.org/rfc/rfc2818",
]
---

# HTTPS & TLS

## Summary
HTTPS is HTTP carried over TLS, adding encryption, integrity, and server authentication to web traffic. TLS is the security layer of the modern Internet, also used by DNS, email, and internal services. Certificate management is the operational core of running HTTPS.

## Details
- TLS 1.3 (RFC 8446) simplified the handshake to one round trip, removed legacy cipher suites, and made forward secrecy mandatory.
- HTTPS is defined by RFC 2818: clients validate the server certificate against a trusted root and the requested hostname.
- Certificates are issued by Certificate Authorities and verified through the chain of trust; automation like ACME keeps issuance manageable at scale.
- Perfect Forward Secrecy means session keys are derived per connection, so captured traffic cannot be decrypted later even if a long-term key leaks.
- Performance costs are real: handshake round trips, CPU for asymmetric crypto, and TLS session resumption all matter for latency.
- In infrastructure, TLS is often terminated at load balancers or proxies, shifting certificate lifecycle and re-encryption to the edge.

## Related
- [[wiki/cloud-infra/tls-1-3-session-resumption|TLS 1.3 Session Resumption]]
- [[wiki/cloud-infra/mutual-tls-internal-services|Mutual TLS for Internal Services]]
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
