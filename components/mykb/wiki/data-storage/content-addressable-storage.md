---
type: "concept"
title: "Content-Addressable Storage"
description: "Storage where an item's address is derived from its content hash"
tags: ["storage", "hashing", "deduplication", "cas"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Content-Addressable Storage

## Summary
Content-addressable storage (CAS) names every item by the hash of its contents, so identical content collapses to one address and corruption becomes detectable. Git's object store and IPFS are the best-known examples.

## Details
- **Mechanics** — `address = hash(content)`; lookup by address returns the item or proves it is absent.
- **Benefits** — automatic deduplication, integrity checking, and immutable history.
- **Agent relevance** — hashing note content would let mykb detect duplicate captures and track exactly when a page changed.

## Related
- [[wiki/data-storage/data-versioning|Data Versioning]] — CAS is the substrate of versioned stores
- [[wiki/data-storage/deduplication|Deduplication]] — CAS makes duplicates impossible
- [[wiki/memory/provenance|Provenance]] — content hashes anchor provenance claims
- [[wiki/data-storage/vector-databases|Vector Databases]] — similarity search vs exact content addressing
- [[wiki/data-storage/index|Data Storage]] — the storage-tech namespace
