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
