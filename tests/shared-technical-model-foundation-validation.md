# Shared Technical Model Foundation validation

Candidate branch: `feature/stage-a-shared-technical-model`
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
