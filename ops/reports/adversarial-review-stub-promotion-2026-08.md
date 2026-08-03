# Adversarial Review — MyKB Stub Promotion Wave (Combined Report)

**Date:** 2026-08-03 · **Scope:** all 1,098 promoted files (5 disjoint slices) · **Reviewers:** 5 parallel adversarial agents (Leibniz, Maxwell, Erdos, Copernicus, Kepler)

**Method:** each reviewer ran the shared invariant checker (`ops/reports/adversarial-reviews/check_slice.py`) over its slice, manually verified every flagged item by reading the file, deep-read 20–48 files per slice (≈200 total), and spot-checked 10–28 link targets each. Prompt: `ops/reports/adversarial-reviews/ADVERSARIAL_REVIEW_PROMPT.md`.

---

## Synthesis (all 5 reviews)

### Verdict in one paragraph

The wave **passed every hard mechanical invariant on all 1,098 files** — zero missing files, zero `status` violations, zero files below the 320-body-word floor, zero missing frontmatter keys, zero non-UTF8 bytes — and the deep-reads found **no broad fabrication**: technical prose (OAuth grants, CL.TE smuggling, Chinchilla scale, GDPR 72h, CoreDNS `ndots`, PDB `minAvailable`, WCAG-adjacent color math, EDR/HDR InfiniBand rates, FP16/BF16/FP8 training, TrueTime/Spanner) was repeatedly verified as accurate and useful. The score is dragged down by a **systemic, machine-generated link-layer and template failure**, not by wrong knowledge: self-links, boilerplate "related coverage in the same cluster" annotations, fixed syntheses trailers, keyword-matched irrelevant links, and padding-to-threshold are spread across every slice. Individual health scores: **68, 57, 79, 71, 64 → mean 67.8, median 68/100**.

### What held (confirmed by all five reviewers)

- **Hard invariants: 0/1,098 failures** on existence, `status: growing`, ≥320 body words (frontmatter excluded), required frontmatter keys (`type`, `title`, `description`, `tags`, `timestamp`, `status`), and UTF-8 encoding.
- **No invented papers/models/APIs** were found; every URL that appeared in deep-read samples was real (NIST SP 800-63B, OWASP, RFC 5321, MITRE ATT&CK, FIDO, GDPR Art. 33/34, Wikipedia).
- The **strongest files are genuinely good reference notes** (e.g. bayesian-networks, forward-chaining, temporal-difference-learning, mixed-precision-training, gcp-spanner-google, transactional-outbox, retry-after).

### Confirmed defects, ranked by prevalence (1,098-file slice)

| # | Defect | Extent | Reviewers |
|---|--------|--------|-----------|
| 1 | **Self-links in `## Related`** ("related coverage in the same cluster" pointing at the file itself) | ≈71 files / 74+ links (~6.5%), incl. triple repeats in refresh-token-rotation & session-invalidation | all 5 |
| 2 | **Boilerplate Related annotations** — "related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" | ~300+ files (~30%); 799 occurrences in slice1 alone; 93 files (slice2); 98 files (slice4) | 1, 2, 3, 4, 5 |
| 3 | **Fixed syntheses trailer** — every article links the two curation syntheses + meta pages | ~200+ files (~20%); creates a star graph on 4 nodes | 1, 3, 4, 5 |
| 4 | **Keyword-matched irrelevant links** — e.g. CPU articles → Networking Fundamentals (41/60 cloud-infra files share one fixed 4-link tail); Savings Plans → Rollback Plans; erasure-coding → OSPF; S3 lifecycle → Pod Lifecycle; regex-engines on policy engines | ~60+ files | 1, 2, 3, 4, 5 |
| 5 | **Unverifiable "the wiki's X does Y" claims** — DNSSEC key rollover, 30/90/365 backup lifecycle, HTTP/3 edge serving, spot-first batch layer, "search fuses TF-IDF + embeddings + backlinks" — no repo evidence; template-identical skeletons | ~40+ files | 1, 2, 4 |
| 6 | **Zero provenance vs. the wave's own checklist** — `concepts/promotion-checklist.md` demands "two or more curl-verified sources"; 218/220 of slice2 carry **zero** URLs/citations | systemic (slice2 99%) | 2 (only reviewer who checked) |
| 7 | **Padding-to-threshold** — 76/220 files (35%, slice2) sit at 320–339 words; ~12 files copy the Summary sentence verbatim into the first Details bullet; formulaic RSIS3-relevance closers in 186/220 (slice1) | ~25% of slice | 1, 2, 3, 4 |
| 8 | **Broken/truncated links** — 3 unclosed `[[raw/archive/…]]` lines (prompt-engineering), 3 dead `README` links (`sources/README` ×2, `syntheses/README` ×1 — the READMEs were archived; `index` exists), 1 literal `[[file:...]]` (memory/org-mode) | 7 files | 4, 5 |
| 9 | **Near-duplicates & title collisions** — 5 duplicate pairs in slice5 (path-resolution ×3, users/groups, CLS, color spaces, viewport units) + sub-320 `growing` siblings with identical titles (`oauth2-authorization-code.md` = "Authorization Code Flow" etc.) | ~12 files | 1, 5 |
| 10 | **Confirmed factual errors (rare but real)** — `web-platforms/contrast-ratios.md` (#767676 is 4.54:1 and **passes**, #595959 is 7.0:1; article inverts the verdict), `infrastructure/gpu-drivers-and-cuda.md` ("`nvidia.ko` — *the only kernel-space component*"), `concepts/calibration.md` (reliability diagram direction reversed), `web-platforms/dom-clobbering.md` (corrupted generator sentence "using const/let shadows? No —"), `android-core/dp-vs-px.md` (xxxhdpi = 3px vs. its own Details = 4x) | 5 files | 1, 2, 4, 5 |

### Checker blind spots (needs fixing before the next wave)

`check_slice.py` missed the unclosed `[[` links, dead `README` targets, self-link alias variants, and the summary-duplication padding. Recommended additions: flag any `[[` without `]]`; resolve `wiki/`-prefixed targets against disk; treat self-target links as a hard gate; detect verbatim Summary→Details repetition; validate `type` against directory namespace (`syntheses/` must be `synthesis`).

### Highest-impact fixes (merged from all five reviews)

1. **Fix the generator, not the files**: regenerate every Related section from the resolved wikilink graph with (a) the node itself excluded, (b) deduped targets, (c) ≥1 topical link required, (d) no boilerplate annotation text. This clears defects #1–#4 in one pass.
2. **Add a provenance gate**: require a real `Sources` section (curl-verified URLs) for any article with numeric/vendor/infrastructure claims — the wave's own checklist already demands it.
3. **Repair the confirmed errors now** (cheap, high value): contrast-ratios.md (recompute WCAG values), dom-clobbering.md (rewrite corrupted sentence), gpu-drivers-and-cuda.md (module-set wording), calibration.md (swap over/under), dp-vs-px.md (4x, not 3px), the 3 truncated `[[raw/…]]` links, and the 3 `README` links (retarget to `index`).
4. **Ground or reword the self-referential infra claims** — point at real config/telemetry or convert to policy statements ("the standing rule is …").
5. **Raise the effective floor / add margin rules**: promotion at exactly 320 invites append-padding; set ~400 with an anti-duplication check, and remove the universal syntheses trailer from every article's Related list.

### Divergences worth noting

- Reviewers 3 (79) and 4 (71) judged content accuracy highly and treated the template issues as systematic but mechanical; reviewers 2 (57) and 5 (64) weighted retrievability/provenance more heavily, calling templated link sections an active retrieval hazard. The disagreements are about severity, not existence — all five independently confirmed the same defect classes.
- Only reviewer 2 checked the provenance standard; the other four flagged "unverifiable" claims but did not measure the 0-citation baseline. Treat the provenance gap as at least as severe as review 2 reports.

---

## Individual reviews


## Review 1

## Adversarial Review 1 — MyKB Stub-Promotion Wave (slice1, 220 files)

Reviewer: adversarial #1 · Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice1.txt` (220 files)
Areas in slice: api-protocols (117), cloud-infra (60), ai-ml (32), agent-systems (8), android-core (3)
Method: invariant checker + manual verification of all 42 flagged files + deep-read of 47 files + 16 link-target spot checks.

### Verdict

**Health score: 68 / 100**

The wave met the mechanical bar it set: all 220 files have `status: growing`, ≥320 body words (min exactly 320), and complete frontmatter; I confirmed zero broken wikilinks/markdown links among every link I checked, and found no fabricated papers, models, or API names in 47 deep-reads — the technical prose (OAuth grants, CL.TE smuggling, Chinchilla 70B/1.4T, GCP tier minimums, Android ANR timeouts) is genuinely accurate and useful. The score is dragged down by a systemic, machine-generated Related-section failure: **30 files link to themselves (33 self-links, two files triple-repeated)**, 17 files contain duplicated Related entries, 114 files (51.8%) repeat the boilerplate annotation "related coverage in the same cluster" (799 occurrences), 41 of 60 cloud-infra files end with an identical, partly irrelevant 4-link tail (CPU articles linking to Networking Fundamentals), 3 android-core files kept leftover stub fragments above their expanded body (duplicating content), and the wave's own meta-articles (graph-density-metrics, link-diversity, article-health-scores) describe exactly the self-link and link-spam pathologies the wave then shipped. Six-plus files also carry unverifiable "the wiki's X does Y" claims (DNSSEC key rollover, a 30/90/365 backup lifecycle, HTTP/3 edge serving) for which the repo shows no supporting config — possible invented specificity. Padding is real but mostly *in the link layer*: e.g. `remote-access-methods.md` clears the 320-word floor only because ~72 of its 320 words are Related list and "RSIS3/mykb relevance" boilerplate.

Per-defect-type quantification (of 220 files): status ≠ growing **0 (0%)** · body < 320 **0 (0%)** · missing frontmatter keys **0 (0%)** · self-links **30 (13.6%)** · duplicated Related entries **17 (7.7%)** · "related coverage in the same cluster" boilerplate **114 (51.8%)** · fixed 4-item Related tail **41/60 cloud-infra (68.3%)** · leftover stub fragments **3 (1.4%)** · placeholder text **0 (0%) — all 14 checker flags were false positives** · broken links **0 (0%, checker); 0/16 spot-checked**.

### Critical findings

1. **Self-links in the Related section — 30 files / 33 links (13.6% of slice). Confirmed invariant violation.**
   Every flagged self-link is real and sits in `## Related`, i.e. the wave's generator emitted a link to the file itself and labeled it "related coverage in the same cluster".
   - `api-protocols/301-vs-302.md` line 31: `- [[wiki/api-protocols/301-vs-302|301 vs 302]] — related coverage in the same cluster`
   - `api-protocols/refresh-token-rotation.md` lines 21–23 contain the self-link **three times**:
     `- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — related coverage in the same cluster` (×3)
   - `api-protocols/session-invalidation.md` lines 23–25: same triple repetition of `[[wiki/api-protocols/session-invalidation|Session Invalidation]]`.
   Other affected files include 401-vs-403, 404-vs-410, api-docs-generators, api-throttling, authorization-code-flow, certificate-chains, charset-encodings, clickjacking-defense, client-credentials-flow, client-libraries, conditional-put, device-flow, error-codes-api, http-parameter-pollution, http-status-checks, iframe-sandboxing, ipv4-vs-ipv6, mime-types, ocsp-stapling, parameter-pollution, popup-security, rest-vs-graphql, rest-vs-grpc, rest-vs-rpc, tcp-vs-udp, throttling-vs-debouncing.
   Why it is wrong: a self-edge is not a relationship; it inflates the link graph the wave's own health metrics count (`ai-ml/graph-density-metrics.md` states "Self-links must be excluded or they inflate the count"), pollutes backlinks, and is unambiguous link padding. The wave's own invariant checker flags these, so the wave shipped known violations.
   Fix: regenerate Related sections from the wikilink graph with the node itself excluded; dedupe.

2. **`growing`-status sibling pages below the 320-word floor (out-of-slice but linked from promoted files). Confirmed invariant violation of the wave's own rule.**
   The promoted files link to near-duplicate pages that are `status: growing` yet sit at 237–256 body words — below the wave's 320 minimum — and in two cases carry identical titles to the promoted article, so links display ambiguously:
   - `api-protocols/oauth2-authorization-code.md` — 249 words, title `"Authorization Code Flow"` (identical to `api-protocols/authorization-code-flow.md`); linked from that file's Related as `[[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]`.
   - `api-protocols/oauth2-client-credentials.md` — 240 words, status growing, links `[[wiki/api-protocols/oauth2-client-credentials|Client Credentials]]` vs `[[wiki/api-protocols/client-credentials-flow|Client Credentials Flow]]`.
   - `api-protocols/oauth2-refresh-tokens.md` — 256 words; `api-protocols/token-refresh-strategies.md` — 237 words.
   Why it is wrong: (a) the 320-word bar was not enforced corpus-wide, so "growing" no longer means what the wave claims; (b) `authorization-code-flow.md`'s Related section simultaneously contains `[[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]` and its own self-link `[[wiki/api-protocols/authorization-code-flow|Authorization Code Flow]]` — two distinct pages rendering identical link text (basename-collision ambiguity, defect class 6).
   Fix: merge the oauth2-* siblings into the promoted articles (Jaccard 0.16–0.23, i.e. they are the same topic), or expand them to ≥320 words; disambiguate titles.

### Major findings

1. **Boilerplate annotation "related coverage in the same cluster" — 799 occurrences across 114 files (51.8%). Confirmed word-stuffing.**
   The annotation adds ~10–12 words per link, ~70–80 words per file in api-protocols, and is identical in every file. Example, `api-protocols/webhook-signatures.md` Related: `- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — related coverage in the same cluster`. In `api-protocols/301-vs-302.md` the Related section alone is 76 words — about 15% of the article — and every line carries the identical tag, contributing nothing a reader can't infer from the link itself. The better files (ai-ml cluster) use real descriptors ("— The leakage mechanism behind much gaming", "— The framework Chinchilla refines"); the wave should have used that style or none. This also games the 320-word metric: e.g. `cloud-infra/remote-access-methods.md` totals exactly 320 words, of which ~37 are Related-list words and ~35 are the formulaic "RSIS3/mykb relevance" paragraph (~72 words of non-content, ~22%).

2. **Duplicated Related entries — 17 files (7.7%). Confirmed.**
   Fifteen files contain the identical Related line twice (e.g. `api-protocols/api-docs-generators.md`: `- [[wiki/api-protocols/client-libraries|API Client Libraries]] — related coverage in the same cluster` ×2; `api-protocols/certificate-chains.md` → OCSP Stapling ×2; `api-protocols/charset-encodings.md` → MIME Types ×2; `api-protocols/ipv4-vs-ipv6.md` → TCP vs UDP ×2; `api-protocols/tcp-vs-udp.md` → IPv4 vs IPv6 ×2; `api-protocols/error-codes-api.md` ↔ `conditional-put.md` cross-duplicate), plus the two triple self-link files from Critical #1. This is unambiguously generator output that was never deduped — a structural defect (duplicated passages, defect class 4).

3. **Keyword-matched, topically irrelevant Related links, including a fixed 4-item tail in 41/60 cloud-infra files. Confirmed.**
   - `cloud-infra/amd-epyc-and-intel-xeon.md` (a CPU-comparison article) Related:
     `- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]` / `- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]` / `- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]` / `- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]`
     — identical to the Related tail of `dnssec-and-validation.md`, `preemptible-vm-workloads.md`, `http-3-0-rtt.md`, `instance-store-vs-ebs.md`, `reserved-instances-vs-on-demand.md`, `savings-plans.md`, `azure-blob-access-tiers.md`, and 34 more cloud-infra files. Networking Fundamentals / TCP/IP Stack are not related to CPU silicon, savings plans, or blob tiers.
   - `cloud-infra/savings-plans.md` Related opens with `- [[wiki/devops-infra/rollback-plans|Rollback Plans]]` — a deployment-rollback page matched on the keyword "plans".
   - `cloud-infra/glacier-and-s3-lifecycle.md` Related opens with `[[wiki/cloud-infra/function-execution-lifecycle|Function Execution Lifecycle]]`, `[[wiki/os-shell/process-signals-and-lifecycle|Process Signals & Lifecycle]]`, `[[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]]` — a pure "lifecycle" keyword match; serverless cold starts and pod states have nothing to do with S3 archive tiering.
   These are exactly the "irrelevant links added purely to inflate the link count" (defect class 6) that the wiki's own `ai-ml/link-diversity.md` warns about ("forcing diversity mechanically — replacing meaningful links with arbitrary ones — destroys precision").

4. **Leftover stub fragments above the expanded body — 3 android-core files, with duplicated content. Confirmed.**
   `android-core/anr-diagnostics.md`, `app-threading.md`, and `dp-vs-px.md` have no `## Summary` heading; instead the pre-wave stub survives verbatim between the H1 and `## Details`, duplicating the new content:
   - `android-core/anr-diagnostics.md`: stub fragment `- Fix by moving work off the main thread and fixing lock ordering.` and `- Watchdog-style telemetry on the main thread catches jank early.` vs Details `**Fix patterns** — move IO off the main thread ...` and `**Operational practice** — ... use watchdog-style telemetry on the main thread ...`.
   - `android-core/app-threading.md`: stub line `- StrictMode flags accidental main-thread IO during development.` vs Details `**Tooling** — StrictMode flags accidental main-thread IO during development (disk read/write and network violations log as soon as they happen)` — near-verbatim duplication.
   The wave expanded these files but never merged/removed the original stub, so readers get the same guidance twice at different depths.

5. **In-file factual contradiction in `android-core/dp-vs-px.md`. Confirmed.**
   Intro: "1dp is 1px on mdpi and 3px on xxxhdpi." Details: "**Density model** — ... xxxhdpi = 4x". 1dp = 3px is xxhdpi, not xxxhdpi; the article contradicts itself one section apart. (Word-count effect: the file's 530 words are otherwise fine.) The adjacent `anr-diagnostics.md` claim "SharedPreferences apply-on-main" as an example of *synchronous* main-thread IO is subtly wrong — `apply()` is asynchronous by design; `commit()` is the synchronous call.

6. **Unverifiable self-referential claims in "RSIS3/mykb relevance" sections (6+ files). Cannot verify — likely invented specificity.**
   These assert concrete facts about the user's infrastructure that nothing in the repo corroborates (I searched the repo for DNS automation, backup-lifecycle configs, edge/HTTP-3 config, preemptible runners, Graviton migrations — no evidence found):
   - `cloud-infra/dnssec-and-validation.md`: "the wiki's domains are signed with automated key rollover; this note records the DS publication and rollover procedure the loop's DNS automation follows."
   - `cloud-infra/glacier-and-s3-lifecycle.md`: "the wiki's backup lifecycle (30/90/365) is recorded here with its restore tests"
   - `cloud-infra/http-3-0-rtt.md`: "the wiki's edge serving enables HTTP/3 with h2 fallback"
   - `cloud-infra/preemptible-vm-workloads.md`: "the wiki's batch experiments run on preemptible capacity with checkpointing"
   - `cloud-infra/graviton-and-aws.md`: "the wiki records per-service Graviton migration results"
   - `api-protocols/authorization-code-flow.md`: "if the hub dashboard adds OIDC login, the code flow plus PKCE plus state validation pattern is the standing rule to encode"
   For a memory store whose value is trusted persistence, confident assertions about the wiki's own infrastructure that the agent cannot verify are as costly as fabricated external facts: future sessions will treat them as ground truth. Mark as "cannot verify offline" or rewrite as policy ("the standing rule is X") rather than state ("the wiki does X").

### Minor & nits

- **Placeholder flags: all 14 checker flags are false positives, verified one-by-one.** Twelve are legitimate RFC 2606 `example.com` doc domains (e.g. `api-protocols/cookie-scoping.md` "With Domain=example.com it is sent to example.com and all subdomains"; `cloud-infra/dnssec-and-validation.md` "an attacker forges a DNS answer for example.com"); `ai-ml/article-health-scores.md` uses "placeholder text" descriptively ("headings present, no placeholder text"); `api-protocols/hash-collision-dos.md` flags are regex artifacts ("every insert and lookup degenerates into a linked-list scan"). No action needed — recorded so the checker's precision is known.
- **"RSIS3/mykb relevance" is a formulaic closing section in 186/220 files (84.5%).** House style, but it is near-template filler in many files ("storing the decision rule here keeps loop-generated incident reviews consistent across sessions" — `401-vs-403.md`). Fine as a frame; the unverifiable variant is the problem (Major #6).
- **Missing `## Summary` heading in the 3 android-core files** (anr-diagnostics, app-threading, dp-vs-px) — they use an intro paragraph instead; inconsistent with the other 217 files.
- **Extra `source: []` frontmatter key** in the 3 android-core files — empty list, present nowhere else in the slice; either populate or drop.
- **`cloud-infra/coldline-and-archive-storage-classes.md`**: "5TB of legal holds in Archive at ~$0.004/GB-month" — GCP Archive list pricing in us-central1 is ~$0.0012/GB-month; $0.004 is Coldline pricing. Prices vary by region and change, so this is "likely conflated" rather than certain; the "5x saving" arithmetic uses the wrong base.
- **`cloud-infra/preemptible-vm-workloads.md`**: "A3-style preemptibles differ" — vague, no citation or detail; either state the difference (30-second vs 24h behavior) or cut it.
- **Style:** the 3 android-core files use "-" where the rest of the wiki uses em-dashes ("blocked too long - input dispatch"), and `anr-diagnostics.md` mixes "ANR" and "ANRs" inconsistently in one paragraph.
- **`api-protocols/401-vs-403.md`** states "A revoked token must stay rejected even after re-login flows" — a policy statement presented as a spec requirement; fine as guidance, but it is advice, not RFC behavior.
- **Titles vs filenames** drift in a few files (`agent-systems/ai-act.md` title "EU AI Act", `agent-systems/deception-research-ai.md` title "Deception Research") — cosmetic only.

### Sample audit table

Deep-read files (words = body words; verdict reflects content quality + wave defects found).

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| ai-ml/chinchilla-law.md | 497 | Pass | Facts check out (70B/1.4T, Gopher 280B, ~1:1 ratio, 400+ models). Real descriptors in Related. |
| ai-ml/scaling-laws.md | 363 | Pass | Kaplan 2020 / Chinchilla framing accurate. |
| ai-ml/deepseek.md | 342 | Pass | MoE, MLA, R1 verifiable reasoning line — accurate. |
| ai-ml/gpt-4.md | 338 | Pass | 2023 report claims accurate; "cannot verify" the RSIS3 benchmarking claim. |
| ai-ml/benchmark-gaming.md | 459 | Pass | Accurate taxonomy; "contamination audits (like the one on GPT-4's training data)" cannot verify. |
| ai-ml/logit-lens.md | 368 | Pass | Residual-stream mechanism described correctly; caveats honest. |
| ai-ml/data-contamination.md | 365 | Pass | Accurate; no invented specifics. |
| ai-ml/model-cards.md | 377 | Pass | Model Cards for Model Reporting (2019) — correct provenance. |
| ai-ml/claude.md | 397 | Pass | Generic but accurate; no fabricated claims. |
| ai-ml/llama.md | 337 | Pass | Accurate; license/caveat framing sound. |
| ai-ml/article-health-scores.md | 478 | Pass | "placeholder" flag = false positive (descriptive). Meta-article describes the wave's own failure modes. |
| ai-ml/hypothetical-document-embeddings.md | 406 | Pass | HyDE mechanism accurate; honest failure modes. |
| ai-ml/graph-density-metrics.md | 371 | Pass | n(n-1) directed ceiling correct; self-link exclusion stated. |
| ai-ml/link-diversity.md | 345 | Pass | Sound; the wave violated its own advice (see Major #3). |
| agent-systems/accountability-ai.md | 347 | Pass | Sound; "Evidence chain:" add-on bullet is content-bearing. |
| agent-systems/lobotomized-optimizers.md | 371 | Pass | Thought experiment framed accurately. |
| agent-systems/deception-research-ai.md | 331 | Pass | Measured tone; no overclaiming. |
| agent-systems/ai-act.md | 363 | Pass | Tiering/obligations accurate; "2025-2027+" timeline cannot fully verify. |
| agent-systems/myopic-reward.md | 356 | Pass | Sound. |
| android-core/anr-diagnostics.md | 548 | Major #4 | Leftover stub fragment duplicates Details; `apply()` miscalled synchronous; no `## Summary`; `source: []`. |
| android-core/app-threading.md | 512 | Major #4 | Stub fragment duplicates Details (StrictMode line near-verbatim). |
| android-core/dp-vs-px.md | 530 | Major #5 | "3px on xxxhdpi" contradicts Details "xxxhdpi = 4x". |
| api-protocols/301-vs-302.md | 512 | Critical #1 | Self-link in Related; 76-word boilerplate Related (15%). |
| api-protocols/401-vs-403.md | 505 | Critical #1 | Self-link; 401/403 mechanics accurate. |
| api-protocols/authorization-code-flow.md | 471 | Critical #1 + Major #3 | Self-link; links to same-title stub sibling oauth2-authorization-code (249 words, growing). |
| api-protocols/client-credentials-flow.md | 497 | Critical #1 | Self-link; accurate PKCE/secret mechanics. |
| api-protocols/refresh-token-rotation.md | 503 | Critical #1 | Self-link ×3; RFC 9700 reference correct. |
| api-protocols/session-invalidation.md | 504 | Critical #1 | Self-link ×3. |
| api-protocols/none-algorithm.md | 455 | Pass | alg=none / JWA accurate; checklist sound. |
| api-protocols/webhook-signatures.md | 499 | Pass | HMAC/raw-body/constant-time guidance correct. |
| api-protocols/request-smuggling.md | 473 | Pass | CL.TE/TE.CL described correctly. |
| api-protocols/ssrf-practice.md | 461 | Pass | Metadata-IP/allow-list guidance accurate. |
| api-protocols/rest-vs-graphql.md | 478 | Critical #1 | Self-link; N+1/DataLoader framing accurate. |
| api-protocols/charset-encodings.md | 473 | Critical #1 + Major #2 | Self-link + duplicated MIME Types link. |
| api-protocols/cookie-prefixes.md | 447 | Pass | example.com flag false positive; __Host-/__Secure- rules correct. |
| api-protocols/hash-collision-dos.md | 480 | Pass | Regex flags false positive; 2011-2012 wave + SipHash defense accurate. |
| cloud-infra/amd-epyc-and-intel-xeon.md | 325 | Major #3 | Irrelevant Related tail (networking pages) shared with 40 other files. |
| cloud-infra/dnssec-and-validation.md | 341 | Major #6 | "wiki's domains are signed with automated key rollover" — cannot verify; shared tail. |
| cloud-infra/glacier-and-s3-lifecycle.md | 342 | Major #3 + #6 | "lifecycle" keyword links; "backup lifecycle (30/90/365)" cannot verify. |
| cloud-infra/preemptible-vm-workloads.md | 332 | Major #6 | "batch experiments run on preemptible capacity" cannot verify; "A3-style preemptibles differ" vague. |
| cloud-infra/http-3-0-rtt.md | 335 | Major #6 | "the wiki's edge serving enables HTTP/3" cannot verify. |
| cloud-infra/graviton-and-aws.md | 328 | Major #6 (mild) | "records per-service Graviton migration results" cannot verify. |
| cloud-infra/reserved-instances-vs-on-demand.md | 341 | Major #3 | Irrelevant tail; otherwise accurate. |
| cloud-infra/coldline-and-archive-storage-classes.md | 328 | Minor | Archive priced at ~$0.004/GB-month (likely Coldline pricing); otherwise accurate tier rules. |
| cloud-infra/instance-store-vs-ebs.md | 340 | Pass | Durable-vs-ephemeral framing correct; tail links irrelevant but harmless. |
| cloud-infra/azure-blob-access-tiers.md | 342 | Major #3 | 180-day archive minimum and 30/90 cool/cold minimums correct; keyword-loose Related. |
| cloud-infra/savings-plans.md | 326 | Major #3 | Related opens with Rollback Plans (keyword match); Compute SP scope correct. |
| api-protocols/device-flow.md | 498 | Critical #1 | Self-link; device_code/user_code flow accurate; example.com legit. |

### Recommendations

1. **Regenerate every Related section from the resolved wikilink graph, excluding the node itself and deduping entries** — clears Critical #1 (30 files, 33 self-links) and Major #2 (17 files, duplicated lines) in one pass. Add a promotion invariant: "no self-links, no duplicate link targets in Related" (the checker already has the logic; wire it into the pipeline).
2. **Delete the "— related coverage in the same cluster" annotation** (799 occurrences, 114 files) and replace with real one-line descriptors in the style the ai-ml files already use, or nothing. Recompute word counts afterward so the 320-word floor measures true content — right now Related + the formulaic "RSIS3/mykb relevance" paragraph can supply ~20–25% of a file's words (e.g. `remote-access-methods.md` at exactly 320).
3. **Fix the keyword-matched/template tails**: audit all 41 cloud-infra files sharing the networking-fundamentals/tcp-ip-stack/knowledge-acquisition tail and drop topically irrelevant links (EPYC/Xeon → Networking Fundamentals; Savings Plans → Rollback Plans; S3 lifecycle → Pod Lifecycle). This is the defect the wiki's own `link-diversity.md` names; the wave should not ship the anti-pattern it documents.
4. **Resolve the title collisions and sub-bar siblings**: merge `oauth2-authorization-code.md` into `authorization-code-flow.md`, `oauth2-client-credentials.md` into `client-credentials-flow.md`, and the three refresh-token pages into `refresh-token-rotation.md` (Jaccard 0.16–0.23 confirms same-topic duplication); then re-audit the whole corpus for `status: growing` files under 320 words (at least 4 exist) and either expand or demote them to `stub`.
5. **Ground or reword the self-referential infra claims** (DNSSEC rollover, 30/90/365 backup lifecycle, HTTP/3 edge, preemptible runners, Graviton migrations, OIDC hub login): either point them at real config/telemetry in the repo or convert to policy statements ("the standing rule is …"), because unverifiable assertions stored as fact corrupt the memory layer the wave is supposed to serve. Also fix the confirmed `dp-vs-px.md` density error (xxxhdpi = 4x, not 3px) and the `anr-diagnostics.md` `apply()`/`commit()` conflation while in there.

---

## Review 2

## Adversarial Review #2 — MyKB Stub Promotion Wave (slice 2)

Reviewer: adversarial reviewer #2 (slice: 220 files)
Date: 2026-08-03
Method: `check_slice.py` on all 220 files; full or near-full deep-read of 44 files across
cloud-infra, concepts, data-storage, dev-tools, communities, compositions, decisions;
28 link targets spot-checked (all exist, all topically related).

### Verdict

**Score: 57 / 100**

The wave passes every mechanical invariant it was measured on: 212/220 files clean per the
checker, zero missing files, zero wrong statuses, zero body-word deficits, zero missing
frontmatter keys, zero broken wikilinks or markdown links (per the checker's resolution
rules and my own spot-checks). But the mechanical bar was the *only* bar that held, and it
was set low. The five self-links are real invariant violations and two of them carry
nonsensical labels. More damaging: the promotion wave's own stated standard — "two or more
curl-verified sources" (`concepts/promotion-checklist.md`) — is met by essentially none of
the slice: 218/220 files contain not a single URL or citation, so the many specific numeric
and infrastructure claims cannot be checked and were evidently written without provenance.
Systemic wave artifacts dominate: 93 files (42%) carry machine-generated Related-block
annotations ("the full treatment of this theme", "existing graph context") that add noise
and inflate link counts; 59 files (27%) have trailing "practice" bullets bolted on after
the RSIS3 relevance bullet (37 of them orphaned by a blank line); 76 files (35%) sit within
20 words of the 320-word floor (minimum exactly 320, median 389.5), consistent with
padding-to-threshold. Twenty files assert unverifiable specifics about "the wiki's" own
infrastructure in template-identical sentence skeletons. There is also one confirmed
semantic error (`concepts/calibration.md`, reliability-diagram direction reversed) and a
stub-naming concatenation artifact (`data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`).
The corpus is mostly *accurate* at the summary level — the best files (bayesian-networks,
forward-chaining, eval-contamination, hotfix-branches, temporal-difference-learning) are
genuinely good — but for a persistent memory store feeding an agentic loop, the systemic
boilerplate, fabricated-relevance framing, and missing provenance are a real quality cost.

### Critical findings

1. **Five confirmed self-links (invariant violation, 5/220 = 2.3%)** — all verified by reading; none are false positives.
   - `concepts/causal-interventions-ai.md` Related: `[[wiki/concepts/causal-interventions-ai|causal-interventions-ai]] — statistical basis` — links to its own page, and the anchor "statistical basis" is semantically wrong for an article about causal interventions.
   - `concepts/content-freshness-review.md` Related: `[[wiki/concepts/content-freshness-review|Content Freshness Review]]` — self-link appended as the last Related entry.
   - `concepts/dependency-attacks-ai.md` Related: `[[wiki/concepts/dependency-attacks-ai|dependency-attacks-ai]] — note` — self-link with filler annotation.
   - `concepts/expected-value-reasoning.md` Related: `[[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — see also` — self-link with filler annotation.
   - `dev-tools/frontmatter-linting.md` Related: `[[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]` — self-link.
   - Why wrong: a self-link adds a node pointing at itself in the knowledge graph, corrupting traversal/backlink statistics, and the pattern (four of five carry filler labels like "— note" / "— see also") shows these were appended mechanically to pad the Related block. Fix: delete the self-links; replace with a real related page or drop the bullet.

2. **Fabricated-looking, unverifiable "the wiki's …" infrastructure claims (20/220 = 9%)** — the RSIS3/mykb relevance paragraphs assert specific facts about the wiki's own infrastructure in a template-identical sentence skeleton ("the wiki's X …; this note records the Y the loop checks"). I cannot verify any of these offline, and the uniformity of the skeleton across unrelated topics (VPN, spot pricing, TLS, storage, Lamport clocks) makes them read as generated filler rather than recorded reality. Examples:
   - `cloud-infra/site-to-site-vpn.md`: "the wiki's hybrid connectivity uses dual tunnels with BGP; this note records the tunnel and route policy the loop checks during network changes."
   - `cloud-infra/spot-instances.md`: "the wiki's batch layer runs spot-first with checkpointing; this note records interruption-rate telemetry so the loop tunes the spot/on-demand mix empirically."
   - `cloud-infra/tls-1-3-session-resumption.md`: "the wiki's API layer enables TLS 1.3 resumption with short-lived tickets; this note records the ticket policy the loop verifies after certificate or proxy changes."
   - `cloud-infra/snapshot-lifecycle-policies.md`: "the wiki's backup policies are recorded with their retention matrices here" — circular: the article claims it *is* the record of the policies, with no pointer to where those policies actually live.
   - Why wrong: a memory store for an agentic loop will retrieve these as premises about the system's own setup; if the claims are invented, the loop will act on false self-knowledge. Fix: either make the claims real (link to the actual config/policies) or rewrite as hedged hypotheticals ("if the wiki ran spot-first …").

3. **Provenance bar violated across the whole slice: 0 citations in 220 files.** The wiki's own `concepts/promotion-checklist.md` (in this slice) states: "two or more curl-verified sources" is a checklist item and "the source item enforces provenance (claims must trace to verifiable references)". Only 2 of 220 files contain any `http(s)` string, both documentation examples (`cloud-infra/service-discovery-dns-based.md` `http://payments.svc.internal:8080`; `dev-tools/curl-patterns.md` `https://api.example/health`), not citations. Zero sources, zero "source:" fields, zero links to a sources index were found in any file read. Consequences: every specific numeric claim in the slice is unverifiable — e.g. `data-storage/hnsw.md` "~95% recall at efSearch 64" and "memory sits around 10x vector size", `cloud-infra/spot-instances.md` "GCP preemptible fixed 24h/80% discount", `cloud-infra/storage-tiering.md` "cut storage spend 50-80%", `cloud-infra/site-to-site-vpn.md` "typically 1.25-10 Gbps on cloud gateways". Either the checklist is aspirational fiction or the wave skipped a stated promotion criterion; both are bad. Fix: add a "Sources" section with real URLs to the articles carrying numeric claims, or relax the checklist and say so explicitly.

### Major findings

1. **Machine-generated Related-block annotation boilerplate (93/220 = 42%, 215 annotations).** Phrases repeated near-verbatim across files: "the full treatment of this theme" (72 files), "existing graph context" (79 files), plus "— the category", "— the class", "— the framework", "— see also", "— note", "— related tool". Examples: `concepts/dependency-attacks-ai.md` `[[wiki/decisions/self-hosting|Self-Hosting]] — the full treatment of this theme`; `concepts/sandbagging.md` `[[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context`. These labels carry no information, are identical across unrelated topics, and inflate the link count — the "irrelevant links added purely to inflate the link count" defect class. Fix: strip the annotations, keep plain links.

2. **Trailing "practice" bullets bolted on after the RSIS3 relevance bullet (59/220 = 27%).** Content that belongs in Details or a dedicated section was appended after the relevance paragraph — 37 files orphan the bullet behind a blank line (list broken), 22 keep it adjacent but still out of place. Examples:
   - `data-storage/pinecone.md`: "## Details" list ends with the RSIS3 bullet, then a blank line, then `- Keep embeddings and metadata exportable so a future self-hosted move does not require re-indexing from scratch.` (same shape in `data-storage/milvus.md`, `data-storage/simhash.md`, `data-storage/postgres-tsvector.md`, `dev-tools/fixed-window.md`, `dev-tools/leaky-bucket.md`, `dev-tools/fuzzing-tools.md`, `decisions/api-access-policies.md`, and 30 more).
   - `cloud-infra/split-horizon-dns.md`: `- Synchronization: generate internal and external views from the same source of truth; manual dual maintenance is how the two views diverge.` directly after the relevance bullet (same shape in `cloud-infra/spot-instances.md`, `cloud-infra/site-to-site-vpn.md`, `compositions/lamport-clocks.md`, etc.).
   - Why wrong: these bullets are effectively orphaned content — half of them render outside any list, and their placement (after the relevance paragraph) is arbitrary, a hallmark of word-count chasing. Fix: merge into Details in reading order or promote to a real section.

3. **Confirmed semantic error in `concepts/calibration.md`.** Details bullet: "A reliability diagram plots the two; points above the diagonal are overconfident, points below are underconfident." This is backwards. In a reliability diagram (x = predicted confidence, y = observed accuracy), a point above the diagonal means accuracy exceeds confidence — i.e. *under*confident; below the diagonal is overconfident. This is exactly the class of "subtly wrong definition" the review targets, in a page about calibration. Fix: swap "over" and "under".

4. **Stub-naming concatenation artifact: `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`.** Filename contains "druid" twice; title is "ClickHouse vs Druid vs Pinot". The slug looks like two stub titles ("clickhouse-vs-druid-pinot" + "druid-architecture") welded together at promotion. Structural/SEO defect and a red flag for the wave's rename/merge hygiene. Fix: rename to `clickhouse-vs-druid-vs-pinot.md` (with referrer updates).

5. **Word-floor clustering consistent with padding (76/220 = 35% at 320–339 words).** Minimum in slice is exactly 320; median 389.5; 25 files at 320–325. `cloud-infra/vpn-split-tunneling.md` (320), `dev-tools/correlation-ids.md` (320), `data-storage/pinecone.md` (322), `dev-tools/four-golden-signals.md` (322), `cloud-infra/site-to-site-vpn.md` (323) all sit just past the bar, and several carry the dangling-bullet filler above. Clustering at the threshold plus the appended bullets is the profile of floor-hitting, not organic expansion. Fix: require a margin above the floor (e.g. ≥380) and spot-check for append-patterns before promoting.

### Minor & nits

1. **Duplicate links to the same target within one file** (4 files): `compositions/fencing-tokens.md` links `wiki/compositions/lease-based-locks` twice; `concepts/activation-patching.md` links `wiki/concepts/causal-interventions-ai` twice; `concepts/causal-interventions-ai.md` links `wiki/concepts/activation-patching` twice; `decisions/data-license-issues.md` links `wiki/syntheses/evidence-and-provenance` twice. Related blocks should have one link per target.
2. **Blank line directly after the "## Related" heading** (20 files), e.g. `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`, `data-storage/scd-type-2-slowly-changing-dimensions.md`, `data-storage/backpressure-and-flow-control.md` — formatting drift from the template.
3. `concepts/sandbagging.md` Related label `Ai Safety Evals` — inconsistent capitalization ("AI Safety Evals").
4. `concepts/early-stopping.md` Related label `eval-splits` — lowercase slug used as display text.
5. `concepts/causal-interventions-ai.md` — self-link mislabeled "statistical basis" (see Critical #1); also double-links `activation-patching` ("the main method" + "the framing").
6. Unverifiable numeric specifics (cannot verify offline; none sourced): `data-storage/hnsw.md` "~95% recall at efSearch 64" / "memory sits around 10x vector size"; `cloud-infra/storage-tiering.md` "cut storage spend 50-80%" and "costs 5-10x"; `cloud-infra/site-to-site-vpn.md` "typically 1.25-10 Gbps on cloud gateways" (mixes AWS's ~1.25 Gbps-per-tunnel with Azure's top-SKU ~10 Gbps without attribution).
7. `cloud-infra/spot-instances.md` — "GCP preemptible fixed 24h/80% discount": discount varies by machine type (60–91%), and GCP preemptible VMs were superseded by GCP Spot in 2021; wording is outdated and the 80% figure is not universal.
8. `dev-tools/flame-graphs.md` — "a wiki build that takes 40 seconds — a flame graph shows 25 seconds in markdown parsing and 10 in link resolution": invented-specific example figures presented as concrete fact; harmless but fabricated precision.
9. Checker false positives (all three placeholder flags are legitimate usage, confirmed by reading): `cloud-infra/split-horizon-dns.md` "example.com" (RFC 2606 documentation domain), `concepts/stub-criteria.md` "placeholder" (defining what a stub is), `data-storage/postgres-tsvector.md` "insert and query" (analyzer-mismatch explanation).

### Sample audit table

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| concepts/causal-interventions-ai.md | 404 | FAIL | self-link "statistical basis"; duplicate link to activation-patching |
| concepts/content-freshness-review.md | 386 | FAIL | self-link in Related |
| concepts/dependency-attacks-ai.md | 386 | FAIL | self-link "— note"; boilerplate annotations |
| concepts/expected-value-reasoning.md | 447 | FAIL | self-link "— see also" |
| dev-tools/frontmatter-linting.md | 340 | FAIL | self-link; dangling bullet after RSIS3 relevance |
| concepts/calibration.md | 409 | FAIL | reliability diagram: above-diagonal = underconfident, not overconfident |
| data-storage/clickhouse-vs-druid-pinot-druid-architecture.md | 378 | FAIL | filename duplicates "druid"; blank line after ## Related |
| cloud-infra/split-horizon-dns.md | 325 | PASS w/ issues | example.com false positive; trailing "Synchronization" bullet after relevance |
| cloud-infra/site-to-site-vpn.md | 323 | PASS w/ issues | unverifiable "the wiki's hybrid connectivity" claim; trailing bullet; unsourced Gbps range |
| cloud-infra/spot-instances.md | 339 | PASS w/ issues | unverifiable "the wiki's batch layer" claim; outdated GCP preemptible wording; trailing bullets |
| cloud-infra/tcp-retransmission.md | 341 | PASS w/ issues | sound mechanics; trailing "Diagnosis order"/"Baseline first" bullets |
| cloud-infra/tls-1-3-session-resumption.md | 321 | PASS w/ issues | accurate; unverifiable "the wiki's API layer" claim |
| cloud-infra/vpn-split-tunneling.md | 320 | PASS (at floor) | exactly 320; trailing bullet |
| cloud-infra/storage-tiering.md | 346 | PASS w/ issues | unsourced "50-80%"/"5-10x"; trailing bullets |
| cloud-infra/snapshot-lifecycle-policies.md | 331 | PASS w/ issues | circular "recorded with their retention matrices here"; trailing bullets |
| cloud-infra/sovereignty-and-compliance-storage.md | 336 | PASS w/ issues | unverifiable "the wiki's data-classification matrix" claim; trailing bullets |
| concepts/stub-criteria.md | 428 | PASS | "placeholder" false positive; good content |
| concepts/activation-patching.md | 404 | PASS w/ issues | duplicate link to causal-interventions-ai; boilerplate annotations |
| concepts/bayesian-networks.md | 396 | PASS | clean; correctly hedged relevance |
| concepts/induction-heads.md | 440 | PASS | accurate; good |
| concepts/polysemanticity.md | 433 | PASS | accurate; boilerplate annotations in Related |
| concepts/sandbagging.md | 470 | PASS w/ issues | "Ai Safety Evals" label; solid body |
| concepts/early-stopping.md | 445 | PASS w/ issues | "eval-splits" lowercase label |
| concepts/forward-chaining.md | 433 | PASS | accurate (XCON example fine); good |
| concepts/temporal-difference-learning.md | 529 | PASS | accurate; good |
| concepts/eval-contamination.md | 406 | PASS | accurate; good |
| data-storage/postgres-tsvector.md | 336 | PASS w/ issues | "insert and query" false positive; dangling bullet |
| data-storage/faiss.md | 366 | PASS | accurate; boilerplate annotations |
| data-storage/hnsw.md | 332 | PASS w/ issues | unsourced "~95% recall"/"10x vector size" |
| data-storage/milvus.md | 337 | PASS w/ issues | dangling bullet |
| data-storage/pinecone.md | 322 | PASS w/ issues | dangling bullet |
| data-storage/simhash.md | 321 | PASS w/ issues | dangling bullet |
| data-storage/scd-type-2-slowly-changing-dimensions.md | 371 | PASS | good; blank line after ## Related |
| dev-tools/correlation-ids.md | 320 | PASS (at floor) | exactly 320; content sound |
| dev-tools/fixed-window.md | 324 | PASS w/ issues | dangling bullet |
| dev-tools/leaky-bucket.md | 329 | PASS w/ issues | dangling bullet |
| dev-tools/fuzzing-tools.md | 325 | PASS w/ issues | dangling bullet |
| dev-tools/link-fix-automation.md | 335 | PASS w/ issues | dangling bullet |
| dev-tools/four-golden-signals.md | 322 | PASS | sound |
| dev-tools/flame-graphs.md | 325 | PASS w/ issues | invented "40-second build" example numbers |
| communities/hotfix-branches.md | 540 | PASS | clean, different (better) template |
| compositions/fencing-tokens.md | 350 | PASS w/ issues | duplicate link to lease-based-locks |
| compositions/lamport-clocks.md | 327 | PASS w/ issues | trailing bullets; unverifiable "the wiki's sync layer" claim |
| decisions/api-access-policies.md | 329 | PASS w/ issues | dangling bullet |

Quantification across the 220-file slice: status failures 0/220 (0%); word-count failures 0/220 (0%); missing/invalid frontmatter 0/220 (0%); broken wikilinks/mdlinks per checker 0/220 (0%); self-links 5/220 (2.3%); real placeholders 0/220 (3 false positives); Related-block annotation boilerplate 93/220 (42%); trailing-bullet defect 59/220 (27%); blank line after "## Related" 20/220 (9%); unverifiable "the wiki's …" relevance claims 20/220 (9%); files at 320–339 words 76/220 (35%); files with any citation URL 0/220.

### Recommendations

1. **Add a provenance gate before the next promotion wave.** The wave's own checklist requires "two or more curl-verified sources"; 0/220 files carry one. Require a `Sources` section (real URLs) for any article containing numeric, vendor, or infrastructure claims, and make the promotion checker fail without it. This is the single highest-impact fix: it turns the "cannot verify" findings into "verified" or "removed".
2. **Remove the machine-generated Related annotations and self-links.** Strip "— the full treatment of this theme" / "— existing graph context" / "— note" / "— see also" labels (215 instances, 93 files), delete the 5 self-links, and deduplicate same-target links (4 files). Enforce in the linter: no self-links, max one link per target.
3. **Re-merge or re-place the 59 trailing "practice" bullets.** Move them back into the Details list in reading order (or promote them to a real section) and restore single-list structure; fix the 37 blank-line-orphaned bullets and the 20 blank lines after "## Related". A structural lint pass can make this mechanical.
4. **Fix the two content defects now**: swap over/under in `concepts/calibration.md` (reliability-diagram paragraph) and rename `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md` to a non-duplicated slug, updating referrers. These are cheap and immediately improve correctness.
5. **Raise the effective promotion floor and require a margin.** With the median at 389.5 and 76 files within 20 words of 320, the threshold invites append-padding (which is visible in the trailing bullets). Set the promotion bar to ~400 body words with a rule that bullets after the RSIS3 relevance paragraph require explicit review, so floor-hitting stops producing the current artifact profile.

---

## Review 3

## Adversarial Review 3 — MyKB Stub Promotion Wave (slice3, 220 files)

Reviewer: adversarial reviewer #3
Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice3.txt` (220 paths)
Areas: dev-tools (21), devops-infra (166), frontend-frameworks (26), identity (7)
Method: ran `check_slice.py`, verified every flagged file by reading it, deep-read 48 files
across all four areas, spot-checked 16 link targets by opening them.

### Verdict

**Score: 79 / 100**

The promotion wave held its hard invariants: all 220 files are `status: growing`, every
body is ≥ 320 words (min observed 323), all six required frontmatter keys are present,
there are no broken wikilinks or markdown links, no missing files, and no non-UTF8 bytes.
I found **no fabrication**: the only URLs in the slice (NIST SP 800-63B, OWASP Auth Cheat
Sheet, GDPR Art. 33, RFC 5321, MITRE ATT&CK TA0006, FIDO Alliance, Wikipedia) are real,
and the technical claims I could check offline (3-2-1 math, 99.9% = 43 min/month, p99
fan-out amplification, CoreDNS `ndots:5`, CSI plugin split, PDB `minAvailable`, GDPR 72h,
Angular signals, GraphQL APQ handshake) are accurate. The score is pulled down by a
systematic template failure: 6 self-links, 16 files with orphan "takeaway" bullets, 14
devops-infra files whose Related sections contain **zero** topical links (only cluster
boilerplate), keyword-matched irrelevant links, and 5 identity files that pad their word
count by repeating the Summary sentence verbatim as the first Details bullet. These are
real defects but not fabricated knowledge; the wiki's memory value is intact.

- Checker: 12 files flagged → 6 confirmed defects (self-links), 6 false positives (all
  placeholder hits were legitimate prose or example domains).
- Per-defect-type: invariant violations 6/220 (2.7%); padding/word-stuffing 5/220
  (2.3%); structural (orphan bullets) 16/220 (7.3%); link hygiene (boilerplate-only
  Related) 14/220 (6.4%); link hygiene (keyword-matched irrelevant links) ≥6/220.

### Critical findings

1. **Self-links in Related sections — 6 files (invariant violation).**
   The cluster-link generator emitted a link to the page itself in each file, labeled
   "related coverage in the same cluster", which is impossible for a related page.
   - `frontend-frameworks/concurrent-rendering.md` (line 25):
     `- [[wiki/frontend-frameworks/concurrent-rendering|Concurrent Rendering]] — related coverage in the same cluster`
   - `frontend-frameworks/reactivity-pitfalls.md` (line 25):
     `- [[wiki/frontend-frameworks/reactivity-pitfalls|Reactivity Pitfalls]] — related coverage in the same cluster`
   - `frontend-frameworks/starttransition.md` (line 25):
     `- [[wiki/frontend-frameworks/starttransition|startTransition]] — related coverage in the same cluster`
   - `frontend-frameworks/suspense-practice.md` (line 25):
     `- [[wiki/frontend-frameworks/suspense-practice|Suspense in Practice]] — related coverage in the same cluster`
   - `frontend-frameworks/vue-composition-api.md` (line 25):
     `- [[wiki/frontend-frameworks/vue-composition-api|Vue Composition API]] — related coverage in the same cluster`
   - `frontend-frameworks/vue-reactivity.md` (line 25):
     `- [[wiki/frontend-frameworks/vue-reactivity|Vue Reactivity]] — related coverage in the same cluster`
   Why it is wrong: a self-link is dead weight, breaks graph tools that assume Related is
   a neighbor set, and shows the Related list was generated without reading it. Suggested
   fix: drop the self entry from the generator output (all six are the 5th of 7 links in
   an otherwise identical template) and re-run the checker's self-link rule on the wave.

### Major findings

1. **Related sections with zero topical links — 14 devops-infra files.**
   These files link only `kubernetes-control-plane`, `observability-pillars`, and the two
   syntheses pages, even though topically adjacent pages exist in the same slice:
   `automated-rollbacks.md`, `cosign-and-sigstore.md`, `devcontainers-revisited.md`,
   `game-days-and-failure-drills.md`, `hostpath-and-subpath.md`,
   `leader-election-and-quorum.md`, `open-tofu-forks.md`,
   `operator-sdk-and-controller-runtime.md`, `pulumi-and-crossplane.md`,
   `readiness-vs-liveness-revisited.md`, `rto-and-rpo.md`, `sbom-and-syft.md`,
   `supply-chain-attestations.md`, `vulnerability-fix-cadence.md`.
   Evidence: `devops-infra/rto-and-rpo.md` Related is only
   `kubernetes-control-plane`, `observability-pillars`, `knowledge-acquisition-workflow`,
   `mykb-acquisition-curation-and-practices` — while `disaster-recovery-tiers.md`,
   `point-in-time-recovery.md`, and `backups.md` (all in this slice) are unlinked.
   `readiness-vs-liveness-revisited.md` does not link `startup-probes-and-graceful-shutdown.md`
   or `health-endpoint-contracts.md`; `cosign-and-sigstore.md` does not link
   `image-signing-and-notary.md` or `supply-chain-attestations.md`. The Related section is
   the primary navigation surface of a knowledge graph; these pages are dead ends.

2. **Keyword-matched irrelevant links (link inflation).**
   Several Related links are topically unrelated and appear matched on a title keyword:
   - `devops-infra/custom-resource-definitions.md` links `[[wiki/os-shell/resource-utilization-analysis|Resource Utilization Analysis]]`,
     `[[wiki/cloud-infra/resource-tagging|Resource Tagging]]`,
     `[[wiki/infrastructure/t-shirt-sizing-and-resource-models|T Shirt Sizing And Resource Models]]`,
     and `[[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]]` — all
     about compute *resources*, none about Kubernetes custom resources (CRDs).
   - `devops-infra/backup-strategies-3-2-1.md` links `[[wiki/devops-infra/cache-invalidation-strategies|Cache Invalidation Strategies]]`
     — a caching page on a backup page — plus `cloud-migration-strategies` and
     `progressive-sync-strategies` (matched the word "strategies").
   - `devops-infra/disaster-recovery-tiers.md` links `[[wiki/cloud-infra/azure-blob-access-tiers|Azure Blob Access Tiers]]`
     and `[[wiki/infrastructure/pulsar-architecture-and-tiers|Pulsar Architecture And Tiers]]`
     — storage/messaging tiers, not DR tiers (matched the word "tiers").
   - `devops-infra/policy-engines-opa-kyverno.md` links `[[wiki/os-shell/regex-engines|Regex Engines]]`.
   - `devops-infra/service-meshes-istio-linkerd.md` links `[[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]`.
   All are labeled with the template phrase `related coverage in the same cluster`, which
   182/220 files use. This reads as an automated linker matching basename keywords without
   semantic checks; it inflates link counts and misdirects navigation.

3. **Orphan "takeaway" bullets appended after the Details list — 16 dev-tools files.**
   Each file ends its Details list with a `- RSIS3 relevance:` bullet, then a blank line,
   then 1–3 additional bullets that belong to no heading and duplicate advice already in
   the list:
   - `dev-tools/log-levels.md`: `- Treat the level contract as part of the code review: wrong levels are caught in review, not in production.`
   - `dev-tools/token-bucket.md`: `- Expose the effective rate and burst in documentation so callers know what the limiter allows before they hit it.`
   - `dev-tools/property-testing-libraries.md` has three stray bullets, including
     `- Combine libraries with model-based testing: ...`
   - `dev-tools/runbook-automation.md` has two stray bullets.
   Others: `log-rotation`, `package-managers`, `printf-debugging`, `profiling-tools`,
   `request-tracing`, `semver-tooling`, `slo-budgets`, `slug-changes`, `status-pages`,
   `summary-quality`, `timeout-policy`, `verbose-flag`. This is a template artifact (the
   takeaway line was appended outside the list) and renders as orphan content between
   Details and Related.

4. **Summary-sentence duplication used to reach the word floor — 5 of 7 identity files.**
   The first Details bullet repeats the Summary's opening sentence verbatim or
   near-verbatim:
   - `identity/brute-force-protection.md`: Summary `Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts so that guessing a password or secret becomes economically infeasible.` → Details bullet `Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts.`
   - `identity/device-fingerprinting.md`: Summary `Device fingerprinting assembles browser, OS, screen, font, and network signals into a stable device identifier without cookies.` → Details bullet starts with the identical sentence.
   - `identity/email-verification.md`: identical sentence repeated as first bullet.
   - `identity/hardware-security-keys.md`: `Hardware security keys (FIDO2/CTAP2 devices such as YubiKeys ...` repeated as `Hardware security keys (FIDO2/CTAP2 devices like YubiKey) ...`.
   - `identity/account-recovery.md`: the NIST SP 800-63B sentence appears in Summary and again as the first Details bullet.
   This is textbook padding (defect class 3/4): ~25 words per file restated with no new
   information to push the body over 320 words. These five files sit at 434–456 words,
   roughly 120 of which is duplicated lead.

5. **Universal trailing boilerplate links — 124 files.**
   Every one of these files ends its Related list with the same two syntheses links and
   identical annotation text: `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb` and
   `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to`.
   The link pair adds no per-file information; on 64 files the entire Related block is
   exactly this 4-link boilerplate (`kubernetes-control-plane` + `observability-pillars` +
   the two syntheses). It makes every page's link graph look connected to the same 4 nodes
   regardless of topic.

### Minor & nits

1. `frontend-frameworks/derived-state.md`: `Selector libraries (Redux \`createSelector\`, Zustand selectors) move the same derivation into the store layer with memoization` — Zustand selectors do not memoize by default (no built-in `createSelector`; needs `useShallow` or middleware); *likely* conflation, minor.
2. `dev-tools/property-testing-libraries.md` links both `[[wiki/dev-tools/property-based-testing|Property-Based Testing]]` and `[[wiki/testing/property-based-testing|Property-Based Testing]]` with identical display text — a basename collision resolved ambiguously; one link is redundant.
3. Boilerplate drift: `identity/account-takeover.md` uses `For RSIS3:` while the other six identity files use `For mykb:` — same slot, two labels.
4. All 220 timestamps are exactly midnight UTC (`T00:00:00Z`) on three dates (07-31, 08-01, 08-02) — templated generation times, not capture times; graph tools cannot distinguish actual edits.
5. `identity/email-verification.md` links `[[wiki/security/ldap|LDAP]] — directory identities often key on email` — LDAP is tangential to email verification; reads as keyword-matched.
6. Illustrative numbers I cannot verify offline (not confirmed defects, flagged per instructions): `dev-tools/profiling-tools.md` "py-spy attach to a slow agent process shows 60% of time in tokenization"; `devops-infra/argocd-applicationsets.md` "`argocd appset list`" (CLI subcommand); `dev-tools/token-bucket.md` "AWS and many gateway rate limits model exactly this". All appear inside `Concrete example` framing, so I treat them as hypotheticals, not fabrication.
7. Repeated sentence template `the mature pattern is ...` closes the Tradeoffs bullet in nearly every dev-tools/devops-infra file; combined with dev-tools bodies clustering at 323–344 words, the files read as minimum-quota generated, though the content itself is accurate.

### Sample audit table

| File (components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| dev-tools/lockfiles.md | 326 | PASS | Accurate; related links topical. |
| dev-tools/log-levels.md | 324 | FAIL (minor) | Orphan takeaway bullet after Details. |
| dev-tools/log-rotation.md | 325 | FAIL (minor) | Orphan takeaway bullet. |
| dev-tools/mutation-testing.md | 344 | PASS | Stryker/PIT, equivalent mutants accurate. |
| dev-tools/package-managers.md | 323 | FAIL (minor) | Orphan takeaway bullet; content accurate. |
| dev-tools/printf-debugging.md | 327 | FAIL (minor) | Orphan takeaway bullet; checker "placeholder" flag is a false positive. |
| dev-tools/profiling-tools.md | 329 | FAIL (minor) | Orphan bullet; unverifiable 60% example. |
| dev-tools/property-testing-libraries.md | 344 | FAIL (major) | 3 orphan bullets; duplicate "Property-Based Testing" display links. |
| dev-tools/request-tracing.md | 338 | FAIL (minor) | Orphan bullet; W3C traceparent claim correct. |
| dev-tools/runbook-automation.md | 335 | FAIL (minor) | 2 orphan bullets. |
| dev-tools/semver-tooling.md | 333 | FAIL (minor) | Orphan bullet; semver claims correct. |
| dev-tools/slo-budgets.md | 330 | FAIL (minor) | Orphan bullet; 43 min/month math correct. |
| dev-tools/status-pages.md | 324 | FAIL (minor) | Orphan bullet. |
| dev-tools/summary-quality.md | 327 | FAIL (minor) | Orphan bullet. |
| dev-tools/tail-latency.md | 327 | PASS | Fan-out math correct; no stray bullet. |
| dev-tools/timeout-policy.md | 328 | FAIL (minor) | Orphan bullet. |
| dev-tools/token-bucket.md | 338 | FAIL (minor) | Orphan bullet; algorithm description accurate. |
| dev-tools/verbose-flag.md | 328 | FAIL (minor) | Orphan bullet. |
| devops-infra/argocd-applicationsets.md | 351 | PASS | Generators accurate; `argocd appset list` cannot verify offline. |
| devops-infra/backup-strategies-3-2-1.md | 431 | FAIL (major) | Keyword-matched links (cache-invalidation, migration, sync strategies). |
| devops-infra/caddy-and-traefik.md | 355 | PASS | Content accurate; example.com flag is a false positive. |
| devops-infra/container-storage-interfaces.md | 369 | PASS | CSI controller/node split accurate. |
| devops-infra/cosign-and-sigstore.md | 354 | FAIL (major) | Boilerplate-only Related; no link to image-signing-and-notary. |
| devops-infra/custom-resource-definitions.md | 399 | FAIL (major) | Keyword-matched "resource" links (resource utilization/tagging/sizing/cgroups). |
| devops-infra/disaster-recovery-tiers.md | 400 | FAIL (major) | Keyword-matched "tiers" links (Azure Blob, Pulsar). |
| devops-infra/envoy-data-plane.md | 388 | PASS | xDS/listener/cluster model accurate. |
| devops-infra/error-budgets.md | 366 | PASS | 99.9%/30d = 43 min correct. |
| devops-infra/haproxy-vs-nginx.md | 380 | PASS | Tradeoffs fair; health-check claims sound. |
| devops-infra/image-signing-and-notary.md | 422 | PASS | Notary/Notation framing reasonable; topical links present. |
| devops-infra/k8s-dns-and-coredns.md | 379 | PASS | ndots/search-domain claims correct. |
| devops-infra/operator-sdk-and-controller-runtime.md | 357 | FAIL (major) | Boilerplate-only Related; envtest claim correct. |
| devops-infra/policy-engines-opa-kyverno.md | 420 | FAIL (major) | regex-engines link irrelevant; Rego/Kyverno content accurate. |
| devops-infra/readiness-vs-liveness-revisited.md | 393 | FAIL (major) | Boilerplate-only Related; probe semantics accurate. |
| devops-infra/retry-policies.md | 408 | PASS | Backoff/jitter/idempotency guidance correct. |
| devops-infra/rto-and-rpo.md | 357 | FAIL (major) | Boilerplate-only Related; content correct. |
| devops-infra/sbom-and-syft.md | 366 | FAIL (major) | Boilerplate-only Related; Syft/Grype claims correct. |
| devops-infra/secret-stores-vault-consul.md | 426 | PASS | Vault/Consul distinction correct; topical links. |
| devops-infra/service-meshes-istio-linkerd.md | 419 | FAIL (minor) | Function-as-a-Service link irrelevant; mesh content accurate. |
| devops-infra/trivy-and-image-scanning.md | 402 | PASS | Trivy Operator/gate claims plausible. |
| frontend-frameworks/angular-signals.md | 464 | PASS | signal/computed/effect/input() claims accurate. |
| frontend-frameworks/concurrent-rendering.md | 502 | FAIL (critical) | Self-link in Related; scheduler model accurate. |
| frontend-frameworks/derived-state.md | 508 | FAIL (minor) | Zustand-selector memoization claim likely conflated. |
| frontend-frameworks/persisted-queries.md | 527 | PASS | APQ handshake and manifest model accurate. |
| frontend-frameworks/react-query-practice.md | 488 | PASS | staleTime/gcTime/invalidation claims accurate. |
| frontend-frameworks/reactivity-pitfalls.md | 527 | FAIL (critical) | Self-link in Related; toRefs/observer guidance accurate. |
| frontend-frameworks/redux-practice.md | 506 | PASS | Redux Toolkit/selector claims accurate. |
| frontend-frameworks/starttransition.md | 499 | FAIL (critical) | Self-link in Related. |
| frontend-frameworks/suspense-practice.md | 510 | FAIL (critical) | Self-link in Related. |
| frontend-frameworks/vue-composition-api.md | 503 | FAIL (critical) | Self-link in Related. |
| frontend-frameworks/vue-reactivity.md | 539 | FAIL (critical) | Self-link in Related. |
| identity/account-recovery.md | 451 | FAIL (major) | NIST sentence duplicated Summary→Details. |
| identity/account-takeover.md | 442 | PASS | Accurate; "For RSIS3:" label drift (nit). |
| identity/breach-notification.md | 446 | PASS | GDPR 72h/Art. 34 claims accurate. |
| identity/brute-force-protection.md | 434 | FAIL (major) | Summary sentence duplicated in Details. |
| identity/device-fingerprinting.md | 456 | FAIL (major) | Summary sentence duplicated in Details. |
| identity/email-verification.md | 452 | FAIL (major) | Summary sentence duplicated; LDAP link tangential. |
| identity/hardware-security-keys.md | 453 | FAIL (major) | Summary sentence duplicated near-verbatim. |

### Recommendations

1. **Fix the cluster-link generator, not the files one by one.** The self-links (6), the
   zero-topical Related blocks (14), and the keyword-matched irrelevant links all come
   from one automated "related coverage in the same cluster" step. Add a self-link guard,
   require ≥1 topical link per Related block (validated against the page's own tags), and
   drop keyword-only matches; then re-run `check_slice.py` plus a semantic spot-check on
   the wave.
2. **Remove the orphan takeaway bullets** (16 dev-tools files): merge the takeaway into
   the `Operational notes` bullet or delete it, and add a lint rule that the Details list
   ends immediately before `## Related` with no dangling bullets.
3. **De-duplicate the identity leads** (5 files): delete the Summary-sentence restatement
   from the first Details bullet and replace it with a genuinely new fact; then enforce
   a similarity check (Summary sentence vs. first Details bullet) in the promotion
   pipeline to stop padding-by-repetition.
4. **Trim the universal syntheses boilerplate**: link the two curation pages from a
   shared template/footer rather than from each article's Related list (124 files), so
   Related lists carry only topical neighbors and the graph stops being a star on 4 nodes.
5. **Re-run the checker with self-links as a hard gate** and add a "no `related coverage
   in the same cluster` label on a link to the page itself" rule; then re-audit the 64
   files whose Related block is exactly the 4-link boilerplate to give each a topical link.

---

## Review 4

## Adversarial Review #4 — MyKB Stub Promotion Wave (slice 4, 219 files)

Reviewer: adversarial reviewer #4. Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice4.txt` (219 paths under `components/mykb/wiki/`; areas: identity, infrastructure, js-ts-ecosystem, llm-agents, memory, meta-learning, ml-frameworks, os-shell).

### Verdict

**Health score: 71 / 100**

The slice's hard invariants mostly held: all 219 files exist, all have `status: growing`, all six required frontmatter keys, all pass the 320-body-word bar, and no non-UTF8 bytes were found. The body content is generally accurate, well-structured, and free of the fabricated model/paper/URL claims this review was hunting for — the strongest files (e.g. `infrastructure/gcp-spanner-google.md`, `ml-frameworks/mixed-precision-training.md`, `meta-learning/willpower-research.md`) are genuinely good reference notes. However, the wave's quality bar was padded, not just met. 98/219 files (45%) carry the boilerplate "related coverage in the same cluster" link descriptions; 80 files repeat a fixed two-line syntheses trailer ("how stubs grow into full articles in mykb" / "the curation loop this stub belongs to") even on topics with zero connection to curation practice; 6 files link to themselves; 2 files duplicate cross-links; 7 files copy the Summary verbatim into the first Details bullet; and dozens of infrastructure files append topically unrelated links (e.g. OSPF Protocols, Storage Systems, WireGuard) purely as padding. One confirmed factual error and one genuinely broken link were found. This is a system-wide link-hygiene and word-stuffing pattern, not random noise — a knowledge store that is a persistent agent memory should treat 45% templated link sections as a real defect.

### Critical findings

1. **`infrastructure/gpu-drivers-and-cuda.md` — fabricated/incorrect kernel fact (confirmed).**
   Quote: "The layer cake: the kernel driver (`nvidia.ko` — *the only kernel-space component*) owns the hardware". The NVIDIA Linux driver is not a single `nvidia.ko`; the kernel package includes multiple modules (`nvidia-modeset.ko`, `nvidia-uvm.ko`, `nvidia-drm.ko`, `nvidia-peermem.ko`, etc.). The parenthetical "the only kernel-space component" is confidently wrong and will mislead retrieval. Fix: say "the core kernel module" or enumerate the module set.
   *(If any vendor change has consolidated to a single module — unverifiable offline — the sentence should still be softened; as written it overstates.)*

2. **`memory/org-mode.md` — broken wikilink (confirmed).**
   Quote: "TODO states track reading and synthesis, and `[[file:...]]` links connect related files". The target `file:...` is a literal placeholder and does not resolve; the checker treats it as broken, and so does the wiki's own resolution. This is one of the wave's two placeholders and the only broken link in the slice. Fix: replace with a real example target (e.g. `[[file:notes.org]]`) or drop the brackets.

3. **Self-links in 6 files (confirmed, systematic).** Each page links to itself in its own Related section with the boilerplate description "related coverage in the same cluster" — a link that cannot resolve to any *other* note and inflates link counts:
   - `js-ts-ecosystem/federated-components.md`: `[[wiki/js-ts-ecosystem/federated-components|Federated Components]]`
   - `js-ts-ecosystem/macrotasks.md`: `[[wiki/js-ts-ecosystem/macrotasks|Macrotasks]]`
   - `js-ts-ecosystem/microtasks.md`: `[[wiki/js-ts-ecosystem/microtasks|Microtasks]]`
   - `js-ts-ecosystem/module-federation.md`: `[[wiki/js-ts-ecosystem/module-federation|Module Federation]]`
   - `js-ts-ecosystem/task-queues.md`: `[[wiki/js-ts-ecosystem/task-queues|Task Queues]]`
   - `meta-learning/delay-of-gratification.md`: `[[wiki/meta-learning/delay-of-gratification|Delay of Gratification]] — self-reference for the construct`
   The self-link is the strongest form of link padding — it adds a Related row that provides no navigation. Fix: delete the row.

4. **Duplicate cross-links (confirmed).** `js-ts-ecosystem/federated-components.md` links `[[wiki/js-ts-ecosystem/module-federation|Module Federation]]` twice with identical text, and `js-ts-ecosystem/module-federation.md` links `[[wiki/js-ts-ecosystem/federated-components|Federated Components]]` twice. Both files also list each other once — so each page's "Related" section pads with a duplicate of a link already present. Fix: deduplicate.

### Major findings

1. **Templated "related coverage in the same cluster" links (98/219 files — ~45% of slice).** These descriptions are exact-string boilerplate, and many link targets are topically unrelated to the page, i.e. link inflation by filler. Confirmed examples:
   - `infrastructure/erasure-coding.md`: Related includes `[[wiki/infrastructure/ospf-protocols|OSPF Protocols]] — related coverage in the same cluster`; erasure coding and OSPF have no topical relation, and `[[wiki/infrastructure/storage-systems|Storage Systems]]` is a generic catch-all repeated across the cluster.
   - `infrastructure/sfp-and-optical-transceivers.md`: Related includes `[[wiki/infrastructure/optical-storage-tape|Optical Storage & Tape]] — related coverage in the same cluster`; optical *transceivers* and optical *tape storage* are unrelated technologies conflated by keyword.
   - `infrastructure/clock-drift-and-ntp.md` and `infrastructure/network-time-protocol.md` and `infrastructure/precision-time-protocol.md`: all three include `[[wiki/cloud-infra/wireguard-protocol|WireGuard Protocol]] — related coverage in the same cluster`; WireGuard is a VPN protocol, unrelated to time sync.
   - `infrastructure/gpu-drivers-and-cuda.md`: includes `[[wiki/infrastructure/storage-systems|Storage Systems]]` and `[[wiki/infrastructure/ospf-protocols|OSPF Protocols]]` with the same filler description.
   Fix: either remove the boilerplate rows or replace descriptions with genuine one-line rationales; audit the cluster's link templates for topical fit.

2. **Fixed syntheses trailer on 80 files (37%).** 80 of 219 files end Related with the identical pair:
   - `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb`
   - `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to`
   These target pages exist and the "stub" wording matches this wave, but the trailer appears on pages with no curation content (e.g. `infrastructure/roce-and-rdma-over-tcp.md`, `infrastructure/clock-drift-and-ntp.md`), reads as batch-generated padding, and dilutes the graph's signal. The two syntheses pages become universal sinks — 86 files link to `syntheses/`. Fix: restrict the trailer to files that actually discuss curation/promotion, or remove it.

3. **Summary copy-pasted into first Details bullet (7 files, confirmed by exact-prefix match).** The Summary paragraph is repeated nearly verbatim as the first bullet of Details, inflating word count without adding information:
   - `identity/jwks.md` — Summary "A JSON Web Key Set (JWKS, RFC 7517) is a JSON document of public keys that verifiers use to check JWT signatures..." repeated as the first Details bullet.
   - `identity/totp.md` — "TOTP (RFC 6238) derives a short-lived code from a shared secret and the current time window, typically 30 seconds, using HMAC." repeated verbatim as first bullet.
   - `identity/otp-codes.md`, `identity/password-managers.md`, `identity/refresh-tokens.md`, `infrastructure/data-anonymization-techniques.md`, `infrastructure/data-encryption-at-rest.md` — same pattern (Details bullet reproduces the Summary's opening sentence).
   Fix: delete the duplicated sentence; the Details section should open with the second, new sentence.

4. **Content-format inconsistency: infra files ship a "For mykb:" paragraph; other areas ship "RSIS3/mykb relevance" or "Agent relevance" (or all three).** The memory/identity/meta-learning files carry bolded sub-bullets (`**Mechanism**`, `**Concrete example**`) while js-ts-ecosystem/ml-frameworks files use plain `-` bullets; several files (e.g. `ml-frameworks/embeddings-api.md`, `llm-agents/reflexion.md`) append two extra `##`-less sub-sections ("Cost per token:", "Quality checks:", "Reflection quality rubric:", "Persistence format:") that are actually `-` bullets masquerading as sections. The template is consistent enough per area to read as batch-generated, and the rubric claims "structural defects" are in scope. Not individually fatal; a symptom of the same templating problem.

5. **RSIS3 relevance claims are unverifiable and often boilerplate (e.g. `ml-frameworks/embeddings-api.md`: "the wiki's search fuses TF-IDF, embeddings, and backlinks"; `llm-agents/agent-telemetry-schema.md`: "the wiki's telemetry schema is the contract every loop agent emits against").** These may be true of the repo, but several pages assert dashboard behaviors that I could not verify against the codebase within scope; they read as template-fitted claims. Marked as "cannot verify" per the review rules — they are a style/cost risk, not confirmed fabrication.

### Minor & nits

1. `infrastructure/tokenization-and-masking.md` — placeholder `user1@example.com` flagged by the checker; in context it is an illustrative example, not a TODO, so **not a defect**. (Recorded to document the false-positive.)
2. `memory/org-mode.md` — placeholder `TODO` in "TODO states track reading and synthesis" is a legitimate noun of org-mode syntax, **not a defect**; but the file is a mass of em-dashes and the Details/Related trailer pattern applies.
3. Timestamps cluster on exactly three values (`2026-08-02` ×138, `2026-07-31` ×58, `2026-08-01` ×23) — consistent with batch generation; not a defect per se, but means "timestamp" carries no per-file provenance signal.
4. 8 files carry a non-required `source:` frontmatter key (RFC/OWASP/Wikipedia URLs) while the other 211 do not — inconsistent schema; the checker's required-key list doesn't include it, so undocumented drift.
5. `[[wiki/index|Wiki Index]]` links (e.g. `memory/obsidian.md`, `memory/atomic-notes.md`, `memory/digital-garden.md`) resolve only via basename fallback to root `index.md` — there is no `wiki/index.md`; works, but fragile and indistinguishable from a near-miss.
6. In `identity/password-managers.md`: "a breach at a forum exposes one of those passwords" — breaches typically expose *hashed* passwords; the sentence presumes plaintext. Minor imprecision in an otherwise good file.
7. `infrastructure/precision-time-protocol.md` — "sub-microsecond accuracy over Ethernet" and "nanosecond-level precision on the wire" are both stated; the two are different claims (precision vs. accuracy) and the summary's "sub-microsecond" conflicts with the body's "nanosecond-level." Minor terminology sloppiness.
8. Em-dash overuse is universal across the slice (every Details bullet uses " — ") — style noise that compounds the batch feel.
9. `infrastructure/roce-and-rdma-over-tcp.md` — RoCEv1 described as "operates on a single L2 Ethernet segment"; correct per v1 spec, but worth noting v1 is legacy and v2 is the deployed variant — the file leads with v1 without saying it is legacy.
10. `llm-agents/prompt-caching.md` — "80-90% of input tokens at cache prices" is a plausible claim but cannot be verified against provider pricing offline; flagged for provenance rather than accepted.

### Sample audit table

| File | Words | Verdict | Notes |
|---|---|---|---|
| infrastructure/gpu-drivers-and-cuda.md | ~460 | FAIL | Confirmed factual error: "nvidia.ko — the only kernel-space component" (multi-module driver); filler links to Storage Systems/OSPF |
| memory/org-mode.md | ~400 | FAIL | Broken `[[file:...]]` link; TODO placeholder (benign); good substance otherwise |
| js-ts-ecosystem/federated-components.md | ~330 | FAIL | Self-link + duplicate module-federation link + filler trailer |
| js-ts-ecosystem/module-federation.md | ~360 | FAIL | Self-link + duplicate federated-components link + filler trailer |
| js-ts-ecosystem/macrotasks.md | ~330 | FAIL | Self-link in Related; content accurate |
| js-ts-ecosystem/microtasks.md | ~330 | FAIL | Self-link in Related; content accurate |
| js-ts-ecosystem/task-queues.md | ~330 | FAIL | Self-link in Related; content accurate |
| meta-learning/delay-of-gratification.md | ~420 | FAIL | Self-link in Related; marshmallow reanalysis content is accurate |
| identity/jwks.md | 462 | FAIL | Summary copy-pasted into first Details bullet; otherwise correct RFC 7517 content |
| identity/totp.md | 457 | FAIL | Summary copy-pasted into first Details bullet; RFC 6238 content correct |
| identity/refresh-tokens.md | 456 | FAIL | Summary copy-pasted into first Details bullet; RFC 6749 content correct |
| identity/password-managers.md | 486 | FAIL | Summary copy-pasted into first Details bullet; "breach exposes password" imprecision |
| infrastructure/tokenization-and-masking.md | ~420 | PASS* | `example.com` false positive; content accurate; solid vault/masking tradeoffs |
| infrastructure/erasure-coding.md | 512 | FAIL | Topically unrelated Related rows (OSPF, Storage Systems); content (Reed-Solomon 6+3) accurate |
| infrastructure/clock-drift-and-ntp.md | ~470 | FAIL | WireGuard in Related; NTP mechanics accurate |
| infrastructure/network-time-protocol.md | ~440 | FAIL | WireGuard/NAT in Related; four-timestamp exchange accurate |
| infrastructure/precision-time-protocol.md | ~460 | FAIL | WireGuard in Related; precision-vs-accuracy wording conflict; BMCA correct |
| infrastructure/rdma-and-infiniband.md | 531 | FAIL | Filler trailer; EDR/HDR/NDR rates and lossless claims accurate |
| infrastructure/roce-and-rdma-over-tcp.md | 399 | FAIL | Filler trailer; RoCEv1/v2 mechanics accurate (v1 marked legacy only implicitly) |
| infrastructure/nvme-over-fabrics-tcp.md | ~430 | FAIL | Filler trailer; queue-pair↔TCP-connection mapping accurate |
| infrastructure/sfp-and-optical-transceivers.md | ~420 | FAIL | "Optical Storage & Tape" in Related (keyword conflate); SFP/QSFP-DD facts accurate |
| infrastructure/gcp-spanner-google.md | 511 | PASS | TrueTime/external consistency, interleaved tables, hotspot guidance all accurate; clean links |
| infrastructure/snowflake-architecture.md | 379 | PASS | Three-layer model and micro-partitions accurate; links on-topic |
| infrastructure/azure-synapse.md | 452 | PASS | Dedicated/serverless SQL, Synapse Link accurate; links on-topic |
| infrastructure/network-policy.md | ~430 | PASS | podSelector/ingress-egress semantics accurate; default-deny guidance correct; links on-topic |
| infrastructure/ipfs-and-content-addressing.md | ~450 | FAIL | Filler trailer + OSPF row; CID/Merkle DAG content accurate |
| js-ts-ecosystem/vite-practice.md | ~360 | PASS | esbuild-dev/Rollup-prod description accurate; links on-topic (some filler description text) |
| js-ts-ecosystem/top-level-await.md | ~350 | PASS | ESM-only constraint, importer blocking accurate; generic filler rows |
| ml-frameworks/prefill-and-decode.md | ~380 | PASS | TTFT/decode split and speculative-decode mitigations accurate |
| ml-frameworks/streaming-responses.md | ~380 | PASS | SSE deltas and proxy-buffering failure accurate |
| ml-frameworks/mixed-precision-training.md | ~400 | PASS | FP16/BF16/FP8, loss scaling, master weights accurate |
| ml-frameworks/embeddings-api.md | ~380 | PASS* | Accurate; RSIS3 claim "fuses TF-IDF, embeddings, backlinks" unverifiable in scope |
| ml-frameworks/openai-api.md | ~420 | PASS* | Accurate; "gpt-4o style aliases" cannot be verified as current in 2026 |
| llm-agents/reflexion.md | ~380 | PASS | Pattern described accurately; light link trailer |
| llm-agents/tree-of-thought.md | ~380 | PASS | BFS/DFS framing accurate |
| llm-agents/agent-logs.md | ~340 | PASS | Structured-logging advice sound; links on-topic |
| llm-agents/prompt-caching.md | ~380 | PASS* | Accurate; "80-90% at cache prices" unverifiable |
| memory/obsidian.md | ~430 | PASS | Local-first/wikilink description accurate; `wiki/index` basename-resolves |
| memory/atomic-notes.md | ~380 | PASS | "Rule of one" accurate; links on-topic |
| memory/progressive-summarization.md | ~420 | PASS | Layer model accurate |
| memory/systems-consolidation.md | ~410 | PASS | Hippocampal-to-cortical model and multiple-trace theory accurate |
| meta-learning/willpower-research.md | ~430 | PASS | RRR/replication-crisis summary accurate; no fabrication |
| meta-learning/grit-research.md | ~380 | PASS | Conscientiousness-overlap critique accurate |
| os-shell/aio-and-epoll.md | ~450 | PASS | O_DIRECT/buffered-fallback/AIO constraints accurate |
| os-shell/btrfs-features-and-limitations.md | ~480 | PASS | CoW snapshots, RAID5/6 caveats, snapper accurate |

Word counts are body-word counts (frontmatter excluded) computed the same way as `check_slice.py`. `PASS*` = content accurate, with an unverifiable or borderline item noted.

### Recommendations (top 5, by impact)

1. **Kill the boilerplate Related sections.** Remove or rewrite the ~98 "related coverage in the same cluster" rows, the ~80 fixed syntheses trailers, and all self-links/duplicate links. A knowledge graph whose edges are templated is actively misleading: the padding rows (OSPF/Storage Systems/WireGuard) will be retrieved as "related" by any graph or backlink consumer.
2. **Fix the confirmed factual error and the broken link first** — `gpu-drivers-and-cuda.md` ("only kernel-space component") and `org-mode.md` (`[[file:...]]`). These are the two defects that poison a specific retrieval, which is the actual cost model for this wiki.
3. **Remove summary-duplication padding** from the 7 files where the first Details bullet repeats the Summary; enforce a "no verbatim Summary sentence in Details" rule in the promotion checker so the 320-word bar cannot be met by copying the summary.
4. **Add link-hygiene checks to the promotion pipeline**: self-link detection (already in `check_slice.py`), duplicate-target detection, topically-garbage boilerplate description detection, and a whitelist/denylist for the syntheses trailer. These are cheap string checks that would have caught 90% of this slice's defects.
5. **Require per-file provenance on the RSIS3/mykb relevance claim.** Either verify claims like "the wiki's search fuses TF-IDF, embeddings, and backlinks" against the repo before publishing, or label them as design intent; batch templates that assert system behavior are how unsupported claims enter a memory store.

---

## Review 5

## Adversarial Review #5 — MyKB Stub-Promotion Wave (slice 5, 219 files)

Reviewer: adversarial-reviewer-5
Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice5.txt` (219 files)
Areas: os-shell, prompt-engineering, software-engineering, web-platforms, syntheses, security-auth, pulses, shell-environment, tooling
Checker run: `python3 ops/reports/adversarial-reviews/check_slice.py <slice>` → 186 clean / 33 flagged; all flags verified by opening the files.

### Verdict

**Health score: 64 / 100**

The wave's core invariants held: all 219 files are `status: growing`, all exceed the 320-body-word floor (min observed 320, in `web-platforms/aspect-ratio-images.md` and `web-platforms/polyglot-xss.md`), all six required frontmatter keys are present, and no UTF-8/markdown-link violations were found. Content quality is genuinely better than a word-count game — the os-shell, software-engineering, and prompt-engineering articles I deep-read are mostly accurate, specific, and technically sound. However, the wave shipped with a systemic link-hygiene and template-artifact problem: 24 confirmed self-links (11.0%), 6 files with broken or truncated links (2.7%), 27 files with generator boilerplate descriptors ("related coverage in the same cluster" plus syntheses meta-links) that often point at topically unrelated pages (12.3%), 5 near-duplicate article pairs, 6 syntheses files whose `type: "concept"` contradicts their location, one corrupted sentence that leaked generator self-correction into a published article, and verifiably wrong numeric claims in `web-platforms/contrast-ratios.md`. For a knowledge base whose value is retrievability and linkability, these are not nits; they degrade the store every time an agent follows a self-link or a "same cluster" link to an unrelated page. The checker also has blind spots it missed entirely (unclosed `[[` links, missing `README` targets, self-link alias variants), which should be fixed before the next wave.

Quantified: word-min 0/219 fail (0%), status 0/219 (0%), frontmatter-keys 0/219 (0%), self-links 24/219 (11.0%), broken/truncated links 6/219 (2.7%), boilerplate-template artifacts 27/219 (12.3%), type/tag contradictions 6/219 (2.7%), corrupted sentence 1/219 (0.5%), wrong numeric claims 1/219 (0.5%), near-duplicate pairs 5 (8 slice files, 3.7%), checker placeholders 9 flagged → 0 confirmed (all false positives), checker wikilink flag 1 flagged → 0 confirmed (false positive: POSIX `[[:alpha:]]` class).

### Critical findings

1. **Truncated, unclosed wikilinks to a non-existent namespace (3 files).** Each file's last Related line is cut mid-link: no closing `]]`, alias is a fragment, and the target namespace `raw/` does not exist anywhere under `components/mykb/wiki/` (verified: no `raw/` directory).
   - `prompt-engineering/indirect-injection.md` (line 30): `- [[raw/archive/session-artifacts-2026-07/topics/security|security — Data-channel trust boundaries`
   - `prompt-engineering/prompt-leakage.md` (line 30): `- [[raw/archive/session-artifacts-2026-07/topics/security|security — Disclosure as a security concern`
   - `prompt-engineering/agentic-rails.md` (line 30): `- [[raw/archive/session-artifacts-2026-07/topics/security|security — Action policy as security control`
   Why it is wrong: the links are structurally invalid Markdown, the anchor text is truncated mid-sentence, and the target cannot resolve. The checker missed all three because it only matches closed `[[…]]` forms. Suggested fix: delete the lines or complete them to a real target; add a checker rule for `[[` without `]]`.

2. **Verifiably wrong numeric claims in `web-platforms/contrast-ratios.md`.** The article states: `#767676 gray on white fails 4.5:1 (about 4.1:1), while #595959 passes (about 5.9:1)`. Computing WCAG relative luminance (sRGB linearization, `(L1+0.05)/(L2+0.05)`): `#767676` on white is **4.54:1** (passes AA normal text), and `#595959` on white is **7.0:1**. Both numbers are wrong, and the first claim inverts the pass/fail verdict — a reader using this note to pick accessible grays will be misled in both directions. Suggested fix: recompute with a real contrast tool (or pick colors that genuinely illustrate the pass/fail boundary, e.g. `#777777` ≈ 4.48:1) and re-verify every example in the article.

3. **Corrupted generator sentence in `web-platforms/dom-clobbering.md`.** The Operational tradeoffs bullet contains leaked model self-correction text: `defenses include using const/let shadows? No — the fix is not using undeclared globals: read via window["name"] after checking typeof, use symbols or Map for name storage, and strip id/name from untrusted markup.` The phrase "using const/let shadows? No —" is not English prose and appears to be an aborted draft; it reads as if a generator mid-sentence corrected itself and the artifact was published. For a memory store, this is exactly the "confident unsupported/padded" class of content the wave was supposed to filter. Suggested fix: rewrite the sentence to `defenses include not relying on undeclared globals: read via window["name"] after checking typeof …`.

4. **Broken `README` links (3 files).** Well-formed links whose targets do not exist; the wiki uses `index.md` instead:
   - `syntheses/evidence-and-provenance.md` (line 28): `- [[wiki/sources/README|Sources]] — the namespace holding evidence` — `sources/README.md` missing (`sources/index.md` exists).
   - `software-engineering/architecture-decision-records.md` (line 28): `- [[wiki/sources/README|Sources]] — decision provenance belongs with source records` — same missing target.
   - `syntheses/knowledge-acquisition-workflow.md` (line 29): `- [[wiki/syntheses/README|Syntheses]] — the namespace this stub belongs to` — `syntheses/README.md` missing (`syntheses/index.md` exists).
   The checker did not flag these (it appears not to resolve `wiki/`-prefixed targets). Suggested fix: retarget to `[[wiki/sources/index|Sources]]` / `[[wiki/syntheses/index|Syntheses]]` and add target-existence validation to the checker.

### Major findings

1. **24 confirmed self-links, all in `web-platforms/` (11.0% of slice).** Every flagged self-link is real: each file's Related section links back to itself, e.g. `web-platforms/css-animations.md` line 29: `- [[wiki/web-platforms/css-animations|CSS Animations]]`; same pattern in css-transforms, css-transitions, dark-mode-practice, device-detection, dom-clobbering, feature-queries, inline-svg, media-queries-practice, pointer-events-css, prefers-color-scheme, prefers-contrast, prototype-pollution-web, scroll-behavior, scroll-snap, sprite-sheets, stacking-contexts, sticky-position, supports-rule, svg-animation, touch-action-css, user-agent-parsing, xs-leaks, z-index-management. This looks like one template bug (the Related list was generated without excluding the article's own slug). A self-link in "Related" is dead weight and signals an uncurated link list. Fix: remove the self-referencing bullet from all 24 files; add a self-target check to the invariant checker.

2. **Template boilerplate in 27 files (12.3%): "related coverage in the same cluster" + syntheses meta-links.** 24 `os-shell/` files (e.g. fuse-and-user-space-filesystems, io-uring-and-async-io, mdadm-and-lvm2, oom-killer-and-memory-pressure, path-resolution-and-symlinks, users-groups-and-acls, zfs-features-and-snapshots — see the file list in the scan output) plus the 3 `shell-environment/` files carry identical Related entries: several links annotated `— related coverage in the same cluster` and, in every one, the identical pair `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb` and `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to`. Example (`os-shell/io-uring-and-async-io.md`): `- [[wiki/infrastructure/io-latency-and-iops|IO Latency & IOPS]] — related coverage in the same cluster`. The syntheses meta-links are identical in all 27 files and describe the curation process, not the article's topic — they are padding that inflates the link count and adds noise to the graph. Fix: replace with hand-curated topical links; at minimum drop the two syntheses meta-links.

3. **Topically wrong "same cluster" links.** The cluster boilerplate matches by keyword, not meaning, producing links that actively mislead:
   - `os-shell/users-groups-and-acls.md` links `[[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]]` — that page is about job control / controlling terminals; it has nothing to do with user/group identity and POSIX ACLs. Keyword match on "groups".
   - `os-shell/path-resolution-and-symlinks.md` links `[[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]]`, `[[wiki/devops-infra/observability-of-network-path|Observability of the Network Path]]`, and `[[wiki/os-shell/dns-resolution|DNS Resolution]]` — DNS is networking resolution, not filesystem path resolution. Keyword match on "resolution".
   - `os-shell/mdadm-and-lvm2.md` and `os-shell/io-uring-and-async-io.md` link `[[wiki/os-shell/memory-management-paging|Memory Management & Paging]]` — no topical relationship to RAID/LVM or io_uring beyond both being kernel-adjacent.
   Fix: re-curate these links or delete them; a wrong link in a memory store is worse than no link.

4. **Five near-duplicate file pairs (8 slice files).** The wave promoted distinct slugs for the same concept with heavily overlapping content:
   - `os-shell/path-resolution.md`, `os-shell/path-resolution-and-symlinks.md`, `os-shell/symlinks.md` (triplet; both path articles cover the same namei walk, ELOOP, openat2, realpath material).
   - `os-shell/users-and-groups.md` vs `os-shell/users-groups-and-acls.md` (both cover UID/GID, /etc/passwd, NSS, effective UID, sudo).
   - `web-platforms/cumulative-layout-shift.md` vs `web-platforms/cls-avoidance.md` (identical summary, mechanism, main-causes, and Related lists).
   - `web-platforms/color-spaces.md` vs `web-platforms/srgb-vs-p3.md` (both: sRGB ~35% / P3 ~45%, gamut mapping, oklch authoring, fallback ordering).
   - `web-platforms/dvh-svh.md` vs `web-platforms/vw-vh.md` (both: mobile URL-bar problem, dvh tracking, vh fallback order).
   Duplicated concepts split the corpus, force agents to choose between near-identical pages, and make future edits drift. Fix: designate one canonical slug per concept, merge, and turn the others into redirect notes (or delete); add a near-duplicate detection pass before promotion.

5. **`syntheses/` frontmatter contradicts location and status (6 files).** All six syntheses files in the slice declare `type: "concept"` (AGENTS.md defines synthesis notes with OKF frontmatter, and MyKB's `syntheses/` namespace implies `type: synthesis`): `syntheses/bug-bounty-ai.md`, `syntheses/coordinated-disclosure.md`, `syntheses/evidence-and-provenance.md`, `syntheses/knowledge-acquisition-workflow.md`, `syntheses/model-updates-risks.md`, `syntheses/safety-case-approach.md`. Two additionally retain the tag `"stub"` while claiming `status: "growing"` (`syntheses/evidence-and-provenance.md` tags `["stub", "provenance", "evidence", "open-questions"]`; `syntheses/knowledge-acquisition-workflow.md` tags `["stub", "knowledge-acquisition", "open-questions"]`) — a self-contradiction the promotion wave should have cleaned. Fix: set `type: "synthesis"` and drop the `stub` tag on growing files.

6. **Duplicate RSIS3 paragraphs in `software-engineering/actor-model.md`.** The Operational tradeoffs bullet ends with an inline `RSIS3 relevance:` clause, and the very next bullet is a second `RSIS3/mykb relevance:` paragraph — the same generator pattern that elsewhere produces one section, here produced two: `…matching the loop's need for bounded, resumable work.` followed by `- RSIS3/mykb relevance: the wiki records actor-style designs for agent runtimes so handoff protocols inherit supervision and delivery discipline.` Minor duplication, but it recurs across templates (see Minor). Fix: keep one RSIS3 relevance bullet per article.

### Minor & nits

1. **Orphan bullet in `prompt-engineering/multi-step-reasoning.md`.** Between the RSIS3 relevance bullet and `## Related` sits a floating bullet with no heading: `- Separate reasoning output from the final answer in the prompt so steps inform, not pollute, the conclusion.` Move it under Details or delete.
2. **Nonstandard `source:` frontmatter key (2 files).** `security-auth/ssrf-prevention.md` and `security-auth/bug-bounty.md` add `source: ["https://…"]` to the six-key schema. Harmless but schema-inconsistent with the rest of the wave; either adopt `source` as a documented key or drop it.
3. **Inconsistent RSIS3 section naming across templates.** os-shell/web-platforms use `RSIS3/mykb relevance:`, prompt-engineering/security-auth use `RSIS3 relevance:`. Cosmetic, but it makes template provenance (and future de-boilerplating) harder to automate.
4. **Borderline word counts.** `web-platforms/aspect-ratio-images.md` and `web-platforms/polyglot-xss.md` sit at exactly 320 body words — right at the floor. Nothing wrong per the invariant, but zero headroom suggests these two were padded to the threshold rather than written to depth; worth a human skim.
5. **Lowercase title in `web-platforms/pointer-events-css.md`** (`title: "pointer-events CSS"` and self-link alias `[[…|pointer-events CSS]]`) — inconsistent with sentence-case titles elsewhere in the slice.
6. **Checker false positives (not defects, but worth recording).** The 9 placeholder flags (`TODO` in `os-shell/grep-patterns.md` is an example search string; `example.com` in dns-prefetch/preconnect/url-normalization are RFC-reserved example domains; "placeholder text/box" in contrast-ratios/aspect-ratio-images/reserved-space are legitimate technical terms; "insert nodes" / "insert as nodes" / "insert via node APIs" in mutation-xss/safe-html-rendering are natural language) and the single wikilink flag (`:alpha:` in `os-shell/grep-patterns.md` is the POSIX character class `[[:alpha:]]` inside a regex discussion) are all false positives. The checker needs a `[[:…:]]` exception and a stoplist for example domains.

### Sample audit table

| File (components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| os-shell/grep-patterns.md | 475 | PASS | Accurate; `[[:alpha:]]` flag is a false positive; TODO is an example |
| os-shell/path-resolution.md | 485 | PASS | Accurate; overlaps path-resolution-and-symlinks (duplication) |
| os-shell/path-resolution-and-symlinks.md | 521 | FAIL | "same cluster" boilerplate; DNS-resolution links are topical mismatches |
| os-shell/symlinks.md | 518 | PASS | Accurate; well-linked (path-resolution, dotfiles, backups) |
| os-shell/users-and-groups.md | 527 | PASS | Accurate; clean Related links |
| os-shell/users-groups-and-acls.md | 556 | FAIL | Boilerplate; process-groups-and-sessions link is a keyword mismatch |
| os-shell/io-uring-and-async-io.md | 479 | FAIL | Content accurate (5.1 kernel, IORING_* correct); boilerplate + memory-management link mismatch |
| os-shell/oom-killer-and-memory-pressure.md | 578 | PASS | Content accurate (oom_score, cgroups, earlyoom/systemd-oomd); boilerplate only |
| os-shell/exit-codes.md | 509 | PASS | Accurate (126/127/128+N, pipefail, mod-256 truncation) |
| os-shell/mdadm-and-lvm2.md | 520 | FAIL | Content accurate; boilerplate; memory-management-paging link mismatch |
| os-shell/zfs-features-and-snapshots.md | 562 | PASS | Content accurate (RAID-Z, ARC, send/receive); boilerplate only |
| prompt-engineering/adversarial-prompts.md | 360 | PASS | Accurate; well-linked |
| prompt-engineering/tool-selection.md | 360 | PASS | Accurate; coherent |
| prompt-engineering/indirect-injection.md | 389 | FAIL | Truncated `[[raw/archive/…]]` link (critical); otherwise accurate |
| prompt-engineering/prompt-leakage.md | 336 | FAIL | Truncated `[[raw/archive/…]]` link (critical) |
| prompt-engineering/agentic-rails.md | 332 | FAIL | Truncated `[[raw/archive/…]]` link (critical) |
| prompt-engineering/multi-step-reasoning.md | 325 | PASS | Accurate (Wei et al. 2022 correct); orphan bullet nit |
| prompt-engineering/json-mode-function-calling.md | 324 | PASS | Accurate |
| software-engineering/saga-orchestration.md | 330 | PASS | Accurate; clean links |
| software-engineering/transactional-outbox.md | 361 | PASS | Accurate (dual-write, CDC, at-least-once); clean links |
| software-engineering/bus-factor.md | 366 | PASS | Accurate; clean links |
| software-engineering/actor-model.md | 348 | PASS | Accurate; duplicate RSIS3 paragraphs (major #6) |
| software-engineering/event-carried-state.md | 332 | PASS | Accurate; clean links |
| software-engineering/retry-after.md | 340 | PASS | Accurate (429/503, HTTP-date, jitter) |
| software-engineering/architecture-decision-records.md | 351 | FAIL | Broken `[[wiki/sources/README|Sources]]` link (critical #4) |
| web-platforms/css-animations.md | 332 | FAIL | Self-link in Related (major #1); content accurate |
| web-platforms/cumulative-layout-shift.md | 321 | PASS | Accurate; near-duplicate of cls-avoidance (major #4) |
| web-platforms/cls-avoidance.md | 326 | PASS | Near-duplicate of cumulative-layout-shift |
| web-platforms/color-spaces.md | 336 | PASS | Near-duplicate of srgb-vs-p3; "~35%/~45%" figures unverifiable offline but consistent |
| web-platforms/srgb-vs-p3.md | 339 | PASS | Near-duplicate; otherwise accurate |
| web-platforms/contrast-ratios.md | 335 | FAIL | Wrong numeric claims: #767676 is 4.54:1 (passes), #595959 is 7.0:1 (critical #2) |
| web-platforms/dom-clobbering.md | 338 | FAIL | Corrupted sentence "using const/let shadows? No —" (critical #3); self-link |
| web-platforms/xs-leaks.md | 341 | FAIL | Self-link; content accurate (CORP/COOP/COEP correct) |
| web-platforms/webp-vs-avif.md | 341 | PASS | Accurate; clean links |
| web-platforms/dvh-svh.md | 336 | PASS | Accurate; near-duplicate of vw-vh |
| web-platforms/vw-vh.md | 339 | PASS | Accurate; near-duplicate of dvh-svh |
| web-platforms/toctou.md | 336 | PASS | Accurate (openat2/O_NOFOLLOW, open-then-fstat); clean links |
| syntheses/evidence-and-provenance.md | 520 | FAIL | type "concept" + "stub" tag vs growing; broken sources/README link |
| syntheses/knowledge-acquisition-workflow.md | 508 | FAIL | type "concept" + "stub" tag; broken syntheses/README link |
| security-auth/ssrf-prevention.md | 332 | PASS | Accurate; nonstandard `source:` frontmatter key (nit) |
| pulses/capability-probes.md | 340 | PASS | Accurate; clean links |

### Recommendations

1. **Fix broken/truncated links and close the checker's blind spots (highest impact).** Repair the 3 unclosed `[[raw/archive/…]]` lines and the 3 `README` links (retarget to `sources/index` / `syntheses/index`); then extend `check_slice.py` to flag (a) any `[[` without closing `]]`, (b) `wiki/`-prefixed targets that don't resolve to a `.md` file, and (c) self-target links. These three rules would have caught every critical finding above at generation time.
2. **Strip the self-links and template boilerplate.** Remove the self-referencing Related bullet from the 24 `web-platforms/` files and delete the "related coverage in the same cluster" + syntheses meta-link boilerplate from the 27 `os-shell/`/`shell-environment/` files, replacing them with hand-curated topical links. This removes ~12% of the slice's noise and fixes the keyword-mismatch links (process-groups, DNS-resolution, memory-management) in the same pass.
3. **De-duplicate the five near-duplicate pairs.** Pick canonical slugs for path-resolution (three files), users/groups (two), CLS (two), color spaces (two), and viewport units (two); merge content, convert losers to redirects, and add a similarity gate to the promotion pipeline so future waves reject near-identical siblings.
4. **Repair the syntheses namespace.** Set `type: "synthesis"` on the six `syntheses/` files per AGENTS.md, remove the lingering `"stub"` tag from the two growing files, and have the checker validate `type` against directory namespace.
5. **Re-verify all numeric claims and corrupted prose before promotion.** Correct `web-platforms/contrast-ratios.md` (recompute examples with a WCAG calculator; current values are wrong and invert a pass/fail verdict) and rewrite the corrupted sentence in `web-platforms/dom-clobbering.md`. Add a cheap "generation-artifact" scan for phrases like "? No —" and "shadows?" plus a spot human review of any file whose body words are within 5% of the floor.

---
