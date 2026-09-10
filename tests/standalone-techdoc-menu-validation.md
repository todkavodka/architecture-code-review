# Standalone Technical Documentation Menu Validation

The pre-change section is immutable historical evidence captured at baseline
682f671996dc00cf64951b03362c9d6ab8d6dc69 before normative edits.

## PRE-CHANGE BASELINE

| ID | Concrete contract inspection | Pre-change result |
|---|---|---|
| TD-MENU-FF-01 | Inspect the NEW menu in Session Orchestration and the final requested-work gate after all three capabilities are configured. | GAP PRESENT: the menu shows capabilities but no required standalone-output configuration phase. |
| TD-MENU-FF-02 | Compare requested_work.standalone_outputs with standalone-output completion state and final summary requirements. | GAP PRESENT: empty standalone_outputs is not distinguished from never shown/unresolved. |
| TD-MENU-FF-03 | Search Technical Documentation routing for API Report and compare with named existing projections. | GAP PRESENT: API Report has no deterministic bounded normalization. |
| TD-MENU-FF-04 | Search NEW/full-review normalization and standalone-output rules. | GAP PRESENT: full review has no explicit standalone-output axis rule. |

Pre-change summary: 4/4 FAIL_FIRST_VALID.

## POST-CHANGE CHECKS

| Check | Concrete verification | Expected result |
|---|---|---|
| TD-MENU-01 | Inspect NEW startup layers for Standalone Outputs / Technical Documentation after capability configuration and before final confirmation. | PASS: standalone step is ALWAYS_SHOW. |
| TD-MENU-02 | Inspect standalone_output_configuration status, selection, explicit_none, and final gate. | PASS: empty unresolved state differs from confirmed NONE. |
| TD-MENU-03 | Inspect API Report normalization and persisted identities. | PASS: bounded existing projections only; no API identity. |
| TD-MENU-04 | Inspect full-review rule and all-three-capability rule. | PASS: neither silently selects standalone outputs. |

## NEW MATRIX — 12/12 DETERMINISTIC

| ID | Concrete verification | Result |
|---|---|---|
| S01 | Inspect always-shown standalone step after Architecture configuration and explicit NONE path. | DETERMINISTIC |
| S02 | Inspect global gate requires standalone status CONFIRMED after all capability outputs. | DETERMINISTIC |
| S03 | Inspect API Report candidate set and confirmation path. | DETERMINISTIC |
| S04 | Inspect API Report output-only normalization with no capability required. | DETERMINISTIC |
| S05 | Inspect Provided Interfaces exact standalone route. | DETERMINISTIC |
| S06 | Inspect bounded Provided/Consumed/Integrations selection. | DETERMINISTIC |
| S07 | Inspect all-applicable documentation preselection still requires confirmation. | DETERMINISTIC |
| S08 | Inspect full review does not imply standalone outputs. | DETERMINISTIC |
| S09 | Inspect TE, CQ, and standalone axes remain separate. | DETERMINISTIC |
| S10 | Inspect standalone Technical Documentation validity without capability. | DETERMINISTIC |
| S11 | Inspect Product-qualified standalone route without capability selection. | DETERMINISTIC |
| S12 | Inspect Product-only request remains invalid. | DETERMINISTIC |

## EXTEND MATRIX — 5/5 DETERMINISTIC

| ID | Concrete verification | Result |
|---|---|---|
| E01 | Add Provided Interfaces with minimum dependencies only. | DETERMINISTIC |
| E02 | Add Consumed Interfaces and Integrations additively. | DETERMINISTIC |
| E03 | Add API Report as standalone sections without reopening capabilities. | DETERMINISTIC |
| E04 | Add Code Quality with its own submenu to a standalone package. | DETERMINISTIC |
| E05 | Add Auth and Trust as standalone projection with dependencies. | DETERMINISTIC |

## RESUME / REVALIDATE MATRIX — 6/6 DETERMINISTIC

| ID | Concrete verification | Result |
|---|---|---|
| R01 | Restore exact confirmed standalone selection. | DETERMINISTIC |
| R02 | Restore explicit NONE as NONE. | DETERMINISTIC |
| R03 | Reconcile legacy empty state without completion evidence. | DETERMINISTIC |
| R04 | Preserve standalone selection through REVALIDATE. | DETERMINISTIC |
| R05 | Do not add outputs from projection freshness changes. | DETERMINISTIC |
| R06 | Keep regeneration separate from requested-output selection. | DETERMINISTIC |

## PRESSURE MATRIX — 12/12 PREVENTED

| ID | Concrete verification | Result |
|---|---|---|
| P01 | Unshown standalone step blocks global confirmation. | PREVENTED |
| P02 | Empty selection without marker remains UNRESOLVED. | PREVENTED |
| P03 | Explicit NONE with CONFIRMED status is valid. | PREVENTED |
| P04 | Unconfirmed API Report candidate set remains unresolved. | PREVENTED |
| P05 | API Report creates no API or PRJ identity. | PREVENTED |
| P06 | Full review does not enable Technical Documentation. | PREVENTED |
| P07 | Capability outputs do not enable standalone outputs. | PREVENTED |
| P08 | Resolved dependencies do not populate selected outputs. | PREVENTED |
| P09 | Provided Interfaces dependencies remain internal. | PREVENTED |
| P10 | Standalone-only request does not select Architecture. | PREVENTED |
| P11 | Product mode cannot bypass standalone confirmation. | PREVENTED |
| P12 | Legacy empty array is not inferred as explicit NONE. | PREVENTED |

## RESULTS

fail_first: 4/4 CAPTURED
menu_findings: TD-MENU-MEDIUM-001 RESOLVED; TD-MENU-MEDIUM-002 RESOLVED; TD-MENU-MEDIUM-003 RESOLVED; TD-MENU-MEDIUM-004 RESOLVED
standalone_discovery: ALWAYS_SHOW
api_report: UMBRELLA_WITH_CONFIRMATION
NEW: 12/12 DETERMINISTIC
EXTEND: 5/5 DETERMINISTIC
RESUME/REVALIDATE: 6/6 DETERMINISTIC
pressure: 12/12 PREVENTED
top_level_capabilities: 3
new_api_identity: NO
new_semantic_authority: NO
migration: COMPATIBLE_EXTENSION
harness: DO_NOT_BUILD_HARNESS
