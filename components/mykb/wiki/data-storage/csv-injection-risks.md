---
type: "concept"
title: "CSV Injection Risks"
description: "Formula injection attacks through spreadsheet import"
tags: ["csv", "injection", "security", "spreadsheets"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CSV Injection Risks

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Cells starting with =, +, -, @ are evaluated as formulas when opened in Excel.
- Malicious values can exfiltrate data or trigger external calls.
- Mitigate: sanitize leading characters, use CSV-safe quoting, or disable formulas.
- Treat CSV exports of user data as untrusted input.

## Related

- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — injection family
- [[wiki/security-auth/data-exfiltration|Data Exfiltration]] — exfiltration risk
- [[wiki/data-storage/excel-and-spreadsheet-data|Excel And Spreadsheet Data]] — spreadsheet context
- [[wiki/data-storage/data-import-export-patterns|Data Import Export Patterns]] — export flows
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
