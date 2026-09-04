# Shared Technical Model Foundation validation

Candidate branch: `feature/stage-a-shared-technical-model`
Validated semantic head: `359e71cac37ca540e5b66ce2439d4db6c0c864f6`
Validation-record head: `PENDING — this documentation-only commit`
Implementation base: `10233b80eb6a46ff1f8d4348c4be890cf1d1f4a2`

## Validation mode and limitation

This repository contains Markdown Skill/reference contracts and pressure
scenarios, but no executable coordinator/runtime. Therefore PS-90..99 below
are static/contract verification, not runtime agent-pressure results. No
runtime behavior is claimed.

## RED-before-GREEN provenance

Task 1 recorded unchanged-baseline observations before production guidance
changes. Where static inspection could not prove the named failure, PS-92 and
PS-97 were corrected to `INCONCLUSIVE` in remediation commit `32a5cb0`.

## Stage A pressure results

| Scenario | Observed candidate result | Evidence mode |
|---|---|---|
| PS90 | `PS90_GREEN_PERSISTENT_STM_BOOTSTRAP` | static contract |
| PS91 | `PS91_GREEN_MODE_PROJECTION` | static contract |
| PS92 | `PS92_GREEN_FACT_INTERPRETATION_BOUNDARY` | static contract |
| PS93 | `PS93_GREEN_SHARED_EVIDENCE_LAYER` | static contract |
| PS94 | `PS94_GREEN_COVERAGE_SEPARATION` | static contract |
| PS95 | `PS95_GREEN_HYBRID_DEPENDENCY_GRAPH` | static contract |
| PS96 | `PS96_GREEN_STM_INCREMENTAL_REUSE` | static contract |
| PS97 | `PS97_GREEN_TECHNICAL_DOCUMENTATION_PROJECTION` | static contract |
| PS98 | `PS98_GREEN_AS_BUILT_PROJECTION_MIGRATION` | static contract |
| PS99 | `PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE` | static contract |

Each result was checked against the scenario's required contract and the
owning reference. The result does not substitute for fresh independent runtime
execution when a coordinator becomes available.

## Regression and integrity checks

- `git diff --check`: PASS for each implementation slice and final candidate.
- Existing Architecture Review and Test Engineering pressure scenarios: no
  executable runner is present; compatibility was checked by reference and
  terminology inspection.
- Authority map: STM, STM coverage, dependencies, evidence, Technical
  Documentation, Architecture Discovery, and Test Engineering ownership are
  routed to separate references.
- `STANDARD_FULL -> FULL/COMPACT` and `FORENSIC -> FULL/FORENSIC` are explicit;
  forensic upgrade is enrichment of the same model.
- `EXTEND`, `REVALIDATE`, legacy reconciliation, and `PROJECTION_REPAIR` are
  documented as minimum-slice/impact-driven behaviors.

## Remaining limitations

Runtime coordinator execution, generated-index regeneration, and Stage B
projection regeneration remain future work. The pressure matrix still needs
fresh runtime evidence once such an execution environment exists.

## Auditable static records

The following records are static contract validations. `run_id` identifies the
inspection record and is not a runtime claim.

```text
scenario_id: PS-90
run_id: static-ps90-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/shared-technical-model.md §7; references/technical-model-coverage.md §§4-5; SKILL.md Persistent Workflow
check_or_probe: rg persistent STM baseline, FULL/TARGETED and bounded NEW terms
expected_behavior: every NEW persists STM; bounded NEW builds only its required slice
observed_behavior: required statements present
violations: none
verdict: PS90_GREEN_PERSISTENT_STM_BOOTSTRAP

scenario_id: PS-91
run_id: static-ps91-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/technical-model-coverage.md §5; tests/pressure-scenario-91-architecture-mode-stm-projection.md
check_or_probe: rg STANDARD_FULL, FORENSIC, FULL/COMPACT, FULL/FORENSIC, enrichment
expected_behavior: one schema; standard FULL/COMPACT; forensic FULL/FORENSIC; no restart
observed_behavior: mapping and enrichment are explicit
violations: none
verdict: PS91_GREEN_MODE_PROJECTION

scenario_id: PS-92
run_id: static-ps92-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/shared-technical-model.md §5; SKILL.md Non-Negotiable Gates; tests/pressure-scenario-92-fact-interpretation-authority.md
check_or_probe: rg TECH_FACT_CANDIDATE, TECH_FACT_CONFLICT, TECH_FACT_REVALIDATION_REQUEST and sole-writer language
expected_behavior: capabilities propose/report/request; Technical Model Gate alone accepts facts
observed_behavior: sole-writer boundary present
violations: none
verdict: PS92_GREEN_FACT_INTERPRETATION_BOUNDARY

scenario_id: PS-93
run_id: static-ps93-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/shared-evidence-model.md; tests/pressure-scenario-93-shared-evidence-layer.md
check_or_probe: inspect WS/EV grouping, baseline binding, history, and bounded retrieval order
expected_behavior: shared worksets contain addressable historical observations
observed_behavior: multiple EV per WS and non-authority are explicit
violations: none
verdict: PS93_GREEN_SHARED_EVIDENCE_LAYER

scenario_id: PS-94
run_id: static-ps94-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/technical-model-coverage.md §§4-7; references/discovery-coverage.md §1; PS-94
check_or_probe: inspect ordered STM and Architecture coverage gates and distinct questions
expected_behavior: STM coverage precedes thematic discovery; neither gate substitutes
observed_behavior: separate tokens, owners, and sequence present
violations: none
verdict: PS94_GREEN_COVERAGE_SEPARATION

scenario_id: PS-95
run_id: static-ps95-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/technical-model-dependencies.md; PS-95
check_or_probe: inspect local direct dependencies, generated reverse index, selectors, and impact strengths
expected_behavior: owning metadata is authority; indexes are reconstructible projections
observed_behavior: hybrid model and impact vocabulary present
violations: none
verdict: PS95_GREEN_HYBRID_DEPENDENCY_GRAPH

scenario_id: PS-96
run_id: static-ps96-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/technical-model-dependencies.md §6; references/shared-technical-model.md §7; PS-96
check_or_probe: inspect minimum-slice reuse, stale revalidation, and forensic enrichment
expected_behavior: EXTEND/REVALIDATE impact-driven; forensic enriches one model
observed_behavior: required routing present
violations: none
verdict: PS96_GREEN_STM_INCREMENTAL_REUSE

scenario_id: PS-97
run_id: static-ps97-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: references/technical-documentation.md; references/report-contract.md; PS-97
check_or_probe: inspect STM source, non-authority, factual scope, and conflict routing
expected_behavior: Technical Documentation is a factual projection
observed_behavior: projection contract and excluded how-to scope present
violations: none
verdict: PS97_GREEN_TECHNICAL_DOCUMENTATION_PROJECTION

scenario_id: PS-98
run_id: static-ps98-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: SKILL.md; references/review-method.md §2; references/shared-technical-model.md §8; PS-98
check_or_probe: search active As-Built authority wording and inspect factual parity requirements
expected_behavior: STM factual authority; As-Built projection preserving material facts
observed_behavior: active contracts route conflicts through Technical Model Gate
violations: none
verdict: PS98_GREEN_AS_BUILT_PROJECTION_MIGRATION

scenario_id: PS-99
run_id: static-ps99-2026-09-04-01
candidate_head: 359e71cac37ca540e5b66ce2439d4db6c0c864f6
validation_type: STATIC_CONTRACT
execution_context: local feature worktree; coordinator unavailable
authoritative_files_inspected: capabilities/test-review/SKILL.md; test-engineering-contract.md; technical-model-coverage.md §4; PS-99
check_or_probe: inspect mandatory Test Engineering precondition across NEW, EXTEND, stale, fresh, and FULL cases
expected_behavior: derive slice, reuse/build/revalidate, Technical Model Gate, targeted acceptance, then Test Engineering
observed_behavior: mandatory predicate and branches present
violations: none
verdict: PS99_GREEN_LEGACY_AND_CROSS_CAPABILITY_REUSE; PS99_GREEN_TEST_ENGINEERING_STM_DEPENDENCY
```

## Named regression records

| Group | Scenarios/contracts | Expected invariant | Observed result | Limitation |
|---|---|---|---|---|
| Context/freshness | PS-39..43; `references/revalidation-and-freshness.md` | bounded expansion and projection repair | PASS, static inspection | runtime unavailable |
| Discovery/authority | PS-45..56; `references/discovery-coverage.md`, `review-method.md` | independent mechanism coverage and authority | PASS, static inspection | runtime unavailable |
| Umbrella | PS-57..64; `review-modes-and-orchestration.md` | capability registry and dependency slicing | PASS, static inspection | runtime unavailable |
| Session/projection | PS-65..80; `session-orchestration.md`, `report-contract.md` | bounded intents and projections | PASS, static inspection | runtime unavailable |
| Test Engineering | PS-79, PS-81..89; test-review contracts | BC/CC/MAT/TM/GAP ownership and four views | PASS, static inspection | runtime unavailable |

## STM-FR-003 disposition

```text
disposition: ACCEPTED_HISTORY_LIMITATION
reason: final branch contains all Technical Documentation authority dependencies;
  changing ancestry would require history rewrite without semantic benefit.
publication_requirement: before promotion, verify dependencies and relative links.
```

## Named legacy regression records

These are static/contract checks (`validation_type: STATIC_CONTRACT`) in the
local feature worktree. `observed_behavior` is recorded explicitly; no row is
an application-runtime claim.

| scenario_id | run_id | authoritative_files_inspected | check_or_probe | expected_behavior | observed_behavior | violations | verdict |
|---|---|---|---|---|---|---|---|
| PS-39 | static-ps39-2026-09-04-01 | `SKILL.md`; `references/session-orchestration.md` | inspect bounded initial read set | route from persisted state | contract present | none | PASS |
| PS-40 | static-ps40-2026-09-04-01 | `references/session-orchestration.md`; `references/revalidation-and-freshness.md` | inspect Context Envelope/expansion wording | expansion is reason-bound | contract present | none | PASS |
| PS-41 | static-ps41-2026-09-04-01 | `references/revalidation-and-freshness.md` | inspect projection fingerprint path | presentation repair preserves semantic fingerprint | contract present | none | PASS |
| PS-42 | static-ps42-2026-09-04-01 | `references/revalidation-and-freshness.md` | inspect stale owning revision handling | stale compact state is rejected | contract present | none | PASS |
| PS-43 | static-ps43-2026-09-04-01 | `references/review-method.md`; `references/session-orchestration.md` | inspect omitted-path expansion trigger | narrow review can request bounded expansion | contract present | none | PASS |
| PS-45 | static-ps45-2026-09-04-01 | `references/discovery-coverage.md` | inspect interpreter inventory/provenance | coverage distinguishes safe/unsafe/ambiguous | contract present | none | PASS |
| PS-46 | static-ps46-2026-09-04-01 | `references/discovery-coverage.md` | inspect auth/object-scope traces | authentication does not replace authorization | contract present | none | PASS |
| PS-47 | static-ps47-2026-09-04-01 | `references/discovery-coverage.md` | inspect outbound target/redirect trace | target control is evidence-bound | contract present | none | PASS |
| PS-48 | static-ps48-2026-09-04-01 | `references/discovery-coverage.md` | inspect cross-version root grouping | versions do not inflate roots | contract present | none | PASS |
| PS-49 | static-ps49-2026-09-04-01 | `references/discovery-coverage.md` | inspect secret propagation contract | storage does not prove propagation safety | contract present | none | PASS |
| PS-50 | static-ps50-2026-09-04-01 | `references/discovery-coverage.md` | inspect replay/order/idempotency trace | duplicate effects are material when evidenced | contract present | none | PASS |
| PS-51 | static-ps51-2026-09-04-01 | `references/discovery-coverage.md` | inspect raw-looking classification | safe constants are not inflated | contract present | none | PASS |
| PS-52 | static-ps52-2026-09-04-01 | `references/discovery-coverage.md` | inspect amplification/resource trace | exhaustion is distinguished from slowness | contract present | none | PASS |
| PS-53 | static-ps53-2026-09-04-01 | `references/discovery-coverage.md` | inspect conditional crypto/TLS coverage | absent mechanisms become evidence-backed N/A | contract present | none | PASS |
| PS-54 | static-ps54-2026-09-04-01 | `references/discovery-coverage.md`; `SKILL.md` | inspect coverage authority reconciliation | contradictory coverage blocks completion | contract present | none | PASS |
| PS-55 | static-ps55-2026-09-04-01 | `references/discovery-coverage.md` | inspect materiality/precision rules | findings count is not completeness | contract present | none | PASS |
| PS-56 | static-ps56-2026-09-04-01 | `references/discovery-coverage.md`; `references/revalidation-and-freshness.md` | inspect late correction impact | dependent artifacts stale without global restart | contract present | none | PASS |
| PS-57 | static-ps57-2026-09-04-01 | `references/review-modes-and-orchestration.md` | inspect capability registry/INDEX resume | later capability uses dependency slice | contract present | none | PASS |
| PS-58 | static-ps58-2026-09-04-01 | `references/revalidation-and-freshness.md` | inspect owning revision comparison | stale projection reconciles before dispatch | contract present | none | PASS |
| PS-59 | static-ps59-2026-09-04-01 | `references/shared-assurance-principles.md` | inspect authority conflict state | unresolved conflict remains explicit | contract present | none | PASS |
| PS-60 | static-ps60-2026-09-04-01 | `references/review-modes-and-orchestration.md` | inspect capability artifact ownership | Test Review owns detailed assurance evidence | contract present | none | PASS |
| PS-61 | static-ps61-2026-09-04-01 | `references/review-modes-and-orchestration.md` | inspect normal stack routing | stack addenda remain references | contract present | none | PASS |
| PS-62 | static-ps62-2026-09-04-01 | `references/review-modes-and-orchestration.md` | inspect routing/decision separation | routing context is not substantive evidence | contract present | none | PASS |
| PS-63 | static-ps63-2026-09-04-01 | `references/review-modes-and-orchestration.md` | inspect dependency-sliced dispatch | narrow context retains provenance | contract present | none | PASS |
| PS-64 | static-ps64-2026-09-04-01 | `references/review-modes-and-orchestration.md` | inspect asymmetric scope | claims do not exceed exercised scope | contract present | none | PASS |
| PS-65 | static-ps65-2026-09-04-01 | `references/session-orchestration.md` | inspect COMPLETE/same HEAD route | USE_EXISTING avoids substantive reread | contract present | none | PASS |
| PS-66 | static-ps66-2026-09-04-01 | `references/session-orchestration.md` | inspect legacy missing profile | metadata backfill does not open technical gates | contract present | none | PASS |
| PS-67 | static-ps67-2026-09-04-01 | `references/session-orchestration.md` | inspect small-diff route | targeted REVALIDATE only | contract present | none | PASS |
| PS-68 | static-ps68-2026-09-04-01 | `references/session-orchestration.md` | inspect IN_PROGRESS changed HEAD | RESUME reconciles before dependent gates | contract present | none | PASS |
| PS-69 | static-ps69-2026-09-04-01 | `references/session-orchestration.md` | inspect boundary-changing diff | affected boundaries only | contract present | none | PASS |
| PS-70 | static-ps70-2026-09-04-01 | `references/session-orchestration.md` | inspect omitted dependency trigger | CONTEXT_EXPANSION_REQUIRED is explicit | contract present | none | PASS |
| PS-71 | static-ps71-2026-09-04-01 | `references/session-orchestration.md` | inspect systemic-change route | full re-audit is not automatic | contract present | none | PASS |
| PS-72 | static-ps72-2026-09-04-01 | `references/revalidation-and-freshness.md` | inspect preservation wording | preserved evidence is not fresh verification | contract present | none | PASS |
| PS-73 | static-ps73-2026-09-04-01 | `references/session-orchestration.md` | inspect Test Review selection | selection remains visible | contract present | none | PASS |
| PS-74 | static-ps74-2026-09-04-01 | `references/session-orchestration.md` | inspect previous-audit choice | identity/status/lineage drive choice | contract present | none | PASS |
| PS-75 | static-ps75-2026-09-04-01 | `references/session-orchestration.md` | inspect dirty-tree handling | committed baseline is recommended | contract present | none | PASS |
| PS-76 | static-ps76-2026-09-04-01 | `references/session-orchestration.md` | inspect unavailable historical profile | limitation is explicit | contract present | none | PASS |
| PS-77 | static-ps77-2026-09-04-01 | `references/session-orchestration.md` | inspect profile reproducibility | collectors agree on canonical records | contract present | none | PASS |
| PS-78 | static-ps78-2026-09-04-01 | `tests/pressure-scenario-78-user-facing-language.md` | inspect language contract | user language and exact IDs coexist | contract present | none | PASS |
| PS-79 | static-ps79-2026-09-04-01 | `tests/pressure-scenario-79-test-assurance-summary.md`; test-review contracts | inspect assurance summary ownership | summary is projection of accepted evidence | contract present | none | PASS |
| PS-80 | static-ps80-2026-09-04-01 | `tests/pressure-scenario-80-projection-repair.md`; `references/revalidation-and-freshness.md` | inspect projection-only repair | repair does not change semantics | contract present | none | PASS |
| PS-81 | static-ps81-2026-09-04-01 | `capabilities/test-review/SKILL.md` | inspect behavior contract boundary | BC remains Test Engineering-owned | contract present | none | PASS |
| PS-82 | static-ps82-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect CC authority | CC remains contract-verification-owned | contract present | none | PASS |
| PS-83 | static-ps83-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect drift-vs-gap distinction | contract drift is not auto GAP | contract present | none | PASS |
| PS-84 | static-ps84-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect dependency slice | minimum upstream slice is reused | contract present | none | PASS |
| PS-85 | static-ps85-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect revalidation routing | changed views impact only dependent semantics | contract present | none | PASS |
| PS-86 | static-ps86-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect simulator boundary | simulator is not automatic | contract present | none | PASS |
| PS-87 | static-ps87-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect output persistence | outputs are independent fields | contract present | none | PASS |
| PS-88 | static-ps88-2026-09-04-01 | `capabilities/test-review/SKILL.md` | inspect NEW selection | output selection remains explicit | contract present | none | PASS |
| PS-89 | static-ps89-2026-09-04-01 | `capabilities/test-review/references/test-engineering-contract.md` | inspect EXTEND selection | extension remains minimum-slice | contract present | none | PASS |
