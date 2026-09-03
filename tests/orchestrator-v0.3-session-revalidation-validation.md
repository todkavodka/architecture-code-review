# Orchestrator v0.3 validation record

## Provenance

- candidate branch: `feature/orchestrator-v0.3-session-revalidation`
- candidate guidance HEAD before this record: `82d5fa5f31f06826c8f0de3f699ea9bfc62a96d6`
- verified base: `6076074ba3783f1ad1584d095b711c78c3957b25`
- merge-base: `6076074ba3783f1ad1584d095b711c78c3957b25`
- current `origin/main`: `6076074ba3783f1ad1584d095b711c78c3957b25`
- changed files before this record: approved design/plan documents, `SKILL.md`, `README.md`, session/revalidation references, and pressure-contract files

## Fail-first baseline observations

These observations were run in fresh independent Codex contexts against the
pre-v0.3 production Skill. The repository has no executable coordinator or
scenario harness, so static reasoning was not converted into runtime GREEN.

| Scenario | Baseline observation | Verdict | Runs |
|---|---|---|---:|
| PS-65 | Existing resume/capability mechanics exist, but no explicit `USE_EXISTING` startup token; runtime behavior could not be established. | `PS-65_INCONCLUSIVE` | 1 |
| PS-66 | Projection-only metadata backfill can avoid reopening technical gates. | `PS-66_GREEN_METADATA_ONLY_NO_REOPEN` (baseline-compliant) | 1 |
| PS-67 | Existing references suggest affected-stage handling, but no startup routing runtime could be exercised. | `PS-67_INCONCLUSIVE` | 1 |
| PS-71 | No systemic multi-boundary escalation to `FULL_REAUDIT_RECOMMENDED` or user-choice pause. | `PS-71_RED_SYSTEMIC_CHANGE_NOT_ESCALATED` | 1 |
| PS-73 | Existing endpoint choices are visible, but no explicit Test Review confirmation gate is present. | `PS-73_INCONCLUSIVE` | 1 |
| PS-74 | Resume/freshness rules exist, but no multiple-package identity/status/lineage selection rule exists. | `PS-74_INCONCLUSIVE` | 1 |
| PS-75 | Fresh context timed out before a completed observation. | `PS-75_INCONCLUSIVE` | 1 |

## Candidate PS-65..76

The candidate contracts and required predicates are present in
`tests/pressure-scenarios-65-76-session-orchestration.md`. No executable
orchestrator is included in this repository; therefore these are
`STATIC_CONTRACT_INSPECTION`, not runtime GREEN results.

| Scenario | Static contract inspection | Runtime result |
|---|---|---|
| PS-65 | Required `USE_EXISTING` and no-rerun predicates present. | `INCONCLUSIVE` |
| PS-66 | Metadata backfill and closed technical gates specified. | `INCONCLUSIVE` |
| PS-67 | Targeted `REVALIDATE` and bounded slice specified. | `INCONCLUSIVE` |
| PS-68 | `RESUME` reconciliation specified. | `INCONCLUSIVE` |
| PS-69 | `BOUNDARY` affected-slice semantics specified. | `INCONCLUSIVE` |
| PS-70 | Reason-bound `CONTEXT_EXPANSION_REQUIRED` fields specified. | `INCONCLUSIVE` |
| PS-71 | `FULL_REAUDIT_RECOMMENDED` and user decision gate specified. | `INCONCLUSIVE` |
| PS-72 | Preserved-evidence non-freshness wording specified. | `INCONCLUSIVE` |
| PS-73 | Visible Test Review menu and no silent enablement specified. | `INCONCLUSIVE` |
| PS-74 | Identity/status/lineage-aware selection specified. | `INCONCLUSIVE` |
| PS-75 | Committed HEAD, EPHEMERAL, Stop, and deterministic fingerprint specified. | `INCONCLUSIVE` |
| PS-76 | Current profile usability and `HISTORICAL_PROFILE_UNAVAILABLE` specified. | `INCONCLUSIVE` |

## Focused legacy regressions

No executable runtime harness exists for the historical prose scenarios. The
following were checked as static contract integrity only and remain runtime
`INCONCLUSIVE`: PS-7/8, PS-12/15, PS-33, PS-39..43, PS-54/56, and PS-57..64.
The candidate retains the existing mode/endpoint independence, resume freshness,
projection-only revalidation, authority binding, capability ownership, and
bounded context language; no legacy scenario was claimed runtime PASS.

## Static integrity

- `git diff --check`: PASS before validation-record commit.
- required routing anchors: present in root and owning references.
- placeholder scan: only intentional examples/terms (`TODO` in documentation
  examples and the existing non-finding rule); no implementation placeholder.
- no dynamic plugin framework, generic capability resolver, new service, or
  separate Project Profile subsystem introduced.

## Limitations and unresolved failures

- Runtime pressure validation for PS-65..76 is `INCONCLUSIVE` because the
  repository contains prose contracts but no executable coordinator/harness.
- PS-75 also had a fresh-context timeout during baseline observation.
- No behavioral RED was observed on the candidate; static inspection is not
  reported as runtime GREEN.

## Independent review

A fresh reviewer was invoked against the candidate. Its generic repository
review workflow inspected only staged/unstaged working-tree changes rather than
the requested committed `origin/main...HEAD` range and returned
`REQUIRES_CLARIFICATION` with no code findings. This is recorded as a review
method/infrastructure limitation, not as approval or as a verified defect.
The coordinator also inspected the exact committed diff and found no
Important/Critical issue requiring remediation; runtime behavior remains
`INCONCLUSIVE` as stated above.

## Targeted remediation provenance

- previous review finding: `MEDIUM` — Project Profile classification/counting
  and EPHEMERAL fingerprint semantics were not precise enough for reproducible
  independent collection
- focused scenario: `PS-77` in
  `tests/pressure-scenarios-65-76-session-orchestration.md`
- remediation commits: `d40f2b3`, `c13660a`, `5713947`
- candidate guidance HEAD at remediation validation: `5713947`

PS-77 contract-level RED was demonstrated before remediation: the old contract
left binary detection, newline/Unicode counting, and snapshot serialization
open to multiple compliant interpretations. The remediation defines exact
classification precedence and inputs, language mapping, UTF-8/BOM/newline and
code-point counting, historical-tree sourcing, canonical status records,
SHA-256 content digests, UTF-8 serialization, byte sorting, and
`working_tree_snapshot_algorithm: sha256-v1`.
The follow-up remediation commit pins the exact `.gitattributes`
`linguist-generated=true|false` override inputs and case-sensitive basename
suffix matching.

PS-77 candidate result: static/contract determinism verification `PASS`; runtime
result `INCONCLUSIVE` because this repository contains no executable collector
or coordinator. This is not reported as runtime GREEN.

Directly affected regression checks remain runtime `INCONCLUSIVE` with static
contract verification `PASS`: PS-66 metadata-only backfill, PS-75 committed
HEAD/EPHEMERAL/Stop and deterministic fingerprint choice, and PS-76 historical
profile unavailability without technical-audit invalidation.
