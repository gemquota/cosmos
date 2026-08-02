---
type: "readme"
title: "sources directory"
description: "Directory placeholder"
tags: [readme]

status: "growing"
---

## Readme

# Sources

Store ingested source pages here. One source page corresponds to one article, book, video, course, conversation, or dataset. The Sources directory is the front door of the knowledge base: every durable idea that enters the wiki should be traceable to a source page, so that claims can be checked, extended, and credited.
Each source page should have:

- YAML frontmatter with `type: source` and a stable `title` matching the original material
- Original publication/link metadata, including the URL, author, and date where known
- A short description of what the source covers and why it was captured
- Key claims extracted with backlinks to the concepts they support
- Uncertainty labeled as `to verify` whenever a claim has not been confirmed

Source pages are the evidence layer beneath synthesis notes and entity pages. When a synthesis distills patterns, it should reference the sources that support them, and when an entity page defines a term, its claims should point back to where they came from. This makes the difference between an opinionated wiki and a traceable one.
The [[wiki/sources/codebase-analysis|Codebase Analysis]] page is an example of a source page in practice: it records the analysis of a codebase as an ingestible source, with extracted claims ready to be linked into concepts.

Keeping the Sources directory tidy is part of wiki hygiene: every file here should be linked from somewhere, and every page should be findable through the index.

Source pages also record the context of capture: the session or date the material was ingested, why it was saved, and what questions it was expected to answer. This context helps later readers judge whether the source is still relevant, whether newer sources supersede it, and how confidently its claims can be reused. A source that is only a URL and a title is nearly useless; a source that documents its own provenance earns trust.

**Domain:** Sources

## Related

- [[wiki/sources/codebase-analysis|Codebase Analysis]]

## Concepts

- [Codebase Analysis — RSIS3 + mykb + myrsikb](codebase-analysis.md) — Codebase Analysis — RSIS3 + mykb + myrsikb
