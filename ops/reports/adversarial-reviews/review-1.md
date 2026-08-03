# Adversarial Review 1 — MyKB Stub-Promotion Wave (slice1, 220 files)

Reviewer: adversarial #1 · Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice1.txt` (220 files)
Areas in slice: api-protocols (117), cloud-infra (60), ai-ml (32), agent-systems (8), android-core (3)
Method: invariant checker + manual verification of all 42 flagged files + deep-read of 47 files + 16 link-target spot checks.

## Verdict

**Health score: 68 / 100**

The wave met the mechanical bar it set: all 220 files have `status: growing`, ≥320 body words (min exactly 320), and complete frontmatter; I confirmed zero broken wikilinks/markdown links among every link I checked, and found no fabricated papers, models, or API names in 47 deep-reads — the technical prose (OAuth grants, CL.TE smuggling, Chinchilla 70B/1.4T, GCP tier minimums, Android ANR timeouts) is genuinely accurate and useful. The score is dragged down by a systemic, machine-generated Related-section failure: **30 files link to themselves (33 self-links, two files triple-repeated)**, 17 files contain duplicated Related entries, 114 files (51.8%) repeat the boilerplate annotation "related coverage in the same cluster" (799 occurrences), 41 of 60 cloud-infra files end with an identical, partly irrelevant 4-link tail (CPU articles linking to Networking Fundamentals), 3 android-core files kept leftover stub fragments above their expanded body (duplicating content), and the wave's own meta-articles (graph-density-metrics, link-diversity, article-health-scores) describe exactly the self-link and link-spam pathologies the wave then shipped. Six-plus files also carry unverifiable "the wiki's X does Y" claims (DNSSEC key rollover, a 30/90/365 backup lifecycle, HTTP/3 edge serving) for which the repo shows no supporting config — possible invented specificity. Padding is real but mostly *in the link layer*: e.g. `remote-access-methods.md` clears the 320-word floor only because ~72 of its 320 words are Related list and "RSIS3/mykb relevance" boilerplate.

Per-defect-type quantification (of 220 files): status ≠ growing **0 (0%)** · body < 320 **0 (0%)** · missing frontmatter keys **0 (0%)** · self-links **30 (13.6%)** · duplicated Related entries **17 (7.7%)** · "related coverage in the same cluster" boilerplate **114 (51.8%)** · fixed 4-item Related tail **41/60 cloud-infra (68.3%)** · leftover stub fragments **3 (1.4%)** · placeholder text **0 (0%) — all 14 checker flags were false positives** · broken links **0 (0%, checker); 0/16 spot-checked**.

## Critical findings

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

## Major findings

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

## Minor & nits

- **Placeholder flags: all 14 checker flags are false positives, verified one-by-one.** Twelve are legitimate RFC 2606 `example.com` doc domains (e.g. `api-protocols/cookie-scoping.md` "With Domain=example.com it is sent to example.com and all subdomains"; `cloud-infra/dnssec-and-validation.md` "an attacker forges a DNS answer for example.com"); `ai-ml/article-health-scores.md` uses "placeholder text" descriptively ("headings present, no placeholder text"); `api-protocols/hash-collision-dos.md` flags are regex artifacts ("every insert and lookup degenerates into a linked-list scan"). No action needed — recorded so the checker's precision is known.
- **"RSIS3/mykb relevance" is a formulaic closing section in 186/220 files (84.5%).** House style, but it is near-template filler in many files ("storing the decision rule here keeps loop-generated incident reviews consistent across sessions" — `401-vs-403.md`). Fine as a frame; the unverifiable variant is the problem (Major #6).
- **Missing `## Summary` heading in the 3 android-core files** (anr-diagnostics, app-threading, dp-vs-px) — they use an intro paragraph instead; inconsistent with the other 217 files.
- **Extra `source: []` frontmatter key** in the 3 android-core files — empty list, present nowhere else in the slice; either populate or drop.
- **`cloud-infra/coldline-and-archive-storage-classes.md`**: "5TB of legal holds in Archive at ~$0.004/GB-month" — GCP Archive list pricing in us-central1 is ~$0.0012/GB-month; $0.004 is Coldline pricing. Prices vary by region and change, so this is "likely conflated" rather than certain; the "5x saving" arithmetic uses the wrong base.
- **`cloud-infra/preemptible-vm-workloads.md`**: "A3-style preemptibles differ" — vague, no citation or detail; either state the difference (30-second vs 24h behavior) or cut it.
- **Style:** the 3 android-core files use "-" where the rest of the wiki uses em-dashes ("blocked too long - input dispatch"), and `anr-diagnostics.md` mixes "ANR" and "ANRs" inconsistently in one paragraph.
- **`api-protocols/401-vs-403.md`** states "A revoked token must stay rejected even after re-login flows" — a policy statement presented as a spec requirement; fine as guidance, but it is advice, not RFC behavior.
- **Titles vs filenames** drift in a few files (`agent-systems/ai-act.md` title "EU AI Act", `agent-systems/deception-research-ai.md` title "Deception Research") — cosmetic only.

## Sample audit table

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

## Recommendations

1. **Regenerate every Related section from the resolved wikilink graph, excluding the node itself and deduping entries** — clears Critical #1 (30 files, 33 self-links) and Major #2 (17 files, duplicated lines) in one pass. Add a promotion invariant: "no self-links, no duplicate link targets in Related" (the checker already has the logic; wire it into the pipeline).
2. **Delete the "— related coverage in the same cluster" annotation** (799 occurrences, 114 files) and replace with real one-line descriptors in the style the ai-ml files already use, or nothing. Recompute word counts afterward so the 320-word floor measures true content — right now Related + the formulaic "RSIS3/mykb relevance" paragraph can supply ~20–25% of a file's words (e.g. `remote-access-methods.md` at exactly 320).
3. **Fix the keyword-matched/template tails**: audit all 41 cloud-infra files sharing the networking-fundamentals/tcp-ip-stack/knowledge-acquisition tail and drop topically irrelevant links (EPYC/Xeon → Networking Fundamentals; Savings Plans → Rollback Plans; S3 lifecycle → Pod Lifecycle). This is the defect the wiki's own `link-diversity.md` names; the wave should not ship the anti-pattern it documents.
4. **Resolve the title collisions and sub-bar siblings**: merge `oauth2-authorization-code.md` into `authorization-code-flow.md`, `oauth2-client-credentials.md` into `client-credentials-flow.md`, and the three refresh-token pages into `refresh-token-rotation.md` (Jaccard 0.16–0.23 confirms same-topic duplication); then re-audit the whole corpus for `status: growing` files under 320 words (at least 4 exist) and either expand or demote them to `stub`.
5. **Ground or reword the self-referential infra claims** (DNSSEC rollover, 30/90/365 backup lifecycle, HTTP/3 edge, preemptible runners, Graviton migrations, OIDC hub login): either point them at real config/telemetry in the repo or convert to policy statements ("the standing rule is …"), because unverifiable assertions stored as fact corrupt the memory layer the wave is supposed to serve. Also fix the confirmed `dp-vs-px.md` density error (xxxhdpi = 4x, not 3px) and the `anr-diagnostics.md` `apply()`/`commit()` conflation while in there.

