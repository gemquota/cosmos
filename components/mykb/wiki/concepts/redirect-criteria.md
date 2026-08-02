---
type: "concept"
title: "Redirect Criteria"
description: "When a page should exist only to forward readers to another article"
tags: ["redirect", "criteria", "navigation", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Redirect Criteria

## Summary
Redirect criteria cover pages whose only job is forwarding: alternate spellings, former titles after a rename, and common abbreviations pointing at the canonical article.

## Details
- A redirect preserves incoming links that would otherwise break when a slug changes, so the graph keeps working after renames.
- Redirects should be rare — each one is a small maintenance cost and a signal that naming should have been settled earlier.
- For mykb, slug-stability minimizes the need for redirects, and renaming-procedure decides when a redirect must be left behind.

## Related
- [[wiki/concepts/alias-criteria|Alias Criteria]]
- [[wiki/dev-tools/renaming-procedure|Renaming Procedure]]
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/dev-tools/slug-changes|Slug Changes]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/concepts/redirect-proposal|Redirect Proposal]]
