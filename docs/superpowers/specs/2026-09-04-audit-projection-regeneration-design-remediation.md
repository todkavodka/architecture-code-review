# Stage B — Audit Projection & Regeneration
## Design Review Remediation Addendum

Status: DESIGN REMEDIATION CANDIDATE

Base design:

```text
docs/superpowers/specs/2026-09-04-audit-projection-regeneration-design.md
f90e82c97d726b1917bf86c02762a4e8985b8375
```

Canonical main baseline:

```text
0ba7c4b5b556ba0de78200d6a6792b408b42523b
```

This addendum is normative. Where it conflicts with the base Stage B design, this addendum supersedes the affected wording. All unaffected Stage B design sections remain unchanged.

It remediates independent design review findings:

```text
SBD-001 IMPORTANT
SBD-002 IMPORTANT
SBD-003 IMPORTANT
SBD-004 IMPORTANT
```

---

# 1. SBD-001 — Composite Architecture Review report authority

## 1.1 Problem

The base design used the final Architecture Review report as an example of a `USER_PROJECTION`, while the existing Stage A contract preserves Architecture-owned semantic meaning in the user-facing review package.

Stage B must not demote Architecture semantic authority merely because user-facing documents are generated.

## 1.2 Normative resolution

The Stage B rule remains:

```text
projection != semantic authority
```

Therefore a generated file may contain rendered architectural interpretation only when that interpretation already exists in separately addressable Architecture-owned semantic authority.

Stage B MUST NOT treat human-readable final-report prose as the sole persistence location for architectural meaning.

The target model is:

```text
Shared Technical Model factual authority
        |
        v
Architecture-owned semantic authority
  RF-*
  SER-*
  accepted architectural properties / invariants
  target-architecture semantics where selected
  roadmap semantics where selected
        |
        v
Architecture projection contracts
        |
        v
fully generated Architecture user-facing projections
```

The final Architecture Review document MAY be fully generated, but only if every piece of meaning that must survive regeneration is owned upstream by an Architecture semantic artifact or another accepted semantic authority.

In particular:

```text
Architecture report prose != sole authority for RF/SER/target semantics
```

and:

```text
regeneration MUST NOT create, change, resolve, strengthen, weaken,
merge, suppress, or reinterpret Architecture semantic authority
```

## 1.3 Migration rule

Existing Stage A wording that calls `01-architecture-review.md` an authoritative user-facing report must be interpreted during Stage B migration as follows:

```text
user-facing authoritative delivery surface
!=
sole semantic persistence authority
```

Before Stage B may make that file fully regeneratable, every persistent semantic element currently owned only by that report MUST be extracted or explicitly mapped to the proper Architecture-owned semantic authority.

This migration is a prerequisite for full regeneration of that projection.

Until migration is proven for a particular section, Stage B MUST NOT silently overwrite that section under the claim that the whole file is already a pure projection.

## 1.4 Generated-boundary rule

Stage B does NOT introduce mixed generated/human-owned sections as the target architecture.

Instead the migration target remains:

```text
all persistent meaning upstream in semantic authority
+
fully generated projection downstream
```

If an existing document contains semantic content that has not yet been externalized into owning authority, that document/section is a migration blocker rather than an exception to the fully-generated invariant.

Required blocker:

```text
PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY
```

## 1.5 Required verification

Implementation planning must include a pressure scenario proving:

```text
Architecture semantic meaning survives projection regeneration
without relying on manually preserved report sections.
```

The scenario must verify at least:

- RF wording/severity/identity cannot be changed by regeneration;
- SER semantics cannot be changed by regeneration;
- target-architecture/roadmap semantics remain owned by their existing authorities;
- factual As-Built content remains STM-backed projection;
- final user-facing report can be regenerated only after all persistent meaning is mapped upstream.

---

# 2. SBD-002 — Preserve Stage A PROJECTION_REPAIR semantics

## 2.1 Problem

The base Stage B design narrowed `PROJECTION_REPAIR` too far to infrastructure-only repair. Stage A already permits bounded presentation-only repair such as language, structure, links, Mermaid, terminology, and summaries, provided semantic authority does not change.

Stage B must preserve that accepted contract.

## 2.2 Normative resolution

`PROJECTION_REPAIR` remains the bounded operation for correcting projection-only defects while semantic authority is unchanged.

Valid `PROJECTION_REPAIR` examples include:

```text
language / wording rendering correction
heading or section structure correction
broken link correction
Mermaid/rendering correction
terminology normalization
summary/projection formatting correction
missing or malformed generated metadata
corrupt generated index/view
```

The invariant is not "infrastructure only".

The invariant is:

```text
PROJECTION_REPAIR may change presentation/projection representation
but MUST NOT change semantic meaning or semantic authority.
```

## 2.3 Repair vs regeneration

Use `REGENERATE` when projection inputs or the projection contract changed and the artifact must be rebuilt from the current accepted dependency snapshot.

Use `PROJECTION_REPAIR` when the accepted dependency snapshot and semantic meaning are unchanged, but the projection representation itself is defective.

Examples:

```text
accepted IF selector membership changed
  -> REGENERATE

report link rendered incorrectly while inputs unchanged
  -> PROJECTION_REPAIR

accepted RF meaning changed
  -> REGENERATE after semantic impact accounting

wording correction that preserves the exact accepted RF meaning
  -> PROJECTION_REPAIR

wording correction would alter RF meaning
  -> NOT PROJECTION_REPAIR
  -> owning Architecture semantic workflow
```

## 2.4 Fully-generated compatibility

The fully-generated target remains unchanged.

`PROJECTION_REPAIR` is NOT a human-owned persistent section mechanism.

A repair must itself produce a valid generated/projection state governed by the projection contract. Anything that must persist semantically across future regeneration still belongs in semantic authority.

## 2.5 Optional repair subtype

Implementation MAY distinguish diagnostic subtypes such as:

```text
EDITORIAL_REPAIR
STRUCTURAL_REPAIR
RENDERING_REPAIR
INDEX_REPAIR
METADATA_REPAIR
```

but these are subtypes of the existing `PROJECTION_REPAIR` operation, not replacements for it and not new semantic authorities.

---

# 3. SBD-003 — Protect authoritative working/INDEX.md

## 3.1 Problem

The base design introduced `WORKFLOW_PROJECTION` and illustrative projection lifecycle paths without explicitly excluding the existing coordinator-owned `working/INDEX.md`.

Stage A uses that INDEX as persistent resume-critical workflow authority.

It MUST NOT enter the generated projection lifecycle.

## 3.2 Normative resolution

The existing:

```text
working/INDEX.md
```

is explicitly classified as:

```text
COORDINATOR_WORKFLOW_AUTHORITY
```

for Stage B purposes.

It is NOT:

```text
USER_PROJECTION
CAPABILITY_PROJECTION
WORKFLOW_PROJECTION
DERIVED_INDEX
```

and MUST NOT receive a `PRJ-*` identity merely because its filename contains `INDEX`.

## 3.3 Authority rule

`working/INDEX.md` owns resume-critical coordinator state according to the existing Stage A/session orchestration contract.

Projection Impact Analysis and Regeneration MUST NOT:

- regenerate it;
- reconstruct it from projection state;
- overwrite gate state stored there;
- overwrite resume routing;
- overwrite handoff/coordinator state that is authoritative there;
- treat its fingerprint as ordinary projection drift;
- retire or revise it through `PRJ-*` lifecycle rules.

## 3.4 WORKFLOW_PROJECTION definition

`WORKFLOW_PROJECTION` is limited to explicitly declared, reconstructable, non-authoritative workflow views.

Examples MAY include:

```text
generated compact status view
generated handoff projection when the underlying handoff authority exists elsewhere
generated projection registry view
generated impact summary
```

A workflow artifact is a `WORKFLOW_PROJECTION` only if its contract explicitly declares it reconstructable and non-authoritative.

Filename/location alone never determines projection status.

Normative rule:

```text
projection classification is explicit by contract,
never inferred from path, filename, Markdown shape, or INDEX naming.
```

## 3.5 Physical layout constraint

If Stage B uses a generated projection index, it MUST NOT reuse the identity/path of the authoritative coordinator INDEX.

A path such as:

```text
working/projections/registry.md
```

or another clearly Stage-B-owned generated location may be chosen during implementation planning.

The exact path is implementation detail, but collision with:

```text
working/INDEX.md
```

is forbidden.

---

# 4. SBD-004 — Canonical projection dependency edge direction

## 4.1 Canonical convention

Stage B uses exactly one dependency-arrow convention everywhere:

```text
CONSUMER -> PREREQUISITE
```

If projection B consumes projection A:

```text
PRJ-B -> PRJ-A
```

means:

```text
B depends on A
A is upstream/prerequisite of B
B is downstream/dependent of A
```

This matches the Stage A rule that the consuming artifact owns outbound direct dependency metadata.

No Stage B example may use the same arrow to mean production/data-flow direction.

## 4.2 Canonical three-node chain

For:

```text
PRJ-C -> PRJ-B -> PRJ-A
```

interpretation is:

```text
C depends on B
B depends on A

A = most-upstream prerequisite
C = most-downstream consumer
```

If all three require regeneration, execution order is:

```text
1. PRJ-A
2. PRJ-B
3. PRJ-C
```

## 4.3 TARGETED upstream closure

If the requested target is:

```text
PRJ-C
```

and:

```text
PRJ-C -> PRJ-B -> PRJ-A
```

then the planner follows outgoing dependency edges from the consumer toward prerequisites and includes only required stale/blocking upstream prerequisites:

```text
requested:
  PRJ-C

expanded upstream:
  PRJ-B
  PRJ-A

execution:
  PRJ-A
  PRJ-B
  PRJ-C
```

If `PRJ-A` is already CURRENT and otherwise valid, it is not regenerated merely because it is in transitive dependency closure.

## 4.4 Downstream impact propagation

If `PRJ-A` becomes STALE or obtains a new verified revision, downstream propagation travels in the reverse direction of declared edges, using the derived reverse dependency index:

```text
PRJ-C -> PRJ-B -> PRJ-A
```

A change in A propagates freshness impact as:

```text
PRJ-A
  -> dependent PRJ-B
  -> dependent PRJ-C
```

This propagation direction is NOT represented by redefining the canonical dependency arrow. It is a reverse-graph traversal derived from consumer-owned direct dependencies.

Normative distinction:

```text
declared dependency traversal for prerequisites:
  consumer -> prerequisite

impact traversal for dependents:
  prerequisite -> dependent
  via generated reverse index
```

## 4.5 Cycle example

A cycle must be written consistently with the canonical convention, for example:

```text
PRJ-A -> PRJ-C
PRJ-B -> PRJ-A
PRJ-C -> PRJ-B
```

which means A depends on C, B depends on A, and C depends on B.

This is:

```text
PROJECTION_DEPENDENCY_CYCLE
```

and blocks the affected regeneration prerequisite graph.

## 4.6 Terminology

Throughout Stage B:

```text
upstream = prerequisite/dependency

downstream = dependent/consumer
```

Do not use `upstream` to mean "the node on the left side of an arrow". The left side is the consumer under the canonical edge convention.

---

# 5. Cross-finding invariants

The following are normative after remediation:

```text
1. A user-facing document may be a fully generated projection only after
   every persistent semantic element it contains has an upstream owning authority.

2. Stage B never demotes RF/SER/STM/BC/CC/MAT/TM/GAP or other accepted
   semantic authority into projection state.

3. Existing Stage A PROJECTION_REPAIR remains valid for bounded
   presentation-only repair with unchanged semantics.

4. working/INDEX.md remains coordinator-owned workflow authority and is
   outside PRJ/RG regeneration lifecycle.

5. Projection classification is explicit by contract, never inferred by path.

6. Canonical dependency edge direction is always CONSUMER -> PREREQUISITE.

7. Upstream/prerequisite closure is found by following declared dependency
   edges from requested consumer toward prerequisites.

8. Downstream stale propagation traverses the generated reverse graph from
   prerequisite toward dependents.

9. Topological execution always runs prerequisites before consumers.

10. Fully-generated projections do not permit hidden human-owned semantic
    islands; unmapped semantic meaning is a migration blocker.
```

---

# 6. Required implementation-plan consequences

Once the Stage B design is approved, the implementation plan MUST include explicit pressure tests for all four remediated boundaries.

At minimum:

```text
SBD pressure A:
Architecture report regeneration cannot modify or erase RF/SER/target semantics.

SBD pressure B:
Stage A editorial PROJECTION_REPAIR remains valid when meaning is unchanged,
while semantic change is rejected from repair and routed to owning authority.

SBD pressure C:
working/INDEX.md is never classified or regenerated as PRJ-* and resume-critical
coordinator state survives Stage B operations.

SBD pressure D:
For PRJ-C -> PRJ-B -> PRJ-A, TARGETED(C) expands A/B as needed, executes
A then B then C, while a new A revision propagates stale state to B then C
without adding them automatically to an unrelated frozen regeneration scope.
```

---

# 7. Design status after this addendum

This addendum does not approve Stage B.

Required next gate:

```text
TARGETED INDEPENDENT DESIGN RE-REVIEW
```

The re-review must explicitly determine whether:

```text
SBD-001 CLOSED
SBD-002 CLOSED
SBD-003 CLOSED
SBD-004 CLOSED
```

and whether the combined authority:

```text
base Stage B design
+
this remediation addendum
```

is precise enough for deterministic implementation planning without reopening architecture.

Do not write the Stage B implementation plan until that re-review approves the design.
