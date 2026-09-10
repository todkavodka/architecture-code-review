# Menu Configuration Completion Validation

This artifact records the pre-change observations before the menu
configuration-completion remediation. The baseline is immutable; post-change
checks are appended after normative edits.

## PRE-CHANGE BASELINE

Baseline: 00f68b65bdd053de42c4de6921792aa931d5202e

| ID | Concrete contract inspection | Pre-change result |
|---|---|---|
| MENU-FF-01 | Inspect requested_work.confirmation_status and the Test Engineering output registry in references/session-orchestration.md and references/review-modes-and-orchestration.md. | FAIL / GAP PRESENT: top-level confirmation has no required TE configuration-completion state. |
| MENU-FF-02 | Inspect the Code Quality outputs registry and NEW transition in references/review-modes-and-orchestration.md. | FAIL / GAP PRESENT: CQ can be selected while output configuration has no completion gate. |
| MENU-FF-03 | Compare registry boolean examples with normative NEW selection rules for TE/CQ outputs. | FAIL / GAP PRESENT: UNSPECIFIED is not distinct from explicit false/NOT_SELECTED. |
| MENU-FF-04 | Compare requested_work.standalone_outputs with capability-owned outputs and the startup layer list. | FAIL / GAP PRESENT: separate fields exist, but separate completion phases are not required. |
| MENU-FF-05 | Search for a gate requiring all selected capability configurations and standalone selection to complete before confirmation_status=CONFIRMED. | FAIL / GAP PRESENT: no hard REQUESTED_WORK_CONFIGURATION_COMPLETE equivalent exists. |
| MENU-FF-06 | Compare Architecture required mode/endpoint registry fields with the top-level confirmation transition. | FAIL / AMBIGUOUS: fields are required, but shared configuration completion and confirmation are not explicit. |

Pre-change summary: 6/6 FAIL_FIRST_VALID.

## POST-CHANGE CHECKS

The following checks are appended after remediation and must demonstrate the
same six premises are closed, plus the NEW/EXTEND/RESUME/REVALIDATE matrices
and menu pressure controls defined by the remediation contract.

## POST-CHANGE CONTRACT CHECKS

| Check | Concrete verification | Expected result |
|---|---|---|
| MENU-01 | Search session orchestration for capability_configuration, configuration_status, and REQUESTED_WORK_CONFIGURATION_COMPLETE. | PASS: selected capabilities have an explicit completion state and hard final gate. |
| MENU-02 | Inspect NEW rules for Test Engineering outputs and the SELECTED/NOT_SELECTED/UNSPECIFIED terms. | PASS: Test Assurance is required; every optional output is explicitly resolved. |
| MENU-03 | Inspect NEW rules for Code Quality outputs and zero-projection confirmation. | PASS: all four outputs are explicit; zero projections require confirmation. |
| MENU-04 | Compare requested_work.standalone_outputs with capability_configuration and standalone_output_configuration. | PASS: standalone and capability-owned output selection are separate. |
| MENU-05 | Inspect the gate conditions connecting configuration_status=CONFIRMED to requested_work.confirmation_status=CONFIRMED. | PASS: incomplete configuration stops with REQUESTED_WORK_CONFIGURATION_INCOMPLETE. |
| MENU-06 | Inspect normalized-summary and Confirm/Change selection requirements. | PASS: summary includes scope, capabilities, capability outputs, standalone outputs, and read-only resolved work. |

## NEW MATRIX — 16/16 DETERMINISTIC

| ID | Concrete verification | Result |
|---|---|---|
| N01 | Architecture selected; inspect required Depth/Endpoint and configuration_status gate. | DETERMINISTIC |
| N02 | Test Engineering only; inspect required TE configuration and unresolved-output block. | DETERMINISTIC |
| N03 | Code Quality only; inspect four-output configuration and unresolved-output block. | DETERMINISTIC |
| N04 | All capabilities; inspect all selected capability statuses before final gate. | DETERMINISTIC |
| N05 | TE plus Test Plan; inspect required Test Assurance and all remaining explicit decisions. | DETERMINISTIC |
| N06 | CQ plus Summary; inspect Summary selected and remaining outputs explicit NOT_SELECTED. | DETERMINISTIC |
| N07 | Natural-language TE/CQ recognition; inspect both capabilities remain UNRESOLVED until confirmation. | DETERMINISTIC |
| N08 | Full review wording; inspect no implicit optional output selection. | DETERMINISTIC |
| N09 | Standalone External Integrations Catalog; inspect no capability config is required when none is selected. | DETERMINISTIC |
| N10 | Broad Technical Documentation; inspect bounded subsection confirmation. | DETERMINISTIC |
| N11 | Product context only; inspect no requested work result. | DETERMINISTIC |
| N12 | Nothing selected; inspect NO_REVIEW_SCOPE_SELECTED. | DETERMINISTIC |
| N13 | TE with explicit no optional outputs; inspect valid confirmed Test Assurance-only state. | DETERMINISTIC |
| N14 | CQ with explicit zero projections; inspect valid confirmed zero-projection state. | DETERMINISTIC |
| N15 | Architecture plus standalone output; inspect two separate confirmed configurations. | DETERMINISTIC |
| N16 | TE plus standalone Stage F output; inspect capability-owned and standalone states separately. | DETERMINISTIC |

## EXTEND MATRIX — 5/5 DETERMINISTIC

| ID | Concrete verification | Result |
|---|---|---|
| E01 | Add TE; inspect normal TE configuration before confirmation. | DETERMINISTIC |
| E02 | Add Test Plan to confirmed TE Assurance-only; inspect preserved state and addition only. | DETERMINISTIC |
| E03 | Add CQ Summary to confirmed Findings View; inspect union without reopening prior choice. | DETERMINISTIC |
| E04 | Add CQ capability; inspect CQ configuration before confirmation. | DETERMINISTIC |
| E05 | Add standalone Stage F output; inspect dependencies remain resolved work. | DETERMINISTIC |

## RESUME / REVALIDATE MATRIX — 8/8 DETERMINISTIC

| ID | Concrete verification | Result |
|---|---|---|
| R01 | Inspect persisted Architecture/TE/CQ configuration restoration. | DETERMINISTIC |
| R02 | Inspect completed state does not reopen configuration. | DETERMINISTIC |
| R03 | Inspect incomplete persisted state routes to reconciliation before continuation. | DETERMINISTIC |
| R04 | Inspect REVALIDATE preserves requested configuration. | DETERMINISTIC |
| R05 | Inspect dependency expansion does not add TE/CQ outputs. | DETERMINISTIC |
| R06 | Inspect legacy endpoint is absent from NEW/EXTEND menu. | DETERMINISTIC |
| R07 | Inspect legacy confirmed booleans remain readable as historical selection. | DETERMINISTIC |
| R08 | Inspect legacy incomplete state is not guessed and requires reconciliation. | DETERMINISTIC |

## MENU PRESSURE MATRIX — 12/12 PREVENTED

| ID | Failure prevented | Concrete verification | Result |
|---|---|---|---|
| P01 | TE false initialization bypasses menu | Inspect UNSPECIFIED initial state and hard gate. | PREVENTED |
| P02 | CQ false initialization bypasses menu | Inspect UNSPECIFIED initial state and hard gate. | PREVENTED |
| P03 | TE Test Plan leaves other choices untouched | Inspect no UNSPECIFIED output at confirmation. | PREVENTED |
| P04 | Natural-language CQ Summary defaults all others | Inspect explicit output resolution requirement. | PREVENTED |
| P05 | Standalone output bypasses unresolved capability | Inspect global gate requires every selected capability confirmed. | PREVENTED |
| P06 | Contract Verification appears user-selected | Inspect internal dependency boundary. | PREVENTED |
| P07 | STM/API dependencies appear selected | Inspect resolved_work separation. | PREVENTED |
| P08 | Full review enables all optional outputs | Inspect no implicit selection rule. | PREVENTED |
| P09 | RESUME loses explicit zero-output CQ decision | Inspect persisted confirmed configuration restoration. | PREVENTED |
| P10 | Legacy all-false state is guessed | Inspect legacy incomplete reconciliation rule. | PREVENTED |
| P11 | EXTEND drops CQ selection | Inspect monotonic union rule. | PREVENTED |
| P12 | Product context bypasses configuration | Inspect scope resolution is a gate condition. | PREVENTED |

## FINAL INTEGRATED RESULT

fail_first: 6/6 CAPTURED
menu_findings: MENU2-HIGH-001 RESOLVED; MENU2-MEDIUM-001 RESOLVED; MENU2-MEDIUM-002 RESOLVED
new_matrix: 16/16 DETERMINISTIC
extend_matrix: 5/5 DETERMINISTIC
resume_revalidate_matrix: 8/8 DETERMINISTIC
pressure: 12/12 PREVENTED
top_level_capabilities: 3
new_authority: NO
migration: COMPATIBLE_EXTENSION
harness: DO_NOT_BUILD_HARNESS
