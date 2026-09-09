# Menu Output Routing Remediation Backward Compatibility Validation

## Checks

| Case | Concrete inspection | Result |
|---|---|---|
| Capability-only legacy session | `rg -n "existing capability selections|capability-only|remain readable" references/review-modes-and-orchestration.md` | PASS; prior capability selections remain valid. |
| Missing standalone-output field | `rg -n "without standalone-output state|empty standalone output list" references/review-modes-and-orchestration.md` | PASS; missing field defaults empty. |
| Architecture Endpoint | `rg -n "Architecture Endpoint|legacy endpoint" references/review-modes-and-orchestration.md` | PASS; endpoint remains authoritative. |
| Test Engineering booleans | `rg -n "Test Engineering output booleans|output selections" references/review-modes-and-orchestration.md` | PASS; existing output state is preserved. |
| Product session | `rg -n "Product sessions|Product mode|accepted Product revision" references/review-modes-and-orchestration.md` | PASS; Product sessions remain interpretable. |
| `COMPLETE` / `USE_EXISTING` | `rg -n "COMPLETE|USE_EXISTING|accepted/current" references/review-modes-and-orchestration.md` | PASS; accepted legacy package is consumable. |
| `RESUME` | `rg -n "RESUME.*restores persisted|old.*RESUME" references/review-modes-and-orchestration.md` | PASS; old resume state remains readable. |
| Historical package identity | `rg -n "No historical package|PRJ-\*.*rewritten|not.*rewritten" references/review-modes-and-orchestration.md` | PASS; no rewrite/enrichment occurs. |
| Migration classification | `rg -n "COMPATIBLE_EXTENSION" docs/superpowers/plans/2026-09-09-menu-output-routing-remediation-implementation-plan.md` | PASS; migration is additive. |

backward_compatibility: PASS
migration: COMPATIBLE_EXTENSION
