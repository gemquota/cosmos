---
type: "concept"
title: "Data Retention and Lifecycle"
description: "Keeping data long enough, not forever"
tags: ["retention", "lifecycle", "governance", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_retention", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html"]
---

# Data Retention and Lifecycle

## Summary

Retention policies define how long data is kept and when it is archived or deleted.
They balance business need, cost, and legal requirements.
Lifecycle automation makes policies operational.
Retention is a business decision with legal consequences; automate it but keep owners accountable.

## Details

- Retention by type: operational, analytical, archival, legal hold.
- Automate deletion/archival with lifecycle rules.
- Privacy laws (GDPR/CCPA) impose maximums, not just minimums.
- Legal holds override routine deletion.
- Document retention decisions and review them periodically.
- Document retention classes and review them with legal.
- Deletion should be irreversible by design; test it.
- Retention policies turn storage from a growing bill into a governed asset.

## Related

- [[wiki/data-storage/hot-and-cold-data-tiering|Hot And Cold Data Tiering]] — tiering
- [[wiki/infrastructure/data-privacy-gdpr-and-ccpa|Data Privacy Gdpr And Ccpa]] — legal limits
- [[wiki/infrastructure/compliance-and-audit-trails|Compliance And Audit Trails]] — audit
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — existing note
- [[wiki/data-storage/downsampling-and-retention-policies|Downsampling And Retention Policies]] — time-series
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions

