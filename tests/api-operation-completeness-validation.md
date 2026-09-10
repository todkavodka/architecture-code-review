# API Operation Completeness Validation

## PRE-CHANGE — immutable fail-first evidence

Evidence base: `d68b9650a29820d8f9a563a81f5d90fb8f11d5e5`.

Inspected path: `references/shared-technical-model.md`, section 10.1, `IF-*`
interface and contract shape (including the existing role/view matrix and
protocol-property table).

| Check | Concrete contract observation at the evidence base | Expected result |
|---|---|---|
| FF01 — coarse one-IF/ten-operation CURRENT projection | The `IF-*` shape has one optional `operation_identity` field and no `operation_children` collection, so a CURRENT projection of ten operations requires coarse interface-level representation rather than ten independently identified children. | GAP PRESENT |
| FF02 — missing inventory accounting | The IF contract has no parent-qualified operation identifier, no child inventory, and no allocation rule from which a complete operation inventory can be accounted. | GAP PRESENT |
| FF03 — missing composed route requirement | The HTTP_REST controlled properties name method and path/template, but the IF contract has no requirement to persist a protocol-specific normalized operation identity composed from the route and operation semantics. | GAP PRESENT |
| FF04 — coarse EXTEND reuse | Reuse is defined only for accepted facts at the coarse STM-fact level; there is no parent-qualified child identity or `supersedes` rule for extending one operation while preserving the remaining IF contract. | GAP PRESENT |
| FF05 — material-only consumed grouping | `IF-*` identifies one material interaction surface and has a single `observed_view`; the `CONSUMED` view cannot group independently evidenced consumed operations without collapsing them into that material IF record. | GAP PRESENT |
| FF06 — complete-claim absence | The IF contract has no operation inventory or child lifecycle/accounting rule that could support a complete-operation claim for an interface. | GAP PRESENT |

This PRE-CHANGE evidence was recorded before the normative IF contract edit and
must not be reconstructed from the edited contract.

## Task 2 — protocol identity and route-composition edge checks

| Check | Scenario | Expected contract outcome |
|---|---|---|
| A01 — method distinguishes HTTP operations | `GET /orders/{orderId}` and `POST /orders/{orderId}` are both declared under the same parent interface. | Two distinct parent-qualified operation identities; the normalized method is part of each identity. |
| A02 — parameter names remain visible | `GET /orders/{orderId}` and `GET /orders/{id}` have otherwise equal route shapes. | Distinct identities unless the evidenced protocol contract explicitly declares the parameter names equivalent. |
| A03 — nested prefix composition | A controller prefix `/api`, router prefix `/v1`, and local route `orders/{orderId}` are declared in that order. | Composition produces the effective path `/api/v1/orders/{orderId}` after separator normalization; each input remains separately evidenced. |
| A04 — aliases require acceptance | One handler is declared at two routes and the declaration claims an alias. | Each route is distinct until an accepted alias relation proves intentional equivalence; a declaration alone does not collapse them. |
| A05 — duplicate declarations remain candidates | Equivalent-looking route declarations appear through different registrations. | Account for each as a candidate until classified as a duplicate declaration or as separate operations. |
| A06 — flags and computed registration limit precision | A feature flag, plugin, reflection, or computed registration controls the route. | Preserve the limitation and use `RESOURCE_BOUNDED` or `UNRESOLVED`; never fabricate an effective path. |
| A07 — declaration and code conflict | A declaration and implementation evidence incompatible method or route values. | Preserve both observations as a conflict and retain an unresolved/bounded candidate pending adjudication. |
| A08 — known HTTP address with unknown schema | An evidenced method and effective path exist, but parameter or request/response schema evidence is unavailable. | The HTTP operation identity is `EXACT`; missing schema is an explicit separate limitation. |
| A09 — unresolved effective path | A local route is known but one required prefix or runtime path construction cannot be resolved. | No exact HTTP identity is claimed; retain only the bounded or unresolved operation with its missing composition input. |
| A10 — dynamic consumer base URL | A consumer call supplies a method/path but obtains its base URL dynamically. | Record the consumer call-site and dynamic-base limitation; do not turn configuration or a runtime guess into an exact consumer address or identity. |

## Task 3 — output-scoped operation inventory coverage checks

| Check | Scenario | Expected contract outcome |
|---|---|---|
| D01 — ten operations under one router | One provided HTTP router exposes ten distinct evidenced method/effective-route operations under one `IF-*` parent. | The requested `PROVIDED` `HTTP_REST` inventory records ten discovered candidates and ten evidence-backed accepted exact operations; one parent interface never collapses the ten child operations. |
| D04 — dynamic route limitation | A route is conditionally registered through a feature flag, plugin, reflection, or computed value. | The candidate is counted and classified as accepted bounded or unresolved only with an accepted dynamic-discovery limitation; an exact identity is not fabricated. |
| D05 — declaration/code mismatch | Declaration and implementation evidence disagree on an operation's method or effective route. | Both observations remain visible; the candidate is counted as accepted bounded or unresolved pending adjudication, not accepted exact. |
| D06 — partial operation detail | An operation identity is evidenced, but schema or parameter detail is only partial. | The operation may satisfy inventory accounting as accepted exact when its identity is accounted; the incomplete detail remains a separate explicit limitation and does not create an `OPERATION_DETAIL` gate. |
| D08 — Architecture-only no enumeration | A full Architecture Review requests ordinary interface surface coverage but no detailed API/interface slice. | `INTERFACE_SURFACE_COMPLETE` remains sufficient; it does not silently require operation enumeration. |
| D09 — API-only targeted acceptance | An API-only requested slice needs a detailed consumed or provided interface inventory without Architecture Review. | The internal `resolved_work` dependency slice names the exact scope, direction, kind, parent IF revisions, and coverage-record revision; acceptance does not select Architecture or another capability. |
| D10 — 5,000-operation partitioning | A requested interface inventory has 5,000 discovered operations across bounded interface and/or protocol partitions. | Every partition has explicit scope/baseline/direction/kind and deterministic counts; aggregate accounting has no unaccounted candidates before the requested inventory is complete. |
| D17 — GraphQL inventory | A requested GraphQL interface slice contains named operations and addressable field/schema surfaces. | `GRAPHQL` candidates use the accepted operation identities and are independently accounted in the requested direction. |
| D18 — gRPC inventory | A requested gRPC interface slice contains several package/service/method operations. | `GRPC_RPC` candidates are independently accounted using package, service, and method identities. |
| D19 — Product member divergence | Two Product members expose identical-looking operations but bind to different Project revisions or baseline members. | Coverage retains qualified Project/member bindings; the operations do not alias, and an unavailable or divergent member remains an explicit limitation. |
| D20 — Product slice acceptance | A Product-scoped requested interface inventory covers only a bounded set of member interfaces. | The coverage record binds the Product revision and immutable baseline vector plus exact member bindings; it accepts only the bounded slice without claiming Product-wide inventory completeness. |

## Task 5 — operation rendering, API Report, and complete-claim checks

| Check | Scenario | Expected contract outcome |
|---|---|---|
| D03 — nested route rendering | A provided operation is composed from controller prefix `/api`, router prefix `/v1`, and local route `orders/{orderId}`. | Render one row for the accepted child with parent IF, child reference, `PROVIDED` role, protocol kind, exact method/effective path `/api/v1/orders/{orderId}`, precision, views, evidence, and no omitted route component. |
| D07 — providerless consumer rendering | A consumed operation is evidenced at a call site but no provider IF is accepted. | Render the consumed operation row and its evidence with an explicit unmatched-provider limitation; do not omit the operation or invent a provider match. |
| D11 — EXTEND from surface-only STM | A detailed Provided/Consumed or API Report section is selected while the matching accepted STM is only `SURFACE`. | Emit an internal `OPERATION_INVENTORY` requirement in `resolved_work` for the exact Project/baseline, direction, kind, parent IF slice, source/evidence scope, and required depth; preserve the accepted surface facts and do not select Architecture, TE, or CQ. |
| D12 — endpoint addition | A new accepted operation child is added beneath a selected parent IF. | The detailed snapshot membership changes, the matching projection becomes `STALE`, and explicit regeneration is required; the new operation is rendered only from the accepted refreshed snapshot. |
| D13 — endpoint removal | An accepted operation child is removed or superseded. | The old child remains in history, the selected snapshot detects removal and stales only the affected detailed projection, and no renderer silently retains it as current content. |
| D14 — path/identity change | An accepted operation keeps its scope but changes its method or effective path identity. | The identity change is detected through the parent-qualified snapshot, stales the affected detailed projection, and the renderer shows the new identity only after accepted authority and an explicit refresh. |
| D15 — auth/trust change | Accepted auth/trust evidence for an operation changes while method/path remains stable. | The operation row keeps its identity but renders the changed accepted auth/trust detail or limitation; verification does not adjudicate or fabricate the security fact. |
| D16 — boundary-evidence change | Accepted request-boundary evidence changes while the operation identity remains stable. | The operation row keeps its identity and renders the changed boundary evidence/limitation; no automatic regeneration or operation-detail authority is created. |

| Complete-claim check | Candidate claim and dependency state | Expected contract outcome |
|---|---|---|
| COMPLETE_CLAIM_01 | “Complete API” or “all endpoints” with missing, partial, unknown, unresolved, stale, blocked, or mismatched selected inventory. | Reject the complete wording and require explicit `PARTIAL`, `UNKNOWN`, or `UNRESOLVED` limitation wording. |
| COMPLETE_CLAIM_02 | “Full endpoint list” with projection `CURRENT` but without an accepted matching `OPERATION_INVENTORY_COMPLETE` and valid snapshot. | Reject the claim; `CURRENT` alone is insufficient. |
| COMPLETE_CLAIM_03 | Provided-only detailed scope with accepted matching Provided inventory complete and Consumed deselected. | Allow the Provided complete claim without requiring Consumed inventory; retain any row-level limitations. |

## Task 6 — EXTEND and REVALIDATE routing checks

| ID | Scenario | Expected contract outcome |
|---|---|---|
| R01 — preserve requested operation scope | A completed detailed output is revalidated against a changed Project baseline. | Preserve the selected output, direction, kind, parent IF slice, and exact baseline-qualified scope; route only the affected operation/evidence dependency slice and do not add outputs or capabilities. |
| R02 — added operation freshness | A new operation child is accepted under a parent in the previously selected detailed scope. | The matching inventory membership/snapshot and detailed projection become `STALE` after impact accounting; no generation or regeneration starts automatically. |
| R03 — removed operation history | An accepted operation is removed or superseded in the current source revision. | Retain the prior parent-qualified child and its removal/supersession history, detect snapshot membership removal, and require an explicit refreshed projection before omitting it from current content. |
| R04 — revised precision and Product qualification | An operation changes identity/precision or one Product member diverges at a new qualified revision. | Revise the matching operation/snapshot and stale only materially dependent detailed projections; keep Project/member/baseline qualification and do not alias divergent members. |

## Task 6 — adversarial routing checks

| ID | Adversarial scenario | Expected contract outcome |
|---|---|---|
| A11 — Product v1/v2 divergence | Two Product members expose the same method/path text but bind to different Project revisions or immutable baseline members. | Keep separate qualified operation identities/inventory memberships; identical text does not create an alias, and missing/divergent evidence remains an explicit limitation. |
| A12 — operation removal and identifier reuse | A removed operation is reintroduced or a sibling is allocated after the original child left the current inventory. | Preserve the removed child in history, never reuse its parent-qualified operation allocation, and represent any semantically new child with explicit revision/history rather than silently restoring stale projection content. |
