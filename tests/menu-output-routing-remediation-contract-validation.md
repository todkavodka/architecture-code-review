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

## Block B focused evidence

| Check | Command/inspection | Result |
|---|---|---|
| 11 canonical outputs and routing classes | `rg -n "Technical Documentation|Provided Interfaces|Consumed Interfaces|Interface Catalog|Integration Map|Events / Messages|Data Access Map|Persistence / Data Resources|Migration Responsibility|External Integrations Catalog|Provider / Consumer Matrix|CANONICAL_PROJECTION_REQUEST|QUALIFIED_VIEW_REQUEST|UMBRELLA_OUTPUT_REQUEST" references/technical-documentation.md` | PASS; all 11 rows and required classes are present. |
| Matrix boundary | `rg -n "new_PRJ_identity=NO|new_lifecycle=NO|new_semantic_authority=NO|compatibility_verdict=NOT_IMPLIED|Product-only" references/technical-documentation.md references/product-multi-project-review.md` | PASS; Matrix is Product-qualified view only with no new identity/lifecycle/authority/verdict. |
| Product/output separation | `rg -n "Product context confirmation|requested output confirmation|scope=PRODUCT|AMBIGUOUS_BROAD" references/product-multi-project-review.md` | PASS; context, qualification, and deliverable confirmation are distinct. |
| Direct compatibility | `rg -n "qualified provider/consumer inputs|Contract Verification|CC-\\*|does not require Product or Matrix|single-project" capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md` | PASS; compatibility routes directly to applicable CC and remains Project-valid. |
| Ownership and runtime/redaction boundaries | `rg -n "Test Assurance|Behavior Model.*internal|planning/design outputs|does not.*execute|SECRET|SENSITIVE_INTERNAL|SAFE_TECHNICAL_IDENTIFIER" SKILL.md capabilities/test-review/SKILL.md references/technical-documentation.md` | PASS; existing owners, unsupported runtime, and redaction classes remain explicit. |

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

## Acceptance matrix — 48/48

| ID | Expected route/observable result | Concrete check | Result |
|---|---|---|---|
| M01 | `NEW` Architecture preserves depth/endpoint | `rg -n "STANDARD_FULL|FORENSIC|REVIEW_ONLY|REVIEW_PLUS_TARGET_ARCHITECTURE" references/session-orchestration.md` | PASS |
| M02 | CQ-only `NEW` remains independent | `rg -n "Code Quality Review|independent capability" references/session-orchestration.md` | PASS |
| M03 | Test Plan uses Test Engineering output state | `rg -n "Test Plan|Test Engineering capability|existing output" capabilities/test-review/SKILL.md` | PASS |
| M04 | Full review + Target uses Architecture Endpoint | `rg -n "Target Architecture|Architecture Endpoint|REVIEW_PLUS_TARGET_ARCHITECTURE" references/session-orchestration.md` | PASS |
| M05 | Forensic + Roadmap uses existing endpoint | `rg -n "FORENSIC|REVIEW_PLUS_TARGET_AND_ROADMAP|Roadmap" references/session-orchestration.md` | PASS |
| M06 | Accepted/current result uses `USE_EXISTING` | `rg -n "USE_EXISTING|accepted/current" references/review-modes-and-orchestration.md` | PASS |
| M07 | Changed source uses impact-driven `REVALIDATE` | `rg -n "REVALIDATE|impacted slices" references/review-modes-and-orchestration.md` | PASS |
| M08 | CQ addition uses additive `EXTEND` | `rg -n "EXTEND|additive" references/review-modes-and-orchestration.md` | PASS |
| M09 | Broken Mermaid uses `PROJECTION_REPAIR` | `rg -n "PROJECTION_REPAIR|semantic drift" references/review-modes-and-orchestration.md` | PASS |
| M10 | Interface request routes to Interface Catalog | `rg -n "Interface Catalog|sections 02 and 03" references/technical-documentation.md` | PASS |
| M11 | DB/table access routes to Data Access Map | `rg -n "Data Access Map|section 05" references/technical-documentation.md` | PASS |
| M12 | External integrations remains exact catalog | `rg -n "External Integrations Catalog|section 04" references/technical-documentation.md` | PASS |
| M13 | Product API map uses canonical output and Product scope | `rg -n "scope=PRODUCT|Interface Catalog" references/product-multi-project-review.md` | PASS |
| M14 | Product data/migration remains two bounded outputs | `rg -n "Data Access Map|Migration Responsibility|bounded" references/product-multi-project-review.md references/technical-documentation.md` | PASS |
| M15 | Broad Product everything confirms bounded set/limits | `rg -n "AMBIGUOUS_BROAD|bounded subsection|limitations" references/product-multi-project-review.md` | PASS |
| M16 | E2E execution unsupported; plan confirmable | `rg -n "E2E Test Plan|planning/design outputs|runtime" capabilities/test-review/SKILL.md` | PASS |
| M17 | Simulator runtime unsupported; design/plan confirmable | `rg -n "Service Simulator|no test.*runtime|planning/design" capabilities/test-review/SKILL.md` | PASS |
| M18 | Generic compatibility routes directly to CC | `rg -n "qualified provider/consumer inputs|Contract Verification|Matrix.*Product" capabilities/test-review/references/test-engineering-contract.md` | PASS |
| M19 | Formatting repair is projection-only | `rg -n "PROJECTION_REPAIR|presentation-only" references/review-modes-and-orchestration.md` | PASS |
| M20 | Interface Catalog works with zero capabilities | `rg -n "valid standalone output|zero outputs|Interface Catalog" references/session-orchestration.md` | PASS |
| MR01 | Technical Documentation confirms section scope | `rg -n "UMBRELLA_OUTPUT_REQUEST|subsection confirmation" references/technical-documentation.md` | PASS |
| MR02 | Interface Catalog selects only sections 02/03 | `rg -n "Interface Catalog.*sections 02 and 03" references/technical-documentation.md` | PASS |
| MR03 | Integration Map selects section 04 | `rg -n "Integration Map.*section 04" references/technical-documentation.md` | PASS |
| MR04 | Data Access Map selects section 05 | `rg -n "Data Access Map.*section 05" references/technical-documentation.md` | PASS |
| MR05 | External catalog selects approved external subsection | `rg -n "External Integrations Catalog.*section 04" references/technical-documentation.md` | PASS |
| MR06 | Product Matrix is qualified view with no CC/new PRJ | `rg -n "Provider / Consumer Matrix|QUALIFIED_VIEW_REQUEST|compatibility_verdict=NOT_IMPLIED" references/technical-documentation.md references/product-multi-project-review.md` | PASS |
| MR07 | Matrix + compatibility uses separate CC route | `rg -n "two separately owned routes|direct.*CC|Matrix.*cannot" capabilities/test-review/references/test-engineering-contract.md` | PASS |
| MR08 | Product Interface Catalog is canonical with Product scope | `rg -n "canonical output identity|scope=PRODUCT|Interface Catalog" references/product-multi-project-review.md` | PASS |
| MR09 | No capability/output is zero-scope | `rg -n "NO_REVIEW_SCOPE_SELECTED|at least one selected capability" references/session-orchestration.md` | PASS |
| MR10 | Product context only is invalid | `rg -n "Product context alone is not requested work|NO_REVIEW_SCOPE_SELECTED" references/session-orchestration.md references/product-multi-project-review.md` | PASS |
| MR11 | Direct Test Plan normalizes to Test Engineering | `rg -n "Test Plan.*normalize|Test Engineering capability" capabilities/test-review/SKILL.md` | PASS |
| MR12 | Direct Target normalizes to Architecture Endpoint | `rg -n "Target Architecture|Architecture Endpoint" references/session-orchestration.md` | PASS |
| MR13 | Interface Catalog does not select Architecture | `rg -n "standalone output|three semantic capabilities|Interface Catalog" references/session-orchestration.md` | PASS |
| MR14 | Multiple outputs deduplicate dependencies | `rg -n "deduplicated minimum dependency union|dependency_slice" references/review-modes-and-orchestration.md` | PASS |
| MR15 | EXTEND adds Data Access Map without reopening Architecture | `rg -n "EXTEND.*additive|unrelated|Data Access Map" references/review-modes-and-orchestration.md` | PASS |
| MR16 | REVALIDATE impacts only affected slices | `rg -n "REVALIDATE.*only impacted slices" references/review-modes-and-orchestration.md` | PASS |
| MR17 | RESUME restores requested/resolved state | `rg -n "RESUME.*restores persisted requested and resolved" references/review-modes-and-orchestration.md` | PASS |
| MR18 | Missing USE_EXISTING routes to EXTEND | `rg -n "missing or new output.*EXTEND" references/review-modes-and-orchestration.md` | PASS |
| MR19 | Formatting repair is projection-only | `rg -n "PROJECTION_REPAIR.*presentation-only" references/review-modes-and-orchestration.md` | PASS |
| MR20 | Semantic correction escalates | `rg -n "SEMANTIC_DRIFT_DETECTED|TECHNICAL_REVALIDATION_REQUIRED" references/review-modes-and-orchestration.md` | PASS |
| MR21 | Broad Product documentation confirms scope | `rg -n "Broad Product|AMBIGUOUS_BROAD|bounded subsection" references/product-multi-project-review.md` | PASS |
| MR22 | Exact Product external integrations bounded | `rg -n "External Integrations Catalog|Exact and bounded" references/technical-documentation.md` | PASS |
| MR23 | Product API + DB confirms only two candidates | `rg -n "Interface Catalog|Data Access Map|BOUNDED_BUT_MULTI_OUTPUT" references/technical-documentation.md` | PASS |
| MR24 | Product context without work invalid | `rg -n "Product context alone is not requested work" references/product-multi-project-review.md` | PASS |
| MR25 | Single-project CC remains applicable | `rg -n "single-project.*applicable|independent.*Product" capabilities/test-review/references/test-engineering-contract.md` | PASS |
| MR26 | Product compatibility does not select Matrix | `rg -n "does not require Product or Matrix" capabilities/test-review/references/test-engineering-contract.md` | PASS |
| MR27 | Matrix absence does not block CC | `rg -n "Matrix availability never blocks" capabilities/test-review/references/test-engineering-contract.md` | PASS |
| MR28 | Unresolved pair preserves CC unresolved state | `rg -n "MATCHING_INDETERMINATE|cannot create.*compatibility" capabilities/test-review/references/test-engineering-contract.md` | PASS |

acceptance_total: 48
acceptance_pass: 48
acceptance_ambiguous: 0
acceptance_fail: 0

## Concrete pressure matrix — 32/32

The plan’s 32-row matrix is executed here against the final contracts. Each
row has one concrete command/inspection and one observable prevention result.

| ID | Owning file/clause | Concrete check | Expected result |
|---|---|---|---|
| MD-P01 | `references/session-orchestration.md` validity | `rg -n "valid standalone output|NO_REVIEW_SCOPE_SELECTED" references/session-orchestration.md` | Output-only valid; 0/0 invalid. |
| MD-P02 | `references/review-modes-and-orchestration.md` state | `rg -n "requested_work|resolved_work|dependency_slice" references/review-modes-and-orchestration.md` | Dependency is resolved work only. |
| MD-P03 | `references/session-orchestration.md` endpoint | `rg -n "Target Architecture|REVIEW_PLUS_TARGET_ARCHITECTURE|Architecture Endpoint" references/session-orchestration.md` | Target remains Endpoint-owned. |
| MD-P04 | `capabilities/test-review/SKILL.md` ownership | `rg -n "Test Plan|Test Assurance|Test Engineering capability" capabilities/test-review/SKILL.md` | Test outputs have one owner. |
| MD-P05 | session validity | `rg -n "Product context alone|NO_REVIEW_SCOPE_SELECTED" references/session-orchestration.md` | Product-only context is invalid. |
| MD-P06 | Product canonical output | `rg -n "scope=PRODUCT|canonical output identity" references/product-multi-project-review.md` | No duplicate Product identity. |
| MD-P07 | Matrix/CC boundary | `rg -n "QUALIFIED_VIEW_REQUEST|compatibility_verdict=NOT_IMPLIED" references/technical-documentation.md` | Matrix cannot create verdict. |
| MD-P08 | CC authority | `rg -n "CC-\*.*sole|sole owner" capabilities/test-review/references/test-engineering-contract.md` | CC remains authority. |
| MD-P09 | dependency union | `rg -n "deduplicated minimum dependency union" references/review-modes-and-orchestration.md` | No full-suite escalation. |
| MD-P10 | impact revalidation | `rg -n "REVALIDATE.*only impacted slices" references/review-modes-and-orchestration.md` | Only impacted slices revalidate. |
| MD-P11 | USE_EXISTING | `rg -n "USE_EXISTING.*accepted/current|missing.*EXTEND" references/review-modes-and-orchestration.md` | Missing output cannot be fabricated. |
| MD-P12 | RESUME | `rg -n "RESUME.*restores persisted.*without" references/review-modes-and-orchestration.md` | Resume does not broaden scope. |
| MD-P13 | EXTEND | `rg -n "EXTEND.*additive|unrelated" references/review-modes-and-orchestration.md` | Extension is bounded. |
| MD-P14 | repair escalation | `rg -n "PROJECTION_REPAIR|SEMANTIC_DRIFT_DETECTED" references/review-modes-and-orchestration.md` | Drift escalates. |
| MD-P15 | runtime boundary | `rg -n "does not execute|E2E|simulator|database-scan" SKILL.md capabilities/test-review/SKILL.md` | Runtime remains unsupported. |
| MD-P16 | authorization boundary | `rg -n "no source-read|no.*permission|commit|push" SKILL.md` | Selection grants no permission. |
| MD-P17 | legacy defaults | `rg -n "standalone-output state|empty.*standalone|legacy" references/review-modes-and-orchestration.md` | Legacy state is not enriched. |
| MD-P18 | alias normalization | `rg -n "canonical output|normalization" references/session-orchestration.md` | Alias maps to existing identity. |
| MD-P19 | conflict route | `rg -n "REQUESTED_WORK_CONFLICT|explicit confirmed|inferred|substantive work" references/session-orchestration.md` | Conflict shown and confirmed before work. |
| MD-P20 | redaction | `rg -n "SECRET|SENSITIVE_INTERNAL|SAFE_TECHNICAL_IDENTIFIER" references/technical-documentation.md` | Sensitive data is omitted/redacted. |
| MD-P21 | class distinction | `rg -n "CANONICAL_PROJECTION_REQUEST|QUALIFIED_VIEW_REQUEST|UMBRELLA_OUTPUT_REQUEST" references/technical-documentation.md` | Classes remain distinct. |
| MD-P22 | Matrix lifecycle | `rg -n "new_PRJ_identity=NO|new_lifecycle=NO" references/technical-documentation.md` | No Matrix lifecycle/identity. |
| MD-P23 | umbrella confirmation | `rg -n "UMBRELLA_OUTPUT_REQUEST|subsection confirmation|never silently" references/technical-documentation.md` | Broad request waits for scope. |
| MD-P24 | Product confirmation | `rg -n "Product context confirmation|requested output confirmation|separate" references/product-multi-project-review.md` | Context and output are separate. |
| MD-P25 | revision/baseline distinction | `rg -n "accepted revision|immutable baseline|output scope" references/product-multi-project-review.md` | Qualification is not deliverable. |
| MD-P26 | exact bounded route | `rg -n "Exact output selects|Exact and bounded" references/technical-documentation.md` | Exact output does not expand. |
| MD-P27 | Project compatibility | `rg -n "single-project|does not require Product" capabilities/test-review/references/test-engineering-contract.md` | Project CC works without Product. |
| MD-P28 | direct CC | `rg -n "qualified provider/consumer inputs|Contract Verification|Matrix" capabilities/test-review/references/test-engineering-contract.md` | CC route bypasses Matrix. |
| MD-P29 | Product Matrix | `rg -n "Product-qualified.*QUALIFIED_VIEW_REQUEST|no standalone Project" references/technical-documentation.md` | Matrix remains Product-qualified. |
| MD-P30 | render-only CC | `rg -n "render-only|cannot create or adjudicate" capabilities/test-review/references/test-engineering-contract.md` | Matrix renders accepted CC only. |
| MD-P31 | candidate authority | `rg -n "MATCH_CANDIDATE|non-authoritative" capabilities/test-review/references/test-engineering-contract.md` | Candidates never become verdicts. |
| MD-P32 | Product/CC authority | `rg -n "Product.*qualif|does not become compatibility authority|CC-\*" references/product-multi-project-review.md capabilities/test-review/references/test-engineering-contract.md` | Product qualifies; CC adjudicates. |

pressure_total: 32
pressure_prevented: 32
pressure_ambiguous: 0
pressure_allows_failure: 0

## Plan-pressure matrix — 26/26 PLAN_PREVENTS

| ID | Exact prevention check | Result |
|---|---|---|
| PF-MENU-01 | Inspect Block A validity predicate for capability OR valid standalone output. | PLAN_PREVENTS |
| PF-MENU-02 | Inspect `requested_work`/`resolved_work` fields and dependency-only rule. | PLAN_PREVENTS |
| PF-MENU-03 | Inspect Technical Documentation as routing output, not capability. | PLAN_PREVENTS |
| PF-MENU-04 | Inspect capability-owned normalization in Blocks A/B. | PLAN_PREVENTS |
| PF-MENU-05 | Inspect Target → Architecture Endpoint route. | PLAN_PREVENTS |
| PF-MENU-06 | Inspect Test Plan → Test Engineering route. | PLAN_PREVENTS |
| PF-MENU-07 | Inspect Product-context exclusion from validity. | PLAN_PREVENTS |
| PF-MENU-08 | Inspect separate Product context/output confirmation. | PLAN_PREVENTS |
| PF-MENU-09 | Inspect umbrella bounded subsection confirmation. | PLAN_PREVENTS |
| PF-MENU-10 | Inspect exact output boundedness. | PLAN_PREVENTS |
| PF-MENU-11 | Inspect Matrix no-new-PRJ/lifecycle rule. | PLAN_PREVENTS |
| PF-MENU-12 | Inspect compatibility route independent of Matrix. | PLAN_PREVENTS |
| PF-MENU-13 | Inspect compatibility route independent of Product. | PLAN_PREVENTS |
| PF-MENU-14 | Inspect candidate matching non-authority. | PLAN_PREVENTS |
| PF-MENU-15 | Inspect Matrix cannot manufacture CC verdict. | PLAN_PREVENTS |
| PF-MENU-16 | Inspect single-project CC applicability. | PLAN_PREVENTS |
| PF-MENU-17 | Inspect `USE_EXISTING` accepted/current requirement. | PLAN_PREVENTS |
| PF-MENU-18 | Inspect `RESUME` persisted-scope rule. | PLAN_PREVENTS |
| PF-MENU-19 | Inspect additive bounded `EXTEND`. | PLAN_PREVENTS |
| PF-MENU-20 | Inspect impact-driven `REVALIDATE`. | PLAN_PREVENTS |
| PF-MENU-21 | Inspect projection-repair semantic-drift escalation. | PLAN_PREVENTS |
| PF-MENU-22 | Inspect selection/authorization separation. | PLAN_PREVENTS |
| PF-MENU-23 | Inspect unsupported runtime boundary. | PLAN_PREVENTS |
| PF-MENU-24 | Inspect additive legacy interpretation/no destructive migration. | PLAN_PREVENTS |
| PF-MENU-25 | Inspect Evidence redaction preservation. | PLAN_PREVENTS |
| PF-MENU-26 | Inspect routing classes remain orchestration-only. | PLAN_PREVENTS |

plan_pressure_total: 26
plan_pressure_prevents: 26
plan_pressure_ambiguous: 0
plan_pressure_allows_failure: 0
