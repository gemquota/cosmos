---
type: "concept"
title: "Package Management"
description: "Installing, publishing, and resolving dependencies across ecosystems"
tags: ["package-management", "dependencies", "registries", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Package_manager", "https://en.wikipedia.org/wiki/Dependency_management"]
---

# Package Management

## Summary
Package managers (npm, pip, Maven, Go modules, cargo) resolve, download, and install dependencies from registries, with lockfiles pinning exact versions. They are the supply-chain front door: package hygiene is security hygiene.

## Details
- The resolution problem: given ranges, pick a consistent, valid set of versions — lockfiles record the answer.
- Registries are trust boundaries: integrity hashes, signatures, and scanning are table stakes.
- Reproducibility requires committing lockfiles and installing from them (npm ci, pip-tools, Cargo.lock).
- Publishing is permanent in most ecosystems: version discipline and canary tags prevent grief.
- Private registries and proxies (Artifactory, Verdaccio, devpi) add control and caching.
- For the mykb bundle, package management covers the tooling's dependencies with pinned, scanned, and locked installs.

Worked example — the wiki tooling uses pip with a committed requirements lock and a private index; CI installs from the lock, scans for vulnerabilities, and fails on critical findings.

## Related
- [[wiki/dev-tools/dependency-management|Dependency Management]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/communities/registry-practice|Registry Practice]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/communities/npm-practice|npm Practice]]
- [[wiki/dev-tools/package-managers|Package Managers]]
