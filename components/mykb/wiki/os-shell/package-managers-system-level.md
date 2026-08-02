---
type: "concept"
title: "System-Level Package Managers"
description: "apt, dnf, pacman, and the packaging formats behind distros"
tags: ["packaging", "apt", "dnf", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.debian.org/doc/debian-policy/ch-binary.html",
  "https://wiki.archlinux.org/title/Pacman",
]
---

# System-Level Package Managers

## Summary
System-level package managers install, upgrade, and remove software across a Linux distribution, resolving dependencies from signed repositories. apt, dnf, and pacman each implement the same core model with different formats and policies. Package management defines how distributions stay consistent and secure.

## Details
- Packages bundle binaries, metadata, and dependency declarations in formats such as deb and rpm.
- The Debian policy manual defines how binary packages are structured and controlled.
- Arch's pacman documentation covers its repository and sync model.
- Dependency resolution, transaction safety, and signing protect the update path.
- Repositories are signed, and package managers verify signatures before install.
- In mykb, package managers connect to OS updates, golden images, and patch management.
- Transaction safety means an interrupted install leaves the system in a consistent state.
- Holding and pinning packages protects specific versions during migrations.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/devops-infra/package-signing-and-repositories|Package Signing & Repositories]]
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/infrastructure/row-level-security|Row Level Security]]
- [[wiki/infrastructure/column-level-security|Column Level Security]]
