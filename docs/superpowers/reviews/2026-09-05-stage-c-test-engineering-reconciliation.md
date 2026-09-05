# Stage C Test Engineering contract reconciliation

Date: 2026-09-05  
Repository: `~/skills/architecture-code-review`  
Canonical branch: `main`

## 1. Baseline

Baseline checks completed after `git fetch origin --prune`:

```text
branch: main
HEAD: ab92798c57ac4b7daf199675dab6dbc8937fe72c
origin/main: ab92798c57ac4b7daf199675dab6dbc8937fe72c
subject: fix: tighten projection generation and review closeout contracts
tracked changes: none
untracked state: task-5-report.md only; preserved and untouched
```

This is a read-only reconciliation of the existing Stage C design and plan. No
Test Engineering implementation, contract edit, runtime check, or harness was
started.

## 2. Existing Stage C artifacts reviewed

The complete artifacts reviewed were:

- `docs/superpowers/specs/2026-09-03-test-engineering-capability-design.md`
- `docs/superpowers/plans/2026-09-03-test-engineering-implementation-plan.md`

## 3. Current Stage A/B contracts used

The reconciliation used the current definitions in:

- `SKILL.md`
- `capabilities/test-review/SKILL.md`
- `capabilities/test-review/references/test-engineering-contract.md`
- `references/shared-evidence-model.md`
- `references/shared-technical-model.md`
- `references/shared-assurance-principles.md`
- `references/technical-model-dependencies.md`
- `references/session-orchestration.md`
- `references/review-modes-and-orchestration.md`
- `references/revalidation-and-freshness.md`
- `references/projection-lifecycle.md`
- `references/projection-dependencies.md`
- `references/projection-verification.md`
- `references/projection-gates-and-packages.md`
- `references/projection-impact.md`

The controlling current additions are the targeted STM precondition in
`capabilities/test-review/SKILL.md:90-106`, the Test Review projection/package
contract in `capabilities/test-review/references/test-engineering-contract.md:118-276`,
and the Stage B V1–V4 publication chain in `references/projection-verification.md:26-40,100-124`.

## 4. Namespace reconciliation

```text
te_redefines_WS: NO
te_redefines_EV: NO
te_conflicts_with_EVENT_namespace: NO
```

The old design's `WS-*` wording at
`docs/superpowers/specs/2026-09-03-test-engineering-capability-design.md:203-204`
describes temporary discovery/evidence state and does not claim Test Engineering
ownership. It is compatible with the current `WS-*` bounded workset and physical
evidence grouping in `references/shared-evidence-model.md:10-20`; implementation
should use the current wording. Neither old artifact defines `EV-*` or
`EVENT-*`, so there is no namespace collision. `EVENT-*` remains the STM
Event/Message family from `references/shared-technical-model.md:27-41`.

Required replacement where the old plan or implementation guidance refers to a
working-set as if it were a behavior record: use shared `WS-*`/`EV-*` evidence,
and create Test Engineering semantics under the capability-owned families below.

## 5. Identity and authority reconciliation

| identifier | existing definition | compatibility | authority owner | required change |
|---|---|---|---|---|
| `RF-*` | Architecture/root finding (`spec:182-183`) | COMPATIBLE | Architecture Review | Preserve; TE may derive BC candidates but cannot redefine RF. |
| `BC-*` | One bounded, independently verifiable material behavior (`spec:185-186,223-249`) | COMPATIBLE | Behavior Model gate | Add the current accepted/fresh STM precondition before writing semantics. |
| `CC-*` | Mismatch among declared/implemented/consumed/tested views (`spec:188-189`) | COMPATIBLE | Contract Verification | Preserve independent lifecycle and adjudication; no automatic winner. |
| `MAT-*` | Material assurance target (`spec:191-192`) | COMPATIBLE | Test Assurance | Keep distinct from BC and evidence. |
| `TM-*` | Executable evidence mapped to MAT/BC (`spec:194-195`) | COMPATIBLE | Test Assurance | Keep test evidence here, not in BC. |
| `GAP-*` | Missing/partial/misleading/inadequate evidence (`spec:197-198`) | COMPATIBLE | Test Assurance | Keep orthogonal to CC drift. |
| `TASK-*` | TE remediation task (`spec:200-201`) | CLARIFICATION_REQUIRED | Capability remediation/workflow owner | It is work/remediation traceability, not product or test-evidence authority; do not treat it as a BC/MAT/GAP synonym. |

The old TE identity model therefore does not collapse Stage A namespaces. The
only identity clarification is that `WS-*`/`EV-*` and STM families are inputs,
not TE-owned semantic records.

## 6. Authority reconciliation

| concept | semantic_owner | allowed_inputs | allowed_outputs | must_not_own |
|---|---|---|---|---|
| Shared Evidence (`WS-*`, `EV-*`) | Shared Evidence | baseline-bound observations and provenance | reusable observations | findings, STM facts, BCs, gaps, verdicts |
| Shared Technical Model (`COMP-*`, `IF-*`, `INT-*`, `DS-*`, `EVENT-*`, `FLOW-*`, `AUTH-*`, `CFG-*`, `ERR-*`) | Technical Model Gate | accepted evidence and technical fact requests | accepted/revised STM facts | BC/CC/MAT/TM/GAP semantics |
| Architecture finding (`RF-*`) | Architecture Review | accepted STM and evidence | root-boundary/adjudicated architecture meaning | TE reinterpretation of root cause |
| Behavior Contract (`BC-*`) | Behavior Model gate | accepted/fresh targeted STM, accepted RF where relevant, observed contract views | accepted/revised BC semantics | test verdicts, CC classification, MAT/GAP authority |
| Consistency Contract (`CC-*`) | Contract Verification | `DECLARED`, `IMPLEMENTED`, `CONSUMED`, `TESTED` observations and BC references | mismatch record/classification/adjudication request | automatic selection of Swagger, code, consumers, or tests as truth |
| Assurance Target / evidence (`MAT-*`, `TM-*`, `GAP-*`) | Test Assurance | accepted BCs, evidence, existing tests and harness topology | bounded assurance accounting and evidence mappings | product behavior authority or contract adjudication |
| Remediation task (`TASK-*`) | capability/workflow remediation owner | accepted gaps and required capability work | actionable work item | semantic contract, evidence, or STM authority |
| Generated TE document (`PRJ-*`) | Projection Layer under Test Review contract | accepted semantic authorities and exact STM slice | candidate, verified revision, freshness state | semantic adjudication or mutation of its inputs |
| Workflow state (`working/INDEX.md`) | coordinator | persisted gates, handoffs, routing | resume/session state | PRJ identity, fingerprint, projection freshness, semantic replacement |

The old design explicitly preserves these boundaries in
`spec:305-319,398-428,1099-1127`; the current contracts add the required STM
and projection gates rather than changing the TE semantic owners.

## 7. STM dependency reconciliation

```text
old_te_private_fact_reconstruction_possible: YES, as written
targeted_stm_precondition_explicit: NO in the old design/plan
stm_freshness_precondition_explicit: NO in the old design/plan
technical_model_gate_dependency_correct: PARTIAL
```

The old design permits the Behavior Model to use accepted As-Built, real code
paths, schemas, consumers, and tests directly (`spec:89-108`). Current
architecture requires accepted/fresh, sufficiently resolved targeted STM plus
independent targeted coverage acceptance before TE constructs or materially
revises any behavior, contract, mapping, environment, simulator, or E2E
artifact (`capabilities/test-review/SKILL.md:90-106` and current TE contract
`190-208,356-369`). Raw source remains evidence for the Technical Model Gate
when facts are missing or disputed; it is not a normal private TE factual model.

TE needs targeted slices of all STM domains that its accepted BCs and scenarios
actually use: components, interfaces, interactions, data stores, events/messages,
flows, auth/trust, configuration, and error/failure contracts. It must request
the minimum slice, require `present + ACCEPTED + sufficiently fresh +
sufficiently resolved + TARGETED STM COVERAGE ACCEPTED`, and reuse an accepted
fresh `FULL` model when it satisfies the exact binding.

Required correction: add this precondition and Technical Model Gate/independent
coverage-review handoff to the implementation plan before downstream TE semantic
artifacts are produced. This is a bounded integration correction, not a second
technical model.

## 8. Stage B projection reconciliation

| artifact | semantic_or_projection | authority_owner | requires_PRJ | dependencies | freshness_sensitive | old_design_status |
|---|---|---|---|---|---|---|
| authoritative BC ledger | semantic authority | Behavior Model | NO | accepted STM slice; evidence/provenance | YES | compatible; old plan places ledgers under `working/` |
| authoritative CC ledger | semantic authority | Contract Verification | NO | compared views; related BC revisions | YES | compatible |
| `MAT-*`/`TM-*`/`GAP-*` ledgers | semantic authority | Test Assurance | NO | evidence, BC references, assurance scope | YES | compatible |
| `TASK-*` records | workflow/remediation authority | remediation/workflow owner | NO | accepted GAP or capability need | YES as work state | clarification required |
| `00-test-assurance-summary.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-00-ASSURANCE-SUMMARY` | scoped MAT/TM/GAP selector snapshot | YES | missing from old design/plan's Stage B integration |
| `01-test-assurance-map.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-01-ASSURANCE-MAP` | scoped MAT/TM/GAP selector snapshot | YES | missing Stage B integration |
| `02-test-plan.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-02-TEST-PLAN` | BC/MAT/TM/GAP accepted revisions | YES | missing Stage B integration |
| `03-behavior-contract-model.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-03-BEHAVIOR-CONTRACT-MODEL` | BC selector snapshot | YES | missing Stage B integration |
| `04-contract-consistency-report.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-04-CONTRACT-CONSISTENCY-REPORT` | CC selector plus referenced BC exact revisions | YES | missing Stage B integration |
| `05-test-environment-design.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-05-TEST-ENVIRONMENT-DESIGN` | accepted TE semantics plus exact STM slice | YES | missing Stage B integration |
| `06-service-simulator-spec.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-06-SERVICE-SIMULATOR-SPEC` | BC/CC plus exact consumer-boundary STM slice | YES | missing Stage B integration |
| `07-service-simulator-implementation-plan.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-07-SERVICE-SIMULATOR-IMPLEMENTATION-PLAN` | BC/CC plus exact `PRJ-06` verified revision | YES | missing Stage B integration |
| `08-e2e-test-plan.md` | generated projection | Test Review | YES: `PRJ-TEST-REVIEW-08-E2E-TEST-PLAN` | BC/MAT/TM/GAP plus exact multi-component STM slice | YES | missing Stage B integration |

The old design correctly distinguishes authority from human-readable output
(`spec:831-868`) and the old plan correctly preserves `working/` ledgers
(`plan:374-388`). It does not, however, specify stable `PRJ-*` identity,
projection-contract revision, exact/selector dependencies, resolution snapshot,
V1–V4, fingerprint, `PRJ-*@revN`, or `CURRENT/STALE/BLOCKED`. Current Stage B
requires all of these before a generated document is a valid current projection.

The canonical projection edge is `CONSUMER -> PREREQUISITE`; regeneration is
prerequisite-first. The old plan has no contrary edge, but it also has no
projection DAG registration. Add explicit registration and verification; do not
make generated documents semantic authorities.

## 9. Execution-mode reconciliation

| mode | compatibility | finding |
|---|---|---|
| `NEW` | CLARIFICATION_REQUIRED | Old design correctly selects outputs and adds internal dependencies (`spec:874-890`), but must bootstrap/persist STM before TE semantics and finish with impact accounting/package membership rather than implicit regeneration. |
| `RESUME` | CLARIFICATION_REQUIRED | Reuse of accepted upstream work is correct (`spec:892-894`); current contract requires persistent workflow/authority state from `working/INDEX.md`, not prose reconstruction. |
| `USE_EXISTING` | COMPATIBLE | Old accepted + fresh + resolved condition (`spec:896-906`) matches current minimum-slice rule. Include the exact STM coverage and PRJ dependency proofs. |
| `EXTEND` | COMPATIBLE | Minimum-slice reuse and no unrelated replay (`spec:908-921`) match current routing. Add explicit package/output membership reconciliation. |
| `REVALIDATE` | CLARIFICATION_REQUIRED | Impact-driven routing and tests/implementation/consumer distinctions are correct (`spec:923-981`, `plan:413-476`). It must end in the current post-semantic `PROJECTION_IMPACT_ACCOUNTED` handoff and never silently regenerate. |
| `PROJECTION_REPAIR` | COMPATIBLE | Old restrictions (`spec:983-1005`) preserve presentation-only repair and semantic drift escalation; current Stage B additionally requires projection revalidation and forbids hidden source/baseline changes. |

No mode requires reopening accepted Stage A architecture. The corrections are
workflow persistence, STM gating, and Stage B handoff details.

## 10. Implementation-plan task assessment

| task | classification | assessment |
|---|---|---|
| Task 1: fail-first pressure scenarios | TEXT_UPDATE_ONLY | The pressure boundaries remain valid. State that these are targeted manual/small deterministic contract checks and do not authorize a reusable harness. The RED-before-guidance ordering remains useful. |
| Task 2: semantic contract | SEMANTIC_ADJUSTMENT | Add the STM precondition, Technical Model Gate, independent targeted coverage acceptance, and Stage B projection lifecycle as required contract sections/steps. The BC/CC ownership and view semantics are otherwise compatible. |
| Task 3: output selection/dependency/artifact ownership | SEMANTIC_ADJUSTMENT | Independent booleans, minimum dependency slices, ledgers, and `EXTEND` are correct. Add `PRJ-*` registration, dependency binding/snapshot, V1–V4, fingerprint/revision, freshness, package membership, and explicit impact-accounting handoff. |
| Task 4: impact-driven revalidation | TEXT_UPDATE_ONLY | Source-view routing is already aligned. Add explicit `PROJECTION_IMPACT_ACCOUNTED` and separate `RG-*` regeneration semantics; preserve concrete runtime revisions rather than placeholders. |
| Task 5: environment/simulator/E2E boundaries | TEXT_UPDATE_ONLY | Strategy vocabulary, separate dependency substitutes, consumer/control planes, BC provenance, and optional simulator for E2E are compatible. Require the exact STM slice and PRJ metadata on resulting documents. |
| Task 6: consolidated validation | SEMANTIC_ADJUSTMENT | Keep compatibility checks, but validate STM gating and Stage B V1–V4/package gates. Replace any implication of a full framework with manual targeted checks or small deterministic checks unless measured reuse justifies more. |
| Task 7: user-facing documentation | TEXT_UPDATE_ONLY | Perform only after accepted behavior; document projections and authoritative ledgers as projections/authority respectively, and do not make README a second contract. |

No old task is wholly invalid. No task needs a different dependency direction.
One genuinely missing obligation must be added within Tasks 2–3 (or as a small
preceding gate): targeted STM acquisition/acceptance and Stage B registration,
verification, and package-closeout integration. This is `NEW_TASK_REQUIRED`
only in the sense of a missing implementation obligation; it does not justify a
new architecture design or full replan.

## 11. Validation proportionality assessment

The old plan does not propose a full reusable validation framework or runtime
test harness. Its six pressure-scenario Markdown files and one acceptance matrix
are persistent contract evidence, not harness infrastructure. They are
justified only if executed as bounded manual or small deterministic checks.

| planned component | uncertainty_removed | why manual/small check is sufficient | expected_reuse | behavior_stability | cost_vs_capability |
|---|---|---|---|---|---|
| PS-81..86 scenario records | whether each ownership, authority, DAG, freshness, and simulator boundary is preserved | Markdown contracts can be challenged directly in fresh targeted checks; no runtime framework is needed | useful as repeatable review prompts | stable contract pressure, not product runtime behavior | low cost; retain |
| consolidated validation matrix | whether the six boundaries and Test Assurance compatibility cohere | a deterministic checklist/result matrix is sufficient after targeted checks | reusable for future capability changes | moderate and bounded | low cost; retain, but do not grow into a framework |
| “fresh context” execution | whether guidance causes rationalization or semantic collapse | manual fresh-agent acceptance is the least expensive useful control | high conceptual reuse | stable process behavior | acceptable |
| reusable harness or full validation framework | none demonstrated beyond the above checks | the plan supplies no behavior whose uncertainty requires a framework | unproven | not established | disproportionate |

`DO_NOT_BUILD_HARNESS`: no persistent reusable harness is justified at this
gate. Follow `evidence first → automation second → framework last`; a harness
would require new evidence of repeated execution value and stable behavior.

## 12. Required corrections

1. Before any extended TE semantic artifact, calculate the minimum factual STM
   slice and require accepted/fresh/resolved facts plus independent targeted
   coverage acceptance after the Technical Model Gate.
2. Prohibit normal TE reconstruction of factual components, interfaces,
   interactions, stores, events, flows, auth, configuration, or errors from
   As-Built prose or arbitrary source. Missing facts become Technical Model
   Gate requests.
3. Register every generated `00`–`08` output as the current capability contract's
   named `PRJ-*` identity, with contract revision, direct semantic/STM and
   `PROJECTION_EXACT` dependencies as applicable, selector resolution snapshot,
   V1–V4 evidence, canonical fingerprint, verified revision, and freshness.
4. Make `CONSUMER -> PREREQUISITE` the persisted projection edge and execute
   prerequisites first; keep semantic dependencies separate from projection
   dependencies.
5. Persist package membership and perform `PROJECTION_IMPACT_ACCOUNTED` before
   closeout. Regeneration is an explicit `RG-*` workflow, never an implicit
   closeout action.
6. Make `RESUME` restore `working/INDEX.md` workflow/authority state; do not
   reconstruct resume-critical state from prose.
7. Limit validation to manual targeted checks/small deterministic checks. Do
   not build a reusable harness or full framework without new reuse evidence.
8. Amend the plan's final “clean status” wording to allow the known preserved
   untracked `task-5-report.md` while requiring no other unrelated changes.

## 13. Explicitly preserved design decisions

- Test Assurance remains the evidence-first compatibility core and keeps `00`,
  `01`, and optional `02` outputs.
- `BC-*` remains one independently verifiable material behavior and is not
  `MAT-*`, `RF-*`, `GAP-*`, `TM-*`, or executable evidence.
- `CC-*` remains distinct from `GAP-*`; contract drift does not automatically
  become an assurance gap.
- `DECLARED`, `IMPLEMENTED`, `CONSUMED`, and `TESTED` remain views without
  automatic precedence.
- Behavior Model is the accepted BC writer; Contract Verification owns CC;
  Test Assurance owns MAT/TM/GAP accounting.
- Service dependency substitutes remain distinct from a Service Simulator.
- Simulator consumer and test-control planes remain separate.
- E2E remains conditional on material multi-component assurance and does not
  require a simulator when topology does not need one.
- `EXTEND` and `REVALIDATE` remain minimum-slice/impact-driven operations.
- `PROJECTION_REPAIR` remains presentation-only and cannot mutate semantic
  authority.
- No simulator, production test code, test infrastructure, or migration is
  implemented as part of this reconciliation.

## 14. Deferred/non-issues

- No WS/EV/EVENT namespace conflict exists; no namespace redesign is needed.
- The environment vocabulary is valid and does not become STM or architecture
  authority; only per-dependency rationale and persistence need implementation
  enforcement.
- Exact ledger syntax, impact heuristics, simulator placement, and localization
  remain implementation details already identified by the old design
  (`spec:1132-1139`).
- No full Skill harness, application runtime verification, or simulator runtime
  acceptance is required for this read-only gate.
- Existing accepted Stage A architecture is not reopened by these corrections.

## 15. Recommended next gate

`BOUNDED_DESIGN_AND_PLAN_RECONCILIATION`:

1. Update the Stage C design/plan only to incorporate the eight bounded
   corrections above, especially the STM precondition and Stage B lifecycle.
2. Re-run the pressure checks as manual/small deterministic checks.
3. Proceed to implementation only after the reconciled plan explicitly names
   the STM and Stage B obligations.

No Stage C implementation should begin in this gate.

## 16. Final verdict

```text
design_status: DESIGN_COMPATIBLE_WITH_BOUNDED_CORRECTIONS
plan_status: PLAN_COMPATIBLE_WITH_BOUNDED_CORRECTIONS
recommended_action: BOUNDED_DESIGN_AND_PLAN_RECONCILIATION
verdict: STAGE_C_REENTRY_BOUNDED_RECONCILIATION_REQUIRED
```

