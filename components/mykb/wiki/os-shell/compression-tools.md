---
type: "concept"
title: "Compression Tools"
description: "gzip/xz/zstd/bzip2 tradeoffs and pipelines"
tags: ["compression", "gzip", "xz", "zstd", "bzip2"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/gzip.1.html", "https://man7.org/linux/man-pages/man1/xz.1.html"]
---

# Compression Tools

## Summary
gzip, bzip2, xz, and zstd compress data with very different speed-to-ratio tradeoffs. Choosing one is about the workload: fast streaming for logs, maximum density for distribution artifacts, and parallelism for big trees.

## Details
- gzip (DEFLATE) is ubiquitous and fast; level 1-9 tunes speed vs ratio, and it is the default for HTTP content-encoding and most .tar.gz files.
- bzip2 (Burrows-Wheeler) compresses better than gzip at similar speed on many inputs but is slower to decompress and has no good parallel story.
- xz (LZMA2) achieves the best ratios, especially for text and binaries, but is CPU-hungry; -T parallelizes on multicore machines.
- zstd targets the modern middle: ratio near xz at gzip-like speed, with levels up to 19 and a --long mode for large data.
- Every tool has transparent variants: zcat/zgrep/zless, xzcat, zstdcat, and --keep to preserve the original file.
- Pipes matter: compressors read stdin and write stdout, so tar cf - dir | zstd > tree.tar.zst composes cleanly.
- For backups and archives, prefer xz or zstd; for ephemeral caches, zstd level 1 or gzip -1; pigz and pzstd parallelize gzip/zstd.

## Related
- [[wiki/os-shell/tar-and-archive-tools|tar & Archiving]] — the compression consumer
- [[wiki/os-shell/rsync-synchronization|rsync]] — -z compression for transfer
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]] — integrity alongside compression
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — compressors in pipes
- [[wiki/cloud-infra/cold-storage|Cold Storage]] — density-driven format choices
