---
type: "concept"
title: "Surrogate vs Natural Keys"
description: "Generated IDs versus business keys and their trade-offs"
tags: ["surrogate-keys", "natural-keys", "primary-keys", "schema-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Surrogate_key", "https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html"]
---

# Surrogate vs Natural Keys

## Summary
A surrogate key is a generated identifier (auto-increment, UUID, snowflake) with no business meaning; a natural key is a real-world value like a passport number or email. Surrogates dominate practice because business values change, but natural keys enforce uniqueness semantics that surrogates do not.

## Details
- **Surrogate strengths** — stable, compact, and immune to business-rule changes; InnoDB likes a compact integer clustering key; UUIDs (v7 with time ordering) work well in distributed systems where sequences are impractical.
- **Surrogate weaknesses** — without a unique constraint on the natural key, duplicates sneak in; every table needs extra join work, and meaningless IDs make debugging and data entry harder.
- **Natural key strengths** — the value is meaningful, deduplicates at write time, and saves a join or lookup; stable natural keys like ISO country codes are excellent keys.
- **Natural key weaknesses** — values change (emails, VAT numbers, usernames), may exceed index width limits, and cascade through foreign keys when corrected.
- **Best practice** — keep the surrogate PK for references and add unique constraints on natural keys; InnoDB and Postgres both make this cheap, and it buys the best of both worlds.
- **Warehouse note** — dimensional models often use surrogate dimension keys with natural keys as attributes, isolating the warehouse from source-system changes.

## Related
- [[wiki/data-storage/database-constraints|Database Constraints]] — unique constraints over natural keys
- [[wiki/data-storage/clustered-tables|Clustered Tables]] — what the PK physically orders
- [[wiki/data-storage/data-modeling|Data Modeling]] — where key decisions are made
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — surrogate dimension keys
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — key choice drives distribution
