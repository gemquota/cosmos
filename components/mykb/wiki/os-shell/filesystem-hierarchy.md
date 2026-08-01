---
type: "concept"
title: "Filesystem Hierarchy"
description: "The standard directory layout of Unix-like systems that defines where files and programs live"
tags: ["filesystem", "fhs", "unix", "directories"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html"]
---

# Filesystem Hierarchy

## Summary
The Filesystem Hierarchy Standard (FHS) defines where programs, configuration, data, and device files live on Linux and other Unix-like systems. Knowing the hierarchy is how developers find their way around any machine and write portable scripts.

## Details
- Root directories: /bin and /usr/bin hold programs, /etc holds configuration, /var holds variable data, /tmp holds scratch space, /home holds user files.
- /usr historically held 'user' programs and now hosts almost all system software; /usr/local is for locally installed software.
- /proc and /sys are virtual filesystems exposing kernel and device state as files — cat /proc/cpuinfo works because everything is a file.
- Permissions, symlinks, and mount points (like /mnt and /media) tie the hierarchy to the permissions model.
- The FHS is a consensus standard, not a law; macOS and BSDs differ in details (e.g., /Applications, /usr/local defaults).
- RSIS3 relevance: cosmos lives under a home directory; knowing the hierarchy helps scripts and agents locate data predictably.
- Worked example: `find /etc -name '*.conf'` explores configuration; `df -h /var` checks variable data capacity.

## Related
- [[wiki/os-shell/path-resolution|Path Resolution]] — how absolute and relative paths traverse the hierarchy
- [[wiki/os-shell/permissions-model|Permissions Model]] — who may read or write each hierarchy node
- [[wiki/os-shell/symlinks|Symlinks]] — aliases that let one file appear in several places
- [[wiki/os-shell/environment-variables|Environment Variables]] — config that lives outside the hierarchy
- [[wiki/devops-infra/backups|Backups]] — what /var and /home mean for backup scope
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — where docs live matters for discovery
- [[wiki/concepts/project-lineage|RSIS3 Project Lineage]] — the project's own tree mirrors FHS conventions
