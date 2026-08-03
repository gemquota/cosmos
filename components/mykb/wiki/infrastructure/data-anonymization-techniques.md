---
type: "concept"
title: "Data Anonymization Techniques"
description: "Irreversibly de-identifying data while preserving analytical utility"
tags: ["anonymization", "privacy", "pii", "data-protection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Anonymization Techniques

## Summary

Anonymization removes or perturbs identifiers so individuals cannot be re-identified from the released data. The goal is de-identification with utility: the data remains useful for analysis while the link from data to person is destroyed. The hard truth at the center of the topic is that true anonymization is much harder than it looks — almost every released dataset can be re-identified with enough auxiliary information.

## Details

- Anonymization removes or perturbs identifiers so individuals cannot be re-identified from the released data. Direct identifiers (names, emails, national IDs) are the easy part — remove or replace them. The hard part is quasi-identifiers: combinations of attributes (age, zip code, gender, job title) that look harmless alone but jointly identify individuals — the classic result that 87% of the US population is uniquely identified by zip code, birth date, and gender. Effective anonymization must handle quasi-identifiers, which is why simple column removal is never enough.
- Techniques include generalization, suppression, perturbation, k-anonymity, l-diversity, and differential privacy. Generalization replaces precise values with ranges (age 42 → 40-45, zip 12345 → 1234*); suppression removes values entirely; perturbation adds noise to values. k-anonymity is the group-level guarantee that every released record is indistinguishable from at least k-1 others on the quasi-identifiers — but it has a known hole (a group can be k-anonymous yet share one sensitive value, which l-diversity fixes by requiring diversity of sensitive values within each group). Differential privacy is the strongest formal framework: it adds calibrated noise to query results so that the output reveals almost nothing about any individual, with a quantifiable privacy budget (epsilon) — at the cost of utility, since the noise degrades the analysis.
- Truly anonymous data is hard: auxiliary data can re-identify; pseudonymization (reversible) is not anonymization. The Netflix Prize and AOL search log incidents demonstrated re-identification from "anonymized" records joined with public data. Pseudonymization (replacing identifiers with tokens, reversible with the key) reduces risk but is not anonymization — regulators and analysts treat it as a weaker protection. The operational consequence: anonymization must be evaluated against realistic re-identification attacks, not assumed from the technique name.
- Differential privacy adds calibrated noise and is the strongest formal guarantee for aggregates. It is the standard for statistics and ML over sensitive data, with the tradeoff being the privacy budget: more privacy, more noise, less accurate results — a deliberate and tunable choice rather than a silent one.
- For mykb: the node connects privacy-by-design, tokenization/masking (the reversible alternatives), and the GDPR/CCPA regulatory drivers.


## Related
- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — privacy principles in design
- [[wiki/security-auth/data-breach-response|Data Breach Response]] — why anonymization reduces breach impact
- [[wiki/infrastructure/tokenization-and-masking|Tokenization And Masking]] — reversible protection alternatives
- [[wiki/infrastructure/data-privacy-gdpr-and-ccpa|Data Privacy Gdpr And Ccpa]] — regulatory drivers
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
