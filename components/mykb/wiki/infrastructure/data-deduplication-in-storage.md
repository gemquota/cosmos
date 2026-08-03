---
type: "concept"
title: "Data Deduplication in Storage"
description: "Removing duplicate blocks to save capacity at write time"
tags: ["deduplication", "storage", "capacity", "backup"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Deduplication in Storage

## Summary
Data deduplication removes duplicate blocks at write time, storing one copy and pointing every duplicate at it — saving capacity on data with redundancy, which is precisely the shape of backups, VM images, and versioned files. Where compression squeezes bytes within a file, deduplication collapses identical chunks across files and versions, so its savings are complementary and often larger.

## Details
- The mechanism: incoming data is split into chunks (fixed-size blocks or content-defined chunks), each chunk is hashed (SHA-1/SHA-256), and the hash is looked up in a chunk index. If the hash exists, the new data is not stored — a reference to the existing chunk is recorded instead; if not, the chunk is stored and indexed. Content-defined chunking (CDC) is the important refinement: chunk boundaries are determined by the data's content (a rolling hash finding stable cut points) rather than fixed offsets, so a one-byte insertion in a file shifts only the affected chunks instead of invalidating every subsequent chunk — which is why CDC makes dedup effective on versioned files.
- Where it pays: backup systems (the canonical case — daily backups of mostly unchanged data dedupe 20-50x), VM and container images (base layers shared across many VMs), and versioned file stores. The savings ratio depends on redundancy: databases with random writes dedupe poorly; logs, archives, and backup streams dedupe spectacularly. The design decision is chunk size: small chunks catch more duplicates but inflate the index and metadata overhead; large chunks reduce index size but miss duplicates at the boundaries — so chunk size is tuned per workload.
- The costs and failure modes: the chunk index itself consumes memory and storage (for petabyte dedup stores, the index is a real design problem — often sharded or on disk); deduplication adds write latency (hashing and lookup on every chunk); and there is a data-integrity risk — if the chunk store corrupts, every logical file referencing the chunk corrupts, which is why dedup stores validate (hash-checking) and replicate. The silent killer is index loss: losing the index can make stored data unrecoverable, so the index needs the same protection as the data.
- Deduplication vs compression: dedup removes cross-object redundancy, compression removes within-object redundancy; the two combine (dedup first, then compress each unique chunk) for maximum savings, which is the standard backup-appliance architecture.
- For mykb: dedup connects to the storage cluster — capacity planning, backup strategies, and block/file storage — and its index-vs-data reliability tradeoff is the classic case study for storage integrity.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]] — related coverage in the same cluster
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]] — related coverage in the same cluster
- [[wiki/infrastructure/data-plane-versus-control-plane|Data Plane vs Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
