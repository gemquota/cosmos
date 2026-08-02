---
type: "concept"
title: "Content-Addressable Storage"
description: "Storage where an item's address is derived from its content hash"
tags: ["storage", "hashing", "deduplication", "cas"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Content-addressable_storage", "https://docs.ipfs.tech/concepts/content-addressing/"]
---

# Content-Addressable Storage

## Summary
Content-addressable storage (CAS) names every item by the hash of its contents, so identical content collapses to one address and corruption becomes detectable. Git's object store and IPFS are the best-known examples.

## Details
- **Mechanics** — `address = hash(content)`; lookup by address returns the item or proves it is absent.
- **Benefits** — automatic deduplication, integrity checking, and immutable history.
- **Agent relevance** — hashing note content would let mykb detect duplicate captures and track exactly when a page changed.
- Content-addressable storage (CAS) addresses data by a cryptographic hash of its content, so the address changes if and only if the content changes.
- The properties fall out of the design: identical content deduplicates naturally, integrity is verified by hashing, and addressing is immutable — an address always names the same bytes.
- The costs are content lookups (a map from hash to location), garbage collection for unreferenced content, and the need for a trust anchor for hash algorithms.
- CAS is the foundation of deduplication systems, IPFS, git object storage, and many backup and container registries.
- **Worked example / comparison** — Worked example — a wiki's export stores each article blob under its hash; two sessions that produce identical articles share one blob, and any corruption is detected on read.
- For mykb, content-addressable storage is documented as the mechanism that makes deduplication and integrity checks natural.

## Related
- [[wiki/data-storage/data-versioning|Data Versioning]]
- [[wiki/data-storage/deduplication|Deduplication]]
- [[wiki/memory/provenance|Provenance]]
- [[wiki/data-storage/vector-databases|Vector Databases]]
- [[wiki/data-storage/index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
