# Adversarial Review #5 — MyKB Stub-Promotion Wave (slice 5, 219 files)

Reviewer: adversarial-reviewer-5
Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice5.txt` (219 files)
Areas: os-shell, prompt-engineering, software-engineering, web-platforms, syntheses, security-auth, pulses, shell-environment, tooling
Checker run: `python3 ops/reports/adversarial-reviews/check_slice.py <slice>` → 186 clean / 33 flagged; all flags verified by opening the files.

## Verdict

**Health score: 64 / 100**

The wave's core invariants held: all 219 files are `status: growing`, all exceed the 320-body-word floor (min observed 320, in `web-platforms/aspect-ratio-images.md` and `web-platforms/polyglot-xss.md`), all six required frontmatter keys are present, and no UTF-8/markdown-link violations were found. Content quality is genuinely better than a word-count game — the os-shell, software-engineering, and prompt-engineering articles I deep-read are mostly accurate, specific, and technically sound. However, the wave shipped with a systemic link-hygiene and template-artifact problem: 24 confirmed self-links (11.0%), 6 files with broken or truncated links (2.7%), 27 files with generator boilerplate descriptors ("related coverage in the same cluster" plus syntheses meta-links) that often point at topically unrelated pages (12.3%), 5 near-duplicate article pairs, 6 syntheses files whose `type: "concept"` contradicts their location, one corrupted sentence that leaked generator self-correction into a published article, and verifiably wrong numeric claims in `web-platforms/contrast-ratios.md`. For a knowledge base whose value is retrievability and linkability, these are not nits; they degrade the store every time an agent follows a self-link or a "same cluster" link to an unrelated page. The checker also has blind spots it missed entirely (unclosed `[[` links, missing `README` targets, self-link alias variants), which should be fixed before the next wave.

Quantified: word-min 0/219 fail (0%), status 0/219 (0%), frontmatter-keys 0/219 (0%), self-links 24/219 (11.0%), broken/truncated links 6/219 (2.7%), boilerplate-template artifacts 27/219 (12.3%), type/tag contradictions 6/219 (2.7%), corrupted sentence 1/219 (0.5%), wrong numeric claims 1/219 (0.5%), near-duplicate pairs 5 (8 slice files, 3.7%), checker placeholders 9 flagged → 0 confirmed (all false positives), checker wikilink flag 1 flagged → 0 confirmed (false positive: POSIX `[[:alpha:]]` class).

## Critical findings

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

## Major findings

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

## Minor & nits

1. **Orphan bullet in `prompt-engineering/multi-step-reasoning.md`.** Between the RSIS3 relevance bullet and `## Related` sits a floating bullet with no heading: `- Separate reasoning output from the final answer in the prompt so steps inform, not pollute, the conclusion.` Move it under Details or delete.
2. **Nonstandard `source:` frontmatter key (2 files).** `security-auth/ssrf-prevention.md` and `security-auth/bug-bounty.md` add `source: ["https://…"]` to the six-key schema. Harmless but schema-inconsistent with the rest of the wave; either adopt `source` as a documented key or drop it.
3. **Inconsistent RSIS3 section naming across templates.** os-shell/web-platforms use `RSIS3/mykb relevance:`, prompt-engineering/security-auth use `RSIS3 relevance:`. Cosmetic, but it makes template provenance (and future de-boilerplating) harder to automate.
4. **Borderline word counts.** `web-platforms/aspect-ratio-images.md` and `web-platforms/polyglot-xss.md` sit at exactly 320 body words — right at the floor. Nothing wrong per the invariant, but zero headroom suggests these two were padded to the threshold rather than written to depth; worth a human skim.
5. **Lowercase title in `web-platforms/pointer-events-css.md`** (`title: "pointer-events CSS"` and self-link alias `[[…|pointer-events CSS]]`) — inconsistent with sentence-case titles elsewhere in the slice.
6. **Checker false positives (not defects, but worth recording).** The 9 placeholder flags (`TODO` in `os-shell/grep-patterns.md` is an example search string; `example.com` in dns-prefetch/preconnect/url-normalization are RFC-reserved example domains; "placeholder text/box" in contrast-ratios/aspect-ratio-images/reserved-space are legitimate technical terms; "insert nodes" / "insert as nodes" / "insert via node APIs" in mutation-xss/safe-html-rendering are natural language) and the single wikilink flag (`:alpha:` in `os-shell/grep-patterns.md` is the POSIX character class `[[:alpha:]]` inside a regex discussion) are all false positives. The checker needs a `[[:…:]]` exception and a stoplist for example domains.

## Sample audit table

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

## Recommendations

1. **Fix broken/truncated links and close the checker's blind spots (highest impact).** Repair the 3 unclosed `[[raw/archive/…]]` lines and the 3 `README` links (retarget to `sources/index` / `syntheses/index`); then extend `check_slice.py` to flag (a) any `[[` without closing `]]`, (b) `wiki/`-prefixed targets that don't resolve to a `.md` file, and (c) self-target links. These three rules would have caught every critical finding above at generation time.
2. **Strip the self-links and template boilerplate.** Remove the self-referencing Related bullet from the 24 `web-platforms/` files and delete the "related coverage in the same cluster" + syntheses meta-link boilerplate from the 27 `os-shell/`/`shell-environment/` files, replacing them with hand-curated topical links. This removes ~12% of the slice's noise and fixes the keyword-mismatch links (process-groups, DNS-resolution, memory-management) in the same pass.
3. **De-duplicate the five near-duplicate pairs.** Pick canonical slugs for path-resolution (three files), users/groups (two), CLS (two), color spaces (two), and viewport units (two); merge content, convert losers to redirects, and add a similarity gate to the promotion pipeline so future waves reject near-identical siblings.
4. **Repair the syntheses namespace.** Set `type: "synthesis"` on the six `syntheses/` files per AGENTS.md, remove the lingering `"stub"` tag from the two growing files, and have the checker validate `type` against directory namespace.
5. **Re-verify all numeric claims and corrupted prose before promotion.** Correct `web-platforms/contrast-ratios.md` (recompute examples with a WCAG calculator; current values are wrong and invert a pass/fail verdict) and rewrite the corrupted sentence in `web-platforms/dom-clobbering.md`. Add a cheap "generation-artifact" scan for phrases like "? No —" and "shadows?" plus a spot human review of any file whose body words are within 5% of the floor.
