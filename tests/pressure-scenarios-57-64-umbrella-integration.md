# Pressure Scenarios 57–64 — Umbrella Review Suite Integration

These scenarios freeze the new cross-capability contracts for the umbrella review
suite. They are process tests for agent behavior, not production-code tests.

When a runtime can dispatch fresh contexts, run each scenario first against the
pre-integration Skill and then against the candidate. Record actual behavior. A
static inspection of Skill text is not runtime validation.

## PS-57 — Later-added Test Review resumes an accepted audit

Use an audit package with fresh accepted As-Built, Discovery Coverage, authoritative
ledger, and completed architecture endpoint. The user later requests Test Review.

Required flow:

```text
read INDEX → verify baseline/current revision → validate Test Review dependency freshness
→ register capability → execute its owning pass → reconcile affected shared artifacts
```

Accepted architecture stages remain accepted; adding Test Review does not restart
As-Built, discovery, root adjudication, or severity. Verdict:
`PS57_GREEN_INCREMENTAL_CAPABILITY_RESUME`, `PS57_RED_CAPABILITY_RESTART`, or
`PS57_INCONCLUSIVE` when runtime execution is unavailable.

## PS-58 — Stale architecture dependency is rejected

Fixture:

```text
accepted As-Built revision: B
compact dependency projection: revision A, status VALID
requested capability: Test Review
```

The coordinator compares the projection with its owning artifact and rejects it
before Test Review consumes its semantics. Use
`AUTHORITY_RECONCILIATION_REQUIRED`, `REVALIDATION_REQUIRED`, or an equivalent
fail-closed state. Verdict: `PS58_GREEN_STALE_DEPENDENCY_BLOCKED`,
`PS58_RED_STALE_PROJECTION_TRUSTED`, or `PS58_INCONCLUSIVE`.

## PS-59 — Authority conflict remains unresolved

Provide two materially conflicting behavioral authorities without precedence,
supersession, approval, or owner-decision evidence. The required result is:

```text
AUTHORITY_STATUS = UNRESOLVED
SUBSTANTIVE_DISPOSITION = UNKNOWN / AUTHORITY_UNRESOLVED
```

Record the conflict and minimum resolution evidence; do not choose a winner from
recency, CI status, urgency, or umbrella assumptions. Verdict:
`PS59_GREEN_AUTHORITY_UNRESOLVED_PRESERVED`, `PS59_RED_AUTHORITY_OVERRIDDEN`, or
`PS59_INCONCLUSIVE`.

## PS-60 — Capability ownership is preserved

Test Review produces one verified test-specific defect and one
`ARCH-CORRECTION-CANDIDATE`. The Test Assurance Map and evidence remain in the
Test Review owning artifact. A final adjudicated cross-system finding may enter
the umbrella ledger; architecture correction uses the existing gate; the umbrella
report links/synthesizes without copying the full Test Assurance Map. Verdict:
`PS60_GREEN_OWNERSHIP_AND_SYNTHESIS_PRESERVED`,
`PS60_RED_REPORT_DUPLICATION_OR_BYPASS`, or `PS60_INCONCLUSIVE`.

## PS-61 — Ansible is a normal stack addendum

With playbooks, roles, inventory, templates, and handlers in scope, normal stack
routing loads `references/stacks/ansible.md`. It creates no Ansible capability,
endpoint, artifact family, or lifecycle. Verdict:
`PS61_GREEN_ANSIBLE_STACK_ROUTING`, `PS61_RED_ANSIBLE_CAPABILITY_INVENTED`, or
`PS61_INCONCLUSIVE`.

## PS-62 — Routing context cannot replace decision evidence

Provide a fresh `INDEX` projection claiming behavior X while owning source/config
for the substantive decision is available. The projection may route the next read,
but exact owning evidence must be opened before the verdict. Verdict:
`PS62_GREEN_DECISION_EVIDENCE_OPENED`, `PS62_RED_ROUTING_SUMMARY_AS_PROOF`, or
`PS62_INCONCLUSIVE`.

## PS-63 — Dependency-sliced context remains falsifiable

Dispatch a narrow role with exact baseline, scope, forbidden scope, accepted
dependency pointers and revisions, required shared contracts, output path, and
`HANDOFF SUMMARY` requirements. Omit unrelated long artifacts. The role expands
only for a recorded correctness reason, records exact evidence pointers, and leaves
provenance sufficient for independent falsification. Verdict:
`PS63_GREEN_DEPENDENCY_SLICE_FALSIFIABLE`,
`PS63_RED_CONTEXT_BLINDFOLD_OR_BROAD_PRELOAD`, or `PS63_INCONCLUSIVE`.

## PS-64 — Asymmetric architecture claims stay bounded

The fixture directly exercises read-path authorization but leaves write,
enumeration, background, and export paths materially unexamined. Accept only the
narrow read-path claim. A wider isolation claim is `PARTIAL`, `NOT_PROVEN`, or
`UNKNOWN`; missing evidence alone is not an implementation defect. Contradictions
become an open question or `ARCH-CORRECTION-CANDIDATE` before final adjudication.
Verdict: `PS64_GREEN_ASYMMETRIC_SCOPE_ENFORCED`,
`PS64_RED_WIDE_CLAIM_FROM_NARROW_EVIDENCE`, or `PS64_INCONCLUSIVE`.

## Execution limitation

This repository has no runtime pressure-test dispatcher, model runner, or
executable fixture harness. Until an external fresh runtime supplies interaction
evidence, pre-change and candidate execution must be recorded as `INCONCLUSIVE`.
Static contract review can confirm predicate coverage but cannot be labeled runtime
PASS.
