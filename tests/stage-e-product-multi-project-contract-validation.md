# Stage E Product / Multi-Project Contract Validation

This is a bounded validation artifact for the completed Stage E contract graph.
It records assertions and expected outcomes; it is not a runtime coordinator,
semantic ledger, or reusable validation harness.

## Preconditions

- Tasks 1–8 and Checkpoints A–C are complete.
- Product mode is explicitly selected for Product assertions.
- The Product context has an accepted Product identity/revision and immutable
  baseline vector.
- The selected source, evidence, STM, dependency, capability, projection, and
  package bindings are qualified to that Product baseline.

## Contract assertions

The following assertions must pass jointly. A single keyword or generated
summary is insufficient evidence.

| Boundary | Required assertion | Expected result |
|---|---|---|
| Product context | Product identity, revision, membership, and baseline are distinct; Product mode is optional and opt-in; Product baseline is an exact vector, never one Git SHA. | Product composition is explicit and historical bindings remain immutable. |
| Evidence | `WS-*`/`EV-*` records preserve qualified Project/source provenance, external participation, and limitations. | Evidence remains observation authority; reports and summaries cannot replace it. |
| STM | Accepted factual records and cross-project relations remain STM-owned and baseline-qualified. | No second Product factual authority exists. |
| Dependencies | Direct metadata remains consumer/dependent → prerequisite with typed strength; relation, reverse index, and impact result remain distinct. | Traversal is derived from direct dependencies and does not itself revalidate. |
| Revalidation | Product `REVALIDATE` follows changed bindings and the minimum affected dependency slice; unaffected state is preserved. | Product revalidation is not a full Product reread; no automatic full Product audit occurs. |
| EXTEND | Added Projects, capabilities, investigations, outputs, and shared resources are additive and explicitly selected. | Existing unaffected Project authority remains accepted and reusable. |
| Availability | Source Availability, Review Coverage, Semantic Availability, Projection Freshness/Availability, and Package Gate Result are independently recorded. | No universal Product status is used. |
| Authorization | Product membership does not grant repository reads, revision selection, dirty acceptance, semantic writes, execution, code changes, worktrees, commit, push, PR, or deployment. | Every action remains separately authorized. |
| Architecture | Product RF uses existing `RF-*`, requires independent Architecture adjudication, and does not promote local RF. | Architecture Review remains RF authority. |
| Code Quality | Product CQ/CQRA uses the disjoint Product namespace, qualified evidence/baseline, material cross-project consequence, and Code Quality adjudication. | CQ aggregation remains projection; CQRA completion does not resolve CQ. |
| Test Engineering | Product TE uses existing `TRS-*` and TE families with qualified Project/baseline provenance. | Test Engineering remains authority; Product Assurance is projection/package. |
| Projection | Product outputs reuse `PRJ-*`, `RG-*`, V1–V4, impact-before-regeneration, and explicit freshness. | Projection is derived and regeneration is never automatic. |
| Package | Product packages reuse finite Stage B membership, dependency closure, and the existing `PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, and `ALL_SCOPED_CURRENT` policies. | `ALL_SCOPED_CURRENT` applies only to resolved selected scope. |
| Compatibility | Provider/consumer revisions, contract identity/version, supported range, evidence, and adjudication remain qualified. | No compatibility engine or version shortcut exists. |
| Storage | Product authority is in the coordinator Product namespace, not an arbitrary member repository. | No database, service, graph, vector, or RAG infrastructure is required. |

## Scenario suite

Validate each referenced scenario as a six-field contract: input state,
expected behavior, forbidden behavior, affected authority, impact scope, and
package/projection outcome. Every scenario must pass without changing its
historical artifact.

| Scenarios | Required outcome |
|---|---|
| PS-132–PS-136 | Product-free compatibility, exact vector, unavailable/dirty classification, and immutable baseline advancement remain precise. |
| PS-137–PS-140 | Cross-project compatibility, shared-resource ownership, genuine Product RF, and local-finding isolation retain their owning authorities. |
| PS-141–PS-144 | EXTEND, targeted REVALIDATE, projection freshness, and older-compatible revision remain bounded and explicit. |
| PS-145–PS-149 | Conflicting evidence, blocked package scope, multi-Product membership, requiredness change, and one-member transition remain isolated and additive. |

## Forbidden integrated outcomes

- Product becomes mandatory for a single-project review.
- A Product baseline is represented by one SHA or silently treated as atomic.
- Reports, projections, packages, indexes, or summaries become semantic
  authority.
- Project-local RF, CQ, or TE records are promoted by aggregation.
- `TASK-*` completion resolves `GAP-*`, or CQRA completion resolves CQ.
- Impact traversal automatically performs semantic revalidation or projection
  regeneration.
- A Product package selects every artifact in every member Project.
- Product membership grants hidden repository or publication permissions.
- Any unplanned identity family, backend, service, graph, vector, or RAG system
  is introduced.

## Verification record

This artifact is accepted only when all contract assertions and PS-132–PS-149
are green, the final tracked scope matches the approved plan, and no semantic
divergence or migration is present.

### Bounded verification record

The following deterministic checks are the execution record for this artifact.
They are intentionally bounded shell assertions over the approved contract
files and selected pressure scenarios; they are not a reusable validation
harness.

| Check | Exact command/check | Observed result |
|---|---|---|
| Product semantic tuple | `rg -l 'Product identity|Product revision|Product baseline|Product mode|Product is not a mandatory parent' references/product-multi-project-review.md` plus joint inspection of the Product identity, baseline, optionality, and non-authority sections | PASS: all four Product distinctions and optional mode are present in one owning contract. |
| Authority ownership | `rg -l 'WS-\*|EV-\*|STM|RF-\*|CQ-\*|CQRA-\*|BC-\*|CC-\*|MAT-\*|TM-\*|GAP-\*|TASK-\*|PRJ-\*|RG-\*' references/product-multi-project-review.md references/shared-evidence-model.md references/shared-technical-model.md references/review-method.md capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md` | PASS: the required authority families are owned by their existing contracts; Product output is described as derived. |
| Lifecycle and authorization negatives | `rg -n 'not.*automatically|does not grant|no automatic|FULL_REAUDIT_RECOMMENDED|relation.*dependency|consumer.*prerequisite' references/product-multi-project-review.md references/revalidation-and-freshness.md references/projection-lifecycle.md references/projection-gates-and-packages.md references/session-orchestration.md` | PASS: bounded impact, explicit authorization, dependency direction, and no automatic full audit/regeneration are all asserted. |
| Scenario contract shape | `for f in tests/pressure-scenario-{132..149}-*.md; do test -f "$f" && rg -q '^## Input state$' "$f" && rg -q '^## Expected semantic behavior$' "$f" && rg -q '^## Forbidden behavior$' "$f" && rg -q '^## Affected authority$' "$f" && rg -q '^## Expected impact scope$' "$f" && rg -q '^## Package/projection outcome$' "$f"; done` | PASS: all 18 approved scenarios satisfy the six-field contract. |
| Approved scope | `test "$(git diff --name-status 2a0fa60e3871b5274c71e7176abe93825552417b..HEAD | awk '$1==\"A\"{n++} END{print n+0}')" = 21` and `test "$(git diff --name-status 2a0fa60e3871b5274c71e7176abe93825552417b..HEAD | awk '$1==\"M\"{n++} END{print n+0}')" = 27` | PASS: the implementation range contains exactly the approved 21 additions and 27 modifications. |

Observed final marker: `STAGE_E_PRODUCT_CONTRACT_VALIDATION_PASS`.
