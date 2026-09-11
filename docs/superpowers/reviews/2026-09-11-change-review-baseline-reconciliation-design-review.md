# Independent Design Review: Change Review and Baseline Reconciliation

## Review boundary

This is a read-only adversarial review of
`docs/superpowers/specs/2026-09-11-change-review-baseline-reconciliation-design.md`
against the current main contracts at
`5be8bbd8a5869bb74d4a2ee804c695cb19620008`. No implementation or normative
contract was changed during this review.

## Review method

The review checked the current session-intent and requested/resolved-work
contracts, revalidation and projection freshness boundaries, Technical Model
and evidence ownership, Product member qualification, CQ/TE/Architecture
ownership, API operation completeness, and Stage B impact/regeneration rules.
It then adversarially traced CR01–CR36 and the required candidate/canonical,
reuse, reconciliation, and baseline-advancement cases.

## Conformance results

| Area | Result | Evidence in design |
|---|---|---|
| New lifecycle separation | PASS | Sections 7, 26–37 explicitly separate CHANGE_REVIEW, REVALIDATE, RECONCILE_CHANGE, and regeneration. |
| Candidate/canonical boundary | PASS | Sections 12, 16–19, 28, and 41 prohibit CR/CF/CRF from satisfying accepted authorities. |
| Immutable source binding | PASS | Sections 8–9 persist exact commit/tree and qualification; Section 22 rejects SHA-only reuse. |
| Baseline mismatch routing | PASS | Sections 8 and 30–33 block silent current-state RESUME, EXTEND, and projection repair. |
| Delta discovery | PASS | Sections 13–15 use bounded diff-guided discovery and explicit context expansion. |
| Finding effects | PASS | Section 18 uses candidate effects without canonical lifecycle mutation. |
| Reconciliation ownership | PASS | Section 28 routes each slice to its existing owner; Section 29 gates baseline advancement. |
| Projection lifecycle | PASS | Sections 35–37 keep predicted impact, actual impact, and explicit RG regeneration separate. |
| Review reuse | PASS | Sections 22–24 cover exact, tree-equivalent, advanced, diverged, merge, squash, conflict, and partial cherry-pick behavior. |
| Product qualification | PASS | Section 43 requires exact member vectors and prevents flattening or permission expansion. |
| Existing API operation model | PASS | Section 42 retains operation-completeness authority and does not bypass STM/coverage. |
| Backward compatibility | PASS | Sections 46–47 preserve existing records and classify the extension as compatible. |
| Pressure coverage | PASS | Section 48 gives deterministic authority/candidate/canonical/projection/next-action outcomes for CR01–CR36. |

## Adversarial checks

- A candidate-only CR cannot resolve a CQ finding, write an STM fact, mark a
  projection stale, or advance the baseline.
- A branch, PR, tag, arbitrary commit, or `HEAD` is treated as an input ref;
  only the resolved immutable commit/tree is persisted as review identity.
- A no-ff or squash merge can reuse a review only when relevant tree and scope
  equivalence is proven; conflict resolution and incomplete cherry-picks do not
  receive unsafe reuse.
- An advanced candidate creates a linked review and does not mutate the
  historical A→B meaning.
- `RESUME`, `EXTEND`, and `PROJECTION_REPAIR` cannot treat B as accepted A.
- A complete CR with `UNKNOWN_IMPACT` exposes the limitation and does not claim
  exhaustive impact discovery.
- Actual impact may differ from prediction without rewriting the CR.
- Reconciliation may accept a baseline containing an open finding, while the
  owner still adjudicates that finding; the design does not invent release
  approval.
- Product changes stay member-qualified, including multi-repository vectors.

## Findings

No HIGH, MEDIUM, or LOW findings remain.

The design preserves current authority boundaries and freezes the decisions
needed for implementation planning. The few items identified as open in the
spec are implementation details only (field ordering, storage path, numeric
allocation, and PR-ref adapter); they do not defer an architecture decision or
permit an alternate authority model.

## Verdict

`CHANGE_REVIEW_BASELINE_RECONCILIATION_DESIGN_READY`

The next authorized step is user design review. No implementation plan or
normative contract change is authorized by this artifact.
