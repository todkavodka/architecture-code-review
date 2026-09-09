# Menu Output Routing Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved requested-work/output routing model while
preserving the three semantic capabilities, all existing ownership and
authority boundaries, and compatible legacy interpretation.

**Architecture:** Session Orchestration records confirmed `requested_work`;
the coordinator separately resolves the minimum dependency/gate/projection
slice as `resolved_work`. Existing Technical Documentation, Product,
Test Engineering, Stage B, STM, Evidence, CC, authorization, and runtime
contracts remain the owning authorities.

**Tech Stack:** Markdown Skill/reference contracts, deterministic bounded
static inspection, Git.

**Spec:**
`docs/superpowers/specs/2026-09-09-menu-output-routing-remediation-design.md`

## Global constraints

- Exactly three semantic top-level capabilities remain selectable: `Architecture Review`, `Test Engineering`, and `Code Quality Review`.
- Validity is at least one selected capability OR at least one valid standalone output; Product context alone is invalid.
- `requested_work != resolved_work`; internal STM, Evidence, Behavior Model, Contract Verification, Product qualification, and projection dependencies never become selected capabilities.
- Capability-owned outputs retain their existing owners: Architecture Endpoint, Test Engineering, and Code Quality Review.
- `CANONICAL_PROJECTION_REQUEST`, `QUALIFIED_VIEW_REQUEST`, and `UMBRELLA_OUTPUT_REQUEST` are routing classes only, not capabilities, factual authorities, identities, or lifecycles.
- Technical Documentation is an umbrella that requires bounded output/subsection confirmation; exact outputs remain bounded.
- Provider / Consumer Matrix is Product-qualified over existing Technical Documentation projections, with no new `PRJ-*`, lifecycle, factual family, or compatibility authority.
- Generic compatibility routes directly through applicable Test Engineering Contract Verification and existing `CC-*`, independent of Matrix and Product; single-project applicability remains.
- Product context and output confirmation are separate; canonical output labels use `scope=PRODUCT` rather than duplicate Product identities.
- All six intents remain exact: `USE_EXISTING`, `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `PROJECTION_REPAIR`.
- Stage B projection lifecycle/freshness/regeneration, STM factual authority, Shared Evidence/redaction, CC authority, authorization separation, runtime unsupported boundary, single-project behavior, and Stage F factual boundaries remain unchanged.
- Migration is `COMPATIBLE_EXTENSION`; old sessions remain readable without historical package or `PRJ-*` rewrite.
- Validation is bounded static/manual inspection. `harness: DO_NOT_BUILD_HARNESS`; no pressure files, parser, DSL, runner, simulator, or framework.
- Before executing Block A/B/C, the executor MUST read this canonical plan and extract the block title, exact files, required semantic changes, verification, commit subject, and final review gate. If a later prompt conflicts: `STOP: IMPLEMENTATION_PROMPT_PLAN_MISMATCH`; THE CANONICAL PLAN WINS.

## Exact implementation file inventory

| Path | Action | Owner | Reason | Block |
|---|---|---|---|---|
| `SKILL.md` | MODIFY | Umbrella orchestration | Add pointer-level requested/resolved-plan routing and preserve boundaries without duplicating owning semantics. | B |
| `references/session-orchestration.md` | MODIFY | Session Orchestration | Add requested-work validity, canonical menu/output routing, normalization, confirmation, and exact conflict handling. | A |
| `references/review-modes-and-orchestration.md` | MODIFY | Review Modes / workflow state | Persist requested/resolved work and preserve six-intent and legacy behavior. | A |
| `references/technical-documentation.md` | MODIFY | Technical Documentation | Add direct Stage F/documentation routing, umbrella confirmation, qualified-view reuse, and limitation/redaction references. | B |
| `references/product-multi-project-review.md` | MODIFY | Product qualification/composition | Separate Product context from deliverable confirmation and define Product-qualified Matrix routing. | B |
| `capabilities/test-review/SKILL.md` | MODIFY | Test Engineering | Normalize direct Test Engineering outputs into existing owner/output state and preserve unsupported execution. | B |
| `capabilities/test-review/references/test-engineering-contract.md` | MODIFY | Test Engineering / CC | Decouple generic compatibility from Matrix/Product while retaining `CC-*` authority and Project applicability. | B |
| `tests/menu-output-routing-remediation-contract-validation.md` | CREATE | Integrated validation | Compact static projection for fail-first post-checks, routing, ownership, boundaries, and 48 acceptance rows; created in Block A, completed in Block C. | A/C |
| `tests/menu-output-routing-remediation-backward-compatibility.md` | CREATE | Integrated validation | Compact static projection for legacy interpretation, migration, and final compatibility evidence; created/completed in Block C. | C |

Totals:

```text
existing_files_modified_planned: 7
new_files_created_planned: 2
validation_files_planned: 2
pressure_files_planned: 0
harness: DO_NOT_BUILD_HARNESS
```

The two new files are integrated validation projections, not a harness. No
individual pressure files are planned.

## Authority and ownership boundaries

The implementation is additive and must preserve this map: Shared Evidence
owns observation/provenance/redaction; Shared Technical Model and Technical
Model Gate own accepted technical facts; Architecture Review owns
interpretation and Architecture Endpoint; Test Engineering owns test semantics,
Contract Verification, and `CC-*`; Code Quality Review owns `CQ-*`/`CQRA-*`;
Technical Documentation owns derived documentation and existing `PRJ-*`;
Product owns qualification/composition; Stage B owns projection lifecycle;
Session Orchestration and Review Modes own requested selection and routing.

No selection grants source-read, dirty-admission, semantic-write, test, code,
worktree, branch, commit, push, PR, deployment, runtime E2E, simulator,
environment, database-scan, SQL, tracing, or crawling permission.

## Block A — Requested Work & Session Orchestration

**Owns:** pre-change `FF-MENU-01` through `FF-MENU-07` evidence;
`requested_work` versus `resolved_work`; validity; capability-only,
output-only, and mixed requests; capability-owned normalization entry points;
`REQUESTED_WORK_CONFLICT`; all six intents; canonical labels; resolved-plan
confirmation; and legacy session interpretation where orchestration owns it.

**Files:** modify `references/session-orchestration.md` and
`references/review-modes-and-orchestration.md`; create
`tests/menu-output-routing-remediation-contract-validation.md` as the first
pre-change evidence container; read the approved design and the shared
authority/freshness references. No other file is modified in this block.

**Fail-first ordering is mandatory:**

1. Before any normative contract edit, create the validation projection with a
   section named `PRE-CHANGE BASELINE — IMMUTABLE`.
2. Capture exact current-contract citations and bounded static checks for
   `FF-MENU-01`..`FF-MENU-07`. The evidence must show the current
   capability-only validity contradiction, missing umbrella/subselection,
   Product/output ambiguity, missing requested/resolved separation, Matrix
   classification gap, compatibility coupling risk, and missing canonical
   requested-work layers.
3. Record the seven results as `FAIL_FIRST_VALID` with the current file path,
   section/table heading, exact command or inspected text, and expected gap.
   This section is immutable historical evidence: later steps may append
   post-change evidence but may not rewrite the baseline.
4. Only after steps 1–3, edit the normative contracts.

**Required normative changes:**

- Replace capability-only startup validity with “at least one selected
  capability OR at least one valid standalone output”; retain the exact three
  capabilities and all Architecture depth/endpoint combinations.
- Add the six canonical labels: `Session Intent`, `Scope Context`, `Review
  Capabilities`, `Requested Outputs`, `Resolved Plan / Required Internal Work`,
  and `Authorization / Execution Boundaries`.
- Persist `requested_work.capabilities`,
  `requested_work.standalone_outputs`, `requested_work.scope`, and
  `requested_work.confirmation_status`; keep dependencies under
  `resolved_work` only.
- Define `EXACT`, `BOUNDED_BUT_MULTI_OUTPUT`, and `AMBIGUOUS_BROAD`; exact
  outputs stay bounded and broad Technical Documentation requires explicit
  subsection confirmation.
- Define all six intent routes, including additive `EXTEND`, impact-driven
  `REVALIDATE`, persisted-scope `RESUME`, accepted/current-only
  `USE_EXISTING`, and presentation-only `PROJECTION_REPAIR` with semantic-drift
  escalation.
- Define exact `REQUESTED_WORK_CONFLICT` semantics: an explicit confirmed user
  selection has precedence over inferred natural-language normalization, but a
  material contradiction is never silently overwritten. When inferred work
  conflicts with an explicit confirmed selection, identify both choices, emit
  or request reconciliation as `REQUESTED_WORK_CONFLICT`, show the conflict,
  require confirmation of the resulting `requested_work`, persist neither a
  conflicting state nor a substantive work start until resolved, and do not
  change the explicit selection implicitly.

Required conflict examples:

| Explicit confirmed selection | Later inferred/requested wording | Required result |
|---|---|---|
| Architecture Endpoint = `REVIEW_ONLY` | “also build Target Architecture” | `REQUESTED_WORK_CONFLICT`; show explicit endpoint and inferred endpoint; reconcile and confirm; do not silently change Endpoint. |
| `REVIEW_PLUS_TARGET_ARCHITECTURE` | “do not generate Target Architecture” | `REQUESTED_WORK_CONFLICT`; show both; require confirmed resulting `requested_work`. |
| External Integrations Catalog only | “make all technical documentation” | Do not expand confirmed `requested_work`; reconcile/confirm any broader scope. |
| Product context selected, no requested work | no output/capability | Not `REQUESTED_WORK_CONFLICT`; invalid `NO_REVIEW_SCOPE_SELECTED`. |
| User-selected capabilities | Internal dependency closure differs | Not `REQUESTED_WORK_CONFLICT`; preserve `requested_work != resolved_work`. |
| Nothing confirmed; two materially ambiguous interpretations | ambiguous natural language | `REQUESTED_OUTPUT_AMBIGUOUS`, not conflict; present alternatives before work. |

**Concrete Block A checks:** use exact `rg` checks for the six labels, three
capabilities, validity table, `requested_work != resolved_work`, all six intent
tokens, and `REQUESTED_WORK_CONFLICT`; inspect the two endpoint examples and
the Product-context-only row in the named sections. Record these checks in the
validation projection. Run `git diff --check`.

**Block A execution checklist:**

- [ ] Read the approved design sections governing requested work, validity, normalization, session intents, confirmation, migration, and authority boundaries.
- [ ] Create the validation projection and capture immutable `FF-MENU-01`..`FF-MENU-07` evidence before the first normative edit.
- [ ] Modify both Block A contract files and append focused post-change checks; do not alter the baseline section.
- [ ] Confirm output-only, capability-only, mixed, Product-context-only, unsupported, ambiguous, and conflict routes.
- [ ] Run the exact checks above and `git diff --check`, then create Commit 1.

**Commit 1:**

```text
docs: implement requested-work session orchestration
```

The commit contains the two modified Block A contract files and the newly
created validation projection with its immutable pre-change section. No
independent review gate occurs here; perform the required local checks only.

## Block B — Documentation, Product & Compatibility Routing

**Owns:** standalone routing classes; Technical Documentation umbrella;
`EXACT` / `BOUNDED_BUT_MULTI_OUTPUT` / `AMBIGUOUS_BROAD`; Product context versus
output confirmation; Product-qualified routing; Provider / Consumer Matrix
qualified-view boundary; generic compatibility independent of Matrix/Product;
CC authority; single-project compatibility; capability-specific cross-
references; authorization/runtime/redaction boundary references.

**Files:** modify `SKILL.md`,
`references/technical-documentation.md`,
`references/product-multi-project-review.md`,
`capabilities/test-review/SKILL.md`, and
`capabilities/test-review/references/test-engineering-contract.md`; read the
Block A files plus shared Evidence, STM, and Stage B references.

**Required normative changes:**

- Preserve the approved 11-row output taxonomy and exact owning contracts for
  Technical Documentation, Provided Interfaces, Consumed Interfaces,
  Interface Catalog, Integration Map, Events / Messages, Data Access Map,
  Persistence / Data Resources, Migration Responsibility, External
  Integrations Catalog, and Provider / Consumer Matrix.
- Route exact outputs through existing projections/sections; route the
  Technical Documentation umbrella only after bounded subsection confirmation;
  preserve partial, unavailable, stale, unresolved, and inapplicable
  limitations.
- Keep Matrix a Product-qualified `QUALIFIED_VIEW_REQUEST` over existing
  interface/integration projections with `new_PRJ_identity=NO`,
  `new_lifecycle=NO`, `new_semantic_authority=NO`, and
  `compatibility_verdict=NOT_IMPLIED`; do not invent a Project Matrix route.
- Reuse canonical output identities with `scope=PRODUCT`; Product identity,
  accepted revision, immutable baseline, membership, availability, coverage,
  freshness, and limitations are separate from output confirmation.
- Normalize direct Test Plan, E2E Test Plan, simulator design/plan, Test
  Environment Design, Contract Consistency Report, and Test Assurance requests
  into existing Test Engineering ownership; planning/design remains
  non-executing. Preserve Code Quality and Architecture ownership pointers.
- Route generic compatibility as qualified inputs → applicable Contract
  Verification → existing `CC-*`, with no Matrix/Product prerequisite and with
  single-project applicability. Candidate matching is non-authoritative; Matrix
  may render accepted CC results but cannot create or adjudicate them.
- Keep `SKILL.md` as a pointer layer to these owners and restate the
  authorization, runtime, redaction, STM, Stage B, and factual boundaries by
  reference only.

**Concrete Block B checks:** run exact `rg` checks for each of the 11 canonical
labels, all three routing-class tokens, `scope=PRODUCT`, the four Matrix
prohibitions, the direct `CC-*` route, `matrix_scope != compatibility_scope`,
`SECRET`/`SENSITIVE_INTERNAL`/`SAFE_TECHNICAL_IDENTIFIER`, unsupported runtime
tokens, and no fourth capability. Inspect the Product broad/exact examples and
the single-project compatibility clause. Run `git diff --check`.

The 11 canonical routing rows are: `Technical Documentation` → umbrella;
`Provided Interfaces` → existing section 02; `Consumed Interfaces` → existing
section 03; `Interface Catalog` → existing sections 02/03; `Integration Map` →
existing section 04; `Events / Messages` → existing section 04;
`Data Access Map` → existing section 05; `Persistence / Data Resources` →
existing section 05; `Migration Responsibility` → existing section 05 and
`MIGRATION_AUTHORITY`; `External Integrations Catalog` → existing external
section 04/07 when applicable; and `Provider / Consumer Matrix` → Product-
qualified existing interface/integration projections only. For every row,
record routing class, owning contract, semantic owner, projection behavior,
confirmation requirement, Project/Product validity, and compatibility
implication in the validation projection.

**Block B execution checklist:**

- [ ] Read the approved design routing, Product, compatibility, authority, runtime, and redaction sections.
- [ ] Modify the five Block B contract files only, preserving existing facts, selectors, identities, lifecycle, and owners.
- [ ] Execute the 11-row routing inspection, Product confirmation examples, Matrix prohibitions, direct CC inspection, and boundary checks above.
- [ ] Run `git diff --check`, then create Commit 2.

**Commit 2:**

```text
docs: route documentation product and compatibility outputs
```

This commit contains exactly the five Block B contract files. No independent
review gate occurs here; local focused checks are required.

## Block C — Integrated Validation

**Owns:** post-change `FF-MENU-01`..`FF-MENU-07` verification; the 48/48
acceptance matrix; the 32/32 concrete pressure matrix; the 26/26 plan-pressure
matrix; backward compatibility; migration; authority boundaries; final
`git diff --check`; and implementation-ready-for-review evidence.

**Files:** complete
`tests/menu-output-routing-remediation-contract-validation.md` and create
`tests/menu-output-routing-remediation-backward-compatibility.md`; inspect all
seven modified contract files and the read-only authority references. No
normative contract file is modified in this block.

**Validation procedure:**

- Read the approved design acceptance rows M01–M20 and MR01–MR28, pressure
  rows MD-P01–MD-P32, and PF-MENU-01..26. Preserve the immutable Block A
  baseline, then append post-change evidence for all seven fail-first rows.
- Record exactly one acceptance row for each of 48 cases with ID, expected
  route, owning clause/file, exact command or bounded inspection, and result.
  Required result: `48 PASS`, `0 AMBIGUOUS`, `0 FAIL`.
- Record exactly one concrete pressure row for every MD-P ID using the matrix
  below. Required result: `32 PREVENTED`, `0 AMBIGUOUS`, `0 UNPREVENTED`.
- Record PF-MENU-01..26 as `PLAN_PREVENTS` with the exact block/clause/check
  that prevents each case. Required result: `26/26 PLAN_PREVENTS`.
- Record backward compatibility for old capability-only sessions, absent
  standalone-output defaults, Architecture Endpoint, Test Engineering
  booleans, Product sessions, `COMPLETE`/`USE_EXISTING`, `RESUME`, no package
  or `PRJ-*` rewrite, and `COMPATIBLE_EXTENSION`.
- Inspect both validation files for exact counts, no invented IDs, no
  placeholders, no authority claims, and `harness: DO_NOT_BUILD_HARNESS`.

**Block C execution checklist:**

- [ ] Append post-change evidence for all seven fail-first rows without changing the immutable baseline.
- [ ] Complete the 48 acceptance rows, 32 concrete pressure rows, and 26 plan-pressure rows below.
- [ ] Complete backward-compatibility and migration evidence, inspect both validation files, and run the final integrated checks.
- [ ] Run `git diff --check`, confirm the required final evidence, and create Commit 3.

### Acceptance coverage map — 48/48

The validation projection must contain one exact row for each ID below, with
the named owner and a command or bounded clause inspection. These IDs and
owners preserve the approved design matrix.

| IDs | Owning block/route |
|---|---|
| M01–M02 | Block A: Architecture/CQ capability-only startup |
| M03 | Block B: Test Engineering + Test Plan |
| M04–M05 | Block A: Architecture Endpoint depth/endpoint |
| M06–M09 | Block A: `USE_EXISTING`, `REVALIDATE`, `EXTEND`, `PROJECTION_REPAIR` |
| M10–M12 | Block B: Interface Catalog, Data Access Map, External Integrations Catalog |
| M13–M15 | Block B: Product exact/broad output confirmation |
| M16–M18 | Block B: unsupported E2E/simulator and direct compatibility |
| M19 | Block A/B: projection repair |
| M20 | Block A/B: zero-capability Interface Catalog |
| MR01–MR05 | Block B: standalone documentation sections 02/03/04/05/07 |
| MR06–MR07 | Block B: Product Matrix and separate CC route |
| MR08–MR10 | Block B/A: canonical Product output and invalid scope |
| MR11–MR13 | Block A/B: Test Plan, Target, Interface Catalog ownership |
| MR14–MR20 | Block A: dependency deduplication, intents, repair/escalation |
| MR21–MR24 | Block B/A: broad/exact Product confirmation and invalid context |
| MR25–MR28 | Block B: single-project/Product compatibility and unresolved Matrix pair |

Expanded acceptance IDs: `M01`, `M02`, `M03`, `M04`, `M05`, `M06`, `M07`,
`M08`, `M09`, `M10`, `M11`, `M12`, `M13`, `M14`, `M15`, `M16`, `M17`, `M18`,
`M19`, `M20`, `MR01`, `MR02`, `MR03`, `MR04`, `MR05`, `MR06`, `MR07`, `MR08`,
`MR09`, `MR10`, `MR11`, `MR12`, `MR13`, `MR14`, `MR15`, `MR16`, `MR17`,
`MR18`, `MR19`, `MR20`, `MR21`, `MR22`, `MR23`, `MR24`, `MR25`, `MR26`,
`MR27`, and `MR28`. The validation file must expand each ID to its exact
scenario text, expected route, owner, command/clause check, and PASS result;
the grouped table above is the ownership index, not a substitute for those
rows.

Required observable result: `acceptance: 48/48 PASS`.

### Plan-pressure coverage map — 26/26 PLAN_PREVENTS

| IDs | Exact prevention owner |
|---|---|
| PF-MENU-01–PF-MENU-03 | Block A/B validity and Technical Documentation routing |
| PF-MENU-04–PF-MENU-06 | Block A/B capability-owned normalization and Architecture/Test owners |
| PF-MENU-07–PF-MENU-10 | Block A/B Product exclusion, confirmation, umbrella, bounded outputs |
| PF-MENU-11–PF-MENU-16 | Block B Matrix/CC/Product/single-project boundaries |
| PF-MENU-17–PF-MENU-21 | Block A intent, extension, revalidation, and repair rules |
| PF-MENU-22–PF-MENU-26 | Block A/B authorization, runtime, migration, redaction, routing classes |

Each grouped row expands to every listed ID in the validation projection with
classification `PLAN_PREVENTS` and an exact cited clause/check; no grouped ID
may be omitted. Required observable result: `26/26 PLAN_PREVENTS`.

### Concrete design-pressure verification matrix

Each check is specific and must be executed against the named contract after
Blocks A and B. The expected observable result is the prevention state recorded
in the final validation projection.

| ID | Failure prevented | Owning normative clause/file | Concrete verification check | Expected observable result |
|---|---|---|---|---|
| MD-P01 | Zero-capability valid output rejected | requested-work validity / `references/session-orchestration.md` | `rg -n "at least one.*capability|valid standalone output|NO_REVIEW_SCOPE_SELECTED" references/session-orchestration.md` and inspect 0/0/output-only rows. | Output-only valid; only 0/0 is `NO_REVIEW_SCOPE_SELECTED`. |
| MD-P02 | Dependencies presented as selections | requested/resolved fields / `references/review-modes-and-orchestration.md` | `rg -n "requested_work|resolved_work|dependency_slice|never.*capabilit" references/review-modes-and-orchestration.md` and compare field tables. | Dependencies appear only under `resolved_work`. |
| MD-P03 | Target bypasses Architecture Endpoint | endpoint normalization / `references/session-orchestration.md` | `rg -n "Target Architecture|REVIEW_PLUS_TARGET_ARCHITECTURE|Architecture Endpoint" references/session-orchestration.md` and inspect the normalization row. | Target maps to the existing Architecture Endpoint. |
| MD-P04 | Test output gets a second owner | Test Engineering ownership / `capabilities/test-review/SKILL.md` | `rg -n "Test Plan|Test Assurance|capability-owned|existing.*boolean" capabilities/test-review/SKILL.md` and inspect owner table. | Every listed Test output remains Test Engineering-owned. |
| MD-P05 | Product context counts as work | Product exclusion / `references/session-orchestration.md` | `rg -n "Product context alone|NO_REVIEW_SCOPE_SELECTED|not requested work" references/session-orchestration.md` and inspect validity row. | Product-only context is invalid, not conflict. |
| MD-P06 | Product output gets duplicate identity | canonical Product output / `references/product-multi-project-review.md` | `rg -n "scope=PRODUCT|canonical output|duplicate.*identity|Product Interface Catalog" references/product-multi-project-review.md` and inspect exact-output example. | Canonical output plus Product scope is persisted. |
| MD-P07 | Matrix manufactures compatibility | Matrix/CC separation / `references/technical-documentation.md` | `rg -n "QUALIFIED_VIEW_REQUEST|compatibility_verdict=NOT_IMPLIED|no.*CC verdict" references/technical-documentation.md` and inspect Matrix row. | Matrix is view-only; no verdict is created. |
| MD-P08 | CC authority is displaced | CC authority / `capabilities/test-review/references/test-engineering-contract.md` | `rg -n "Contract Verification|CC-\\*|sole|semantic authority" capabilities/test-review/references/test-engineering-contract.md` and inspect compatibility route. | `CC-*` remains the sole adjudication authority. |
| MD-P09 | Multiple outputs escalate to full suite | minimum dependency union / `references/review-modes-and-orchestration.md` | `rg -n "minimum.*slice|dependency union|deduplicat|complete Review Suite" references/review-modes-and-orchestration.md` and inspect resolver rule. | Shared dependencies deduplicate without unrelated capabilities. |
| MD-P10 | Revalidation reopens everything | impact-driven revalidation / `references/review-modes-and-orchestration.md` | `rg -n "REVALIDATE|impacted|only.*slice|complete Review Suite" references/review-modes-and-orchestration.md` and inspect intent row. | Only impacted slices are revalidated. |
| MD-P11 | USE_EXISTING fabricates output | accepted/current gate / `references/review-modes-and-orchestration.md` | `rg -n "USE_EXISTING|accepted/current|missing.*EXTEND" references/review-modes-and-orchestration.md` and inspect intent table. | Missing output routes to `EXTEND`. |
| MD-P12 | RESUME silently broadens scope | persisted resume / `references/review-modes-and-orchestration.md` | `rg -n "RESUME|restores|without scope addition|persisted" references/review-modes-and-orchestration.md` and inspect resume rule. | Persisted scope is restored unchanged. |
| MD-P13 | EXTEND reopens unrelated work | additive extension / `references/review-modes-and-orchestration.md` | `rg -n "EXTEND|additive|unrelated|read-only" references/review-modes-and-orchestration.md` and inspect extension rule. | Only confirmed additions are offered. |
| MD-P14 | Projection repair hides semantic drift | repair escalation / `references/review-modes-and-orchestration.md` | `rg -n "PROJECTION_REPAIR|SEMANTIC_DRIFT_DETECTED|TECHNICAL_REVALIDATION_REQUIRED" references/review-modes-and-orchestration.md` and inspect repair rule. | Drift escalates; presentation repair cannot change facts. |
| MD-P15 | Planning request executes runtime | runtime boundary / `SKILL.md` | `rg -n "E2E|simulator|environment|database|SQL|tracing|crawling|does not execute" SKILL.md` and inspect boundary list. | Runtime execution remains unsupported. |
| MD-P16 | Selection grants authorization | authorization boundary / `SKILL.md` | `rg -n "no.*permission|source-read|semantic-write|commit|push|deploy" SKILL.md` and inspect authorization list. | Selection grants no listed permission. |
| MD-P17 | Legacy session gains new outputs | legacy defaults / `references/review-modes-and-orchestration.md` | `rg -n "absent.*standalone|defaults.*empty|legacy|historical" references/review-modes-and-orchestration.md` and inspect default rule. | Legacy outputs default empty; no silent enrichment. |
| MD-P18 | Alias creates new identity | alias normalization / `references/session-orchestration.md` | `rg -n "alias|canonical output|no new.*identity|normalization" references/session-orchestration.md` and inspect alias table. | Alias resolves to an existing canonical item. |
| MD-P19 | Explicit/inferred conflict silently overwrites | conflict reconciliation / `references/session-orchestration.md` | `rg -n "REQUESTED_WORK_CONFLICT|explicit.*confirmed|inferred|reconciliation|do not.*silently" references/session-orchestration.md` and inspect both endpoint examples. | Conflict is shown and confirmed before persistence/work; explicit choice is not silently changed. |
| MD-P20 | Sensitive facts render unsafely | redaction / `references/technical-documentation.md` | `rg -n "SECRET|SENSITIVE_INTERNAL|SAFE_TECHNICAL_IDENTIFIER|redact|omit" references/technical-documentation.md` and inspect rendering rule. | Secret omitted; sensitive value redacted/aliased. |
| MD-P21 | Routing classes collapse | class taxonomy / `references/technical-documentation.md` | `rg -n "CANONICAL_PROJECTION_REQUEST|QUALIFIED_VIEW_REQUEST|UMBRELLA_OUTPUT_REQUEST" references/technical-documentation.md` and inspect 11-row class column. | Classes remain distinct and orchestration-only. |
| MD-P22 | Matrix receives lifecycle | Matrix lifecycle prohibition / `references/technical-documentation.md` | `rg -n "new_PRJ_identity=NO|new_lifecycle=NO|no.*lifecycle" references/technical-documentation.md` and inspect Matrix route. | No Matrix identity or lifecycle is added. |
| MD-P23 | Umbrella silently selects all | umbrella confirmation / `references/technical-documentation.md` | `rg -n "Technical Documentation|bounded.*confirmation|never silently|subsection" references/technical-documentation.md` and inspect broad-request example. | Broad request pauses for bounded selection. |
| MD-P24 | Product context substitutes deliverable | separate confirmations / `references/product-multi-project-review.md` | `rg -n "Product context|output confirmation|separate|context.*alone" references/product-multi-project-review.md` and inspect two-step flow. | Both confirmations are separately required. |
| MD-P25 | Revision/baseline becomes output | Product qualification fields / `references/product-multi-project-review.md` | `rg -n "accepted revision|immutable.*baseline|deliverable|output scope" references/product-multi-project-review.md` and inspect confirmation payload. | Qualification state remains distinct from requested output. |
| MD-P26 | Exact output expands | bounded exact routing / `references/technical-documentation.md` | `rg -n "exact|bounded|never.*expand|Interface Catalog|Data Access Map" references/technical-documentation.md` and inspect exact route rows. | Only the confirmed sections/projections are selected. |
| MD-P27 | Project compatibility requires Product | Project CC applicability / `capabilities/test-review/references/test-engineering-contract.md` | `rg -n "Project|single-project|does not require Product|compatibility" capabilities/test-review/references/test-engineering-contract.md` and inspect applicability clause. | Valid Project compatibility routes without Product. |
| MD-P28 | Compatibility requires Matrix | direct CC route / `capabilities/test-review/references/test-engineering-contract.md` | `rg -n "direct|Contract Verification|Matrix.*not required|CC-\\*" capabilities/test-review/references/test-engineering-contract.md` and inspect route sequence. | Qualified inputs go directly to CC. |
| MD-P29 | Matrix becomes non-Product view | Product-qualified Matrix / `references/product-multi-project-review.md` | `rg -n "Provider / Consumer Matrix|Product-qualified|QUALIFIED_VIEW_REQUEST|Project.*Matrix" references/product-multi-project-review.md` and inspect scope row. | Matrix remains Product-qualified; no Project route is invented. |
| MD-P30 | Matrix renders a new verdict | render-only CC behavior / `capabilities/test-review/references/test-engineering-contract.md` | `rg -n "render|accepted CC|cannot create|candidate matching" capabilities/test-review/references/test-engineering-contract.md` and inspect combined route. | Matrix can render accepted CC only. |
| MD-P31 | Candidate matching is authoritative | candidate non-authority / `capabilities/test-review/references/test-engineering-contract.md` | `rg -n "candidate|non-authoritative|MATCH_CANDIDATE|compatibility result" capabilities/test-review/references/test-engineering-contract.md` and inspect state table. | Candidate states never become compatibility results. |
| MD-P32 | Product qualification owns CC | Product/CC boundary / `references/product-multi-project-review.md` | `rg -n "Product.*qualification|CC-\\*|compatibility authority|does not.*authority" references/product-multi-project-review.md` and inspect compatibility paragraph. | Product qualifies inputs; CC adjudicates. |

**Final integrated check:** confirm `FF-MENU-01..07` were captured before
normative edits and pass after changes; acceptance `48/48`; design pressure
`32/32` concrete and `0 AMBIGUOUS`; plan pressure `26/26 PLAN_PREVENTS`;
session intents `6/6`; migration `COMPATIBLE_EXTENSION`; design coverage
preserved; no placeholders; no normative contract was changed by this plan
task; and `git diff --check` passes.

**Commit 3:**

```text
docs: add integrated menu output routing validation
```

This commit contains the newly created backward-compatibility validation file
and the completed Block A validation projection. It is the last implementation
commit in the future implementation worktree.

## Commit and review strategy

Expected implementation commits: exactly 3, with subjects:

1. `docs: implement requested-work session orchestration`
2. `docs: route documentation product and compatibility outputs`
3. `docs: add integrated menu output routing validation`

Use one future implementation worktree only, created at execution time from
the future published approved plan checkpoint. Do not implement on `main`; do
not create a worktree now; do not create one branch/worktree per block.

After Block C, keep exactly one independent implementation review gate:

```text
IMPLEMENTATION_READY_FOR_REVIEW
```

The flow is approved plan checkpoint → one implementation worktree → Block A
→ Block B → Block C → one independent implementation review → targeted
remediation only if real findings → promotion. Block-local checks are not
independent reviews. No intermediate semantic checkpoints, push, merge,
promotion, PR, tag, or release is authorized by this plan.

## Required final evidence

```text
acceptance: 48/48 PASS
pressure: 32/32 PREVENTED
plan_pressure: 26/26 PLAN_PREVENTS
fail_first: 7/7 PRECHANGE
session_intents: 6/6 PASS
harness: DO_NOT_BUILD_HARNESS
migration: COMPATIBLE_EXTENSION
```

## Plan-only prohibitions

```text
normative_contracts_modified: NO (by this planning task)
implementation_performed: NO
implementation_branch_created: NO
worktree_created: NO
push_performed: NO
```
