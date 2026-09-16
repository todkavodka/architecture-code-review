# REVALIDATE Closeout Hardening Design

## Goal

Prevent REVALIDATE closeout from crossing semantic-authority and projection boundaries, advancing the accepted baseline before owner gates complete, or marking rewritten Markdown as `CURRENT` without an accepted `PRJ-*` lifecycle record.

## Observed regression

A real REVALIDATE run produced a valid delta overlay for a changed source baseline, then incorrectly:

1. treated the overlay as accepted semantic state;
2. advanced the accepted baseline before owner adjudication and current-baseline coverage gates;
3. dispatched `02-authoritative-findings-ledger.md`, `03-target-architecture.md`, and `04-remediation-roadmap.md` as `RG-*` work;
4. rewrote generated outputs without projection registration, V1-V4 verification, fingerprinting, or accepted projection revisions;
5. marked all projections `CURRENT` and reconciled `working/INDEX.md` despite contradictory baseline bindings.

The subsequent closeout verification correctly returned `CLOSEOUT_INVALID`.

## Design principles

### 1. Semantic authority and projections are disjoint execution domains

`RG-*` may operate only on explicitly registered, active `PRJ-*` identities. Paths, filenames, Markdown shape, or a `STALE` label in coordinator state never make an artifact a projection.

Semantic authorities are never `RG-*` targets. This includes, at minimum:

```text
02-authoritative-findings-ledger.md
03-target-architecture.md
04-remediation-roadmap.md
working/INDEX.md
STM semantic artifacts
Architecture RF/SER/property ledgers
Code Quality CQ/CQRA authority
Test Engineering BC/CC/MAT/TM/GAP authority
```

### 2. REVALIDATE overlay is proposed delta until owner acceptance

A REVALIDATE overlay records evidence-backed proposed changes relative to the previous accepted baseline. It is not accepted authority by itself.

The required closeout chain is:

```text
REVALIDATE overlay
→ PROPOSED_REVALIDATION_DELTA
→ affected owner adjudication gates
→ accepted semantic revisions
→ current-baseline technical-model / coverage gates
→ DELTA_RECONCILIATION
→ BASELINE_ADVANCE_ALLOWED
→ accepted baseline advancement
→ Projection Impact Analysis
→ optional explicit RG-* regeneration
```

The shortcuts below are invalid:

```text
overlay → accepted baseline
overlay → RG-*
RG-* → semantic authority mutation
```

### 3. Baseline roles are explicit

Coordinator state distinguishes:

```text
accepted_baseline
candidate_baseline
source_head
```

`candidate_baseline` may equal `source_head`, but `accepted_baseline` changes only after `BASELINE_ADVANCE_ALLOWED` is accepted.

### 4. ALL_STALE is registry-defined

`ALL_STALE` means exactly:

```text
all ACTIVE explicitly registered PRJ-* identities
whose persisted projection freshness == STALE
```

It never means all files described as stale or all deliverables that appear outdated.

A target that cannot resolve to an active registered `PRJ-*` fails before an `RG-*` session is created with:

```text
REGENERATION_TARGET_NOT_PROJECTION
```

### 5. CURRENT requires verified lifecycle evidence

A rewritten or readable file is not `CURRENT`. An `RG-*` success observation is not `CURRENT`.

`CURRENT` requires:

```text
active PRJ identity
projection contract + revision
accepted dependency / selector snapshot
V1 STRUCTURAL
V2 DEPENDENCY / PROVENANCE
V3 CONTRACT COMPLETENESS
V4 AUTHORITY CONSISTENCY
canonical fingerprint
accepted PRJ-*@revN or verified NO_CHANGE
```

### 6. Final reconciliation detects contradictions instead of normalizing them away

`FINAL_WORKFLOW_AUTHORITY_RECONCILED` may be accepted only when coordinator baseline fields, owner artifact revisions, coverage bindings, projection registry, projection freshness, package membership, and unresolved-policy accounting all agree with their owning authorities.

Metadata correction may repair false coordinator claims, but it cannot accept semantic content, advance a baseline, or make a projection current.

## Regression scenario

### Invalid

```text
A = accepted baseline
B = changed source

REVALIDATE overlay
→ rewrite 02/03/04 from RG workers
→ set accepted baseline B
→ rewrite Markdown outputs
→ mark everything CURRENT
```

### Valid

```text
A = accepted baseline
B = candidate/source baseline

REVALIDATE overlay
→ STM / Architecture / Test Engineering / Code Quality owner gates
→ Target Architecture review cycle when affected
→ Roadmap execution-consistency review cycle when affected
→ DELTA_RECONCILIATION
→ BASELINE_ADVANCE_ALLOWED
→ accepted baseline A → B
→ Projection Impact Analysis
→ resolve ALL_STALE from registered PRJ-* only
→ RG-* generation
→ V1 → V2 → V3 → V4
→ fingerprint + revision/NO_CHANGE
→ CURRENT
→ final authority reconciliation
```

## Files to harden

- `SKILL.md` — add closeout invariants and completion guard.
- `references/projection-lifecycle.md` — make semantic-authority exclusions operational and bind `CURRENT` to complete lifecycle evidence.
- `references/projection-regeneration.md` — add target preflight, strict `ALL_STALE`, and `REGENERATION_TARGET_NOT_PROJECTION`.
- `references/revalidation-and-freshness.md` — formalize proposed-delta semantics, owner acceptance, delta reconciliation, baseline advancement ordering, and regression example.
- `references/session-orchestration.md` — split baseline roles and forbid accepted-baseline movement before the gate.
- `references/report-contract.md` — explicitly exclude Architecture authority documents from `RG-*` / `PRJ-*` treatment except the separately defined generated final report surface.

## Non-goals

- No new semantic authority family.
- No new session intent.
- No automatic regeneration after REVALIDATE.
- No change to capability selection semantics.
- No change to Russian human-facing documentation.
- No attempt to make open findings disappear before baseline advancement; open accepted findings remain allowed only where an explicit existing policy permits them.

## Success criteria

The hardened contracts make the observed invalid sequence explicitly non-compliant and make the valid recovery path mechanically clear to an agent. A future agent must be unable to justify any of these states from the written contract:

```text
semantic authority as RG target
ALL_STALE containing an unregistered file
accepted baseline changed before owner gates
CURRENT without PRJ identity + V1-V4 + fingerprint + revision/NO_CHANGE
FINAL_WORKFLOW_AUTHORITY_RECONCILED with contradictory baseline/coverage bindings
```
