# Projection lifecycle authority

This reference is the owning Stage B contract for derived projection identity,
verified content revisions, freshness, drift, and required action. It defines a
projection lifecycle; it does not create or replace semantic authority.

## 1. Explicit classification and authority boundary

An artifact is a projection only when an explicit contract declares it to be a
reconstructable, non-authoritative derived artifact. Classification is never
inferred from path, filename, Markdown shape, or the presence of `INDEX` in a
name. In particular:

```text
projection != semantic authority
path != projection identity
Git commit != projection revision
```

The following are outside automatic projection classification and outside the
`PRJ-*` lifecycle:

```text
working/INDEX.md
STM semantic artifacts
Architecture findings and semantic ledgers
Test Engineering BC/CC/MAT/TM/GAP authorities
```

`working/INDEX.md` is `COORDINATOR_WORKFLOW_AUTHORITY`. Projection impact
analysis and regeneration must not regenerate, overwrite, reconstruct, retire,
or fingerprint it as a generated projection. Its resume-critical state remains
owned by the Stage A session-orchestration contract.

Semantic authorities remain owned by their applicable contracts. A projection
may consume an authority or another projection, but its prose cannot resolve a
semantic conflict, promote manual content into authority, or mutate the
authority to make the projection consistent.

## 1.1 Operational registry view

The shared lifecycle may publish a generated registry view at:

```text
working/projections/registry.md
```

This is a reconstructable navigation/status view over explicitly registered
active and historical `PRJ-*` identities. Its rows may include the projection
ID, owning contract, declared path, identity lifecycle, accepted revision,
freshness, required action, and owning record revision. It is not a second
registry authority: the projection contract and its lifecycle records remain
authoritative, and direct dependency metadata remains owned by each consumer.

The registry view must not include `working/INDEX.md` as a projection, assign
it a `PRJ-*` identity, or copy/derive its resume-critical coordinator state.
The path is intentionally distinct from `working/INDEX.md`; neither path nor
the word `registry` changes explicit classification.

## 1.2 Legacy projection registration

A pre-Stage-B generated or human-readable artifact without accepted `PRJ-*`
lifecycle metadata is legacy state, not an implicitly current projection. Its
registration is an additive migration of identity, contract, dependencies, and
verification metadata; it does not rewrite the artifact or reopen unrelated
semantic work.

The registration path is:

```text
legacy artifact
→ identify capability owner
→ assign PRJ identity
→ define contract
→ resolve dependencies
→ verify against accepted authority
→ establish fingerprint/revision
→ CURRENT
```

The registration record must bind, at minimum, the artifact kind and declared
path, owning capability, stable active `PRJ-*` identity, projection contract and
contract revision, exact dependencies and selector-resolution snapshot, accepted
authority references and revisions, baseline, and the canonical content
fingerprint. A retired identity cannot be reused for a different meaning, and
a Git commit, file timestamp, readable Markdown file, or prior human
acceptance is not a projection revision.

The existing artifact may be used as the registration candidate, but only after
the contract and all required authority/dependency bindings are explicit. The
first accepted `PRJ-*@revN` and fingerprint are established only after the
candidate passes the applicable `V1`–`V4` verification gates. Therefore:

```text
readable legacy file != CURRENT
registered identity != CURRENT
verified fingerprint/revision + V1..V4 = CURRENT
```

Historical or human-edited wording remains a candidate or historical context;
it cannot create, revise, resolve, or strengthen semantic authority merely by
appearing in the legacy artifact. If persistent meaning has no accepted owning
authority, record `PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY` where that
contract applies and do not infer an owner from the artifact's prose.

Registration with missing, stale, conflicting, or otherwise unresolved
authority does not weaken verification. The artifact remains without an
accepted projection revision, is `BLOCKED`, and routes to
`SEMANTIC_REVALIDATION` and the owning semantic migration/revalidation gate.
An insufficient or disputed projection contract/classification routes to
`CONTRACT_ADJUDICATION` instead. Neither route permits `CURRENT`.

## 2. Stable identity and lifecycle

Each independently regeneratable projection receives a stable logical identity
of the form:

```text
PRJ-<stable-id>
```

The ID identifies the logical meaning and contract, not its filesystem path.
A path move does not require a new ID when meaning and contract are unchanged.
An `ACTIVE` identity may be generated and freshness-checked. A `RETIRED`
identity is historical and must never be reassigned to another meaning.

Identity lifecycle and content freshness are separate axes:

```text
identity:  ACTIVE | RETIRED
freshness: CURRENT | STALE | BLOCKED
```

`CURRENT` means the active projection was generated and verified against the
current required semantic dependency snapshot, selector resolution, upstream
projection revisions, and projection contract revision. `STALE` means
freshness is no longer proven; it does not by itself prove that the visible
content is false. `BLOCKED` means the Projection Layer cannot restore
`CURRENT` until a structural prerequisite or semantic authority problem is
resolved.

## 3. Projection revisions and contract revisions

`PRJ-*@revN` is the verified content revision, for example:

```text
PRJ-020@rev7
```

An accepted projection revision is created only after successful generation,
all required verification dimensions pass, and the canonical content
fingerprint changes. A regeneration attempt/session has a separate execution
identity (`RG-*`). Neither identity is a Git commit identity.

The projection contract also has an explicit revision. A contract change
invalidates the projection even when semantic inputs are unchanged:

```text
PROJECTION_CONTRACT_CHANGED
-> STALE
-> required-action: REGENERATE
```

The verified fingerprint is the fingerprint of canonical generated content
recorded by a successful verification. It is compared with the current file
only for artifacts explicitly classified as fully generated projections.

If generation or verification fails, no new accepted projection revision is
created.

## 4. Freshness causes and required action

Required action is orthogonal to identity and freshness:

```text
required-action:
  NONE
  REGENERATE
  PROJECTION_REPAIR
  SEMANTIC_REVALIDATION
  CONTRACT_ADJUDICATION
```

Use `NONE` only when no action is required. An accepted semantic revision,
dependency membership/revision/freshness change, selector resolution change,
upstream projection revision change, or projection contract change marks the
affected projection `STALE` and persists the reason. It does not silently
regenerate the file and does not let projection content become semantic input.

Use `REGENERATE` when accepted inputs and contract are available and the
projection can be deterministically rebuilt. Use `SEMANTIC_REVALIDATION` when
required authority is missing, stale, conflicting, or unresolved. Use
`CONTRACT_ADJUDICATION` when the projection contract or classification itself
is disputed or insufficient to determine the required build/verification
behavior. A blocked projection routes to the owning semantic or contract gate;
the Projection Layer does not invent an authority.

For a projection dependency, the canonical edge is:

```text
consumer -> prerequisite
```

For example, `PRJ-B -> PRJ-A` means B consumes A; it does not make A semantic
authority. A prerequisite becoming stale or receiving a new verified revision
invalidates the consumer's freshness until the consumer is reconciled.

If regeneration verifies byte-identical canonical output, record:

```text
NO_CHANGE
-> keep PRJ-*@revN
-> CURRENT
-> no downstream revision invalidation
```

`NO_CHANGE` is not a new revision and is not equivalent to a Git commit.

## 5. Fully generated content and manual drift

A fully generated projection has no human-owned persistent sections. Anything
that must survive regeneration lives in semantic authority:

```text
Anything that must survive regeneration lives in semantic authority.
```

Manual edits to fully generated projection content are disposable drift, not
semantic input. When the current file fingerprint differs from the last
verified fingerprint without a successful regeneration producing that content,
record:

```text
PROJECTION_CONTENT_DIVERGED
-> STALE
-> required-action: REGENERATE
```

If the classified projection file is absent, record:

```text
PROJECTION_FILE_MISSING
-> STALE
-> required-action: REGENERATE
```

Do not preserve manual sections as hidden authority, extract them into STM or
another semantic ledger automatically, create `.bak`/`.old` forensic copies as
part of regeneration, or silently accept the divergent file as `CURRENT`.
Git remains file history; it is not projection revision authority.

## 6. Verification gate

Generation produces candidate output, not accepted projection state. Before an
active projection may become `CURRENT`, the candidate must pass all applicable
dimensions:

```text
V1 STRUCTURAL
V2 DEPENDENCY / PROVENANCE
V3 CONTRACT COMPLETENESS
V4 AUTHORITY CONSISTENCY
```

The normative gate definitions, V4 authority boundary, failure routing, and
revision-publication algorithm are in [Projection verification and revision
publication](projection-verification.md). After all four gates pass, an
unchanged canonical fingerprint records `NO_CHANGE` and retains the existing
revision; only a changed fingerprint publishes `PRJ-*@rev(N+1)`.

`REGENERATED` is an execution/result observation, not a freshness state and not
an alias for `CURRENT`. A verifier checks the candidate against accepted
authority and contract; it does not adjudicate or rewrite semantic authority.
Any failed dimension leaves the projection without a new accepted revision
and keeps it `STALE` or `BLOCKED` according to the unresolved prerequisite.

## 7. Bounded `PROJECTION_REPAIR`

Stage A `PROJECTION_REPAIR` remains valid and bounded. It is used for
presentation-only correction of an already accepted projection when semantic
meaning and accepted dependencies are unchanged, including wording, structure,
links, terminology, or Mermaid presentation. It uses
`PROJECTION_REVALIDATION` and does not create a human-owned persistent section.

If repair changes evidence, identity/boundary, severity, owner, lifecycle or
target invariant, roadmap dependency, security assumption, or any other
accepted semantic meaning, return:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

Dependency or source/baseline change is not repaired by relabeling it as
`PROJECTION_REPAIR`; it follows the applicable semantic revalidation and
regeneration route.
