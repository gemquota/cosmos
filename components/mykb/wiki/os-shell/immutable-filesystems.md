---
type: "concept"
title: "Immutable Filesystems"
description: "Read-only roots and overlay layers for tamper-resistant systems"
tags: ["immutable", "filesystem", "security", "ostree"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Immutable Filesystems

## Summary
Immutable filesystems make the operating system's root read-only, so the base system cannot be modified at runtime. Implementations range from a simple remount of `/` to layered designs (ostree, Fedora Silverblue, NixOS, ChromeOS) where the OS image is verified, versioned, and swapped atomically, while writable state lives in separate overlays or mount points.

## Details
- Mechanism: the core idea is to deny writes to the system tree. The simple form remounts `/` read-only (`mount -o remount,ro /`) and redirects mutable paths (`/etc`, `/var`, `/home`) to writable partitions or tmpfs overlays. The sophisticated form uses a content-addressed, immutable store: ostree stores each OS version as a verified tree of content-addressed objects, and "deploying" an update checks out a new tree and atomically switches the boot target — a failed boot falls back to the previous version. Overlayfs layers writable state (`/etc`, `/var`) on top of the read-only base, so applications see a normal filesystem while the base stays pristine.
- Concrete examples: Fedora Silverblue/Universal Blue ships an ostree-managed read-only `/usr` with `rpm-ostree` for layered packages and `toolbox`/`distrobox` containers for dev tools; NixOS builds the whole system from the Nix store with `/nix/store` as the immutable source; a security appliance remounts `/` read-only at boot and stores logs and config in `/var`; a kiosk uses a read-only root plus tmpfs overlays so any tampering or corruption vanishes on reboot; `atomic` container hosts use the same pattern for the host OS.
- Failure modes: the classic failures are writable-state assumptions — services that insist on writing to `/usr` or `/opt` break unless redirected, so package installs and config edits need the overlay/container escape hatch (which reintroduces mutability if not disciplined); updates fail if the bootloader or firmware partitions cannot be written; and verification failures (signature or checksum mismatch) can strand a system between versions. Misconfigured overlays that are too permissive (whole `/` writable via overlay) defeat the security benefit entirely.
- Operational tradeoffs: immutability buys tamper resistance, reliable rollback, and reproducible deployments — the base image is a versioned artifact, not an accumulating pile of state — at the cost of flexibility: ad hoc installs require containers or layered packages, some legacy software refuses to run, and the mental model of "edit files in /" must be abandoned. The modern guidance: for servers and workstations that can absorb it, an immutable base plus containerized tooling and a writable `/var`/`/etc` overlay is a strong default; for systems needing arbitrary package installs, the mutable model remains simpler.
- RSIS3/mykb relevance: the wiki's snapshot discipline would be immutability applied to knowledge: read-only, versioned corpus states with atomic promotion and rollback, exactly the ostree model — and the same "verify before deploy, roll back on mismatch" loop is what RSIS3 checkpoints would encode.

## Related
- [[wiki/os-shell/journaling-filesystems|Journaling Filesystems]]
- [[wiki/os-shell/copy-on-write-filesystems|Copy-on-Write Filesystems]]
- [[wiki/os-shell/disk-partitioning-and-filesystems|Disk Partitioning & Filesystems]]
- [[wiki/os-shell/fuse-and-user-space-filesystems|FUSE & User-Space Filesystems]]
