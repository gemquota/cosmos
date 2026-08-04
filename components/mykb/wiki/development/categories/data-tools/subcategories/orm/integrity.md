---
type: "entity"
title: "Integrity"
description: "Integrity: correctness and consistency of data enforced by constraints, transactions, and validation"
tags: ["entity", "cli", "ide", "orm", "data-integrity"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Integrity

## Summary

Integrity is the property of data being correct, consistent, and unchanged by unauthorized or erroneous operations. Databases enforce it with constraints, transactions, and referential rules. It matters because every downstream decision inherits the quality of the data it reads. Integrity is the property downstream analysis silently depends on, so it deserves explicit design.

## Details

- **Definition** — Data integrity means stored values remain accurate, consistent, and coherent with the rules that describe them over time.
- **Constraints** — Primary keys, unique constraints, check clauses, and not-null rules prevent invalid records at write time.
- **Referential integrity** — Foreign keys keep related rows aligned, preventing orphans when records are deleted or updated.
- **Transactions** — Atomic operations ensure a multi-step change either fully applies or fully rolls back, so partial writes cannot corrupt state.
- **Validation layers** — Schema validation, application-level checks, and input sanitization complement database rules where SQL cannot express the policy.
- **Checksums and hashes** — Hashing stored records detects silent corruption from disk errors or bugs, which is vital for long-lived archives.
- **Failure modes** — Disabled constraints, unchecked nullable fields, and non-transactional writes are the usual paths into corrupted state.
- **Practical relevance** — ORM layers expose integrity rules as model definitions, making correctness part of the schema rather than scattered code.
- **Audit trails** — Recording who changed what and when supports forensic recovery when integrity is breached.
- **Repair paths** — Detected corruption needs a defined recovery: restore, rebuild, or quarantine the affected records.
- **Testing** — Integrity rules should be exercised by tests that attempt invalid writes and assert rejection.
- **Integrity monitoring** — Periodic checksum and constraint scans detect silent decay early, turning integrity from an assumption into a maintained property.

## Related

- [[wiki/development/categories/data-tools/subcategories/orm/analyzing|Analyzing]] — consuming trustworthy data
- [[wiki/development/categories/data-tools/subcategories/orm/layer|Layer]] — where integrity rules live
- [[wiki/development/categories/data-tools/subcategories/orm/platform|Platform]] — shared data guarantees
- [[wiki/development/categories/data-tools/subcategories/orm/experiment|Experiment]] — valid measurements need integrity
