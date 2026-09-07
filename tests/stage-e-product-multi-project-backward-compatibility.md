# Stage E Product / Multi-Project Backward Compatibility Validation

This bounded artifact proves that Product support is additive and does not
make Product state a prerequisite for existing single-project operation.

## Legacy single-project input

Use an existing single-project review containing its normal Project, `WS-*`,
`EV-*`, STM, Architecture `RF-*`, Code Quality `CQ-*`/`CQRA-*`, Test
Engineering records, `PRJ-*` projections, and package declarations. The review
does not select Product mode and has no Product registry, membership, baseline,
cross-project evidence, or Product package.

## Required compatibility assertions

| Assertion | Expected result |
|---|---|
| Product selection | The review remains valid without a Product ID, Product revision, or Product mode selection. |
| Membership and baseline | No Product membership snapshot or Product baseline vector is required. |
| Cross-project state | No cross-project WS/EV or STM state is required. Existing local facts and evidence remain usable under their own bindings. |
| Identity preservation | Existing Project, `WS-*`, `EV-*`, STM, `RF-*`, `CQ-*`, `CQRA-*`, TE, `PRJ-*`, and `RG-*` identities remain valid and are not rewritten. |
| Selectors and packages | Existing repository-scoped selectors, projections, package declarations, and Stage B policies remain valid without Product members. |
| Authority | Existing capability owners remain writers; no Product aggregate or summary is inserted into a local authority path. |
| Freshness | Local freshness and lifecycle remain independent from Product projection or package freshness. |
| Authorization | Product membership and Product mode are irrelevant to the existing local authorization path. |
| Migration | No registry migration, bulk conversion, historical rewrite, or forced Product enrollment occurs. |

## Forbidden compatibility outcomes

- Requiring a Product ID, Product baseline, Product package, or Product
  membership for a local review.
- Rewriting historical local identifiers or moving local authority into Product
  storage.
- Treating Product participation as a prerequisite for local STM, RF, CQ, TE,
  projection, or package state.
- Making a Product summary, report, or package the local semantic authority.
- Introducing automatic migration or hidden repository access.

## Verification record

The following deterministic checks are the execution record for this artifact.
They are bounded assertions over the legacy contract and Product contract; no
runtime harness or migration tool is required.

| Check | Exact command/check | Observed result |
|---|---|---|
| Product-free route | `rg -n 'Product mode is optional|without Product|Product-free|no Product ID|No Product membership' SKILL.md references/session-orchestration.md references/product-multi-project-review.md` | PASS: local review routing remains valid without Product state. |
| Identity preservation | `rg -n 'Project|WS-\*|EV-\*|RF-\*|CQ-\*|CQRA-\*|PRJ-\*|RG-\*|not rewritten|no historical' references/session-orchestration.md references/shared-evidence-model.md references/projection-lifecycle.md tests/stage-e-product-multi-project-backward-compatibility.md` | PASS: historical local identity and lifecycle preservation is explicitly retained. |
| No forced migration/permission | `rg -n 'no.*migration|no.*rewrite|does not grant|without Product|Product.*optional' references/product-multi-project-review.md references/session-orchestration.md tests/stage-e-product-multi-project-backward-compatibility.md` | PASS: Product enrollment, rewrite, and membership-based authorization are forbidden. |
| Negative compatibility outcomes | `rg -n 'Requiring a Product|Rewriting historical|Treating Product participation|automatic migration|hidden repository access' tests/stage-e-product-multi-project-backward-compatibility.md` | PASS: all forbidden compatibility outcomes are recorded as rejection cases. |

Observed final marker: `STAGE_E_PRODUCT_BACKWARD_COMPATIBILITY_PASS`.
