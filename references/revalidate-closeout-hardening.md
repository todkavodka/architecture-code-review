# REVALIDATE closeout hardening

This reference hardens the boundary between REVALIDATE semantic closeout, baseline advancement, Projection Impact Analysis, and Stage B regeneration. It does not create a new Session Intent, capability, semantic authority family, or projection lifecycle. Existing owner contracts remain authoritative.

## 1. Regression this contract prevents

The following sequence is invalid:

```text
accepted baseline A
→ REVALIDATE against source B
→ produce overlay
→ treat overlay as accepted semantic state
→ let RG workers edit semantic-authority documents
→ move accepted baseline to B
→ rewrite Markdown outputs
→ mark outputs CURRENT without PRJ identity / V1-V4 / fingerprint / revision
→ mark FINAL_WORKFLOW_AUTHORITY_RECONCILED
```

A rewritten file, completed worker task, changed baseline pointer, or successful `RG-*` execution is never sufficient evidence for semantic acceptance or projection freshness.

## 2. Required REVALIDATE closeout chain

REVALIDATE produces bounded decision evidence and a proposed semantic delta. The required closeout chain is:

```text
previous accepted baseline
→ candidate/source baseline binding
→ REVALIDATE evidence and impact analysis
→ PROPOSED_REVALIDATION_DELTA
→ affected owner revalidation / adjudication gates
→ accepted semantic revisions at the candidate baseline
→ required Technical Model / coverage gates at the candidate baseline
→ DELTA_RECONCILIATION
→ BASELINE_ADVANCE_ALLOWED
→ accepted baseline advancement
→ Projection Impact Analysis
→ PROJECTION_IMPACT_ACCOUNTED
→ optional explicit RG-* request
→ registered PRJ-* targets only
→ generation + V1-V4
→ accepted PRJ revision or verified NO_CHANGE
→ CURRENT
→ FINAL_WORKFLOW_AUTHORITY_RECONCILED
```

These shortcuts are prohibited:

```text
PROPOSED_REVALIDATION_DELTA → accepted semantic authority
PROPOSED_REVALIDATION_DELTA → accepted baseline advancement
PROPOSED_REVALIDATION_DELTA → RG-* semantic mutation
RG-* → semantic authority mutation
Markdown rewritten → CURRENT
RG completed → CURRENT
baseline pointer changed → baseline accepted
```

## 3. Proposed delta semantics

`working/revalidation-overlay.md`, or any equivalent REVALIDATE overlay, is a proposed-delta artifact until the owning semantic gates adjudicate the affected slices. It may preserve evidence, candidate changes, impact classification, and routing decisions, but it cannot by itself:

- create, revise, resolve, supersede, or accept `RF-*`, STM, `CQ-*`, `CQRA-*`, `BC-*`, `CC-*`, `MAT-*`, `TM-*`, or `GAP-*` authority;
- accept Target Architecture or Remediation Roadmap semantics;
- advance the accepted baseline;
- satisfy a downstream semantic dependency as accepted state.

Every material delta item must finish `DELTA_RECONCILIATION` as exactly one of:

```text
ACCEPTED_OWNER_CHANGE
ACCEPTED_PRESERVED
EVIDENCED_NON_MATERIAL
POLICY_PERMITTED_UNRESOLVED
BLOCKING_UNRESOLVED
```

`POLICY_PERMITTED_UNRESOLVED` requires an explicit applicable policy reference. A generic statement that open findings or unknowns are allowed is insufficient.

## 4. Baseline roles

Coordinator state distinguishes three roles:

```text
accepted_baseline   # baseline currently accepted by semantic authorities
candidate_baseline  # exact baseline being revalidated/adjudicated
source_head         # observed current source revision; may move independently
```

During REVALIDATE it is legal for:

```text
candidate_baseline == source_head
candidate_baseline != accepted_baseline
```

`accepted_baseline` MUST NOT change until `BASELINE_ADVANCE_ALLOWED` is accepted. If coordinator state needs a human-facing `current_baseline` alias, it must state which role it represents and must not collapse candidate and accepted meaning.

`BASELINE_ADVANCE_ALLOWED` requires all of the following against the exact candidate baseline:

```text
exact candidate source binding is still current for the decision
all material delta is reconciled
all required owner adjudications are accepted
required Technical Model gates are accepted
required coverage gates are accepted
remaining unresolved/unknown items are explicitly policy-permitted
```

Acceptance bound only to the old baseline cannot satisfy candidate-baseline advancement.

## 5. Semantic authority is never an RG target

`RG-*` is projection regeneration only. The following are outside automatic projection classification and MUST NOT receive `PRJ-*` identity, projection freshness, or `RG-*` execution state merely because their rendered content changed:

```text
working/INDEX.md
02-authoritative-findings-ledger.md
03-target-architecture.md
04-remediation-roadmap.md
STM semantic artifacts
Architecture RF/SER/property/invariant authority
Code Quality CQ/CQRA authority
Test Engineering BC/CC/MAT/TM/GAP authority
```

If a requested regeneration target resolves to semantic authority, an unregistered path, or an ambiguous artifact instead of an active registered projection identity, fail before creating an `RG-*` plan:

```text
REGENERATION_TARGET_NOT_PROJECTION
```

The coordinator routes the requested semantic change to the owning revalidation/adjudication workflow instead.

## 6. Strict `ALL_STALE`

`ALL_STALE` means exactly:

```text
all ACTIVE explicitly registered PRJ-* identities
whose persisted projection freshness == STALE
```

It does not mean:

```text
all files described as stale
all final documents that look outdated
all semantic authorities changed by REVALIDATE
all paths listed in working/INDEX.md
```

The stale snapshot is frozen only after target resolution confirms active projection registration and valid projection-contract metadata. Semantic authorities are rejected, not silently omitted after plan creation.

## 7. Projection CURRENT evidence

An active projection may be persisted as `CURRENT` only when the lifecycle record contains or binds all required evidence:

```text
stable active PRJ-* identity
projection contract + contract revision
accepted dependency / selector-resolution snapshot
V1 STRUCTURAL: PASS
V2 DEPENDENCY / PROVENANCE: PASS
V3 CONTRACT COMPLETENESS: PASS
V4 AUTHORITY CONSISTENCY: PASS
canonical generated-content fingerprint
accepted PRJ-*@revN or verified NO_CHANGE
```

Therefore:

```text
readable Markdown != CURRENT
rewritten Markdown != CURRENT
registered identity != CURRENT
RG execution success != CURRENT
REGENERATED != CURRENT
```

A missing required record leaves the projection `STALE` or `BLOCKED` according to the owning lifecycle rule; coordinator metadata cannot upgrade it.

## 8. Final authority reconciliation

`FINAL_WORKFLOW_AUTHORITY_RECONCILED` may be accepted only after the coordinator checks the owning records, not merely its own cached summary. At minimum reconcile:

```text
accepted_baseline
candidate_baseline state
source_head
semantic authority revisions and owner acceptance
Technical Model baseline and coverage baseline
open findings and unresolved-policy accounting
projection registration and accepted revisions
projection dependency snapshots
projection freshness
resolved package membership and gate result
```

A contradiction such as `accepted_baseline = B` while Technical Model or required coverage remains accepted only for A prevents final reconciliation.

Metadata correction may change false coordinator claims to `BLOCKED`, `STALE`, or `NOT_ACCEPTED`. Metadata correction MUST NOT accept semantic content, advance a baseline, generate a `PRJ-*` revision, or satisfy V1-V4.

## 9. Canonical regression example

Given:

```text
A = previous accepted baseline
B = changed source/candidate baseline
REVALIDATE finds changed STM facts, a new Architecture finding, CQ regressions,
and stale user-facing outputs
```

Invalid:

```text
overlay
→ RG workers update 02/03/04
→ accepted baseline = B
→ rewrite outputs
→ all projections CURRENT
```

Valid:

```text
overlay
→ Technical Model Gate for affected STM slices
→ Architecture owner adjudication for affected RF slices
→ Test Engineering / Code Quality owner revalidation for affected records
→ Target Architecture review/correction/fresh re-review when affected
→ Roadmap execution-consistency review/correction/fresh re-review when affected
→ DELTA_RECONCILIATION
→ candidate-baseline model/coverage gates
→ BASELINE_ADVANCE_ALLOWED
→ accepted baseline A → B
→ Projection Impact Analysis
→ ALL_STALE resolves registered PRJ-* only
→ explicit RG-* generation
→ V1 → V2 → V3 → V4
→ fingerprint + accepted revision/NO_CHANGE
→ CURRENT
→ FINAL_WORKFLOW_AUTHORITY_RECONCILED
```

This example is normative for boundary ordering, not for the number or type of findings in a specific repository.
