---
type: "concept"
title: "Experimental Metadata"
description: "Experimental metadata: provenance, configuration, and lineage that make experiments reproducible"
tags: ["ast", "entity", "guid", "ide", "orm", "spa", "metadata", "reproducibility"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# Experimental Metadata

## Summary

Experimental metadata is the provenance information that makes an experiment reproducible: the code version, configuration, inputs, and environment that produced each result. Without it, measurements cannot be trusted or re-run. It matters because metadata is what separates a one-off observation from reusable knowledge. Treating metadata as a first-class artifact keeps experiments auditable long after the original session ends.

## Details

- **Definition** — Experimental metadata records the conditions of an experiment: commit hashes, parameters, input data references, tool versions, and timestamps.
- **Provenance** — Every result should be traceable to the exact code and inputs that produced it, enabling audits and re-runs later.
- **Configuration capture** — Saving the full configuration, not just the interesting knobs, prevents silent differences between runs.
- **Data lineage** — Recording where inputs came from and what transformed them turns raw artifacts into a traceable pipeline.
- **Schema stability** — Metadata fields should be versioned so older records remain interpretable as the experiment tooling evolves.
- **Worked example** — A benchmark run writes a manifest with the code commit, seed, model parameters, and output hash alongside the measured results.
- **Failure modes** — Missing timestamps, unreferenced input files, and hand-edited results destroy reproducibility and inflate confidence.
- **Practical relevance** — Structured metadata stored alongside experiment records lets the wiki's knowledge graph connect outcomes to their causes.
- **Hash anchoring** — Content hashes link records to exact inputs, so tampering or accidental edits become detectable.
- **Version pinning** — Recording tool and dependency versions prevents the silent drift that invalidates comparisons.
- **Query surface** — Indexing metadata by experiment, date, and parameter makes past runs discoverable and reusable.
- **Retrieval practice** — Indexing metadata by experiment, date, and parameter values makes past runs discoverable and reusable by later sessions.

## Related

- [[wiki/development/categories/data-tools/subcategories/orm/experiment|Experiment]] — the activity that produces metadata
- [[wiki/development/categories/data-tools/subcategories/orm/analyzing|Analyzing]] — consuming metadata for insight
- [[wiki/development/categories/data-tools/subcategories/orm/integrity|Integrity]] — trustworthiness of recorded data
- [[wiki/development/categories/data-tools/subcategories/orm/platform|Platform]] — storage for metadata artifacts
