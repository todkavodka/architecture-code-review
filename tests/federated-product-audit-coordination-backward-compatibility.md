# Federated Product Audit Coordination — Backward Compatibility

This matrix is a compatibility guard for the existing architecture. It does
not claim that federated behavior existed before implementation. Each row must
name the exact owner mechanism and final evidence after implementation.

| ID | required outcome | forbidden regression | owning contract/mechanism | status |
|---|---|---|---|---|
| BC01 | Single-repository Project startup remains unchanged. | Normal startup implicitly becomes Product coordination. | `references/session-orchestration.md` existing startup route. | OPEN |
| BC02 | Product mode remains explicit/opt-in. | Root containment silently creates membership. | `references/session-orchestration.md` Product selection. | OPEN |
| BC03 | Persisted intents are exactly USE_EXISTING, NEW, RESUME, REVALIDATE, EXTEND, CHANGE_REVIEW, PROJECTION_REPAIR. | FEDERATED_* or Product coordination label becomes an intent. | `references/session-orchestration.md` intent enumeration. | OPEN |
| BC04 | Top-level capabilities remain Architecture Review, Test Engineering, Code Quality Review. | TD/readiness/coordination becomes a fourth capability. | `SKILL.md` capability routing. | OPEN |
| BC05 | RECONCILE_CHANGE remains contextual and proof-gated. | A federated startup intent bypasses owner gates. | `references/review-modes-and-orchestration.md` reconciliation section. | OPEN |
| BC06 | Product baseline remains an immutable exact member/source vector. | Root SHA or mutable latest pointer is accepted. | `references/product-multi-project-review.md` baseline contract. | OPEN |
| BC07 | Existing Product CR reuse still requires complete qualified vector equality. | One changed child permits old Product CR reuse. | `references/product-multi-project-review.md` reuse qualification. | OPEN |
| BC08 | One/many Project↔repository cardinalities remain supported. | Discovery allocates Project identity from repository roots. | `references/product-multi-project-review.md` Project/repository contract. | OPEN |
| BC09 | Reports/projections/indexes/readiness remain non-authoritative. | Coordinator summary becomes Product STM/finding authority. | Product ownership and `SKILL.md` boundaries. | OPEN |
| BC10 | Projection regeneration remains explicit after accepted semantic impact. | Coordination automatically regenerates projections. | `references/projection-impact.md` and regeneration contract. | OPEN |
| BC11 | Child authority remains owned by the child workflow. | Product coordinator clones or writes child STM/capability state. | `references/product-multi-project-review.md` child authority. | OPEN |
| BC12 | `working/INDEX.md` remains the sole coordinator workflow authority. | A second Product INDEX/state machine is introduced. | `references/review-modes-and-orchestration.md` and Product namespace. | OPEN |
