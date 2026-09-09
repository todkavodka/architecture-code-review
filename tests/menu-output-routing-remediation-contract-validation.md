# Menu Output Routing Remediation Contract Validation

## PRE-CHANGE BASELINE — IMMUTABLE

Captured before the first normative contract edit in Block A at the approved
plan checkpoint `75e73720b71434946999772f79357cfa73b24961`.

| ID | Current-contract citation/check | Expected gap | Result |
|---|---|---|---|
| FF-MENU-01 | `rg -n "Review Capabilities|at least one|Architecture Review|Test Engineering|Code Quality Review" references/session-orchestration.md` — current startup exposes capability configuration but no capability-or-valid-standalone-output predicate. | A zero-capability `Interface Catalog` request cannot be represented as valid requested work. | FAIL_FIRST_VALID |
| FF-MENU-02 | `rg -n "Technical Documentation|subsection|umbrella|Requested Outputs" references/session-orchestration.md references/technical-documentation.md` — documentation is a projection taxonomy, not a direct bounded umbrella request. | Broad Technical Documentation has no mandatory bounded subselection contract. | FAIL_FIRST_VALID |
| FF-MENU-03 | `rg -n "Product context|Product output|Output selection|Product Technical Documentation" references/session-orchestration.md references/product-multi-project-review.md` — Product context and output selection are separate concepts but no startup requested-output confirmation layer exists. | Product selection can be read as context-only or broad output selection. | FAIL_FIRST_VALID |
| FF-MENU-04 | `rg -n "dependency|resolved_work|requested_work|Required Internal Work" references/review-modes-and-orchestration.md` — current coordinator state has dependency/gate fields but no persisted requested/resolved work pair. | Internal dependency closure cannot be represented independently from user-selected work. | FAIL_FIRST_VALID |
| FF-MENU-05 | `rg -n "Provider/Consumer Matrix|Provider / Consumer Matrix|qualified view|new.*PRJ|compatibility" references/technical-documentation.md references/product-multi-project-review.md capabilities/test-review/references/test-engineering-contract.md` — existing views and compatibility boundaries are not one explicit menu routing class. | Matrix qualification and no-new-identity behavior are not exposed at the menu route. | FAIL_FIRST_VALID |
| FF-MENU-06 | `rg -n "Stage F compatibility|Product mode|Contract Verification|CC-\*|Matrix" capabilities/test-review/references/test-engineering-contract.md` — compatibility is described as a catalog-facing view with Product consumption, but direct Matrix/Product-independent routing is not explicit. | Generic compatibility can be coupled to Matrix or Product by orchestration. | FAIL_FIRST_VALID |
| FF-MENU-07 | `rg -n "Session Intent|Review Capabilities|Requested Outputs|Required Internal Work|requested_work" SKILL.md references/session-orchestration.md references/review-modes-and-orchestration.md` — no complete canonical six-layer requested-work startup model exists. | Requested outputs, internal work, and authorization boundaries are not separately confirmed. | FAIL_FIRST_VALID |

This section is immutable historical evidence. Block A may append post-change
checks and Block C may append final results, but must not rewrite these rows.

## Block A post-change evidence

| Check | Command/inspection | Result |
|---|---|---|
| Canonical startup labels and three capabilities | `rg -n "Session Intent|Scope Context|Review Capabilities|Requested Outputs|Resolved Plan / Required Internal Work|Authorization / Execution Boundaries|Architecture Review|Test Engineering|Code Quality Review" references/session-orchestration.md` | PASS; all six labels and exactly three capability names present. |
| Requested-work validity and separation | `rg -n "NO_REVIEW_SCOPE_SELECTED|requested_work != resolved_work|capability or at least one valid standalone output" references/session-orchestration.md references/review-modes-and-orchestration.md` | PASS; output-only is valid, 0/0 and Product-only are invalid, dependencies remain resolved work. |
| Six intents | `rg -n "USE_EXISTING|NEW|RESUME|REVALIDATE|EXTEND|PROJECTION_REPAIR" references/session-orchestration.md references/review-modes-and-orchestration.md` | PASS; 6/6 exact intents retained. |
| Conflict semantics | `rg -n "REQUESTED_WORK_CONFLICT|explicit confirmed|inferred|reconcile|substantive work" references/session-orchestration.md` plus inspection of both endpoint examples | PASS; conflict is shown and confirmed before persistence/work. |
| Product/ambiguous distinctions | `rg -n "Product context.*not requested|REQUESTED_OUTPUT_AMBIGUOUS|Technical Documentation" references/session-orchestration.md` | PASS; Product-only is scope invalidity and unconfirmed ambiguity uses `REQUESTED_OUTPUT_AMBIGUOUS`. |

## Post-change and integrated evidence

Block A appends exact checks for requested-work validity, normalization,
confirmation, `REQUESTED_WORK_CONFLICT`, and six intents. Block B appends the
11-row routing, Product, Matrix, compatibility, ownership, authorization,
runtime, and redaction checks. Block C appends the expanded 48-row acceptance
matrix, the 32-row pressure matrix, and final counts.

Required final results:

```text
fail_first_prechange: 7/7 CAPTURED
fail_first_postchange: 7/7 PASS
acceptance: 48/48 PASS
pressure: 32/32 PREVENTED
plan_pressure: 26/26 PLAN_PREVENTS
harness: DO_NOT_BUILD_HARNESS
migration: COMPATIBLE_EXTENSION
```
