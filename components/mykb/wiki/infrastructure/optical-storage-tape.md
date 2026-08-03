---
type: "concept"
title: "Optical Storage & Tape"
description: "Cheap archival media for cold data"
tags: ["tape", "optical", "archival", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Optical Storage & Tape

## Summary
Optical storage and tape are the archival tier of the storage hierarchy: media optimized for cold data — data that must be kept but is rarely read. Tape wins on raw economics (the lowest cost per byte in the industry), optical (blu-ray, archival discs) wins on media longevity and physical robustness, and both trade random access and speed for their defining property: cheap, durable, long-term retention.

## Details
- Tape: the medium is a magnetic tape in a cartridge (LTO is the standard — Linear Tape-Open, with generations roughly doubling capacity: LTO-9 ~18TB native, LTO-10 and beyond planned). The economics are unmatched: tape costs a small fraction of disk per byte, consumes almost no power when idle (it sits in a library, not spinning), and cartridges last decades. The operational model is the tape library: a robot moves cartridges between slots and drives, software (LTFS, backup suites) manages the media pool, and backups stream sequentially onto tape — tape is fundamentally sequential, so it is for bulk writes and rare whole-file reads, not random access. The access reality: retrieving a file from tape means finding the cartridge (robotic), loading it, and seeking — minutes, not milliseconds, which is why tape sits at the bottom of the storage pyramid (hot disk → warm object → cold tape).
- Optical: archival-grade blu-ray discs and the M-DISC class are rated for decades of data life, are physically robust (no magnetic fields, no head crashes), and are immune to the ransomware/bit-rot classes that plague connected media. The tradeoffs: capacity per disc is small (100-300GB per BD-R XL) and write/read is slow, so optical is for select archives (legal holds, compliance copies, irreplaceable records) rather than bulk data. The discipline: optical media still need verification (read-back after write) and periodic re-reading, because no medium is truly permanent.
- The failure modes of archival storage: media degradation (tape binder breakdown, dye degradation on discs — countered by environmental storage and periodic recertification), format/device obsolescence (a tape format whose drives no longer exist is an unreadable archive — the reason migration is part of archival planning), and the silent-corruption class (an archive that is never read is an archive that may be dead; the practice is periodic sampling reads and checksum verification).
- The decision framework: tape for bulk cold data with a library and software managing it; optical for small, high-value, long-horizon records; disk/object for anything that might be needed promptly. The common mistake is treating archival as "just cheap storage" without the migration and verification programs that make archives readable decades later.
- For mykb: tape and optical anchor the archival branch of the storage cluster — the cold end of the hot/cold tiering spectrum.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]] — related coverage in the same cluster
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]] — related coverage in the same cluster
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
