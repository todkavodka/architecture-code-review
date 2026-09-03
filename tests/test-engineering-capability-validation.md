# Test Engineering Capability — Validation

## Scope

This record validates the approved Test Engineering contract and its
compatibility with the existing Test Assurance capability. The repository is a
Markdown Skill and has no executable coordinator, collector, or capability
runtime; pressure verdicts below are therefore static/contract results unless
explicitly marked otherwise.

## RED-before-GREEN provenance

Commit `9dbf143` contains PS-81 through PS-86 before any Test Engineering
guidance change. Against the unchanged capability, the scenarios observed:

```text
PS81_RED_BEHAVIOR_IDENTITY_COLLAPSED
PS81_RED_EVIDENCE_EMBEDDED_IN_BC
PS82_RED_AUTOMATIC_CONTRACT_WINNER
PS82_RED_DRIFT_NORMALIZED_AWAY
PS83_RED_DRIFT_FORCED_TO_GAP
PS83_RED_GAP_HIDES_DRIFT
PS84_RED_LINEAR_PIPELINE_EXPANSION
PS84_RED_FULL_REVIEW_RESTART
PS85_RED_GLOBAL_REVALIDATION
PS85_RED_SERVICE_ONLY_FRESHNESS_MODEL
PS86_RED_SIMULATOR_BOUNDARIES_COLLAPSED
PS86_RED_CONTROL_PLANE_LEAKED
PS86_RED_E2E_ALWAYS_REQUIRES_SIMULATOR
```

The observations were contract-level absence/divergence checks, not fabricated
runtime results.

## Static/contract validation

```text
PS-79  PS79_GREEN_DECISION_SUMMARY
PS-81  PS81_GREEN_BEHAVIOR_BOUNDARY
PS-82  PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED
PS-83  PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP
PS-84  PS84_GREEN_MINIMUM_DEPENDENCY_SLICE
PS-85  PS85_GREEN_IMPACT_DRIVEN_REVALIDATION
PS-86  PS86_GREEN_SIMULATOR_E2E_BOUNDARIES
PS-87  PS87_GREEN_OUTPUT_SELECTION_PERSISTED
```

The static checks confirm:

- `00/01/02` compatibility is preserved;
- Behavior Model is not a user checkbox;
- Contract Verification is automatic when applicable and its report is optional;
- Behavior Model writes accepted `BC-*`, while Contract Verification writes `CC-*`;
- resolving `CC-*` cannot silently rewrite `BC-*`;
- `USE_EXISTING`, `EXTEND`, and `REVALIDATE` require/reuse the minimum fresh
  dependency slice;
- `PROJECTION_REPAIR` cannot alter BC/CC/MAT/TM/GAP semantics;
- dependency substitutes and Service Simulator planes remain distinct.
- persisted output selections distinguish Test Assurance-only, Test Plan, E2E,
  Simulator+E2E, and Contract Consistency Report combinations; legacy endpoints
  normalize without inferring optional outputs.
- `NEW` exposes direct independent Test Engineering output selection; legacy
  `REVIEW_ONLY` and `REVIEW_PLUS_TEST_PLAN` are reconciliation inputs only.

## Test Review-only compatibility canary

The contract still requires Test Assurance and preserves the existing summary
and map. Test Plan remains optional. Extended projections `03`–`08`, and the
Contract Consistency Report, are not silently enabled by selecting only Test
Assurance.

Static result: `PS79_GREEN_DECISION_SUMMARY` plus compatibility PASS.

## Application/coordinator runtime validation

No executable coordinator/capability runtime is present, so application-level
execution of PS-81 through PS-87 is not applicable in this repository.

Application/coordinator result: `NOT_APPLICABLE` — no executable coordinator,
collector, or capability runtime exists.

This limitation does not downgrade or upgrade the separately recorded fresh
agent Skill pressure results.

## Fresh independent Skill pressure validation

The following runs were performed after the capability guidance and Finding 1
remediation, in fresh independent Codex subagent contexts. They are agent-level
contract applications, not application/coordinator runtime tests. Only
observable summaries are retained.

### PS-81

```text
run_id: PS81-20260903-independent-01
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: PS-81 — Behavior Contract boundary
execution_context: fresh independent read-only Skill pressure run
observed_response_summary: BC-* was treated as independently verifiable behavior; BC was separated from MAT/RF/GAP/TM, ownership was assigned, and executable-evidence verdicts were kept outside BC.
expected_behavior: Preserve independent BC identity and keep evidence verdicts outside BC.
violations: none observed
verdict: PS81_GREEN_BEHAVIOR_BOUNDARY
```

### PS-82

```text
run_id: PS82-20260903-independent-pressure-01
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: PS-82 — Contract Verification authority
execution_context: fresh independent read-only Skill pressure run
observed_response_summary: DECLARED, IMPLEMENTED, CONSUMED, and TESTED were preserved as non-precedence views; CC-* and AUTHORITY_UNRESOLVED were retained.
expected_behavior: Preserve all four views and leave authority unresolved pending adjudication.
violations: none observed
verdict: PS82_GREEN_CONTRACT_AUTHORITY_PRESERVED
```

### PS-83

```text
run_id: PS83-independent-pressure-20260903-01
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: PS-83 — Contract drift versus assurance gap
execution_context: fresh independent read-only Skill pressure run
observed_response_summary: Case A retained CC-* without automatic GAP-*; Case B retained CC-* plus separate BC -> MAT -> TM/GAP accounting.
expected_behavior: Keep contract drift and assurance gaps orthogonal.
violations: none observed
verdict: PS83_GREEN_ORTHOGONAL_DRIFT_AND_GAP
```

### PS-84

```text
run_id: PS84-pressure-20260903-independent-01
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: PS-84 — Test Engineering minimum dependency slice
execution_context: fresh independent coordinator-level contract application; no application runtime required
observed_response_summary: E2E selected Test Assurance -> Behavior Model -> applicable Contract Verification -> E2E Design, adding Service Simulator Design only when topology requires it; EXTEND reused accepted fresh upstream work.
expected_behavior: Execute only the minimum dependency slice and avoid unrelated replay.
violations: none observed
verdict: PS84_GREEN_MINIMUM_DEPENDENCY_SLICE
```

### PS-85

```text
run_id: PS85-fresh-independent-pressure-run
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: PS-85 — Test Engineering impact-driven revalidation
execution_context: fresh independent coordinator-level contract application; no application runtime required
observed_response_summary: A tests-only -> TM/MAT/GAP; B implementation/OpenAPI -> IMPLEMENTED/DECLARED plus CC/BC analysis; C consumer-only -> CONSUMED plus consumer-facing simulator/E2E impact.
expected_behavior: Impact-driven routing without automatic BC invalidation or whole-package replay.
violations: none observed
verdict: PS85_GREEN_IMPACT_DRIVEN_REVALIDATION
```

### PS-86

```text
run_id: PS-86-pressure-20260903-independent-01
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: PS-86 — Service Simulator and E2E boundaries
execution_context: fresh independent read-only Skill pressure run
observed_response_summary: Dependency substitutes and Service Simulator roles were separated; consumer and test-only control planes remained distinct; E2E was topology-dependent.
expected_behavior: Preserve simulator boundaries and avoid requiring a simulator for every E2E design.
violations: none observed
verdict: PS86_GREEN_SIMULATOR_E2E_BOUNDARIES
```

### PS-87

```text
run_id: PS-87-fresh-independent-2026-09-03
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
scenario: output-selection persistence across five combinations, legacy normalization, RESUME, and EXTEND
execution_context: fresh independent read-only coordinator pressure run; no application runtime required
observed_response_summary: Independent mappings distinguished Assurance-only, Assurance+Test Plan, Assurance+E2E, Assurance+Simulator+E2E, and Assurance+Contract Consistency Report. Legacy endpoints normalized conservatively; RESUME reused selection and EXTEND added only requested outputs.
expected_behavior: Persist independent output booleans without inventing internal gates or optional outputs.
violations: none observed at the contract level
verdict: PS87_GREEN_OUTPUT_SELECTION_PERSISTED
```

### PS-88

```text
run_id: PS88-20260903-independent-red-01
feature_head: 37862d0d68d5d51ddd124ec9b962f97f4bce1f34
scenario: PS-88 — NEW Test Engineering output selection
execution_context: fresh independent read-only Skill pressure run against unchanged current Skill
observed_response_summary: NEW exposed `Capabilities → Test Review: OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN`; independent Test Engineering outputs were hidden. No internal-gate exposure or silent enablement was observed.
expected_behavior: NEW exposes Architecture Review separately from Test Engineering and allows independent output selection persisted directly as `outputs`; legacy endpoint values remain reconciliation-only.
violations: legacy NEW menu; output selection hidden
verdict: PS88_RED_LEGACY_NEW_MENU
```

After the startup guidance change, a fresh independent run observed:

```text
run_id: PS88-20260903-independent-green-01
feature_head: ec2c20bda0abf313c3e4bd3d0ee551d9bd47a7dc
scenario: PS-88 — NEW Test Engineering output selection
execution_context: fresh independent read-only Skill pressure run
observed_response_summary: Architecture Review and Test Engineering were separate; Test Engineering exposed OFF or independent outputs; selected outputs persisted directly; Behavior Model and Contract Verification remained internal; E2E did not force Service Simulator; legacy modes remained reconciliation-only.
expected_behavior: Allow independent Test Assurance, Test Environment Design, and E2E Test Plan selection with other optional outputs disabled.
violations: none
verdict: PS88_GREEN_NEW_OUTPUT_SELECTION
```

The first PS-84/PS-85 attempts stopped at static inspection; they were not
scored as final runs. The records above are the subsequent fixture-application
runs. No private chain-of-thought is retained.

Fresh Skill pressure result: PS-81 through PS-87 GREEN.

Fresh Test Assurance compatibility canary:

```text
run_id: compat-canary-2026-09-03-test-assurance-only-001
feature_head: 1da39f2fa14b8a8987754ef89d7c6ef2afac0f6b
execution_context: fresh independent read-only compatibility canary
observed_response_summary: Test Assurance remains required; 00 and 01 remain
capability-owned; 02 remains optional; legacy REVIEW_ONLY selects only Test
Assurance; outputs 03–08 and Contract Consistency Report are not forced.
verdict: PASS
```

Application/coordinator runtime result remains `NOT_APPLICABLE`: no executable
coordinator or capability runtime exists in this repository.
