---
type: "concept"
title: "Checksums & Hashing"
description: "sha256sum/md5sum usage and verification"
tags: ["checksums", "hashing", "sha256", "integrity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/sha256sum.1.html", "https://man7.org/linux/man-pages/man1/md5sum.1.html"]
---

# Checksums & Hashing

## Summary
Checksum tools compute a fixed-size digest of a file's contents, letting you verify that a download or copy is intact. sha256sum is the modern default; md5sum and sha1sum remain common but are cryptographically broken and should not be used for security checks.

## Details
- sha256sum file prints "digest  filename"; -c verifies against a .sha256 file of the same format and reports OK/FAILED per file.
- Generate check files with sha256sum *.iso > SHA256SUMS, then verify with sha256sum -c SHA256SUMS; output is safe with odd filenames if produced with the same tool.
- md5 and SHA-1 have practical collision attacks, so they are fine for casual integrity or dedup but never for authenticity.
- b2sum (BLAKE2) is fast and strong; sha512sum exists for longer digests. For authenticity, combine a digest with a signature (gpg --verify).
- cmp -s file1 file2 compares byte-for-byte without hashing; hashing shines for large or remote files.
- Hash-and-sort pipelines (sort | uniq) deduplicate, and data-storage tools like content-addressable storage use digests as names.
- Watch for line-ending issues in check files and always verify the check file's own integrity first.

## Related
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]] — digests as identifiers
- [[wiki/os-shell/tar-and-archive-tools|tar & Archiving]] — verify archives after download
- [[wiki/security/supply-chain-security|Supply Chain Security]] — signed hashes in release pipelines
- [[wiki/os-shell/compression-tools|Compression Tools]] — hashing what compression produces
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — digests prove build identity
