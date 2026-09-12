# Federated Product Audit Coordination — Backward Compatibility

This matrix is a compatibility guard for the existing architecture. It does
not claim that federated behavior existed before implementation. Each row must
name the exact owner mechanism and final evidence after implementation.

| ID | required outcome | forbidden regression | owning contract/mechanism | exact owner evidence | status |
|---|---|---|---|---|---|
| BC01 | Single-repository Project startup remains unchanged. | Normal startup implicitly becomes Product coordination. | `references/session-orchestration.md` | Product mode is explicit; local route remains unchanged. | PASS |
| BC02 | Product mode remains explicit/opt-in. | Root containment silently creates membership. | `references/session-orchestration.md` | Coordination Root is locator only; membership requires Product context/authorization. | PASS |
| BC03 | Persisted intents are exactly USE_EXISTING, NEW, RESUME, REVALIDATE, EXTEND, CHANGE_REVIEW, PROJECTION_REPAIR. | FEDERATED_* or Product coordination label becomes an intent. | `references/session-orchestration.md` | Existing Session Intent enumeration is unchanged; labels are routing-only. | PASS |
| BC04 | Top-level capabilities remain Architecture Review, Test Engineering, Code Quality Review. | TD/readiness/coordination becomes a fourth capability. | `SKILL.md` | Product coordination normalizes to existing capabilities; TD remains output. | PASS |
| BC05 | RECONCILE_CHANGE remains contextual and proof-gated. | A federated startup intent bypasses owner gates. | `references/review-modes-and-orchestration.md` | Existing contextual reconciliation gate remains the only canonical dispatch path. | PASS |
| BC06 | Product baseline remains an immutable exact member/source vector. | Root SHA or mutable latest pointer is accepted. | `references/product-multi-project-review.md` | Baseline contract requires exact per-member bindings and rejects synthetic root SHA. | PASS |
| BC07 | Existing Product CR reuse still requires complete qualified vector equality. | One changed child permits old Product CR reuse. | `references/product-multi-project-review.md` | Reuse section requires complete vector, Product revision, and member qualification equality. | PASS |
| BC08 | One/many Project↔repository cardinalities remain supported. | Discovery allocates Project identity from repository roots. | `references/product-multi-project-review.md` | Cardinalities and explicit Project/source binding remain unchanged. | PASS |
| BC09 | Reports/projections/indexes/readiness remain non-authoritative. | Coordinator summary becomes Product STM/finding authority. | Product ownership and `SKILL.md` | Product records reference existing authorities; summaries/readiness are derived. | PASS |
| BC10 | Projection regeneration remains explicit after accepted semantic impact. | Coordination automatically regenerates projections. | `references/projection-impact.md` and regeneration contract | Product routing hands accepted impact to existing Stage B flow; no RG starts automatically. | PASS |
| BC11 | Child authority remains owned by the child workflow. | Product coordinator clones or writes child STM/capability state. | `references/product-multi-project-review.md` | Child authority remains local and Product consumes qualified references. | PASS |
| BC12 | `working/INDEX.md` remains the sole coordinator workflow authority. | A second Product INDEX/state machine is introduced. | `references/review-modes-and-orchestration.md` and Product namespace | Coordinator state stores refs under INDEX; Product namespace is Product-key-qualified. | PASS |
