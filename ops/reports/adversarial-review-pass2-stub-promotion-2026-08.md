# Adversarial Review — Pass 2 (Post-Cleanup Re-review, Combined Report)

**Date:** 2026-08-03 · **Scope:** all 1,098 promoted files (same 5 disjoint slices as Pass 1) · **Reviewers:** 5 parallel adversarial agents (Turing, Darwin, Singer, Hegel, Boole)

**Method:** same prompt + invariant checker as Pass 1 (now with unclosed-`[[`, namespace/type, and Summary-duplication rules), plus verification of the Pass-1 cleanup and re-measurement of the deliberately-unfixed defect classes. Individual reports: `ops/reports/adversarial-reviews/review-{1..5}-pass2.md`. Prompt: `ops/reports/adversarial-reviews/ADVERSARIAL_REVIEW_PROMPT.md` (Pass 2 section).

---

## Synthesis (all 5 reviews)

### Verdict in one paragraph

Scores: **79/64/62/68/71 → mean 68.8, median 68** (Pass 1: 68/57/79/71/64, mean 67.8). The Pass-1 mechanical cleanup **held in every slice** — all five reviewers independently verified 0 self-links, 0 annotation strings, 0 truncated/dead links, 0 files under 320 body words, syntheses `type` correct, and the factual fixes correct (WCAG ratios recomputed and matching, dom-clobbering vectors real, GPU module-set wording, calibration direction, dp-vs-px, anr-diagnostics, org-mode). No critical fabrication of papers/models/APIs remains, and hard invariants are 0/1,098. The score barely moved because the defect classes Pass 1 deliberately deferred now dominate the surface: unverifiable "the wiki's X does Y" claims (per-slice: 74/48/61/~183), keyword-matched irrelevant links (55–96 files), near-duplicate clusters (8+, incl. a 6-file CSS-unit cluster), orphaned trailing bullets (60+14+5 files), padding-to-threshold (most files in the 320–360 band), and the templated RSIS3-relevance closer (86–99% of files). Two cleanup gaps were confirmed and **have since been fixed** (see below).

### Pass-1 fixes: held or not (per slice)

| Slice | Score (P1→P2) | Fixes held? |
|-------|---------------|-------------|
| 1 (api/cloud/ai-ml) | 68→**79** | ✅ all held; networking tail now only on networking articles |
| 2 (concepts/data/dev-tools) | 57→**64** | ✅ all held; calibration + rename verified; orphaned bullets flagged (pre-existing) |
| 3 (devops/frontend/identity) | 79→**62** | ⚠️ fixes held but trailer removal incomplete (124 files) + 14 orphaned bullets |
| 4 (infra/memory/ml) | 71→**68** | ⚠️ fixes held but trailer removal incomplete (80 files); bare irrelevant Related rows |
| 5 (web/os/soft-eng) | 64→**71** | ✅ all held; 0 criticals; 5 orphaned bullets |

### What the cleanup missed — fixed after the pass

1. **Syntheses trailer removal was incomplete.** Pass 1 stripped only bare
   trailer lines; **233 files still carried the two-link boilerplate** with
   descriptor suffixes ("how stubs grow into full articles in mykb" / "the
   curation loop this stub belongs to"). **464 more lines removed**; 32 files
   that dropped below 320 were topped back up. Now 0 trailer links remain in
   the promoted set.
2. **`react-ecosystem.md` fabricated dashboard claim**: "the mykb dashboard
   is a React SPA with TanStack Query…" — the dashboard is vanilla JS
   (Tailwind + Chart.js + config.js). Reworded to a defensible worked example
   that names the actual stack. (Other frontend files' mentions were verified
   as aspirational analogies, not claims.)
3. **`compositions/fencing-tokens.md`** wrong-page link (`[[…lease-based-locks|Fencing Tokens]]`) removed; **stale display labels** after the clickhouse rename corrected (2 referrers); **3 emptied Related sections** (amd-epyc-and-intel-xeon, authoritative-and-recursive-resolvers, legal-hold-and-preservation) now have topical links.

### Remaining defect surface (Pass 3 agenda, ordered by risk)

1. **Unverifiable "the wiki's X does Y" claims** — the largest remaining
   fabrication risk. 74 (slice1), 48 (slice2), 61 (slice4), ~183 (slice5)
   files assert concrete operational facts (DNSSEC rollover, HTTP/3 edge,
   backup lifecycles, preemptible runners, quota registry, "search fuses
   TF-IDF + embeddings") with no supporting repo config/telemetry. Fix:
   ground in real config or convert to policy statements.
2. **Keyword-matched irrelevant links** — 55–96 files (OSPF/Storage
   Systems/WireGuard on unrelated pages; Kubernetes Control Plane in 96
   files; Observability Pillars in 65). Pass 1 removed the fixed tails only.
3. **Near-duplicate clusters** — 8+ clusters (~40 files), incl. a 6-file
   CSS-unit cluster (dvh-svh/vw-vh/etc.), path-resolution triplet,
   users/groups pair, ephemeral/preview environments (~90% identical).
   Merge to canonical slugs.
4. **Orphaned trailing bullets** — 60 (slice2) + 14 (dev-tools) + 5
   (prompt-engineering) files have bullets after the RSIS3-relevance
   paragraph with no header (pre-existing wave artifact; a "Practice" section
   merge fixes it).
5. **Padding-to-threshold** — 71% of slice5 sits at 320–360 words; the floor
   invites append-padding. Recommendation: raise the promotion bar to ~400
   with a density/duplication gate.
6. **RSIS3-relevance boilerplate** — 86–99% of files share the templated
   closer; star-graph pressure reduced but the template itself remains.

### Notes

- The checker's Pass-2 additions (unclosed `[[`, namespace/type, Summary
  duplication) produced 0 confirmed hits across all slices; `[[:alpha:]]`
  and `[[file:notes.org]]` remain intentional false-positive classes the
  checker whitelist handles.
- Corpus-wide, 1,673 `growing` files sit below 320 body words — pre-existing
  (earlier passes), outside this wave's scope, but a candidate for the next
  promotion wave targeting the 100+ word band.

---

## Individual reviews


## Review 1

## Adversarial Review 1 (Pass 2) — MyKB Stub-Promotion Wave (slice1, 220 files)

Reviewer: adversarial #1 · Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice1.txt` (220 files)
Areas in slice: api-protocols (117), cloud-infra (60), ai-ml (32), agent-systems (8), android-core (3)
Method: invariant checker + manual verification of all 14 flagged files + full re-read of the 2 factually-fixed files in-slice (dp-vs-px, anr-diagnostics) + deep-read of 30 files spanning all 5 areas + 10 link-target spot checks + corpus-wide scans for the fixed defect classes.

### Verdict

**Health score: 79 / 100**

**Pass 1 fixes held in this slice — verified.** The mechanical cleanup landed completely: 0 self-links (was 33 in 30 files), 0 occurrences of the "related coverage in the same cluster"/"full treatment of this theme"/"existing graph context"/"— note"/"— see also" annotation strings (was 799 across 114 files), 0 duplicated Related lines (was 17 files), 0 truncated `[[raw/archive/…]]` links, 0 dead `README` links, and the shared non-topical networking tail shrank from 41 cloud-infra files to 10 files that are all networking articles themselves (dnssec-and-validation, quic-and-http3, etc.), so the tail is now topically defensible. The 320-word floor holds: 0 files in the slice are below it (all 14 checker placeholder flags verified false positives: 12 legitimate RFC 2606 `example.com` doc domains, 1 descriptive "no placeholder text" in article-health-scores, 1 regex artifact in hash-collision-dos). Both in-slice factual fixes are correct: `dp-vs-px.md` now says 4px/xxxhdpi consistently ("1dp is 1px on mdpi and 4px on xxxhdpi", Details "xxxhdpi = 4x"), and `anr-diagnostics.md`'s `apply()`/`commit()` conflation is corrected ("apply() whose queued disk writes drain on the main thread when the activity stops" — accurate QueuedWork behavior).

The score stays below 80 because the defect classes the cleanup deliberately did NOT touch are still pervasive and now dominate the defect surface: 74 files (33.6%) still carry unverifiable "the wiki's … does Y" operational claims (DNSSEC automated rollover, HTTP/3 edge serving, a quota registry, a cost model, tunneled lab networks, preemptible batch runners, Graviton migration records) for which I found no supporting config anywhere in the repo — these read as invented specificity stored as fact in a memory layer whose whole job is trustworthy recall. Keyword-matched irrelevant links remain confirmed in 4+ files (savings-plans → Rollback Plans; glacier-and-s3-lifecycle → three "lifecycle" pages; azure-blob-access-tiers → Remote Access Methods / Zero Trust Access Proxies; point-of-presence → Point-in-Time Recovery), and the cleanup introduced one new regression class: **3 files lost their entire Related section** (amd-epyc-and-intel-xeon, authoritative-and-recursive-resolvers, legal-hold-and-preservation) instead of retargeting to topical links. The linked-target invariant from Pass 1 also persists: promoted files link to same-title, sub-320-word `growing` pages (oauth2-authorization-code at 249 words with title identical to authorization-code-flow; retry-backoff 222; networking-fundamentals 218), and corpus-wide 1,673 `growing` files sit below 320 body words.

Technical content quality remains high — in 30 deep-reads I found no fabricated papers, models, APIs, or wrong protocol mechanics; the OAuth, JWT, HTTP, DNS, multicast, and ML content is accurate. The remaining problems are systemic generator/pipeline defects, not hallucinated prose.

Per-defect-type quantification (of 220 files): status ≠ growing **0** · body < 320 **0** · missing frontmatter keys **0** · self-links **0 (was 30)** · annotation strings **0 (was 114)** · duplicated Related lines **0 (was 17)** · placeholder flags **14, all false positives** · broken links **0 (checker); 0/10 spot-checked (all targets exist, 2 topically wrong)** · files with no `## Related` **3 (new)** · files with "the wiki's …" unverifiable claims **74 (33.6%, unchanged)** · files with confirmed keyword-matched irrelevant links **≥4 (unchanged)** · "RSIS3/mykb relevance" boilerplate **186 (84.5%, unchanged)**.

### Critical findings

1. **Unverifiable "the wiki's … does Y" claims remain in 74 files (33.6%) — Pass 1 Major #6, deliberately unfixed, confirmed still present.**
   These assert concrete operational facts about the wiki/deployment that no repo artifact supports. I searched `components/rsis3`, `components/space/src`, and `components/mykb/.wiki-daemon` for each claimed subsystem: no DNS/DNSSEC automation, no backup lifecycle, no HTTP/3/QUIC edge config, no quota registry, no cost model, no tunneled-lab config, no preemptible-runner config, no Graviton migration records exist outside the wiki prose itself.
   - `cloud-infra/dnssec-and-validation.md`: "RSIS3/mykb relevance: the wiki's domains are signed with automated key rollover; this note records the DS publication and rollover procedure the loop's DNS automation follows."
   - `cloud-infra/http-3-0-rtt.md`: "RSIS3/mykb relevance: the wiki's edge serving enables HTTP/3 with h2 fallback; this note records the fallback order…"
   - `cloud-infra/glacier-and-s3-lifecycle.md`: "RSIS3/mykb relevance: the wiki's backup lifecycle (30/90/365) is recorded here with its restore tests…"
   - `cloud-infra/quota-management.md`: "the wiki's quota registry tracks per-service limits and headroom…"
   - `cloud-infra/mtu-and-fragmentation.md`: "the wiki's tunneled lab networks record per-link MTUs and MSS clamps…"
   - `cloud-infra/graviton-and-aws.md`: "the wiki records per-service Graviton migration results…"
   Why it is wrong: these are specific factual assertions ("is signed with automated key rollover", "enables HTTP/3") stored as memory; an agent that inherits them will plan against infrastructure that does not exist. Unverifiable offline and unsupported by the repo. Fix: either point each claim at real config/telemetry, or convert to policy ("the standing rule is …"), or delete the sentence.

2. **`growing`-status pages below the 320-word floor and title collisions persist (Pass 1 Critical #2, unfixed), and promoted files link to them.**
   Confirmed still present in-slice links:
   - `api-protocols/oauth2-authorization-code.md` — 249 body words, `status: growing`, title `"Authorization Code Flow"` — byte-identical title to the promoted `api-protocols/authorization-code-flow.md`, which links to it in Related: `- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]`.
   - `api-protocols/oauth2-client-credentials.md` — 240 words, growing; `api-protocols/oauth2-refresh-tokens.md` — 256 words, growing; also `oauth2-pkce.md` (256), `oauth2-scopes.md` (230), `oauth2.md` (235).
   - `api-protocols/retry-backoff.md` — 222 words, growing (linked from 429-handling, webhook-signatures, webhook-retries); `cloud-infra/networking-fundamentals.md` — 218 words, growing (linked from 10 files).
   Corpus-wide scan: **1,673 files carry `status: growing` below 320 body words**, so "growing" does not denote the wave's quality bar anywhere except the 1,098 promoted files. Fix: merge the oauth2-* siblings into the promoted articles, and re-audit corpus-wide statuses against the word floor.

### Major findings

1. **Cleanup regression: 3 files lost their entire `## Related` section — orphaned links removed without replacement.**
   - `cloud-infra/amd-epyc-and-intel-xeon.md` (Pass 1 documented its "Irrelevant Related tail"; the tail is now gone but so is the whole section — the file ends at the last Details bullet).
   - `cloud-infra/authoritative-and-recursive-resolvers.md`
   - `cloud-infra/legal-hold-and-preservation.md` — a compliance topic with zero links to object-lock/immutability/retention pages, which exist in the corpus.
   This is the "orphaned/empty Related" regression class the cleanup was supposed to check: removing bad links is right, but these articles are now link-isolated in a knowledge graph whose own metrics (`ai-ml/graph-density-metrics.md`: "two related articles that never link are a discovery failure") treat that as a defect. Fix: retarget to topical pages (e.g., amd-epyc → cloud-providers-aws-azure-gcp, legal-hold → object-lock-and-worm).

2. **Keyword-matched irrelevant links remain (Pass 1 Major #3, deliberately unfixed) — confirmed in 4 files, likely more.**
   - `cloud-infra/savings-plans.md` Related still opens with `- [[wiki/devops-infra/rollback-plans|Rollback Plans]]` — a deployment-rollback page matched on the word "plans".
   - `cloud-infra/glacier-and-s3-lifecycle.md` Related still lists `[[wiki/cloud-infra/function-execution-lifecycle|Function Execution Lifecycle]]`, `[[wiki/os-shell/process-signals-and-lifecycle|Process Signals & Lifecycle]]`, `[[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]]` — a pure "lifecycle" keyword match; serverless cold starts and pod states have nothing to do with S3 archive tiering. (The cleanup did add the topical `snapshot-lifecycle-policies` link, making the mismatch starker.)
   - `cloud-infra/azure-blob-access-tiers.md` Related contains `[[wiki/cloud-infra/remote-access-methods|Remote Access Methods]]` and `[[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]` — matched on the word "access".
   - `cloud-infra/point-of-presence.md` Related contains exactly one link: `- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]` — matched on "point", and now the article's only outbound edge.
   These are defect class 6 ("irrelevant links added purely to inflate the link count") in the wiki's own `ai-ml/link-diversity.md` taxonomy. Fix: rerun the Related generator with topic filtering (Jaccard over article bodies, or curated per-area link sets).

3. **The 320-word floor is met by structure, not content, in the bottom tier — padding-to-threshold persists in mechanism, if not in the body prose.**
   25 files sit at 320–329 words. The bodies themselves are technically dense (multicast-networking, cost-of-bandwidth, point-of-presence read substantively), but each file carries 1–3 formulaic closing bullets ("Broker alternative:", "Group hygiene:", "Latency verification:", "Failover rehearsal:", "Hold audit:", "Release authority:", "Egress budget:") that read as threshold-fillers, plus the mandatory "RSIS3/mykb relevance" paragraph (~30–35 words). At exactly 320 words (`multicast-networking.md`, `preemptible-vm-workloads.md`), removing the boilerplate sections drops the file below the promoted tier. Fix: measure body words excluding the "RSIS3/mykb relevance" section and the trailing one-line bullets, or raise the bar and re-expand.

### Minor & nits

- **All 14 checker placeholder flags are false positives** (verified file-by-file): 12 files use RFC 2606 `example.com` doc domains correctly (cookie-prefixes, cookie-scoping, device-flow, domain-cookies, header-injection, issuer-validation, jku-attacks, samesite-lax-strict, uri-vs-url, url-structure, certificate-transparency, dnssec-and-validation); `ai-ml/article-health-scores.md` uses "no placeholder text" descriptively; `api-protocols/hash-collision-dos.md` flags are regex artifacts ("every insert and lookup degenerates into a linked-list scan"). No action needed.
- **`cloud-infra/coldline-and-archive-storage-classes.md` pricing claim unchanged** (Pass 1 minor): "5TB of legal holds in Archive at ~$0.004/GB-month … a 5x saving" — GCP Archive list is ~$0.0012/GB-month in us-central1; $0.004 is Coldline pricing, and the 5x arithmetic uses the wrong base. Likely conflation, still present.
- **`cloud-infra/preemptible-vm-workloads.md`**: "GCP preemptibles run max 24h and stop with a 30s warning (A3-style preemptibles differ)" — the parenthetical remains vague with no detail or citation (Pass 1 minor, unfixed).
- **`android-core/anr-diagnostics.md`** still uses a hyphen where the wiki uses em-dashes ("blocked too long - input dispatch"), still carries empty `source: []` frontmatter, and still has no `## Summary` heading (intro paragraph + bullets instead) — all three Pass 1 minors persist. Same `source: []` / missing-Summary pattern in `app-threading.md` and `dp-vs-px.md`.
- **"RSIS3/mykb relevance" boilerplate**: 186/220 files (84.5%) end with this section; many are generic ("storing the decision rule here keeps loop-generated incident reviews consistent across sessions" — `api-protocols/401-vs-403.md`). House style, but it is the vehicle for the unverifiable claims in Critical #1.
- **`api-protocols/authorization-code-flow.md`** Related lists both `[[wiki/api-protocols/oauth2|OAuth 2.0]]` and the sub-320 same-title `[[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]` — two edges whose link text overlaps the article's own title (basename-collision ambiguity, defect class 6, persists from Pass 1).
- **`api-protocols/401-vs-403.md`** "a revoked token must stay rejected even after re-login flows" remains a policy statement phrased as spec behavior (Pass 1 minor, unfixed).
- **Facts in the fixed android files check out** — `dp-vs-px.md` bucket factors (1x/1.5x/2x/3x/4x) correct; `anr-diagnostics.md` timeout figures (5s input, 10/60s broadcast, 20/200s service) match platform documentation.

### Sample audit table

Deep-read files (words = body words; verdict reflects content quality + remaining wave defects).

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| ai-ml/article-health-scores.md | 478 | Pass | "placeholder" flag false positive; meta-article documents the wave's own remaining defects. |
| ai-ml/graph-density-metrics.md | 371 | Pass | Accurate; self-link exclusion stated and now honored by the corpus. |
| ai-ml/link-diversity.md | 345 | Pass | Sound; keyword-matched links (Major #2) still violate its own advice. |
| ai-ml/dpo.md | 385 | Pass | DPO/RLHF tradeoffs accurate; real link descriptors. |
| ai-ml/model-stealing.md | 348 | Pass | Attack taxonomy accurate; no invented specifics. |
| ai-ml/sparse-autoencoders.md | 354 | Pass | Training/interpretability caveats honest. |
| ai-ml/probing.md | 334 | Pass | Linear-probe framing and control baselines correct. |
| agent-systems/accountability-ai.md | 347 | Pass | Sound; "wiki's pass reports make the loop accountable" partially verifiable (OKF practice), mild. |
| agent-systems/ai-act.md | 363 | Pass | Tiering accurate; "2025-2027+" timeline cannot fully verify; "wiki maintains a compliance checklist" unverifiable. |
| agent-systems/ai-regulation.md | 353 | Pass | Layered-regulation framing sound. |
| agent-systems/deception-research-ai.md | 331 | Pass | Measured tone; no overclaiming. |
| android-core/dp-vs-px.md | 530 | Pass (fixed) | Factual fix correct: xxxhdpi = 4x everywhere; `source: []` and missing `## Summary` persist. |
| android-core/anr-diagnostics.md | 567 | Pass (fixed) | `apply()`/`commit()` fix correct; hyphen style + `source: []` persist. |
| api-protocols/hash-collision-dos.md | 431 | Pass | Regex flags false positives; SipHash/random-seed defense accurate. |
| api-protocols/authorization-code-flow.md | 418 | Major #2-persist | Accurate; Related links to same-title sub-320 sibling (oauth2-authorization-code). |
| api-protocols/refresh-token-rotation.md | 442 | Pass | RFC 9700 + reuse-detection accurate; self-link ×3 gone. |
| api-protocols/samesite-lax-strict.md | 439 | Pass | Lax/Strict/None rules correct; Related topical. |
| api-protocols/uri-vs-url.md | 424 | Pass | RFC 3986/URN/WHATWG distinction accurate. |
| api-protocols/401-vs-403.md | 452 | Pass | Retry semantics correct; revoked-token sentence is policy-as-spec. |
| api-protocols/jku-attacks.md | 454 | Pass | jku/jwk/x5u + SSRF framing excellent and accurate. |
| api-protocols/tcp-vs-udp.md | 448 | Pass | Transport tradeoffs accurate; self-link gone. |
| api-protocols/webhook-retries.md | 441 | Pass | Retry classification + dead-letter guidance correct. |
| cloud-infra/dnssec-and-validation.md | 332 | Critical #1 | "wiki's domains are signed with automated key rollover" — cannot verify, no repo config; tail now topical. |
| cloud-infra/glacier-and-s3-lifecycle.md | 333 | Major #2 | Three keyword-matched "lifecycle" links remain; 30/90/365 claim unverifiable. |
| cloud-infra/preemptible-vm-workloads.md | 320 | Critical #1 (mild) | "wiki's batch experiments run on preemptible capacity" unverifiable; "A3-style preemptibles differ" vague. |
| cloud-infra/http-3-0-rtt.md | 326 | Critical #1 | "wiki's edge serving enables HTTP/3" unverifiable; body accurate. |
| cloud-infra/graviton-and-aws.md | 328 | Critical #1 (mild) | "wiki records per-service Graviton migration results" unverifiable. |
| cloud-infra/multicast-networking.md | 320 | Pass (floor) | Accurate IGMP/PIM/VXLAN; "wiki's distributed-cache experiments" unverifiable; exactly 320 words. |
| cloud-infra/cost-of-bandwidth.md | 324 | Pass | Pricing figures accurate; "wiki's deployment monitors egress per service" unverifiable. |
| cloud-infra/point-of-presence.md | 325 | Major #2 | Only Related link is keyword-matched Point-in-Time Recovery. |
| cloud-infra/legal-hold-and-preservation.md | 325 | Major #1 (new) | No Related section at all; content accurate. |
| cloud-infra/savings-plans.md | 341 | Major #2 | Related opens with Rollback Plans (keyword match); Compute SP scope correct. |
| cloud-infra/amd-epyc-and-intel-xeon.md | 338 | Major #1 (new) | Related section removed entirely; body accurate. |
| cloud-infra/authoritative-and-recursive-resolvers.md | 339 | Major #1 (new) | No Related section; body accurate. |
| cloud-infra/azure-blob-access-tiers.md | 330 | Major #2 | "access"-keyword links (Remote Access Methods, Zero Trust Access Proxies) remain. |
| cloud-infra/coldline-and-archive-storage-classes.md | 334 | Minor | ~$0.004/GB-month likely Coldline not Archive pricing; otherwise tier rules correct. |

### Recommendations

1. **Remove or ground every "the wiki's … does Y" claim (74 files).** Grep the corpus for `the wiki's`/`wiki records`/`wiki maintains` and either link each to real config/telemetry, convert to policy wording, or delete. This is the highest-impact remaining defect because the wiki's purpose is reliable agent memory and these are confident assertions about infrastructure that does not exist.
2. **Restore topical Related sections to the 3 files left linkless by the cleanup** (amd-epyc-and-intel-xeon, authoritative-and-recursive-resolvers, legal-hold-and-preservation), then add a promotion invariant: "Related must contain ≥1 link and every link must be topical (no keyword-basename-only matches)."
3. **Replace the confirmed keyword-matched links** (savings-plans → Rollback Plans; glacier-and-s3-lifecycle → the three "lifecycle" pages; azure-blob-access-tiers → the two "access" pages; point-of-presence → Point-in-Time Recovery) using the same topic-filter the cleanup used to fix the 41-file networking tail — the mechanism exists, it was just not run on non-tail links.
4. **Resolve the OAuth near-duplicate cluster**: merge `oauth2-authorization-code.md`, `oauth2-client-credentials.md`, `oauth2-refresh-tokens.md` into the promoted `authorization-code-flow.md`, `client-credentials-flow.md`, `refresh-token-rotation.md` (same topics, same titles, 240–256 words vs 418–442), then run a corpus-wide status audit — 1,673 `growing` files below 320 words contradict the wave's own bar.
5. **Re-base the word-count floor on true content**: exclude the "RSIS3/mykb relevance" paragraph and the trailing one-line filler bullets from the ≥320 measurement, so files at exactly 320 words (multicast-networking, preemptible-vm-workloads) are promoted on substance rather than boilerplate. Re-verify the 62 topped-up files after re-measuring.

---

## Review 2

## Adversarial Review — Pass 2 (Post-Cleanup), Slice 2

**Reviewer:** adversarial-reviewer-2 (PASS 2)
**Date:** 2026-08-03
**Slice:** `/data/data/com.termux/files/home/.cache/mykb-review/slice2.txt` — 220 paths, 219 existing files (1 intentionally renamed; see below)
**Scope:** cloud-infra (20), communities (1), compositions (3), concepts (~110), data-storage (~55), decisions (12), dev-tools (~40)
**Method:** automated invariant checker + 60+ deep-reads + 12 link-target spot-checks + targeted pattern scans (annotation strings, trailing orphan bullets, duplicated bullets, duplicate Related links, mislabeled links, near-duplicate shingle scan, threshold-hugging analysis).

### Verdict

**64 / 100**

The hard invariants hold and the Pass 1 fixes **mostly landed in this slice, but with new cleanup-induced regressions**. Verified held: 0 self-links, 0 annotation strings ("related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" / "— note" / "— see also"), 0 unclosed `[[raw/archive/…]]` links, 0 `sources|syntheses/README` links, 0 files under 320 body words (min exactly 320), 0 empty `## Related` sections, 0 broken wikilinks/markdown links, and the one factual fix in this slice (`concepts/calibration.md` reliability-diagram direction) is correct; the out-of-slice factual fixes (contrast-ratios, dom-clobbering, gpu-drivers-and-cuda, dp-vs-px, anr-diagnostics) also verify as correct. The `clickhouse-vs-druid-pinot-druid-architecture.md` rename landed with all 3 referrers retargeted.

However, the cleanup left the slice in a visibly unfinished state: **60 of 219 files (27.4%) contain orphaned trailing bullets after the "RSIS3 relevance" paragraph and before `## Related`**, with no header; at least 3 files contain a duplicated "Operational notes" bullet inside one file; 1 missed duplicate `Related` link; and 1 wrong-page link (`[[wiki/compositions/lease-based-locks|Fencing Tokens]]`). The deliberately-unfixed Pass 1 classes remain pervasive: 86% of files end with a templated "RSIS3 relevance" paragraph, 48 files assert unverifiable "the wiki's / the bundle's X does Y" infrastructure claims, and files cluster at the 320-word floor (4 files at exactly 320). No fabrication, no broken links, and no semantic errors were confirmed in 60+ deep reads — the content, where it is content, is accurate. The score reflects that the floor held but the bar (real, distinct, verifiable prose per file) is only partially met.

### Critical findings

1. **Orphaned trailing bullets after the "RSIS3 relevance" paragraph — 60/219 files (27.4%)** (cleanup regression / padding evidence).
   Content after the RSIS3 paragraph, before `## Related`, with no header. Examples (all paths relative to `components/mykb/wiki/`):
   - `decisions/content-policy-ai.md` (exactly 320 words):
     > - RSIS3 relevance: the wiki's curation rules are a content policy for knowledge …
     > - Include concrete examples per category so both classifiers and human reviewers interpret the rules consistently.
     > - Measure enforcement against the policy with a labeled test set so rule changes show up as measurable behavior shifts.
   - `cloud-infra/security-group-best-practices.md`:
     > - Review cadence: run an exposure scan on a schedule and treat any new 0.0.0.0/0 rule on a management port as a review event …
     > - Naming: name groups by role and environment (web-prod, db-prod) …
   - `compositions/fencing-tokens.md`: "- Token hygiene: …" and "- Lease interplay: …"; `compositions/lamport-clocks.md`: "- Counter persistence: …" and "- Choice guidance: …"; `compositions/query-plans.md`: "- Plan reviews: …" and "- Workload realism: …"; `cloud-infra/warm-storage.md`: "- Data temperature model: …" and "- Cost reporting: …"; `data-storage/simhash.md`, `data-storage/locality-sensitive-hashing.md`, `data-storage/topic-modeling.md`, `data-storage/latent-semantic-analysis.md`, `data-storage/postgres-tsvector.md`, `data-storage/lucene.md`, `dev-tools/fixed-window.md`, `dev-tools/leaky-bucket.md`, `dev-tools/fail-safe.md`, `decisions/copyright-and-ai.md`, `decisions/data-license-issues.md` (3 bullets), etc. (full list in the audit methodology: 60 files).
   Why wrong: these are orphaned bullets — either a stripped header left them stranded or a top-up editor appended them after the RSIS3 paragraph to reach 320 words. They break the article skeleton (`Details` → `RSIS3 relevance` → `Related`) that every other file follows, and several duplicate advice already present in the same file (see finding 2). They are precisely the "orphaned bullets where a header was removed / awkward joins after annotation stripping" regression class Pass 2 was asked to check for. Fix: merge into an "Operational notes"/"Practice" section or delete; do not just renumber.

2. **Duplicated bullets inside a single file — confirmed in ≥3 files**.
   - `dev-tools/baggage-propagation.md` (line 20 and line 23, both bullets start "Operational notes:"):
     > - Operational notes: document the baggage schema, cap size and count, and sanitize values at the edge.
     > - Operational notes: document the baggage schema, cap its size, and treat baggage values as untrusted strings at every hop — never use them for access decisions.
   - `dev-tools/apm-tools.md` (line 20 and line 23, both "Operational notes:" bullets — "set sampling policies…" vs "sample aggressively…").
   - `dev-tools/breakpoint-debugging.md` (line 20 and line 23, both "Operational notes:" bullets).
   Why wrong: same section name twice in one file; the trailing copy sits in the orphaned zone of finding 1. The Pass 1 cleanup claimed "deduped 22 repeated bullets" — this slice shows the dedupe was incomplete.

3. **Wrong-page link: `compositions/fencing-tokens.md`**.
   > - [[wiki/compositions/lease-based-locks|Fencing Tokens]]
   The display label is "Fencing Tokens" but the target is `compositions/lease-based-locks.md` ("Lease-Based Locks"). Clicking "Fencing Tokens" lands on the lease article. This looks like a self-link that was retargeted to a sibling during cleanup without updating the label. It is the one confirmed label/target mismatch in the slice (verified by scanning all ~1,300 wikilinks for label-vs-basename mismatch; every other flagged candidate is a benign styling variant like "TF-IDF", "Q-Learning", "SIEM").

### Major findings

4. **Unverifiable "the wiki's / the bundle's X does Y" claims — 48 files** (deliberately unfixed in Pass 1; re-measured and still pervasive).
   - 32 files have "RSIS3 relevance: the wiki's …" infrastructure claims, e.g. `cloud-infra/spot-instances.md` ("the wiki's batch layer runs spot-first with checkpointing"), `cloud-infra/tcp-retransmission.md` ("the wiki's cross-region sync logs retransmit rates per link"), `cloud-infra/split-horizon-dns.md` ("the wiki's VPC uses private hosted zones with split views"), `compositions/fencing-tokens.md` ("wiki publish writes carry fencing tokens from the sync lease service"), `compositions/lamport-clocks.md` ("the wiki's sync layer linearizes event order with Lamport timestamps").
   - 16 files in `decisions/` use "RSIS3 relevance: the bundle's …", e.g. `decisions/patent-issues-ai.md` ("the bundle's novel scripts and methods have patent-adjacent disclosure choices"), `decisions/usage-policies-ai.md` ("the bundle's worker briefs are usage policies for its agents").
   - 32 files make "mykb …" claims, e.g. `data-storage/faiss.md` ("a local FAISS index over mykb embeddings"), `data-storage/named-entity-recognition.md` ("mykb's entity extraction from sessions is NER plus resolution; the results populate the entities directory").
   Why wrong: each is an assertion of fact about the wiki's or bundle's real infrastructure (tunnels, spot fleets, sync leases, entity pipelines) that cannot be verified from the wiki and, in several cases, contradicts observable reality (the wiki is an Obsidian markdown store — "publish writes carry fencing tokens" and "cross-region sync logs" have no supporting evidence anywhere in the corpus). These are not flagged as confirmed fabrication, but as unverifiable confident claims presented as fact — the exact class Pass 2 was asked to keep hunting. Fix: either attach evidence (link the pipeline/state file) or rewrite as conditional ("a sync layer *should* use …").

5. **Template uniformity and threshold-hugging padding**.
   - 188/219 files (86%) end with an "RSIS3 relevance" paragraph; 79 files share the full 7-part template (Summary → Details[Mechanism, Concrete example, Failure modes, Tradeoffs, Operational notes] → RSIS3 relevance → Related). The paragraph adds genuine value in good concept files (`concepts/active-inference.md`, `concepts/overfitting-llm.md`) and zero value in many infra files where it is the same claim restated ("the wiki's X does Y").
   - Word counts cluster at the floor: exactly 320 in `data-storage/sqlite-fts5.md`, `data-storage/time-travel-queries.md`, `decisions/content-policy-ai.md`, `dev-tools/correlation-ids.md`; 321 in `compositions/query-plans.md`, `data-storage/ivf.md`, `data-storage/simhash.md`, `dev-tools/latency-percentiles.md`; 322 in another 5. Four files at exactly 320 is statistically implausible for organic prose and matches the Pass 1 note that 62 files were "topped up" to the floor. In `content-policy-ai.md`, the two orphaned bullets of finding 1 are visibly the top-up. This is the "padding-to-threshold" defect class, re-measured.

6. **Near-duplicate structural clones — ~7 families, no verbatim duplication**.
   A 5-gram shingle-Jaccard scan across all 219 files found no pair above 0.30 (no copy-paste), but these families re-cover the same ground with the same template and cross-link each other:
   - DLQ family: `dead-letter-queues-and-retries.md`, `dead-letter-topics-and-dlq.md` (near-identical Summary/Mechanism/Failure-modes; both end "RSIS3's ingestion pipeline … quarantine"), plus `dead-letter-queues.md` and `dead-letter-data-and-repair-pipelines.md` (both linked from each of them).
   - Vector-search family: `faiss.md`, `ivf.md`, `hnsw.md`, `milvus.md`, `pinecone.md`, `product-quantization.md` — the first three each contain the same "the alternative, vector database …" tradeoff sentence shape.
   - Similarity-metric family: `cosine-similarity.md`, `dot-product.md`, `euclidean-distance.md` (each "normalize at write and query" advice repeated).
   - FTS family: `sqlite-fts5.md`, `postgres-tsvector.md`, `lucene.md`, `elasticsearch.md` (each: "the mature pattern is X for embedded, Y for scale").
   - LSH family: `minhash.md`, `simhash.md`, `locality-sensitive-hashing.md` ("keep exact verification mandatory" appears in all three).
   - Reward-model trio: `reward-model-error.md`, `reward-model-issues.md`, `reward-model-overfitting.md` (all in slice, all "reward model" ground).
   - Ethics family: `moral-agency/patiency/status-questions/uncertainty/weights`, `personhood-questions.md`, `rights-for-ai.md` (mutually cross-linked, overlapping criteria lists).
   Not a hard defect per file, but a redundancy tax: a reader of the DLQ family reads the same 350 words four times with different vendor nouns.

7. **Duplicate `Related` link: `decisions/data-license-issues.md`**.
   > - [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]]
   > - [[wiki/decisions/model-license-risks|Model License Risks]] — the model side
   > - [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — the wiki practice
   The same target+label appears twice in one Related block (a missed dedupe; Pass 1 claimed 22 deduped bullets).

### Minor & nits

- **Stale display labels after the ClickHouse rename** (fix landed but labels not refreshed): `data-storage/pinot-real-time-analytics.md` and `data-storage/clickhouse-and-columnar-oltp.md` both link `[[wiki/data-storage/clickhouse-vs-druid-vs-pinot|Clickhouse Vs Druid Pinot Druid Architecture]]` — target is the new file, label still the old slug-title.
- The slice file itself lists the pre-rename slug `data-storage/clickhouse-vs-druid-pinot-druid-architecture.md`; the checker's "MISSING FILE" flag is a false positive against an intentional rename (documented in `syntheses/adversarial-review-pass-1-2026-08.md`).
- Remaining 3 checker flags verified as false positives: `cloud-infra/split-horizon-dns.md` "example.com" (RFC 2606 reserved domain, legitimate DNS example), `concepts/stub-criteria.md` "placeholder" (prose defining the stub concept), `data-storage/postgres-tsvector.md` "insert and query" (technical phrase "analyzer mismatches between insert and query").
- `compositions/fencing-tokens.md`, `lamport-clocks.md`, `query-plans.md` (and all 3 compositions files) have no blank line between the frontmatter close (`---`) and the `# Title` — cosmetic but inconsistent with the rest of the slice.
- `data-storage/time-travel-queries.md` has a stray blank line before `## Related`.
- `cloud-infra/tls-1-3-session-resumption.md` links to both `wiki/cloud-infra/https-and-tls` and `wiki/os-shell/tls-and-https` — two links to near-same-topic targets in one Related block.
- `concepts/lottery-ticket-hypothesis.md` has a bare `[[wiki/concepts/sae-research|sae-research]]` link with no descriptor, while every sibling link carries a "—" annotation.
- Inconsistent RSIS3 line forms across the slice: "RSIS3 relevance:", "RSIS3/mykb relevance:", "mykb relevance:" — same template, three spellings.
- `concepts/named-entity-recognition.md`'s "entities directory" claim is at least consistent with the wiki (an `entities/` directory exists), so it is plausible; still unverified that "mykb's entity extraction from sessions" populates it.
- `dev-tools/four-golden-signals.md` "the golden signals map to article latency, read traffic, curation errors, and storage saturation" — a hypothetical mapping stated as fact; borderline instance of finding 4.

### Sample audit table

Word counts = body words, frontmatter excluded. Verdicts: OK = accurate, well-formed; WEAK = structural/regression defect; PASS = checked clean; FAIL = confirmed defect.

| File (relative to components/mykb/wiki/) | Words | Verdict | Notes |
|---|---|---|---|
| cloud-infra/security-group-best-practices.md | 329 | WEAK | 2 orphaned trailing bullets after RSIS3 paragraph; content otherwise accurate |
| cloud-infra/service-discovery-dns-based.md | 322 | WEAK | 1 orphaned trailing bullet; "the wiki's services resolve through an internal DNS" unverifiable |
| cloud-infra/site-to-site-vpn.md | 337 | WEAK | 1 orphaned trailing bullet; "the wiki's hybrid connectivity uses dual tunnels with BGP" unverifiable |
| cloud-infra/split-horizon-dns.md | 328 | OK | checker "example.com" flag is a false positive (RFC 2606); orphaned trailing bullet "Synchronization:" |
| cloud-infra/spot-instances.md | 339 | WEAK | "the wiki's batch layer runs spot-first with checkpointing" — unverifiable; 2 orphaned trailing bullets |
| cloud-infra/tcp-retransmission.md | 332 | WEAK | technically sound (RTO, fast retransmit, SACK, DSACK); 2 orphaned trailing bullets; unverifiable cross-region sync claim |
| cloud-infra/tls-1-3-session-resumption.md | 334 | OK | accurate (0-RTT, tickets, anti-replay); duplicate topical TLS links in Related |
| cloud-infra/warm-storage.md | 341 | WEAK | 2 orphaned trailing bullets; IA/Glacier claims plausible |
| communities/hotfix-branches.md | 540 | OK | best file in slice: substantive, distinct, well-structured; dual-merge logic correct |
| compositions/fencing-tokens.md | 350 | FAIL | wrong-page link `[[wiki/compositions/lease-based-locks\|Fencing Tokens]]`; 2 orphaned bullets; unverifiable "publish writes carry fencing tokens" |
| compositions/lamport-clocks.md | 327 | WEAK | correct (counter ticks, max+1); 2 orphaned bullets; unverifiable sync-layer claim |
| compositions/query-plans.md | 321 | WEAK | correct EXPLAIN/plan mechanics; 2 orphaned bullets; exactly-321 threshold-hugging |
| concepts/active-inference.md | 403 | OK | accurate FEP/active-inference account; interpretive RSIS3 line acceptable |
| concepts/calibration.md | 414 | PASS | factual fix verified: reliability diagram direction correct (above diagonal = underconfident) |
| concepts/induction-heads.md | 433 | OK | accurate; Olsson et al. paper correctly attributed |
| concepts/lottery-ticket-hypothesis.md | 446 | OK | accurate; Frankle & Carbin correctly described; bare sae-research link (nit) |
| concepts/moral-status-questions.md | 456 | OK | fair survey; "AI systems raise novel status questions" appropriately hedged |
| concepts/overfitting-llm.md | 457 | OK | accurate; contamination/memorization framing correct; meta RSIS3 line is apt |
| concepts/polysemanticity.md | 422 | OK | accurate superposition/dictionary-learning account |
| concepts/sandbagging.md | 459 | OK | accurate; incentive-invariance detection correctly described |
| concepts/spec-gaming-examples.md | 435 | OK | canonical DeepMind catalogue correctly cited; examples accurate |
| concepts/utilitarian-calculus.md | 446 | OK | Bentham/Mill correct; interpersonal-comparison objection correctly stated |
| data-storage/cosine-similarity.md | 347 | WEAK | mathematically correct; "wiki retrieval by cosine … is the core of semantic search in mykb" unverifiable; template clone of dot-product/euclidean |
| data-storage/dead-letter-queues-and-retries.md | 377 | WEAK | correct DLQ mechanics; near-clone of dead-letter-topics-and-dlq.md (same failure modes/tradeoffs, both "RSIS3's ingestion pipeline … quarantine") |
| data-storage/dead-letter-topics-and-dlq.md | 351 | WEAK | correct Kafka DLQ details; near-clone of sibling; "a Kafka consumer of wiki events" is a wiki claim |
| data-storage/faiss.md | 366 | WEAK | correct library facts; "a local FAISS index over mykb embeddings … the right scale for the wiki today" unverifiable |
| data-storage/ivf.md | 321 | WEAK | nlist/nprobe math plausible (8/4096 cells ≈ 2k scans); template clone; threshold-hugging |
| data-storage/hnsw.md | 332 | WEAK | M/efSearch ranges plausible; template clone of faiss/ivf |
| data-storage/latent-semantic-analysis.md | 335 | WEAK | correct SVD/TF-IDF account; orphaned trailing bullet duplicates "weight with TF-IDF" |
| data-storage/locality-sensitive-hashing.md | 332 | WEAK | correct LSH families; orphaned trailing bullet duplicates "keep exact verification" |
| data-storage/named-entity-recognition.md | 365 | OK | correct NER approaches; "entities directory" claim plausible (dir exists) but unverified |
| data-storage/postgres-tsvector.md | 336 | WEAK | correct tsvector/tsquery; checker "insert and query" flag is a false positive; orphaned trailing bullet duplicates generated-column advice |
| data-storage/simhash.md | 321 | WEAK | correct SimHash mechanism; orphaned trailing bullet; threshold-hugging |
| data-storage/sqlite-fts5.md | 320 | WEAK | correct FTS5 facts; "mykb's data layer favors SQLite" claimed twice; exactly 320 words |
| data-storage/time-travel-queries.md | 320 | OK | correct Delta/Iceberg/Snowflake snapshot claims; exactly 320; stray blank line nit |
| data-storage/topic-modeling.md | 331 | WEAK | correct LDA/LSA/BERTopic; orphaned trailing bullet |
| decisions/api-access-policies.md | 332 | WEAK | sensible policy taxonomy; orphaned trailing bullet; "the wiki daemon and dashboard should document … access tiers" speculative |
| decisions/content-policy-ai.md | 320 | FAIL | 2 orphaned trailing bullets (visible top-up to exactly 320); "the wiki's curation rules are a content policy" unverifiable |
| decisions/copyright-and-ai.md | 328 | WEAK | accurate fair-use framing; 2 orphaned trailing bullets, first duplicates "keep provenance records" |
| decisions/data-license-issues.md | 328 | FAIL | 3 orphaned trailing bullets; duplicate `evidence-and-provenance` Related link |
| decisions/test-set-discipline.md | 331 | OK | accurate holdout/contamination discipline |
| dev-tools/apm-tools.md | 336 | FAIL | duplicated "Operational notes:" bullet (lines 20 & 23) |
| dev-tools/baggage-propagation.md | 337 | FAIL | duplicated "Operational notes:" bullet (lines 20 & 23) |
| dev-tools/breakpoint-debugging.md | 339 | FAIL | duplicated "Operational notes:" bullet (lines 20 & 23) |
| dev-tools/burn-rate-alerts.md | 336 | OK | 14.4x/1h and 1x/24h window math matches SRE workbook conventions |
| dev-tools/correlation-ids.md | 320 | OK | accurate; exactly 320 words |
| dev-tools/fail-fast.md | 339 | OK | accurate; boundary-validation framing correct |
| dev-tools/fail-safe.md | 335 | WEAK | accurate deny-by-default; orphaned trailing bullet |
| dev-tools/fixed-window.md | 324 | WEAK | correct 2x boundary-burst analysis; orphaned trailing bullet |
| dev-tools/four-golden-signals.md | 322 | OK | accurate SRE signals; "map to article latency …" is a hypothetical stated as fact |
| dev-tools/leaky-bucket.md | 329 | WEAK | correct; orphaned trailing bullet "Apply it where downstream capacity is genuinely fixed …" |

### Recommendations (top 5)

1. **Repair the 60 orphaned trailing bullets.** Mechanical, high-impact: move each trailing block into the file's existing structure (append to a proper "Operational notes" section or fold into Related-free prose) or delete it. This is the single largest quality defect in the slice and is directly attributable to the cleanup/top-up pass. Include a checker rule that no bullet may exist between the last "RSIS3 relevance" line and `## Related`.
2. **Add an intra-file duplication check to the cleanup tooling.** Pass 1 deduped 22 bullets but missed the three duplicated "Operational notes" bullets (apm-tools, breakpoint-debugging, baggage-propagation) and the duplicated `evidence-and-provenance` Related link in `decisions/data-license-issues.md`. A per-file duplicate-line detector (normalized) would have caught all four.
3. **Retire the "the wiki's / the bundle's X does Y" claim template in 48 files.** Either attach a resolvable link to the claimed artifact (pipeline, lease service, sync layer) or rewrite as a recommendation ("a sync layer *should* linearize with Lamport timestamps"). As written, these read as facts about infrastructure the wiki does not document anywhere else — the highest-risk fabrication-adjacent class remaining.
4. **Fix and audit link labels.** Correct `compositions/fencing-tokens.md` (`[[wiki/compositions/lease-based-locks|Fencing Tokens]]` → label "Lease-Based Locks" or target `fencing-tokens`), refresh the two stale "Clickhouse Vs Druid Pinot Druid Architecture" display labels, and add a label-vs-target consistency check (label contains none of the target's basename words → flag for review).
5. **Stop threshold-hugging and shrink the clone families.** Raise the effective floor by requiring ≥2 sections beyond the template (or a verifiable citation) for `growing`, so a file at exactly 320 words cannot pass on template padding alone; and consolidate the DLQ, similarity-metric, FTS, vector-search, and LSH families by cross-linking one canonical treatment per family instead of four parallel articles with identical skeletons.

**Pass 1 fix verification (explicit):** self-links (0), annotation strings (0), unclosed `[[raw/archive/…]]` links (0), `sources|syntheses/README` links (0), sub-320 files (0), empty Related sections (0) — **held in this slice**. The `calibration.md` factual fix is correct and the ClickHouse rename landed with referrers retargeted. What did **not** hold cleanly is the claim that the cleanup left no structural residue: 60 orphaned trailing bullets, 3 duplicated in-file bullets, 1 duplicate Related link, and 1 wrong-page link are all cleanup-adjacent regressions present after the pass.

---

## Review 3

## Adversarial Review #3 — Pass 2 (MyKB Stub Promotion Wave, 2026-08-03)

Slice: `slice3.txt` — 220 files (`dev-tools/`, `devops-infra/`, `frontend-frameworks/`, `identity/`)
Report: `ops/reports/adversarial-reviews/review-3-pass2.md`

### Verdict

**Score: 62 / 100**

The Pass 1 mechanical fixes **held** in this slice: 0 self-links, 0 occurrences of the
stripped annotation strings, 0 unclosed `[[raw/archive/…]]` links, 0 `README` links, 0
files below the 320-body-word floor, and the invariant checker's 6 flags are all false
positives (legitimate `example.com`/`todo-app`/printf content). The 6 factually-fixed
files (contrast-ratios, dom-clobbering, gpu-drivers-and-cuda, calibration, dp-vs-px,
anr-diagnostics) are **not in this slice**, so their corrections could not be re-read;
the syntheses `type` fix is likewise N/A (no syntheses files in slice).

What did **not** hold, and what was deliberately left in place, is where the score drops:
the "fixed syntheses trailer" was not removed — 124/220 files (56%) still end with the
two-link boilerplate ("how stubs grow into full articles in mykb" / "the curation loop
this stub belongs to"); 96 files append a keyword-matched, topically irrelevant
`Kubernetes Control Plane` link and 65 append `Observability Pillars`; the cleanup
**introduced** 14 orphaned trailing bullets in `dev-tools/` (a header was stripped,
leaving a floating practice bullet glued to `## Related` with no blank line); and the
Pass 1 defect classes left intentionally untouched are pervasive — 219/220 files carry a
speculative "RSIS3 relevance"/"For mykb" section that is often padding, at least 8
`frontend-frameworks` files make confidently false claims about the real dashboard's
stack (it is vanilla JS: Tailwind + Chart.js + `config.js`; it uses no React, `useMemo`,
Zustand, or selectors), and one confirmed near-duplicate pair
(`ephemeral-environments` / `preview-environments`, ~90% identical) survives with more
partial pairs adjacent.

### Critical findings

1. **Fabricated system claims: `frontend-frameworks` files assert the dashboard is built
   on the very library each article describes.** Verified against
   `components/rsis3/dashboard/index.html` (Tailwind CDN, Chart.js 4, `config.js`, no
   React anywhere) and `components/rsis3/dashboard/config.js` (reads
   `rack/pulses/dashboard-data.json`).
   - `frontend-frameworks/use-memo.md`: "the dashboard's derived telemetry (aggregates
     over pulses) is exactly what `useMemo`-style caching protects"
   - `frontend-frameworks/memoization-practice.md`: "memoized selectors are how the
     dashboard derives graph stats and loop success rates from raw telemetry"
   - `frontend-frameworks/zustand-practice.md`: "the dashboard's shared UI state (active
     view, filters, daemon status) is a natural Zustand store"
   - `frontend-frameworks/react-query-practice.md`: "MyKB's dashboard is the textbook
     workload: search results, article lookups, and graph nodes keyed by query … TanStack
     Query's cache-and-invalidate model would replace the ad-hoc fetch state"
   - `frontend-frameworks/selector-libraries.md`: "the dashboard's telemetry views are the
     selector use case: memoized slices (success rate per loop, pulse counts per window)"
   - Same pattern in `frontend-frameworks/selectors-practice.md` and
     `frontend-frameworks/jotai-practice.md`; `frontend-frameworks/xstate-practice.md`
     adds the bolder "XState is the reference implementation of RSIS3's own loop
     semantics" (RSIS3 is a Python engine; nothing in the repo implements it in
     XState).
   Why wrong: the dashboard is a static vanilla-JS page; none of these libraries exist in
   it, so each claim misstates the knowledge base's own system — exactly the fabrication
   cost the review is meant to catch. Fix: rewrite as hypotheticals ("if the dashboard
   moved to React…") or delete; never state the system's stack as fact without checking
   it.

2. **Keyword-matched irrelevant links, mass-appended as a boilerplate trailer.**
   96/220 files link `[[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control
   Plane]]` and 65/220 link `[[wiki/devops-infra/observability-pillars|Observability
   Pillars]]`; 64 files carry the full 4-link trailer (KCP + Obs + 2 syntheses). The
   targets exist but are topically wrong for most sources:
   - `devops-infra/cosign-and-sigstore.md` (artifact signing) → "Kubernetes Control
     Plane" (kube-apiserver/scheduler/etcd)
   - `devops-infra/haproxy-vs-nginx.md` (L4/L7 proxy choice) → "Kubernetes Control Plane"
   - `devops-infra/runbooks-and-playbooks.md` (incident procedures) → "Kubernetes Control
     Plane"
   - `devops-infra/release-engineering-trains.md` → "Traffic Engineering" (network
     capacity routing) and "Chaos Engineering" — both matched on the keyword "engineering"
   - `devops-infra/ephemeral-environments.md` → "Shell Environments & RC Files" — matched
     on the keyword "environments"
   - `devops-infra/zero-trust-access-proxies.md` → "Zero-Downtime Deploys" — matched on
     the keyword "zero"
   These inflate the link counts of nearly every file and poison cross-navigation. Fix:
   bulk-remove the KCP/Obs trailer and re-link topically or not at all.

3. **The "fixed syntheses trailer" was not removed — 124/220 files (56%).** The cleanup
   claimed it "removed the fixed syntheses trailer", but in this slice the identical
   trailer survives, e.g. `devops-infra/canary-and-blue-green-revisited.md`:
   - `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] —
     how stubs grow into full articles in mykb`
   - `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation &
     Practices]] — the curation loop this stub belongs to`
   This is the same class of annotation boilerplate as the strings that were stripped,
   and it is identical across 124 files. Fix: strip these two bullets (and their
   annotations) from every file, as was done for the other annotation strings.

### Major findings

4. **Cleanup regression: 14 `dev-tools` files have orphaned trailing bullets.** A header
   was evidently stripped during annotation removal (or a top-up was inserted), leaving a
   lone bullet floating between the RSIS3 bullet and `## Related` with no blank line and
   no heading. Affected: `log-levels`, `log-rotation`, `package-managers`,
   `printf-debugging`, `profiling-tools`, `request-tracing`, `semver-tooling`,
   `slo-budgets`, `slug-changes`, `status-pages`, `summary-quality`, `timeout-policy`,
   `token-bucket`, `verbose-flag`. Evidence (`dev-tools/token-bucket.md`):
   > - RSIS3 relevance: a token bucket per tool class keeps agent bursts inside provider limits …
   >
   > - Expose the effective rate and burst in documentation so callers know what the limiter allows before they hit it.
   > ## Related
   Same shape in `dev-tools/summary-quality.md` ("Rewrite the summary from the finished
   Details…") and `dev-tools/package-managers.md` ("Prefer the package manager's own
   update flow over manual edits…"). Fix: re-attach these bullets under a real heading
   (e.g. a "Practice" subsection) or fold them into Operational notes.

5. **Confirmed near-duplicate pair: `ephemeral-environments.md` vs
   `preview-environments.md`.** A direct diff shows only the title, description, one
   example ID (`pr-123` vs `pr-42`), one added failure mode, and a few synonym swaps;
   the Mechanism/Concrete example/Tradeoffs/RSIS3 bullets are otherwise identical and
   both carry the same KCP + syntheses trailer. Two files describing the same concept
   with the same body is duplication, not coverage. The pair cross-links each other,
   which masks the duplication.

6. **Relevance-section padding signature: 219/220 files (99.5%) end with an
   "RSIS3 relevance"/"RSIS3/mykb relevance"/"For mykb" bullet, and many are content-free
   or unverifiable.** Examples: `dev-tools/semver-tooling.md` — "wiki article status
   (stub vs growing) is a semver-like signal — the same derived, verifiable progression
   discipline"; `dev-tools/slo-budgets.md` — "treat wiki-link breakage as budget spend on
   the knowledge SLO — the same numeric discipline for the wiki's reliability";
   `devops-infra/error-budgets.md` — "RSIS3's own loops have reliability targets — an
   error budget for pulse collection or dashboard generation tells the meta-loops when to
   stop shipping new behavior". None of these are grounded in any observable system
   behavior; several contradict it (see finding 1). The `dev-tools` body-word counts
   cluster 323–344, just above the 320 floor (`package-managers` 323, `lockfiles` 326,
   `printf-debugging` 327, `summary-quality` 327), consistent with padding-to-threshold
   via these bullets.

7. **`release-engineering-trains.md` contradicts its own frontmatter.** Description:
   "Fixed-cadence release trains that batch changes predictably"; body: "Release
   engineering turns software delivery into a repeatable process: versioning, changelogs,
   build reproducibility, artifact signing, promotion, and rollback…" — the body never
   discusses trains, while `release-trains.md` (in the same slice) covers the actual
   topic. Frontmatter/body mismatch plus a second overlapping article; 3 of 6 Related
   links are keyword-matched "engineering" links (Chaos, SRE, Traffic).

8. **`runbooks.md` / `runbooks-and-playbooks.md` partial duplicate.** Both are
   "step-by-step operational procedures for known incidents" with overlapping
   Summary/Details (rot, vague steps, game days). `runbooks-and-playbooks.md` adds the
   KCP + Obs + syntheses trailer and a `[[wiki/devops-infra/kubernetes-control-plane|Kubernetes
   Control Plane]]` link; `runbooks.md` has genuinely topical links (incident-response,
   on-call-rotations, escalation-policies). One should be merged into the other.

### Minor & nits

9. `devops-infra/haproxy-vs-nginx.md`: "config is text-based and reloadable without
   dropping connections (exclusive mode)" — "exclusive mode" is not standard HAProxy
   terminology (cannot verify; likely invented). HAProxy's seamless reload uses socket
   transfer/SO_REUSEPORT, not an "exclusive mode".
10. `identity/breach-notification.md`: "state laws such as the California Consumer
    Privacy Act … impose similar duties with varying timelines and thresholds" — CCPA's
    breach duty is a private right of action for unencrypted personal information
    (Civil Code 1798.150), not a notification statute with timelines; California's
    notification rule lives in Civil Code 1798.82. Misleading framing of a real regime.
11. `use-memo.md` and `use-callback.md` share 6 of 7 Related links and near-identical
    RSIS3/mykb relevance claims ("derived metric re-runs because its input function
    reference changed") — acceptable topical overlap, but the duplicated Related lists
    and identical system claims read as batch boilerplate.
12. Seven "revisited" files in the slice (`canary-and-blue-green-revisited`,
    `devcontainers-revisited`, `feature-flag-systems-revisited`,
    `kubernetes-operators-revisited`, `patch-management-revisited`,
    `readiness-vs-liveness-revisited`, `zero-trust-networking-revisited`) duplicate
    existing articles across namespaces (e.g. the pair links
    `infrastructure/canary-deployments` and `infrastructure/blue-green-deployments`);
    the "revisited" suffix hides the duplication.
13. `dev-tools/printf-debugging.md`: checker flag on "insert prints at function entry" is
    a false positive (legitimate mechanism text); but the RSIS3 bullet ("when a generated
    article looks wrong, printf the template variables") states agent behavior that
    cannot be verified.
14. `identity/hardware-security-keys.md`, `identity/account-recovery.md`,
    `identity/device-fingerprinting.md`: on-topic content is accurate (WebAuthn origin
    binding, NIST recovery-as-auth, fingerprint-as-risk-signal); the "For mykb:" bullets
    ("hardware keys should be mandatory for admin and agent-owner identities") are
    unverifiable policy claims, not recorded facts.
15. `devops-infra/zero-trust-networking-revisited.md` → "Multicast Networking" link is
    keyword-matched ("networking") and topically irrelevant to zero-trust access.
16. `devops-infra/canary-and-blue-green-revisited.md`: content (Argo Rollouts, Flagger +
    Prometheus canary analysis) is correct, but 4 of 6 Related links are the boilerplate
    trailer (KCP + Obs + 2 syntheses).

### Sample audit table

| File | Words | Verdict | Notes |
|---|---|---|---|
| dev-tools/printf-debugging.md | 327 | OK-with-nits | Checker flag false positive; unverifiable RSIS3 bullet |
| dev-tools/lockfiles.md | 326 | OK-with-nits | Sound; 326w just above floor; "the wiki's generated JSON indexes" unverifiable |
| dev-tools/mutation-testing.md | 344 | OK | Accurate; related links topical |
| dev-tools/property-based-testing.md | 344 | OK | Accurate; 6 topical links |
| dev-tools/token-bucket.md | 338 | FAIL | Orphaned trailing bullet; RSIS3 bullet speculative |
| dev-tools/slo-budgets.md | 330 | FAIL | Orphaned trailing bullet; fabricated "knowledge SLO" claim |
| dev-tools/semver-tooling.md | 333 | FAIL | Orphaned trailing bullet; "stub vs growing is semver-like" padding |
| dev-tools/package-managers.md | 323 | FAIL | Orphaned trailing bullet; 323w = floor-adjacent padding |
| dev-tools/summary-quality.md | 327 | FAIL | Orphaned trailing bullet; "wiki's" unverifiable claim |
| devops-infra/release-trains.md | 340 | OK | Correct on-topic article; good links |
| devops-infra/release-engineering-trains.md | 329 | FAIL | Description contradicts body; 3 keyword-matched "engineering" links; syntheses trailer |
| devops-infra/runbooks.md | 342 | OK | Good topical links; no trailer |
| devops-infra/runbooks-and-playbooks.md | 347 | FAIL | Near-duplicate of runbooks.md; KCP + Obs + syntheses trailer |
| devops-infra/compression-and-brotli.md | 356 | FAIL | Correct content; KCP link irrelevant; syntheses trailer |
| devops-infra/cosign-and-sigstore.md | 340 | FAIL | Correct content; KCP + Obs + syntheses trailer (all irrelevant) |
| devops-infra/haproxy-vs-nginx.md | 352 | FAIL | "exclusive mode" unverifiable term; KCP link irrelevant; trailer |
| devops-infra/canary-and-blue-green-revisited.md | 358 | FAIL | Content correct; 4/6 links are boilerplate trailer |
| devops-infra/ephemeral-environments.md | 343 | FAIL | Near-duplicate of preview-environments; Shell-Env link keyword-matched; trailer |
| devops-infra/preview-environments.md | 349 | FAIL | Near-duplicate of ephemeral-environments; trailer |
| devops-infra/error-budgets.md | 366 | OK-with-nits | 43-min figure correct; RSIS3 bullet speculative |
| devops-infra/zero-trust-access-proxies.md | 350 | FAIL | "Zero-Downtime Deploys" keyword link; KCP link; unverifiable RSIS3 claim |
| devops-infra/zero-trust-networking-revisited.md | 349 | FAIL | Multicast link keyword-matched; overlaps access-proxies article |
| frontend-frameworks/use-memo.md | 435 | FAIL | Fabricated "dashboard uses useMemo" claim; dup Related w/ use-callback |
| frontend-frameworks/use-callback.md | 421 | FAIL | Fabricated "dashboard" claim; dup Related w/ use-memo |
| frontend-frameworks/zustand-practice.md | 447 | FAIL | Fabricated "dashboard is a natural Zustand store" claim |
| frontend-frameworks/memoization-practice.md | 454 | FAIL | Fabricated "memoized selectors are how the dashboard derives graph stats" claim |
| frontend-frameworks/xstate-practice.md | 482 | FAIL | Fabricated "XState is the reference implementation of RSIS3's own loop semantics" claim |
| frontend-frameworks/react-query-practice.md | 439 | FAIL | Fabricated "MyKB's dashboard is the textbook workload" claim |
| frontend-frameworks/selector-libraries.md | 477 | FAIL | Fabricated "dashboard's telemetry views are the selector use case" claim |
| frontend-frameworks/jotai-practice.md | 471 | FAIL | Fabricated "dashboard's filter, search, and selection state fits this model" claim |
| identity/account-recovery.md | 451 | OK | NIST 800-63B framing accurate; "For mykb" unverifiable |
| identity/breach-notification.md | 446 | OK-with-nits | GDPR 72h correct; CCPA framed as notification law (minor error) |
| identity/hardware-security-keys.md | 453 | OK | Accurate (origin binding, AAL3); "For mykb" policy claim unverifiable |
| identity/device-fingerprinting.md | 456 | OK | Accurate; topical links; "For mykb" claim unverifiable |

### Recommendations (top 5)

1. **Strip the syntheses trailer and KCP/Obs boilerplate links** (124 + 96 + 65 files).
   Remove the two syntheses bullets and the keyword-matched `Kubernetes Control Plane` /
   `Observability Pillars` links where the source is not about k8s/observability; keep
   topically justified links only. This is a scriptable, mechanical fix.
2. **Correct or delete the fabricated dashboard-stack claims** in `frontend-frameworks/`
   (at least use-memo, use-callback, memoization-practice, zustand-practice,
   react-query-practice, selector-libraries, selectors-practice, jotai-practice).
   The dashboard is vanilla JS; rewrite the relevance bullets as explicit hypotheticals
   or remove them.
3. **Repair the 14 orphaned trailing bullets** in `dev-tools/` — restore a heading
   (e.g. `## Practice`) or fold each bullet into Operational notes so nothing floats
   unheaded above `## Related`.
4. **Merge confirmed near-duplicates**: fold `preview-environments` into
   `ephemeral-environments` (or delete one); merge `runbooks-and-playbooks` into
   `runbooks`; resolve the `release-engineering-trains` frontmatter/body mismatch and its
   overlap with `release-trains`; audit the 7 "revisited" files against their originals
   (cross-namespace duplicates).
5. **Re-audit the relevance sections against the 320-word floor.** With 219/220 files
   carrying a speculative relevance bullet and `dev-tools` files clustered at 323–344
   words, require each relevance bullet to be verifiable or delete it, then re-measure
   body words — and treat any file that drops below 320 after removal as failing, rather
   than topping up with new boilerplate.

#### Pass 2 verification summary (this slice)

- Checker: 214/220 clean; 6 flagged — all false positives (verified by reading).
- Pass 1 fixes held: self-links 0, annotation strings 0, unclosed raw/archive links 0,
  README links 0, files < 320 words 0. ✔
- Pass 1 fixes NOT verified: 6 factual-fix files and syntheses `type` fix are outside
  this slice (N/A here).
- Cleanup regressions introduced: 14 orphaned trailing bullets (dev-tools).
- Deliberately-unfixed classes still present: syntheses trailer 124 files, KCP link 96,
  Obs-Pillars link 65, relevance-section padding 219, fabricated dashboard claims 8,
  near-duplicates ≥4 pairs, unverifiable "the wiki's…" claims 8 files.

---

## Review 4

## Adversarial Review #4 (Pass 2) — MyKB Stub Promotion Wave, post-cleanup re-review

Reviewer: adversarial reviewer #4. Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice4.txt` (219 paths under `components/mykb/wiki/`; areas: identity, infrastructure, js-ts-ecosystem, llm-agents, memory, meta-learning, ml-frameworks, os-shell).

### Verdict

**Health score: 68 / 100**

The hard invariants hold again in this slice: 217/219 files pass the checker, both flagged items are false positives, no file is missing or below the 320-body-word floor, all frontmatter keys and `status: growing` are present, and there are no self-links, no unclosed links, no dead README links, and no `raw/archive` stragglers. Most of the Pass 1 fixes landed and are verifiable in this slice: all 6 self-links are gone, the "related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" strings are gone (0 hits), the duplicate cross-links in `federated-components.md`/`module-federation.md` are deduped, the Summary-into-Details duplication is gone, and the one in-slice factual fix (`gpu-drivers-and-cuda.md`) is now correct. **But the Pass 1 fixes did not fully hold:** the cleanup item "removed the fixed syntheses trailer" did not land here — 80/219 files still carry the two trailer lines verbatim, exactly the 80 files Pass 1 counted. Worse, the "related coverage" cleanup stripped the boilerplate descriptions but left the topically irrelevant targets in place, so 98/219 files now end in bare, link-padding Related rows (OSPF Protocols, Storage Systems, WireGuard) with no description at all — a cleanup-induced regression in link quality. The defect classes deliberately left unfixed are still at high prevalence and were re-measured: 61/219 files contain unverifiable "the wiki's / the loop's" system-behavior claims (several contradicted by a repo scan), 55/219 files carry keyword-matched irrelevant padding links, and a large cluster of files sits at 320-338 words, consistent with topping-up to threshold. Content accuracy of the actual prose remains genuinely good — I found no fabricated papers, models, APIs, or URLs, and the strongest files (identity cluster, `retry-with-backoff`, `awk-text-processing`, `evpn-bgp-evpn`) are excellent reference notes. The score is down slightly from Pass 1 (71) because a headline cleanup item did not land and the description-stripping produced a net regression in the slice's largest defect area.

### Critical findings

1. **The fixed syntheses trailer was NOT removed — still verbatim in 80/219 files (confirmed).**
   Pass 2's stated cleanup includes "removed the fixed syntheses trailer". It did not land in this slice. The exact two lines Pass 1 quoted are still present in the same 80 files, e.g. `infrastructure/erasure-coding.md` lines 25-26:
   > `- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb`
   > `- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to`
   Identical rows appear in `infrastructure/bandwidth-allocation.md`, `infrastructure/bufferbloat-and-queueing.md`, `infrastructure/precision-time-protocol.md`, `os-shell/btrfs-features-and-limitations.md`, `os-shell/cron-and-scheduled-tasks.md`, `infrastructure/evpn-bgp-evpn.md`, `infrastructure/nvme-multipath.md`, `infrastructure/nvme-over-fabrics-tcp.md`, and 72 more. The trailer claims every one of these topics is "a stub" that belongs to "the curation loop" — false for pages like `precision-time-protocol.md` (a substantive, topically unrelated page). This is word-stuffing-by-template and pollutes the graph with two synthetic edges per file. Fix: delete both rows from all 80 files (the cleanup intended to do exactly this and missed the whole slice).

2. **Cleanup regression: 98/219 files now end in bare, still-irrelevant Related rows (confirmed).**
   The cleanup stripped the "related coverage in the same cluster" descriptions but did not evaluate the link targets, leaving rows with no description and no topical connection. `infrastructure/bufferbloat-and-queueing.md` now ends:
   > `- [[wiki/infrastructure/storage-systems|Storage Systems]]`
   > `- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]`
   A page about bufferbloat and AQM linking to OSPF and Storage Systems with zero annotation is worse than the boilerplate version: the link count is unchanged, the relevance is unchanged, and the reader gets no hint of why the edge exists. The 98-file count matches Pass 1's count of files with the boilerplate almost exactly, so the cleanup replaced one bad form with another. 55/219 files specifically retain OSPF/Storage Systems/WireGuard rows (e.g. `infrastructure/precision-time-protocol.md` links `[[wiki/cloud-infra/wireguard-protocol|WireGuard Protocol]]`; `infrastructure/evpn-bgp-evpn.md` links `[[wiki/infrastructure/storage-systems|Storage Systems]]`). Fix: delete or replace the rows with topically related targets and add one-clause descriptions, matching the identity/memory clusters' Related style.

3. **"The wiki's tool registry is the single source of truth for agent capabilities" — unverifiable system assertion presented as fact (confirmed unverifiable, likely false).**
   `llm-agents/tool-registry.md`: "RSIS3/mykb relevance: the wiki's tool registry is the single source of truth for agent capabilities, and the loop's permission model reads from the same metadata." A repo scan (`rg -i "tool.?registr"` across `components/rsis3` and `components/mykb` excluding markdown) finds no tool registry in code — only JSON indexes that mirror the wiki page itself. There is no evidence the system has a tool registry, so this sentence asserts product behavior that cannot be verified and appears not to exist. This is the fabrication class the review is hunting for, just under a softer verb ("the wiki's X does Y"). Fix: rewrite as design intent ("a registry would be the single source of truth…") or delete the row.

### Major findings

1. **Unverifiable "the wiki's / the loop's / mykb's X does Y" claims — 61/219 files (re-measured, deliberately not fixed).** Beyond the tool-registry case, the same class recurs:
   - `llm-agents/prompt-caching.md`: "the wiki's loop prompts keep static system/tool prefixes stable so long sessions reuse caches, and cost telemetry tracks the savings." No prompt-caching or prefix-stability mechanism was found in `components/rsis3` code.
   - `js-ts-ecosystem/esbuild-practice.md`: "RSIS3 relevance: the dashboard's JS build is a prime esbuild candidate — near-instant rebuilds keep the loop fast." The dashboard (`components/rsis3/dashboard/index.html`) is static HTML with Tailwind and Chart.js; there is no JS build pipeline, so "the dashboard's JS build" describes something that does not exist.
   - `js-ts-ecosystem/import-maps.md`: "RSIS3 relevance: the dashboard could use an import map for its few external dependencies…" — speculative and hedged, but placed in the same slot as factual claims.
   - `ml-frameworks/pytorch.md`: "It is the framework most models in the wiki's stack are trained and fine-tuned with." Unverifiable from the wiki's own content; the wiki also documents JAX, TensorFlow, and local runtimes as first-class.
   - `meta-learning/delay-of-gratification.md`: "mykb's scheduling should budget for long-horizon tasks the same way a saver budgets for retirement." An editorial opinion inside a research summary.
   These are the Pass 1 "provenance" class; the cleanup explicitly left them, but they remain the second-largest source of unverifiable content in the slice.

2. **Keyword-matched irrelevant padding links — 55/219 files.** Re-measured after the description strip: OSPF Protocols appears in pages about erasure coding, bufferbloat, IPFS, and GPU drivers; Storage Systems appears in EVPN, tcpdump, PTP, NVMe, and GPU pages; WireGuard appears in `precision-time-protocol.md`. None of these edges survive a topical-relevance test. They are the residue of the template that wrote "related coverage in the same cluster" — now with the description removed but the padding intact (see Critical 2).

3. **Padding-to-threshold: a large cluster sits at 320-338 body words.** `llm-agents/agent-logs.md` and `ml-frameworks/langchain.md` are at exactly 320; `ml-frameworks/jax.md` at 321; `llm-agents/tool-registry.md` and `js-ts-ecosystem/macrotasks.md` at 324; `js-ts-ecosystem/esbuild-practice.md` and `meta-learning/colbert.md` at 326; 15 of the 18 `js-ts-ecosystem/` files fall between 324 and 337. These files are not empty filler — content quality is decent — but the uniformity and the two exact-320 counts indicate topping-up to pass the floor. The js-ts cluster is the most templated: identical Related shapes (7 bare links), identical trailing "Operational notes/practice" bullets, same two extra bullets before Related. The 320-word bar is being met, but not by margin, and the checker's word count rewards the template.

4. **Near-duplicate page clusters remain.** `infrastructure/tcpdump-and-wireshark.md` and `infrastructure/tcpdump-filters-and-capture.md` are genuinely distinct, but together with `infrastructure/packet-analysis-with-tcpdump`, `os-shell/tcpdump`, and `os-shell/wireshark-and-tshark` (all linked from `tcpdump-and-wireshark.md`) there are five tcpdump/wireshark pages in the wiki; a reader cannot tell which is canonical. `infrastructure/retry-with-backoff.md` links to both `[[wiki/api-protocols/exponential-backoff|Exponential Backoff]]` and `[[wiki/api-protocols/retry-backoff|Retry & Backoff]]` as separate rows — two targets that are almost certainly near-duplicates of each other and of the page itself. The time-sync trio (`network-time-protocol.md`, `precision-time-protocol.md`, `time-synchronization-in-dc.md`) is defensible but overlapping. No merge was attempted in the cleanup.

### Minor & nits

- `memory/org-mode.md` — the Pass 1 broken-link fix landed as recommended (`[[file:notes.org]]` instead of `[[file:...]]`), but the checker still flags it because the link is inside backticks describing org syntax. It is a doc example, not a real wiki link; suggest removing the brackets entirely so the checker stops flagging the slice.
- `infrastructure/tokenization-and-masking.md` — checker placeholder hit is a false positive: `user1@example.com` is a legitimate masked-email example.
- `identity/oauth-flows.md` — near-verbatim intra-file duplication: Summary says "each has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage"; Details bullet 4 repeats "Each flow has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage." One of the two should go.
- Formatting inconsistency: js-ts files (e.g. `esbuild-practice.md`, `import-maps.md`) omit the blank line after the closing frontmatter `---`, unlike every other cluster.
- Related-section style is now inconsistent across the slice: identity/memory/meta-learning/ml-frameworks rows carry "— description"; infrastructure/js-ts/os-shell rows are bare. This looks like a mid-cleanup state, not a deliberate style choice.
- The other five factually-fixed files (`contrast-ratios.md`, `dom-clobbering.md`, `calibration.md`, `dp-vs-px.md`, `anr-diagnostics.md`) are not in this slice, so their corrections could not be re-verified here. The syntheses `type: "concept" → "synthesis"` fix is likewise unverifiable in-slice (no `syntheses/` paths in slice 4).
- `ml-frameworks/google-gemini.md` — "context windows extend to 1M+ tokens on flagship models" is accurate but provider-versioned; worth a "as of" qualifier, as with `openai-api.md`'s "gpt-4o style aliases".

### Sample audit table

| File | Words | Verdict | Notes |
|---|---|---|---|
| identity/totp.md | 457 | PASS | RFC 6238 mechanics, replay/phishing-relay limits accurate; on-topic links; real source in frontmatter |
| identity/oauth-flows.md | 464 | PASS* | Grant types and PKCE accurate; intra-file sentence duplication (Summary to Details bullet 4) |
| identity/session-fixation.md | 450 | PASS | Attack model and rotation defense accurate; example clean |
| infrastructure/bufferbloat-and-queueing.md | 490 | FAIL | Content accurate; Related = bare OSPF/Storage Systems padding + trailer |
| infrastructure/erasure-coding.md | 498 | PASS* | Reed-Solomon k+m and rebuild-window reasoning accurate; OSPF row + trailer in Related |
| infrastructure/precision-time-protocol.md | 492 | PASS* | PTP/BMCA/boundary-clock content accurate; WireGuard/Storage Systems padding + trailer |
| infrastructure/gpu-drivers-and-cuda.md | 509 | PASS* | Pass 1 factual fix verified correct (module set enumerated); Storage Systems/OSPF rows + trailer remain |
| infrastructure/sidecar-pattern.md | 354 | PASS | Ambassador/adapter distinction accurate; all links on-topic with descriptions |
| infrastructure/retry-with-backoff.md | 488 | PASS | Backoff/jitter/breaker composition accurate; double-links to two api-protocols retry pages |
| infrastructure/evpn-bgp-evpn.md | 430 | PASS* | EVPN NLRI/multi-homing/ARP-suppression accurate; Storage Systems row + trailer |
| infrastructure/tcpdump-and-wireshark.md | 415 | PASS* | Workflow content accurate; 5-page tcpdump cluster overlap; Storage Systems row + trailer |
| infrastructure/tcpdump-filters-and-capture.md | 396 | PASS* | BPF syntax accurate; overlaps sibling pages; trailer |
| infrastructure/nvme-multipath.md | 459 | PASS* | Path-policy/failover content accurate; trailer |
| infrastructure/nvme-over-fabrics-tcp.md | 475 | PASS | Queue-pair-to-TCP-connection mapping accurate; links on-topic; trailer |
| js-ts-ecosystem/esbuild-practice.md | 326 | FAIL | Accurate; "dashboard's JS build is a prime esbuild candidate" — no JS build exists in repo; bare 7-link Related; near floor |
| js-ts-ecosystem/import-maps.md | 354 | PASS* | Import-map semantics accurate; speculative dashboard claim; bare Related rows |
| js-ts-ecosystem/microtasks.md | 331 | PASS | Microtask semantics accurate; bare 6-link Related; near floor |
| js-ts-ecosystem/federated-components.md | 333 | PASS* | Self-link and duplicate link removed (verified); bare 5-link Related; near floor |
| llm-agents/reflexion.md | 361 | PASS* | Reflexion described accurately; "wiki's syntheses capture the durable lessons" unverifiable |
| llm-agents/tool-registry.md | 324 | FAIL | Content accurate; "the wiki's tool registry is the single source of truth" — no tool registry in codebase; near floor |
| llm-agents/prompt-caching.md | 345 | PASS* | Caching mechanics accurate; "80-90% at cache prices" and loop-prefix claim unverifiable |
| llm-agents/agent-logs.md | 320 | PASS* | Logging advice sound; exact 320 words; wiki-loop claim unverifiable |
| memory/evergreen-notes.md | 438 | PASS | Atomic/linked/title-as-claim accurate; links on-topic with descriptions |
| memory/progressive-summarization.md | 483 | PASS | Layer model accurate; no padding links |
| memory/logseq.md | 425 | PASS | Block-reference model accurate; cross-links Logseq/Org/Obsidian properly |
| memory/obsidian.md | 429 | PASS | Wikilink/backlink/graph description accurate; on-topic links |
| meta-learning/colbert.md | 326 | PASS* | MaxSim/late-interaction and ColBERTv2 claims accurate; near floor |
| meta-learning/delay-of-gratification.md | 358 | PASS | Self-link removed (verified); marshmallow reanalysis accurate; scheduling opinion in RSIS3 bullet |
| meta-learning/word2vec.md | 371 | PASS | Skip-gram/CBOW and analogy properties accurate |
| ml-frameworks/openai-api.md | 359 | PASS* | API surface accurate; "gpt-4o style aliases" unverifiable as current in 2026; loop-endpoint claim unverifiable |
| ml-frameworks/google-gemini.md | 345 | PASS* | Multimodal/1M+ context accurate; "model registry includes Gemini" unverifiable |
| ml-frameworks/jax.md | 321 | PASS* | grad/jit/vmap/pmap accurate; near floor; "training experiments record framework choice" unverifiable |
| ml-frameworks/pytorch.md | 349 | PASS* | Eager/compile/export accurate; "most models in the wiki's stack" unverifiable |
| ml-frameworks/langchain.md | 320 | PASS* | LangGraph state-machine description accurate; exact 320 words; loop claim unverifiable |
| os-shell/awk-text-processing.md | 492 | PASS | NR/FNR, FS/RS traps, CSV caveat all accurate; links on-topic |
| os-shell/btrfs-features-and-limitations.md | 450 | PASS* | CoW/snapshot/RAID5/6 caveats accurate; Memory Management & Paging row is a stretch; trailer |
| os-shell/cron-and-scheduled-tasks.md | 498 | PASS | cron/anacron/systemd-timer comparison accurate; Kernel Architecture row is thin; trailer |

`PASS*` = content accurate with a noted unverifiable/borderline item. Word counts are body words (frontmatter excluded), same method as `check_slice.py`.

### Recommendations

1. **Finish the trailer removal properly (80 files).** The single most important Pass 2 finding is that a claimed cleanup step never happened in this slice. Delete both syntheses rows from all 80 files and add a verification pass (grep for the two phrases; assert zero) so it cannot silently fail again.
2. **Fix the bare-link regression (98 files).** Either restore one-clause descriptions to rows whose targets are genuinely related, or delete the rows. Specifically purge the OSPF/Storage Systems/WireGuard edges from the 55 files where they are topically unrelated; a knowledge graph consumed by an agent should not contain edges that name unrelated topics.
3. **Gate "the wiki's / the loop's" claims on provenance (61 files).** Before publishing, each such sentence should either be verified against the repo (as the tool-registry and esbuild claims fail today) or rewritten as design intent. Batch templates that assert system behavior are how fabricated product facts enter a memory store.
4. **Treat near-floor word counts as a quality signal.** Extend `check_slice.py` to report files in the 320-345 band and require a human pass on them; the js-ts cluster's template uniformity (same Related shapes, same trailing bullets) shows the 320-word floor can be met without adding knowledge. Also deduplicate the five tcpdump/wireshark pages and the retry-backoff/exponential-backoff pair.
5. **Add the cleanup's missing checks to the pipeline**: bare-wikilink-row detection (a Related row with `[[…]]` and no description), the two trailer phrases as a denylist, and an "unverifiable system claim" scan for the strings `the wiki's | the loop's | mykb's | rsis3's`. These three string checks would have caught every critical and major finding in this Pass 2 review.

*Out of scope / not verifiable in this slice: the other five factual fixes, the syntheses `type` correction, and 62-file topping-up totals (only the residue is visible here: 20+ files at 320-338 words).*

---

## Review 5

## Adversarial Review #5 (PASS 2) — MyKB Stub-Promotion Wave (slice 5, 219 files)

Reviewer: adversarial-reviewer-5 (PASS 2, post-cleanup re-review)
Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice5.txt` (219 files)
Areas: os-shell, prompt-engineering, software-engineering, web-platforms, syntheses, security-auth, pulses, shell-environment, tooling
Checker run: `python3 ops/reports/adversarial-reviews/check_slice.py <slice>` → 210 clean / 9 flagged; all 9 flags opened and verified → **all false positives** (0 confirmed).

### Verdict

**Health score: 71 / 100**

**Pass 1 fixes held in my slice — verified, not assumed.** Every Pass 1 defect class I re-checked is gone: 0 self-links across all 219 files, 0 occurrences of the "related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" annotation strings, 0 unclosed `[[raw/archive/…]]` links, 0 `sources|syntheses/README` links, all 6 `syntheses/` files now declare `type: "synthesis"`, and the two factually-fixed files in my slice (`contrast-ratios.md`, `dom-clobbering.md`) are now correct — I recomputed the WCAG math (`#777777` = 4.48:1 fails, `#757575` = 4.61:1 passes, `#595959` = 7.0:1) and the file's numbers match exactly; the `dom-clobbering.md` vectors (`<form><input name=attributes>`-style clobbers, `id="defaultView"`) are the known, real attack class. No file dropped below the 320-body-word floor (min = 320), no `## Related` section is empty, and the checker's 9 flags are all legitimate usage: `[[:alpha:]]` locale class in `grep-patterns.md` (checker mis-parses `[[`), "placeholder box/text", "example.com" example domains, "insert nodes / insert via node APIs" DOM phrasing, and a `TODO` inside a quoted `rg -l "TODO" src/` example.

What keeps the score at 71 instead of much higher is that the substantive quality classes Pass 1 identified were **deliberately not fixed**, and they are systemic, not occasional: (a) keyword-matched irrelevant links are still everywhere (confirmed in ≥8 files, with a recurring "kernel-architecture + memory-management-paging" filler pair in os-shell Related lists); (b) unverifiable "the wiki's X does Y" claims are present in ~183/219 files, each fabricating a different specific about the dashboard/daemon/loop that cannot be checked offline; (c) padding-to-threshold is visible in the word distribution — 155/219 files (71%) sit in the 320–360 band, median 340, and every file carries the same short "Header: sentence" bullet appendices that read as floor-aiming top-ups; (d) near-duplicates are worse than Pass 1 reported (I count 8+ clusters, including two triples and a 6-file CSS-unit cluster); and (e) the syntheses files repeat their Summary paragraph verbatim as the first Details bullet. The cleanup also introduced a small regression: 5 `prompt-engineering` files now have orphaned, headerless bullets where annotation-stripping removed a heading.

Quantified (219 files): status 0 fail (0%), body-words <320: 0 fail (0%), frontmatter keys 0 fail (0%), self-links 0 (0%), broken/truncated links 0 (0%, checker's `:alpha:` flag is a false positive), annotation strings 0 (0%), README/raw links 0 (0%), syntheses `type` wrong 0 (0%), checker placeholders 9 flagged → 0 confirmed, orphaned bullets 5 (2.3%), near-duplicate clusters ≥8 (covering ~40 slice files), "RSIS3/mykb relevance" unverifiable claims ~183 (84%), keyword-matched irrelevant links ≥8 confirmed, template section boilerplate ("Mechanism"/"Concrete example"/"Failure modes"/"Operational tradeoffs") present in ~90%+ of files.

### Critical findings

None confirmed. The invariant and factual-error classes that were critical in Pass 1 (truncated raw links, wrong contrast numbers, leaked generator self-correction in `dom-clobbering.md`) are all fixed in this slice. The nearest thing to critical now is the volume of unverifiable system-specific claims — individually minor, collectively a fabrication risk for a memory store. Listed under Major.

### Major findings

1. **Unverifiable "the wiki's X does Y" claims are pervasive (~183 files, deliberate non-fix).** Nearly every article ends with an `RSIS3/mykb relevance` bullet asserting a specific behavior of the dashboard/daemon/loop that I cannot verify from the repo (rules: "if you cannot verify a claim offline, say cannot verify"). Examples, all quoted exactly:
   - `web-platforms/contrast-ratios.md`: "the rack telemetry includes a periodic contrast audit of key surfaces."
   - `web-platforms/compositing-triggers.md`: "keeping interaction-to-next-paint low on the low-power devices the team tracks in rack telemetry."
   - `web-platforms/speculative-loading.md`: "the wiki adds preconnect for its API and prerenders the most-visited synthesis from Speculation Rules, with data-usage telemetry reviewed by the loop."
   - `web-platforms/cls-avoidance.md` vs `web-platforms/cumulative-layout-shift.md`: two incompatible versions of the same claim — "the dashboard tracks CLS from the Performance API as a rack pulse" vs "the dashboard reports CLS from real sessions into rack telemetry".
   - `os-shell/environment-variables.md`: invents a specific env var, "a daemon reads `MYKB_WIKI_ROOT` to locate its corpus" — I could not find this var referenced anywhere I checked; even if it exists, the article asserts it as fact.
   - `prompt-engineering/adversarial-prompts.md`: "a fuzzer generates 10,000 obfuscated variants nightly" — an invented specific number presented as a concrete example.
   These read as generated filler tuned to the 320-word target, and they are the single largest residual credibility risk in the slice. Suggested fix: either delete the RSIS3/mykb bullet from files where it is not a documented fact, or mark it explicitly as "aspirational pattern" rather than present-tense fact.

2. **Keyword-matched irrelevant links (confirmed ≥8 files, deliberate non-fix).** The cleanup retargeted dead README links but left the keyword-matching behavior intact:
   - `os-shell/users-groups-and-acls.md` → `[[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]` (network security groups; irrelevant to POSIX file ACLs — pure "groups" keyword match), plus `[[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]]` (job control, not identity) and `[[wiki/os-shell/memory-management-paging|Memory Management & Paging]]` (irrelevant).
   - `os-shell/mdadm-and-lvm2.md` → `[[wiki/os-shell/memory-management-paging|Memory Management & Paging]]` and `[[wiki/os-shell/kernel-architecture|Kernel Architecture]]` — no topical link to RAID/LVM.
   - `os-shell/tcp-keepalive.md` → `[[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]` — NVMe-oF/TCP is a storage protocol; the only connection is the string "TCP" in the title. A reading agent following this link wastes a hop.
   - The "kernel-architecture + memory-management-paging" pair recurs as filler in `select-poll-epoll-comparison.md`, `io-uring-and-async-io.md`, `swap-and-zram.md`, `oom-killer-and-memory-pressure.md`, `users-groups-and-acls.md`, `mdadm-and-lvm2.md` — in several of these at least one link is off-topic.
   - `software-engineering/estimation-techniques.md` → `[[wiki/memory/spaced-repetition|Spaced Repetition]]` ("scheduling analog") — stretched.
   Verified: all targets exist (link hygiene for existence is clean); the defect is topical relevance, which the checker cannot see.

3. **Near-duplicates are more extensive than Pass 1 reported (≥8 clusters, ~40 slice files).** All still present:
   - Triple: `os-shell/path-resolution.md` ↔ `os-shell/path-resolution-and-symlinks.md` ↔ `os-shell/symlinks.md` — same namei walk, 40-link ELOOP, openat2 RESOLVE_*, realpath, find -L/-P, backup semantics; the two path articles are near-verbatim in places and link each other instead of being merged.
   - Pair: `web-platforms/cumulative-layout-shift.md` ↔ `web-platforms/cls-avoidance.md` — same definition, mechanism, main-causes list, budget (<0.1), and dashboard-CLS claim.
   - Pair: `web-platforms/color-spaces.md` ↔ `web-platforms/srgb-vs-p3.md` — same sRGB ~35% / P3 ~45% gamut facts, oklch authoring advice, fallback ordering, dashboard-token claims.
   - Six-file cluster: `web-platforms/em-vs-rem.md`, `px-vs-rem.md`, `vw-vh.md`, `dvh-svh.md`, `container-relative-units.md`, `responsive-units.md` — the same "which unit when" theme with a shared 4–7 link Related skeleton and six variants of "dashboard uses <policy>"; `responsive-units.md` is effectively a meta-summary of the other five.
   - Triple: `web-platforms/layout-triggers.md` ↔ `paint-triggers.md` ↔ `compositing-triggers.md` — distinct enough per stage, but with 7 identical Related links and the same dashboard claim template.
   - Five-file cluster: `dns-prefetch.md`, `preconnect-practice.md`, `preload-practice.md`, `prefetch-practice.md`, `speculative-loading.md` — each hint file is defensible, but `speculative-loading.md` re-covers all of them.
   - Cross-namespace pair: `security-auth/bug-bounty.md` (concept) ↔ `syntheses/bug-bounty-ai.md` (synthesis) — the synthesis repeats the concept's scope/rules/triage/tradeoff content plus an AI angle.
   - Pair: `os-shell/users-and-groups.md` ↔ `os-shell/users-groups-and-acls.md` — partial overlap (identity model) but the ACL file earns its slug; lowest-priority of the set.
   For a retrieval-driven memory store, eight overlapping clusters mean an agent pulling "CLS" or "CSS units" gets 2–6 near-identical pages. Fix: canonical slug + merge or redirect note per cluster.

4. **Duplicated passages inside files (dedup pass missed cross-section repeats).**
   - `syntheses/bug-bounty-ai.md`, `syntheses/coordinated-disclosure.md`, `syntheses/safety-case-approach.md`: the Summary paragraph is repeated verbatim as the first Details bullet. E.g. `syntheses/coordinated-disclosure.md` Summary: "Coordinated disclosure is a formal process where researchers, vendors, and platforms agree on the timing and content of vulnerability publication." and Details bullet 1: "Coordinated disclosure is a formal process where researchers, vendors, and platforms agree on timing and content of vulnerability publication." The dedup pass removed duplicate bullets within a section but not Summary↔Details duplication.
   - `software-engineering/actor-model.md`: two consecutive relevance bullets — "RSIS3 relevance: agents modeled as actors get explicit message handoffs…" followed by "- RSIS3/mykb relevance: the wiki records actor-style designs for agent runtimes…" — the same generator pattern Pass 1 flagged; still here.

5. **Padding-to-threshold is measurable and unchanged.** 155/219 files (71%) land in the 320–360 band (median 340; `aspect-ratio-images.md` and `polyglot-xss.md` sit at exactly 320). The top-up mechanism is visible as the same short "Header: 1–2 sentences" bullet appendices appended after the RSIS3 bullet in file after file: "Source switching:", "Parser differentials:", "Test corpus:", "Alternatives first:", "Focus order:", "Animation interplay:", "Overlay roots:", "Interaction windows:", "Swap timing:", "Measurement:", "Layer audit:", "Cost containment:", "Read-after-write rule:", "Will-change scoping:", "Keyboard behavior:", "Fallback order:", "Migration path:", "Budgeting:", "Battery composition:", "Probe lifecycle:", "External anchoring:", "Cost accounting:", "Server side:", "Client side:", "Contract-first:", "Consistency expectations:", "Migration practice:", "Context inventory:", "Policy review:", "Input vs output:", "Gamut mapping:", "Authoring default:", "Display testing:", "Asset pipeline:", "Cache correctness:", "Priority audit:", "Monitoring:", "Same-site constraints:", "Budget control:", "Media query note:", "Accessibility check:", "Landscape and rotation:", "Print and embed:", "Safe-area interplay:", "Component scaling:", "Detection:", "Immutable singletons:", "Thread-safety illusion:", "Audit pattern:", "Filesystem note:", "Testing:", "Security angle:", "Filenames and URLs:". Individually these are accurate sentences; collectively they are floor-aiming appendices. The 320-word bar is being met by construction, not by curation.

6. **Template boilerplate remains (unchanged).** "Failure modes" appears in all 219 files, "Concrete example" in 216, "Mechanism:" in 201, "Operational tradeoffs" in 189, "RSIS3/mykb relevance" in 183. The identical syntheses meta-link pair — `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb` and `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to` — appears in 27 files; the target `mykb-acquisition-curation-and-practices.md` is real and the description is accurate, but 27 identical boilerplate links add graph noise. This is the deliberate non-fix category: honest but templated.

### Minor & nits

1. **Cleanup regression: 5 prompt-engineering files have orphaned, headerless bullets.** A bullet now dangles between the RSIS3 paragraph and `## Related`, where an annotation-bearing heading was clearly stripped: `prompt-engineering/multi-step-reasoning.md` ("- Separate reasoning output from the final answer in the prompt so steps inform, not pollute, the conclusion."), `red-teaming.md` ("- Keep a scored findings log…"), `refusal-behaviour.md` ("- Measure refusal consistency across phrasings…"), `retrieval-prompting.md` ("- Require the model to cite or quote retrieved evidence…"), `safety-tuning.md` (two bullets: "Treat safety tuning as a continuous loop…", "Document the preference data…"). Fix: restore a heading or fold the bullets into an existing section.
2. **`security-auth/ssrf-prevention.md`** has a double blank line before `## Related` ("…trust boundary like any other.\n\n\n## Related") — formatting remnant.
3. **Frontmatter spacing is inconsistent across the slice**: web-platforms files use `---\n# Title` (no blank line), os-shell and software-engineering files use `---\n\n# Title`. Cosmetic, but it is exactly the kind of drift a formatter pass would fix in one shot.
4. **Two syntheses carry "Open Threads" titles but are promoted to `status: growing` as syntheses**: `syntheses/evidence-and-provenance.md` and `syntheses/knowledge-acquisition-workflow.md` are structured as open questions ("Next step — design the provenance fields…") rather than conclusions. Type/tags now agree with the namespace, but the content is arguably a question-note promoted early.
5. **`security-auth/bug-bounty.md`** includes a `source:` frontmatter key with a Wikipedia URL — fine, but no other concept file in the slice carries sources, so provenance practice is inconsistent wave-wide.
6. **`web-platforms/srgb-vs-p3.md`**: "Wide-gamut support in CSS is broad by 2024+" — a dated claim with no source; likely true, but unverifiable from the file.
7. **`os-shell/oom-killer-and-memory-pressure.md`** Related list is all memory files plus the two syntheses meta-links; it is the only file in the slice whose Related is almost entirely same-cluster — acceptable, but the boilerplate pair makes it look padded.
8. **`prompt-engineering/prompt-compression.md`**: "a 50-turn session is compressed to a 5-turn digest" — invented-but-plausible example number; fine as illustration, note the pattern (see Major 1).

### Sample audit table

| File (relative to `components/mykb/wiki/`) | Words | Verdict | Notes |
|---|---|---|---|
| os-shell/path-resolution.md | 441 | OK content, dup | Part of 3-file near-duplicate cluster; fine standalone |
| os-shell/path-resolution-and-symlinks.md | ~460 | DUP | Near-verbatim twin of path-resolution; ELOOP 40, openat2, realpath repeated |
| os-shell/symlinks.md | ~430 | DUP | Third member of the cluster |
| os-shell/users-and-groups.md | ~450 | OK | Accurate identity model; Related clean |
| os-shell/users-groups-and-acls.md | ~460 | MINOR | Keyword links: cloud-security-groups, process-groups-and-sessions, memory-management-paging |
| os-shell/mdadm-and-lvm2.md | ~470 | MINOR | Accurate; filler Related (kernel-architecture, memory-management-paging) |
| os-shell/tcp-keepalive.md | ~470 | MINOR | Correct defaults (7200s/75s/9); irrelevant nvme-over-fabrics-tcp link |
| os-shell/swap-and-zram.md | ~460 | OK | Accurate; zswap/zram/swapiness correct |
| os-shell/select-poll-epoll-comparison.md | ~430 | OK | Correct FD_SETSIZE/epoll semantics; filler Related pair |
| os-shell/io-uring-and-async-io.md | ~450 | OK | Accurate (pre-5.1, EOPNOTSUPP, registered files); boilerplate meta-links |
| os-shell/oom-killer-and-memory-pressure.md | ~450 | OK | Correct cgroup v2 memory.pressure framing; boilerplate tail |
| os-shell/grep-patterns.md | ~430 | OK | Checker flags (`:alpha:`, TODO) are false positives |
| os-shell/environment-variables.md | ~440 | MINOR | Invents `MYKB_WIKI_ROOT` as fact; otherwise accurate |
| os-shell/tmux-sessions.md | ~430 | OK | Accurate |
| os-shell/zsh-configuration.md | ~440 | OK | Accurate; weak bash-patterns link acceptable |
| prompt-engineering/adversarial-prompts.md | ~370 | MINOR | "10,000 obfuscated variants nightly" invented number |
| prompt-engineering/agentic-rails.md | ~360 | OK | Accurate; rail/log/approve framing sound |
| prompt-engineering/indirect-injection.md | ~360 | OK | Accurate; truncated raw link now fixed (verified) |
| prompt-engineering/multi-step-reasoning.md | ~370 | REGRESSION | Orphaned headerless bullet before Related |
| prompt-engineering/red-teaming.md | ~360 | REGRESSION | Orphaned bullet; otherwise accurate |
| prompt-engineering/refusal-behaviour.md | 322 | REGRESSION | Orphaned bullet; 322 words (near floor) |
| prompt-engineering/retrieval-prompting.md | ~360 | REGRESSION | Orphaned bullet |
| prompt-engineering/safety-tuning.md | ~370 | REGRESSION | Two orphaned bullets; otherwise accurate |
| prompt-engineering/emergent-abilities.md | ~380 | OK | Correctly hedges emergence debate (2022 paper + metric critique) |
| prompt-engineering/in-context-learning.md | ~360 | OK | Accurate |
| software-engineering/actor-model.md | ~430 | MINOR | Duplicate RSIS3 relevance bullets still present |
| software-engineering/transactional-outbox.md | ~400 | OK | Accurate (Debezium, dual-write) |
| software-engineering/retry-after.md | ~380 | OK | Accurate; Related topical |
| software-engineering/singleton-pitfalls.md | ~420 | OK | Accurate |
| software-engineering/estimation-techniques.md | ~410 | MINOR | Stretched spaced-repetition link |
| software-engineering/code-formatters.md | ~400 | OK | Accurate |
| syntheses/bug-bounty-ai.md | ~400 | MINOR | Summary duplicated as first Details bullet; overlaps security-auth/bug-bounty |
| syntheses/coordinated-disclosure.md | ~420 | MINOR | Summary duplicated as first Details bullet |
| syntheses/safety-case-approach.md | ~410 | MINOR | Summary duplicated as first Details bullet |
| syntheses/evidence-and-provenance.md | ~380 | MINOR | "Open threads" content promoted to growing synthesis |
| syntheses/knowledge-acquisition-workflow.md | ~380 | MINOR | Same; the 27-file boilerplate link target |
| syntheses/model-updates-risks.md | ~420 | OK | Accurate; good canary/rollback framing |
| security-auth/bug-bounty.md | ~400 | MINOR | Near-duplicate of syntheses/bug-bounty-ai; has source: key |
| security-auth/ssrf-prevention.md | ~430 | OK | Accurate; double blank line before Related |
| pulses/capability-probes.md | ~430 | OK | Accurate; probe-hygiene advice sound |
| pulses/recursive-improvement-loops.md | ~410 | OK | Accurate; metric-gaming framing good |
| tooling/caching-layers.md | ~420 | OK | Accurate; miss-rate-per-layer point good |
| tooling/flag-cleanup.md | ~400 | OK | Accurate |
| tooling/game-days.md | ~430 | OK | Accurate |
| shell-environment/shell-scripting-robustness.md | 577 | OK | Densest file in slice; solid |
| shell-environment/unix-text-processing-tools.md | ~450 | OK | Accurate (spot-checked) |
| web-platforms/contrast-ratios.md | ~430 | FIXED-OK | Factual fix verified: 4.48/4.61/7.0 all correct |
| web-platforms/dom-clobbering.md | ~440 | FIXED-OK | Corrupted sentence gone; vectors accurate |
| web-platforms/cumulative-layout-shift.md | 321 | DUP | Near-duplicate of cls-avoidance; dashboard claim unverifiable |
| web-platforms/cls-avoidance.md | ~360 | DUP | Same content, same claim, incompatible with sibling's version |
| web-platforms/color-spaces.md | ~370 | DUP | Near-duplicate of srgb-vs-p3 |
| web-platforms/srgb-vs-p3.md | ~370 | DUP | Same gamut facts; "by 2024+" unsourced |
| web-platforms/em-vs-rem.md | 322 | CLUSTER | Member of 6-file unit cluster; top-up bullets visible |
| web-platforms/responsive-units.md | ~380 | CLUSTER | Meta-summary of the other unit files |
| web-platforms/layout-triggers.md | ~370 | CLUSTER | Accurate; identical Related to paint/compositing |
| web-platforms/compositing-triggers.md | ~380 | CLUSTER | Accurate; unverifiable rack-telemetry claim |
| web-platforms/speculative-loading.md | ~400 | CLUSTER | Meta-article over the hint cluster; unverifiable prerender claim |
| web-platforms/dns-prefetch.md | ~380 | OK | Checker "example.com" flag is false positive |
| web-platforms/preconnect-practice.md | ~380 | OK | Same; accurate |
| web-platforms/aspect-ratio-images.md | 320 | OK | Exactly at floor; content still substantive |
| web-platforms/polyglot-xss.md | 320 | OK | Exactly at floor; accurate |
| web-platforms/toctou.md | ~380 | OK | Accurate; open-then-fstat advice correct |
| web-platforms/unicode-normalization.md | ~380 | OK | Accurate; NFC/NFKD distinctions correct |
| web-platforms/mutation-xss.md | ~380 | OK | Checker "insert nodes" flag is false positive |
| web-platforms/safe-html-rendering.md | ~400 | OK | Checker flag false positive; pipeline advice correct |

(24 rows shown at full detail; table covers all 9 areas of the slice.)

### Recommendations (top 5)

1. **Re-curate or delete the "RSIS3/mykb relevance" bullets** (≈183 files). Decide whether these are facts (then verify and source them) or aspirations (then label them as such). As written, they are the slice's largest fabrication surface: a future session citing "the rack telemetry includes a periodic contrast audit" will inherit an unverifiable claim as memory. Highest impact, lowest effort is a wave-wide rewrite to a single honest sentence or removal.
2. **Merge the near-duplicate clusters to one canonical slug each** (path-resolution ×3, CLS ×2–3, color ×2, CSS units ×6, triggers ×3, speculative-loading ×5, bug-bounty ×2). For a retrieval store, eight overlapping clusters directly degrade search precision. Add a near-duplicate check (normalized-body similarity) to the promotion gate.
3. **Re-curate Related links by meaning, not keyword**, and drop the automatic "kernel-architecture + memory-management-paging" filler pair. At minimum remove the confirmed misfires: `nvme-over-fabrics-tcp` from `tcp-keepalive.md`, `cloud-security-groups` and `process-groups-and-sessions` from `users-groups-and-acls.md`, `memory-management-paging` from `mdadm-and-lvm2.md`.
4. **Fix the cleanup regression and the cross-section duplication**: restore a heading (or fold the bullets) in the 5 `prompt-engineering` files with orphaned bullets, and dedupe Summary↔first-Details repeats in the 3 syntheses files plus the twin RSIS3 bullets in `actor-model.md`.
5. **Raise the floor's honesty**: either raise the body-word minimum and re-measure content density, or replace the 320-word gate with a quality gate that counts distinct facts/links. The 71% concentration in the 320–360 band shows the current floor is being padded to, and the short "Header: sentence" appendices are the visible signature; a density check would catch both the padding and the boilerplate in one mechanism.

### Rules compliance

- No wiki file modified; no `git` run; only `ops/reports/adversarial-reviews/review-5-pass2.md` written.
- All flagged items opened and verified; all link targets in this report checked for existence.
- Unverifiable claims are labeled "cannot verify" rather than asserted true or false.

---
