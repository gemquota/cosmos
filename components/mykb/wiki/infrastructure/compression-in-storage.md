---
type: "concept"
title: "Compression in Storage"
description: "Inline and post-process compression to shrink stored data"
tags: ["compression", "storage", "capacity", "filesystem"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Compression in Storage

## Summary
Compression in storage shrinks data before it is written (inline) or after it is written (post-process), trading CPU cycles and latency for capacity. It is one of the highest-leverage capacity levers in storage systems: text, logs, and databases routinely compress 2-10x, and compression is effectively free when the data is already being moved through a CPU on the write path.

## Details
- Inline compression runs on the write path: the data is compressed before hitting disk, so the compressed form is all that is ever stored — capacity savings are immediate, and the read path decompresses on access. Post-process compression runs as a background job on data already written (common in backup and archival systems), which avoids write-path latency but temporarily stores the uncompressed data and needs a job scheduler and enough headroom to rewrite. Hybrids combine both: inline for known-compressible data, post-process for everything else.
- The algorithm choice is the main engineering decision. Fast, symmetric algorithms (LZ4, Zstd at low levels, Snappy) prioritize throughput — they compress modestly (1.5-3x on typical data) but add microseconds; heavy algorithms (Zstd at high levels, gzip, bzip2) reach 3-10x on compressible data but cost CPU and latency, which matters on the read path when every access must decompress. Zstd's position in the middle — near-LZ4 speed with near-gzip ratios, plus a built-in dictionary mode for small records — has made it the default modern choice. The tradeoff is always data-dependent: logs and JSON compress dramatically; already-compressed formats (JPEG, video, encrypted data) compress to almost nothing and waste CPU if forced.
- Where compression lives matters: filesystem-level (btrfs/zfs transparent compression), block-level (storage arrays compressing in silicon), database-level (columnar compression — the foundation of warehouse efficiency, where per-column dictionaries and run-length encoding give 10-100x on repetitive columns), and object-level (cloud storage classes with compression options). Each layer has different visibility: database and filesystem compression are automatic and transparent; application-level compression gives the developer control but requires every reader to decompress.
- Failure modes: compressing incompressible data (wasted CPU, no savings — mitigated by compressibility checks and skip thresholds), CPU saturation on the read path for hot data (the decompression cost exceeds the I/O savings), and fragmentation or alignment overhead in block devices.
- For mykb: compression connects to the storage cluster — block/file storage, deduplication (its sibling), and capacity planning — and the same compress-vs-skip logic applies to the wiki's own artifacts (text compresses well; PNGs and videos do not).

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]] — related coverage in the same cluster
- [[wiki/devops-infra/compression-and-brotli|Compression & Brotli]] — related coverage in the same cluster
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
