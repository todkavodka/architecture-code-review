# Finding Lifecycle & Progress Reporting — Backward Compatibility Validation

This bounded matrix preserves existing owner contracts and single-Project
operation. It does not migrate old packages or create a generic test harness.

| ID | Compatibility assertion | Expected result | Forbidden outcome | Status |
|---|---|---|---|---|
| BC01 | RF IDs and accepted revisions | Stable IDs/history remain usable | Renumber/rewrite | PASS |
| BC02 | CQ IDs/lifecycle/dispositions | CQ `ACTIVE`, `RESOLVED`, `SUPERSEDED`, `ACCEPTED_EXCEPTION`, `WONT_FIX` remain owner-specific | Flatten CQ or make WONT_FIX accepted risk | PASS |
| BC03 | TE families | `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` keep TE authority | Apply RF/CQ lifecycle | PASS |
| BC04 | Seven Session Intents | Existing seven intents remain exact; `RECONCILE_CHANGE` contextual | New intent | PASS |
| BC05 | Three capabilities | Architecture, Test Engineering, Code Quality remain top-level capabilities | Finding/Progress capability | PASS |
| BC06 | Single Project | Current/history/progress works without Product state | Product required | PASS |
| BC07 | Product mode | Product qualifies and composes accepted child views | Product mutates child finding | PASS |
| BC08 | Change Review | Candidate-only `POTENTIALLY_RESOLVES`; reconciliation remains gated | Direct CR→RESOLVED | PASS |
| BC09 | REVALIDATE | Existing bounded impact/revalidation route remains | Full automatic audit | PASS |
| BC10 | EXTEND | Existing additive scope semantics remain | Implicit baseline mismatch bypass | PASS |
| BC11 | Projection lifecycle | `PRJ-*`, V1–V4, stale/current boundaries remain | Markdown becomes authority | PASS |
| BC12 | Explicit regeneration | RG flow remains explicit and non-mutating | Auto regeneration | PASS |
| BC13 | Legacy packages | Existing packages retained and qualified conservatively | Mass rewrite/default lifecycle | PASS |
| BC14 | Product baseline | Exact vector and acceptance gate remain immutable | Latest-pointer/automatic advance | PASS |
| BC15 | Unavailable member | Limitation retained; no zero or unchanged claim | False Product total | PASS |
| BC16 | Authority/YAGNI | No DB, service, event system, dashboard, watcher, scheduler, or new authority | Scope expansion | PASS |

## Compatibility references

The normative support is provided by the existing contracts plus the feature
clauses cited in the lifecycle validation artifact:

- `references/report-contract.md` — RF authority and derived views;
- `capabilities/code-quality-review/references/code-quality-lifecycle.md` — CQ;
- `capabilities/test-review/SKILL.md` — TE;
- `references/review-modes-and-orchestration.md` — intents and Change Review;
- `references/revalidation-and-freshness.md` — revalidation;
- `references/product-multi-project-review.md` — Product qualification/baseline;
- `references/projection-lifecycle.md` and `references/projection-regeneration.md` — projections.

## Final marker

`FINDING_LIFECYCLE_PROGRESS_BACKWARD_COMPATIBILITY_PASS`
