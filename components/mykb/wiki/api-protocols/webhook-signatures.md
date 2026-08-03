---
type: "concept"
title: "Webhook Signatures"
description: "HMAC or asymmetric signatures proving webhook payload authenticity"
tags: ["webhooks", "security", "signatures", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Webhook Signatures

## Summary
Webhook signatures prove that a delivery genuinely came from the producer and was not altered in transit. The producer computes a cryptographic signature over the payload with a secret the subscriber also holds, and the subscriber recomputes and compares before processing, which blocks forged events and tampered bodies from reaching application logic.

## Details
- Mechanism: the common scheme is HMAC: the producer computes `HMAC-SHA256(secret, raw_body)` and sends it in a header like `X-Signature` or `X-Hub-Signature-256`; the subscriber recomputes over the exact raw body bytes it received and compares with a constant-time comparison. Signing the raw body rather than a re-serialized version is essential — if the subscriber parses and re-serializes before verifying, whitespace or key-order differences break or, worse, let an attacker smuggle changes past a loose comparison. Asymmetric variants (Ed25519 or RSA) let many subscribers verify with a public key while only the producer holds the signing secret.
- Concrete examples: GitHub signs webhook payloads with HMAC-SHA256 using a per-webhook secret and sends `X-Hub-Signature-256`; Stripe signs with a timestamped scheme to limit replay windows; a custom delivery pipeline signs with Ed25519 so internal consumers verify without sharing a secret. The timestamp or delivery-ID in the signed envelope is what lets receivers bound replay attacks — a captured, validly signed delivery should not be replayable hours later.
- Failure modes: the classic failures are verifying a re-parsed body instead of the raw bytes, using a non-constant-time comparison (enabling timing attacks), shipping with an empty or default secret, and not rotating secrets after an endpoint is decommissioned. Signature-scheme confusion (mixing HMAC and asymmetric variants) and accepting unsigned deliveries when a signature header is absent both silently disable the protection. Replay is the other gap: a signature proves authenticity and integrity, not freshness, so without a timestamp or delivery-ID check an attacker can replay old legitimate events to trigger duplicate side effects.
- Operational tradeoffs: signatures protect the subscriber, but the producer must manage per-subscriber secrets, secret rotation (with overlapping valid secrets during transition so old deliveries verify), and signing performance at scale. Subscribers should fail closed: no header or bad signature means reject, log the mismatch, and surface it in delivery dashboards. Standardized envelopes (like the IETF webhooks signature draft) reduce integration friction, but the raw-body rule and constant-time comparison remain non-negotiable.
- RSIS3/mykb relevance: webhook-style callbacks in RSIS3 (session captures, loop notifications) should carry the same signatures so a compromised or spoofed endpoint cannot inject false knowledge into MyKB — authenticity at the ingestion boundary protects the memory layer's integrity.

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-events|Webhook Events]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-topics|Webhook Topics]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]] — related coverage in the same cluster
- [[wiki/api-protocols/webhooks|Webhooks]] — related coverage in the same cluster
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
