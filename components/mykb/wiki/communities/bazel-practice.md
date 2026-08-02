---
type: "concept"
title: "Bazel Practice"
description: "Using Bazel's content-addressed build graph for large-scale reproducible builds"
tags: ["bazel", "builds", "monorepos", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Bazel Practice

## Summary
Bazel builds from a declared dependency graph with content-addressed caching, parallelism, and remote execution. It shines in large monorepos where incremental correctness and caching at scale matter; it costs configuration discipline.

## Details
- BUILD files declare targets and deps explicitly — the graph enables correctness and caching.
- Remote caches and execution make CI fast by reusing work across machines.
- Bazel is strict: everything must be declared, which is its power and its friction.
- mykb relevance: a multi-language wiki toolchain could share Bazel's cache across jobs.

## Related
- [[wiki/communities/build-caching|Build Caching]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
- [[wiki/dev-tools/monorepos|Monorepos]]
- [[wiki/dev-tools/build-systems|Build Systems]]
- [[wiki/communities/nix-practice|Nix Practice]]
