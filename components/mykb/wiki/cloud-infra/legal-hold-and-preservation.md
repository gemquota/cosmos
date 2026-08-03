---
type: "concept"
title: "Legal Hold & Preservation"
description: "Freezing data during litigation or investigation"
tags: ["legal-hold", "preservation", "compliance", "e-discovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Legal Hold & Preservation

## Summary

Legal hold freezes data from deletion or modification when litigation or investigation is pending — overriding normal retention and lifecycle policies. It is a compliance control with sharp teeth: failures are spoliation, and spoliation is a case-losing event.

## Details
- Mechanism: when a hold is issued (per matter, custodian, or data class), the platform must prevent deletion/overwrite of the covered data: object lock/immutability, backup copies, versioning, or quarantined buckets; holds interact with retention policies (the stricter wins), lifecycle rules must be suspended or scoped, and the hold itself must be documented with scope, custodian list, and release authority.
- Concrete example: a legal matter puts a hold on a custodian's email and files; the storage team applies object lock (compliance mode) to their buckets and pauses lifecycle expiration; after resolution, the hold is released by counsel with a written record. A mistaken release or a lifecycle rule that deleted covered data becomes a discovery dispute.
- Failure modes: lifecycle or deletion automation not aware of holds (the classic accidental purge); holds applied to copies but not originals (or vice versa); retention vs hold conflicts resolved by deletion; and hold metadata (who, what, until) not recorded, making the hold unenforceable in review.
- Operational tradeoffs: holds are expensive by design (storage growth, operational friction); the trade is legal risk vs cost. Build hold tooling that is independent from admins' deletion powers, test the release path, and audit hold coverage against retention policies regularly.
- RSIS3/mykb relevance: the wiki's artifact storage supports holds via object lock with a documented release procedure; this note is the reference the loop uses when retention changes must respect active holds.
- Hold audit: reconcile active holds against retention policies quarterly; the intersection is where deletion automation and legal obligations collide.
- Release authority: define who may release a hold and require written confirmation; an unauthorized release is a spoliation event with legal consequences.

