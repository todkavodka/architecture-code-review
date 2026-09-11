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

## Task 7 — CQ, TE, and CC operation-reference checks

| Check | Scenario | Expected contract outcome |
|---|---|---|
| T7-A06 — CQ bounded operation evidence | A feature flag, plugin, reflection, or computed registration limits operation precision. | CQ may point to the accepted parent and specific operation evidence with the limitation; it does not fabricate or classify an exact operation child. |
| T7-A07 — CQ declaration/code mismatch | Declaration and implementation evidence disagree on method or effective route. | CQ may reference the relevant operation evidence and preserve the conflict; CQ does not revise STM operation facts or decide CC compatibility. |
| T7-A08 — exact identity with unknown schema | Method and effective path are exact while request/response schema evidence is unavailable. | CQ/TE may target the exact operation and record unknown schema as a limitation; unknown schema does not become a fabricated field fact or TESTED result. |
| T7-A09 — unresolved effective path | A required prefix or runtime path construction cannot be resolved. | TE targets the accepted parent or bounded child with the unresolved limitation; neither TE nor CQ guesses a method/path or creates an operation identity. |
| T7-A10 — dynamic consumer base URL | A consumer call supplies method/path but obtains its base URL dynamically. | CC may retain qualified consumer operation evidence or an explicit dynamic-base limitation; same method/path does not auto-match or establish compatibility. |
| T7-D05 — operation mismatch ownership | A declaration/code mismatch is raised during CQ or TE review. | The observation remains evidence for the owning STM/CC workflow; CQ and TE may reference it but cannot create, revise, or classify operation inventory facts. |
| T7-D06 — partial operation detail | An accepted operation identity lacks schema or parameter detail. | TE may target the operation field in a boundary/negative/contract case, while `accepted_test_case != executed_test != tested_result` and inventory completeness is not redefined as detail completeness. |
| T7-D07 — providerless consumer operation | A consumed operation is evidenced without an accepted provider IF. | The consumer operation reference/evidence and unmatched-provider limitation remain visible; CC does not invent a provider or compatibility result. |
| T7-D08 — Architecture-only surface review | Architecture requests ordinary interface coverage without detailed API enumeration. | CQ/TE operation references remain optional downstream links; they do not create an operation inventory requirement or change Architecture’s surface-depth contract. |

## Task 8 — final integrated validation evidence

The rows below are the final integrated checks. Their unique `T8-` identifiers
keep the final evidence distinct from the earlier task-local rows while the
scenario order and wording remain the canonical D01–D20 and A01–A12 cases.
Every row names an owning contract area, a concrete check, and the expected
deterministic outcome. No runtime harness is required or created by this file.

### D01–D20 deterministic acceptance matrix

| Validation ID | Canonical scenario | Owner | Concrete contract check | Expected outcome |
|---|---|---|---|---|
| T8-D01 | Ten operations under one router | Task 3 — Technical Model Coverage | Count ten discovered candidates and account for ten accepted parent-qualified operation children under one IF. | `20/20 DETERMINISTIC`; no collapse to one interface row. |
| T8-D02 | Nested prefixes | Task 2 — protocol identity | Compose controller, router, and local prefixes from evidence; retain the unresolved component when composition cannot be proven. | Exact effective route when resolvable; otherwise visible bounded/unresolved limitation. |
| T8-D03 | Same-path methods | Task 2 — protocol identity | Compare `GET /orders/{id}` and `POST /orders/{id}` under the same parent. | Two distinct identities because normalized method is part of HTTP identity. |
| T8-D04 | Dynamic route | Task 2 — protocol identity | Classify feature-flag, plugin, reflection, computed, or runtime-only registration without inventing its path. | Candidate is accounted as `RESOURCE_BOUNDED` or `UNRESOLVED`; no fabricated exact identity. |
| T8-D05 | Declaration/code mismatch | Task 2 — protocol identity | Preserve incompatible DECLARED and IMPLEMENTED method/path observations and route the conflict to coverage/CC adjudication. | Candidate remains bounded/unresolved; no exact operation is silently accepted. |
| T8-D06 | Undeclared implementation | Task 3 — inventory accounting | Include an implemented operation absent from declarations in discovered candidates and mismatch evidence. | Candidate is not omitted; accounting remains explicit until classified. |
| T8-D07 | Providerless consumer | Task 5 — output rendering | Render an evidenced consumed operation even when no provider IF is accepted. | Consumed row remains visible with unmatched-provider limitation; no provider is invented. |
| T8-D08 | Partial schema detail | Task 5 — output rendering | Separate exact method/path identity from missing request, response, parameter, or schema detail. | Inventory can be complete while the row visibly reports partial detail. |
| T8-D09 | Architecture-only surface review | Task 3 — coverage depth | Request ordinary Architecture `FULL` surface coverage without a detailed API/interface slice. | `INTERFACE_SURFACE_COMPLETE` remains sufficient; no operation enumeration is required. |
| T8-D10 | API Report-only targeted depth | Task 5 — API Report dependencies | Select API Report/Provided/Consumed detail without selecting Architecture, TE, or CQ; resolve only the selected operation slice. | Targeted operation depth is added to `resolved_work`; unrelated capabilities remain unselected. |
| T8-D11 | EXTEND from surface-only STM | Task 6 — EXTEND routing | Add detailed API output where accepted STM depth is only SURFACE and inspect the resolved dependency tuple. | Only exact Project/baseline, direction, kind, IF slice, and evidence scope are enriched; existing surface facts remain valid. |
| T8-D12 | Operation addition | Task 4 — projection snapshot | Add an accepted child beneath a selected IF and compare the detailed membership snapshot. | Membership changes and the detailed projection becomes `STALE`; explicit regeneration remains required. |
| T8-D13 | Operation removal | Task 4 — lifecycle/freshness | Remove or supersede an accepted child and compare current membership with historical records. | Removal is detected, history is retained, and only affected detailed projections become stale. |
| T8-D14 | Path or identity change | Task 4 — lifecycle/freshness | Change an operation method, effective path, or parent binding and inspect the parent-qualified identity/history. | New or revised identity is explicit; dependent snapshot/projection is stale until accepted refresh. |
| T8-D15 | Auth/trust change | Task 7 — downstream references | Change accepted auth/trust evidence while operation identity remains stable. | Same operation reference renders changed accepted detail/limitation; CQ/TE/CC do not adjudicate the fact. |
| T8-D16 | Boundary-evidence change | Task 7 — downstream references | Change accepted request-boundary evidence while method/path remains stable. | Operation identity remains stable; changed boundary evidence/limitation propagates to applicable dependencies. |
| T8-D17 | 5,000-operation scale | Task 3 — partitioned accounting | Partition 5,000 candidates by IF, direction, kind, and bounded source scope; verify no unaccounted candidates. | Searchable parent-qualified records and deterministic aggregate counts; no 5,000 top-level IF families. |
| T8-D18 | GraphQL inventory | Task 2/3 — protocol-general identity and coverage | Account named GraphQL operations/fields with protocol-specific identity in the requested direction. | GraphQL candidates are independently accounted; field/schema limitations remain explicit. |
| T8-D19 | gRPC inventory | Task 2/3 — protocol-general identity and coverage | Account package/service/method RPC identities beneath a service IF. | `GRPC_RPC` children are independently accounted; the service IF remains the parent surface. |
| T8-D20 | Product member divergence | Task 6 — Product-qualified routing | Aggregate bounded member inventories while comparing Project revisions, immutable baseline, and member bindings. | Divergent or unavailable members remain visibly qualified limitations; no cross-member alias or Product-wide claim. |

Expected result: `20/20 DETERMINISTIC`.

### A01–A12 adversarial matrix

| Validation ID | Canonical adversarial scenario | Owner | Concrete contract check | Expected outcome |
|---|---|---|---|---|
| T8-A01 | Method identity | Task 2 — protocol identity | Normalize method into the identity comparison for same-path HTTP declarations. | GET/POST are never collapsed. |
| T8-A02 | Parameter-name identity | Task 2 — protocol identity | Compare `{orderId}` with `{id}` when the protocol does not declare names equivalent. | Identities remain distinct; names are not discarded as evidence location noise. |
| T8-A03 | Nested prefix composition | Task 2 — route composition | Verify each prefix/mount is separately evidenced and separator-normalized into the effective path. | Exact route only when every required composition input is resolved. |
| T8-A04 | Dual mounts and aliases | Task 2 — protocol identity | Treat one handler mounted at two routes as two candidates until an accepted alias relation proves equivalence. | No declaration-only collapse; each route remains addressable. |
| T8-A05 | Duplicate declarations | Task 3 — candidate accounting | Compare equivalent-looking registrations from different registration paths. | Each candidate is classified as duplicate or distinct; no silent omission. |
| T8-A06 | Feature flags and computed registration | Task 2 — dynamic limitation | Inspect conditional, plugin, reflection, and computed registration evidence. | Preserve `RESOURCE_BOUNDED`/`UNRESOLVED`; never fabricate an effective path. |
| T8-A07 | Declaration/implementation gap | Task 2 — conflict preservation | Feed incompatible declaration and implementation values into the identity/adjudication path. | Both observations remain visible and the candidate is not exact. |
| T8-A08 | Partial operation fields | Task 5 — faithful rendering | Provide exact method/path with unavailable schema or parameters. | Exact identity is renderable with explicit partial detail; no invented fields or TESTED result. |
| T8-A09 | Unresolved effective path | Task 2 — route composition | Omit one required prefix or runtime path-construction input. | No exact HTTP identity is claimed; missing input is rendered as limitation. |
| T8-A10 | Dynamic consumer base URL | Task 7 — CC/consumer reference | Supply consumer method/path while resolving the base URL dynamically. | Call-site evidence and dynamic-base limitation remain; no exact match from a runtime guess. |
| T8-A11 | Product v1/v2 divergence | Task 6 — Product qualification | Compare identical method/path text bound to different Project revisions or immutable Product members. | Qualified identities remain separate; divergence is not an alias. |
| T8-A12 | Removal history and identifier reuse | Task 4/6 — lifecycle | Remove an operation, then allocate a semantically new sibling or reintroduced operation. | Removed child remains historical; its parent-qualified allocation is never reused silently. |

Expected result: `12/12 MAPPED` with deterministic outcomes.

### Corrected fail-first checks

| Validation ID | Original fail-first gap | Post-Task 8 verification | Expected outcome |
|---|---|---|---|
| T8-FF01 | Coarse one-IF/ten-operation CURRENT projection | Inspect IF-owned `operation_children` and detailed membership snapshot. | `CORRECTED`: ten children can be addressed without changing the parent surface authority. |
| T8-FF02 | Missing inventory accounting | Inspect coverage counters and the `N4 = 0` completion rule for a bounded slice. | `CORRECTED`: every discovered candidate is classified; no unaccounted candidate passes. |
| T8-FF03 | Missing composed-route requirement | Inspect protocol identity and evidence for method, local route, every prefix/mount, and effective route. | `CORRECTED`: exact identity requires resolved composition; limitations remain explicit. |
| T8-FF04 | Coarse EXTEND reuse | Inspect `resolved_work` for targeted enrichment and operation/IF revision references. | `CORRECTED`: targeted operation depth is added without retroactive child creation or unrelated rerun. |
| T8-FF05 | Material-only consumed grouping | Inspect consumed operation children and providerless rendering. | `CORRECTED`: independently evidenced consumed operations remain separately addressable. |
| T8-FF06 | Complete-claim absence | Inspect claim guard dependencies and selected-scope validation. | `CORRECTED`: complete wording requires accepted matching inventory and valid snapshot. |

Expected result: `6/6 CORRECTED`; the original PRE-CHANGE GAP PRESENT rows remain
immutable above.

### Complete-claim guard — five checks

| Validation ID | Candidate claim/dependency state | Concrete check | Expected outcome |
|---|---|---|---|
| T8-CLAIM-01 | Detailed Provided scope is missing, partial, unknown, unresolved, blocked, stale, or mismatched. | Evaluate “complete API”/“all endpoints” wording against selected Provided inventory. | Reject the claim and require explicit `PARTIAL`, `UNKNOWN`, or `UNRESOLVED` limitation wording. |
| T8-CLAIM-02 | Detailed Consumed scope is missing, partial, unknown, unresolved, blocked, stale, or mismatched. | Evaluate equivalent wording against selected Consumed inventory and unmatched-provider limitations. | Reject the claim; provider absence or consumer uncertainty cannot be hidden. |
| T8-CLAIM-03 | Exact bounded scope has accepted `OPERATION_INVENTORY_COMPLETE` and a valid matching dependency snapshot. | Check Project/baseline, direction, kind, IF slice, `N4 = 0`, and snapshot validity. | Allow the claim only for that exact bounded scope. |
| T8-CLAIM-04 | Only detailed Provided is selected and its accepted inventory is complete. | Ensure the guard does not add a hidden Consumed dependency. | Allow Provided-only complete wording without requiring Consumed coverage; retain row-level limitations. |
| T8-CLAIM-05 | Projection is `CURRENT` but no accepted matching complete inventory exists. | Attempt the claim using `CURRENT` alone. | Reject it; `CURRENT` is projection freshness, not operation completeness. |

### Impact and lifecycle — seven checks

| Validation ID | Change | Concrete check | Expected outcome |
|---|---|---|---|
| T8-IMPACT-01 | Operation addition | Compare accepted child membership before and after the change. | `SELECTOR_MEMBERSHIP_CHANGED`; dependent detailed projection is `STALE`. |
| T8-IMPACT-02 | Operation removal/supersession | Compare current inventory with historical child records. | Removal impact is recorded; history remains addressable; no stale row is silently retained as current. |
| T8-IMPACT-03 | Method/path/parent identity change | Compare parent-qualified identity and revision/history link. | Identity revision/new child is explicit and dependent snapshot is stale. |
| T8-IMPACT-04 | Schema or operation-detail change | Compare the affected operation semantic revision and row limitation. | Detail changes propagate to the applicable dependent slice without changing inventory authority. |
| T8-IMPACT-05 | Auth/trust change | Compare accepted auth evidence while keeping method/path stable. | Same child identity renders changed accepted auth detail/limitation and stales affected outputs as applicable. |
| T8-IMPACT-06 | Boundary/evidence change | Compare request-boundary or evidence references for the same child. | Applicable operation/IF, CQ, TE, and projection dependencies receive the changed evidence/limitation. |
| T8-IMPACT-07 | Coverage definition or Product member/baseline change | Compare inventory definition revision or qualified Product membership snapshot. | Dependency-contract or Product-qualified impact is recorded; unaffected slices are preserved only when their bindings remain valid. |

All impact checks require explicit semantic acceptance and, when a fresh
document is requested, an explicit `RG-*`; impact accounting never regenerates
content automatically.

### Integrated authority, compatibility, Product, documentation, and harness gates

| Validation ID | Gate | Concrete check | Expected outcome |
|---|---|---|---|
| T8-EXTEND-01 | EXTEND targeting | Start from accepted surface-only STM and select detailed Provided/Consumed/API output. | Enrichment remains targeted in `resolved_work`; no capability selection, unrelated rebuild, or hidden full audit. |
| T8-AUTHORITY-01 | Authority ownership | Trace operation facts, coverage, API output, CQ/TE/CC references, and Product aggregation. | IF/STM and Technical Model Coverage remain factual/coverage authorities; projections and downstream modules cannot rewrite them. |
| T8-LIFECYCLE-01 | Lifecycle separation | Change operation membership/revision and inspect `VALID`, `REVALIDATION_REQUIRED`, `STALE`, and explicit `RG-*` routing. | History and freshness are preserved; prose, stale output, or impact analysis cannot promote or repair semantic state. |
| T8-COMPAT-01 | Backward compatibility | Load a historical surface-only IF without operation children. | It remains valid for surface-depth consumers with `UNASSESSED`/`UNKNOWN` inventory and is not retroactively rewritten or invalidated. |
| T8-SCOPE-01 | Single-project scope | Request detailed inventory for one Project and local baseline without Product mode. | Project/source qualification remains first-class; no synthetic Product or cross-project requirement is introduced. |
| T8-PRODUCT-01 | Product qualification | Request a bounded Product inventory with exact member bindings and immutable baseline. | Product composes qualified views only; it cannot flatten divergence or gain source, write, test, commit, push, deploy, or runtime authority. |
| T8-DOCS-01 | Human documentation | Search the named docs for operation rows, limitations, Architecture surface/detail distinction, API Report ownership, EXTEND, and complete-claim wording. | Docs describe operation-complete detailed outputs without turning human prose into normative authority or claiming all endpoints from Architecture `FULL`. |
| T8-HARNESS-01 | No harness | Inspect the final change set for a runtime scanner, renderer-private source reconstruction, automatic regeneration, Product requirement, or one-file-per-case harness. | `DO_NOT_BUILD_HARNESS`: only deterministic evidence tables and human docs are added. |

## Final integrated result

| Evidence group | Result |
|---|---|
| Design scenarios | `20/20 DETERMINISTIC` |
| Adversarial scenarios | `12/12 MAPPED` |
| Fail-first corrections | `6/6 CORRECTED` |
| Complete-claim guard | Five checks: reject missing/partial/unknown/stale/unmatched detail, allow exact accepted bounded scope, and allow Provided-only scope without hidden Consumed dependency. |
| Impact coverage | Seven checks: add, remove, identity, detail, auth, boundary/evidence, and definition/Product qualification changes. |
| EXTEND | Targeted operation-depth enrichment in `resolved_work`; no unrelated rerun or automatic regeneration. |
| Authority/lifecycle | IF/STM and Technical Model Coverage own facts/coverage; history and freshness remain separate. |
| Compatibility | Historical surface-only IFs remain valid as `UNASSESSED`/`UNKNOWN`; migration is `COMPATIBLE_EXTENSION`. |
| Product/single-project | Local Project scope remains first-class; Product remains qualified composition/view scope. |
| Documentation | Detailed outputs enumerate accounted operations and expose limitations; API Report remains the existing umbrella. |
| Harness | `DO_NOT_BUILD_HARNESS` |
