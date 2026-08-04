---
type: "entity"
title: "ADDR"
description: "ADDR: addressing schemes for URLs, memory, and resource identity"
tags: ["entity", "acronym", "ajax", "alpine", "android", "angular", "addressing"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# ADDR

## Summary

ADDR is the frontend entity for addressing: how resources are located and referenced, from URLs to memory addresses. Consistent addressing is what makes systems linkable, cacheable, and debuggable. It matters because broken or ambiguous addresses are a top source of integration failures. Addressing discipline pays off as a system grows: stable addresses mean fewer broken references.

## Details

- **Definition** — Addressing assigns stable, resolvable identities to resources so they can be found, referenced, and shared.
- **URLs** — Uniform resource locators combine scheme, host, path, and query to address web resources precisely.
- **Memory addressing** — Programs reference data through addresses; pointer bugs are among the most common and dangerous failure modes.
- **Resource identity** — Content-addressed or ID-based identity makes references robust to location changes and duplication.
- **Canonicalization** — Normalizing addresses prevents duplicate entries for the same resource and simplifies comparison.
- **Failure modes** — Relative versus absolute confusion, encoding mismatches, and stale links break navigation and data integrity.
- **Worked example** — An SPA routes by URL path, looks up resources by stable ID, and normalizes trailing slashes to avoid duplicate API calls.
- **Practical relevance** — The wiki itself relies on addressing: wikilinks are addresses, and broken links are broken addresses.
- **Encoding** — Addresses embedded in URLs need correct escaping; encoding bugs corrupt paths and query strings.
- **Indirection** — Named references resolved to addresses decouple users from location changes.
- **Lifecycle** — Retired addresses need redirects or tombstone records so old references fail loudly and helpfully.
- **Testing** — Address parsing and generation belong in unit tests, where edge cases like empty and malformed values are cheap to cover, and canonical forms prevent one resource from accruing many addresses.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/aaaa|AAAA]] — hostname addressing records
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/area|AREA]] — cluster acronym neighbor
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — asset addressing in builds
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/aaaa|AAAA]] — hostname addresses
