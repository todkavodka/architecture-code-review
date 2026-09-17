# Artifact Layout and Package Completeness

This reference owns deterministic review-package topology, frozen artifact
layout, final filesystem/package reconciliation, and package-structural
readiness. It does not own semantic meaning, projection identity, capability
selection, or review methodology. Existing owner contracts still define
artifact semantics; this contract defines where resolved artifacts are allowed
to live and how package completeness is proven.

## 1. Artifact layout is resolved state, not agent preference

Before the first substantive persistent review artifact is written, the
coordinator resolves and persists one frozen:

```text
ARTIFACT_LAYOUT_MANIFEST
```

The canonical persistent manifest path, relative to the review-package root,
is:

```text
working/ARTIFACT_LAYOUT_MANIFEST.md
```

The manifest itself is coordinator routing state and MUST be included in the
frozen manifest as an allowed coordinator path. Storing it elsewhere requires
an explicitly accepted local layout convention; a convenient root-level
`ARTIFACT_LAYOUT_MANIFEST.md` is not implicitly exempt from layout rules.

The manifest records at minimum:

```text
package_root
layout_source: ESTABLISHED_LOCAL_CONVENTION | CANONICAL_DEFAULT
selected_mode
selected_endpoint
semantic_authority_paths
requested_projection_paths
capability_owned_paths
required_working_paths
conditional_paths
allowed_operational_paths
coordinator_meta_paths
```

A path not present in the frozen manifest or directly declared by an owning
contract is not writable review topology merely because it looks tidy, matches
a semantic category, or was created by a worker.

The manifest is coordinator routing state. It does not create semantic
authority, projection authority, or a second artifact registry.

### Project Profile persistence

Project Profile is routing metadata. When it is materialized as a file in the
review package, the canonical coordinator path is:

```text
working/project-profile.md
```

and that path must appear in `coordinator_meta_paths` before creation. If the
workflow stores Project Profile only as `INDEX.md` state or an external
reference, do not create a convenience file.

There is no generic category of "non-blocking undeclared file". A persistent
review-package file is either declared/contract-owned or it is layout drift
until reconciled.

## 2. Package root resolution

If the repository already contains an established, coherent review-package
convention compatible with the selected workflow, the coordinator may preserve
it. The decision must be evidenced and persisted before substantive writes.

Otherwise use exactly:

```text
docs/reviews/architecture-review/
```

Do not shorten the default to `docs/reviews/`, invent a sibling root, or move
files after generation merely for presentation.

Once frozen, the package root cannot change inside the same review execution
without explicit layout reconciliation. A later path change is a package
migration decision, not a convenience rename.

## 3. Canonical Architecture package roles

Absent an accepted established local convention that preserves the same roles,
Architecture Review uses:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md          # when endpoint selects Target Architecture
├── 04-remediation-roadmap.md          # when endpoint selects Roadmap
├── capabilities/
│   └── <capability-owned user-facing outputs>
├── technical-documentation/
│   └── <selected Technical Documentation projections>
└── working/
    ├── README.md
    ├── INDEX.md
    ├── ARTIFACT_LAYOUT_MANIFEST.md
    └── <mode/capability working artifacts declared by contract>
```

These role assignments are binding:

```text
01 = human-readable Architecture Review delivery projection
02 = Architecture semantic findings ledger
03 = Target Architecture semantic authority when selected
04 = Remediation Roadmap semantic authority when selected
```

The executing agent MUST NOT:

- omit `02-authoritative-findings-ledger.md` while claiming Architecture findings are complete;
- renumber Target Architecture or Roadmap to fill a visual gap;
- replace semantic authority with a similarly named working file;
- move Architecture authority into a capability projection directory;
- infer a new package numbering scheme from requested capability count.

## 4. Mode-specific working artifacts are executable manifest inputs

The mode-specific artifact sets in `review-modes-and-orchestration.md` are not
examples once mode is selected. They are inputs to
`ARTIFACT_LAYOUT_MANIFEST`.

For `STANDARD_FULL` and `FORENSIC`, every unconditional working artifact
declared by the selected mode must appear in the manifest and must exist before
package closeout. A conditional correction or re-review artifact is included
only when its documented trigger occurred.

Therefore:

```text
selected mode artifact list
→ resolve unconditional members
→ resolve triggered conditional members
→ freeze exact working paths
→ create/write only as work reaches each member
```

Missing unconditional or triggered conditional files return:

```text
REQUIRED_ARTIFACT_MISSING
```

A mode artifact cannot be silently replaced by one broad combined note unless
the owning contract explicitly permits that substitution.

## 5. Capability output ownership and paths

Capability outputs retain the paths and identities declared by their owning
contracts. Umbrella orchestration may link, summarize, or include them in a
resolved package, but it cannot invent replacement aggregate paths.

Examples of invalid umbrella-created outputs unless separately registered by
an approved projection contract:

```text
05-test-engineering.md
06-code-quality.md
working/test-engineering.md
working/code-quality.md
```

A human-readable capability name is not a filesystem path contract.

For Code Quality, registered Stage B user-facing output paths are owned by
`capabilities/code-quality-review/references/code-quality-projection.md`:

```text
capabilities/code-quality-review/00-code-quality-findings.md
capabilities/code-quality-review/01-code-quality-summary.md
capabilities/code-quality-review/02-maintainability-hotspots.md
capabilities/code-quality-review/03-roadmap-contribution.md
```

Only selected registered members are required. The former
`working/projections/code-quality/*` delivery paths are superseded and must not
be used as current Code Quality publication locations.

For Test Engineering, use the exact capability-owned output/projection paths
declared by `capabilities/test-review/SKILL.md` and
`capabilities/test-review/references/test-engineering-contract.md`. Do not
derive umbrella numbering from the Architecture package.

For Technical Documentation, use the exact selected `PRJ-TECH-DOC-*` paths
declared by `technical-documentation.md`. "All outputs" means the finite set of
selected registered projections, not one aggregate document.

If a requested output has no declared path/registration and no approved local
convention resolves it, stop with:

```text
ARTIFACT_PATH_NOT_DECLARED
```

Do not invent a path to keep execution moving.

## 6. No inferred directory taxonomy

Semantic taxonomy does not imply filesystem taxonomy.

Examples:

```text
STM domain "Components / Runtime Units" != permission to create working/technical-model/components/
STM domain "Provided Interfaces"       != permission to create working/technical-model/interfaces/
STM domain "Authentication / Trust"    != permission to create working/technical-model/auth/
```

Directories may be created only when at least one manifest-declared artifact or
owning contract requires that exact directory.

Create directories lazily at first required write. Do not run broad speculative
`mkdir -p` for directories that may never receive declared artifacts.

An undeclared generated directory inside the review package is:

```text
ARTIFACT_LAYOUT_DRIFT
```

Empty speculative directories must be removed before closeout; their presence
proves the actual tree is not reconciled with the frozen manifest.

## 7. Allowed operational paths

Operational Stage B history may use paths explicitly defined by owning
contracts, for example:

```text
working/projections/registry.md
working/projections/impact.md
working/projections/sessions/RG-*.md
```

These are operational views, not capability delivery outputs. Their existence
does not authorize arbitrary sibling directories.

Likewise `working/evidence/` is valid when the selected mode/evidence contract
declares shared `WS-*` worksets. Its validity comes from the contract, not from
a generic permission to create utility directories.

## 8. Projection publication completeness

Filesystem presence and projection acceptance are separate checks.

For every selected generated projection required by the resolved package,
package reconciliation must bind accepted lifecycle evidence from
`projection-lifecycle.md` and the owning projection contract:

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
freshness: CURRENT
```

For first generation there is no pre-existing revision to preserve with
`NO_CHANGE`; successful publication establishes the initial accepted
`PRJ-*@revN` (normally `rev1` under the owning allocation rules).

The following do not satisfy projection publication:

```text
Markdown file exists
Git tracked/untracked status
Git commit SHA
file timestamp
YAML header without lifecycle authority
ad-hoc MD5/SHA computed after generation
worker says generated
package tree contains the expected filename
```

If a selected projection file exists but any required lifecycle element is
missing, record:

```text
PACKAGE_LIFECYCLE_INVALID
```

and do not accept the package gate that requires that projection to be current.

## 9. Artifact package reconciliation

Before final editorial acceptance and before `REVIEW_COMPLETE`, perform:

```text
ARTIFACT_PACKAGE_RECONCILIATION
```

Compare:

```text
frozen ARTIFACT_LAYOUT_MANIFEST
        ↕
actual filesystem/package tree
        ↕
working/INDEX.md artifact registry
        ↕
owning semantic/projection/capability contracts
        ↕
selected projection lifecycle records
```

The accepted result is exactly:

```text
ARTIFACT_PACKAGE_RECONCILED
```

Otherwise persist:

```text
ARTIFACT_PACKAGE_RECONCILIATION_REQUIRED
```

At minimum verify:

1. the actual package root equals the frozen root;
2. every unconditional mode artifact exists;
3. every triggered conditional artifact exists;
4. every selected endpoint authority exists at its declared role/path;
5. every selected capability output uses its declared capability path;
6. every actual persistent review file is declared by the manifest or an allowed owning contract;
7. no semantic authority is substituted by a projection or working note;
8. no projection path contradicts its registered projection contract;
9. every selected package projection has accepted lifecycle evidence and `CURRENT` freshness when required by package policy;
10. no undeclared generated directory remains;
11. no empty speculative undeclared directory remains;
12. `working/INDEX.md` artifact registry and actual tree agree;
13. actual role, owner, and classification of each final artifact agree with the owning contract;
14. coordinator meta files are present only at manifest-declared paths.

## 10. Reconciliation failures

Use these failures consistently:

```text
ARTIFACT_PATH_NOT_DECLARED
  a worker wants to write a path not resolved by manifest/owning contract

REQUIRED_ARTIFACT_MISSING
  a required unconditional or triggered artifact is absent

ARTIFACT_LAYOUT_DRIFT
  actual package tree contains undeclared persistent path/directory or wrong root

ARTIFACT_ROLE_MISMATCH
  file exists but its semantic/projection/capability role contradicts the contract

PACKAGE_LIFECYCLE_INVALID
  selected generated projection exists but lacks accepted lifecycle evidence
  required by its package policy

ARTIFACT_PACKAGE_RECONCILIATION_REQUIRED
  final expected-vs-actual/lifecycle reconciliation has not passed
```

Do not repair a role mismatch by merely renaming a file if its contents or
authority were produced through the wrong workflow. Route semantic/projection
ownership problems to their owning gate.

An undeclared persistent path is never downgraded to a generic non-blocking
exception. It must be removed, moved to an already-declared path when that move
is semantically safe, or explicitly added through the owning contract and
manifest reconciliation.

## 11. Completion gate and verdict vocabulary

A review may return `REVIEW_COMPLETE` only when both are accepted:

```text
FINAL_WORKFLOW_AUTHORITY_RECONCILED
ARTIFACT_PACKAGE_RECONCILED
```

Package verdicts are mutually exclusive:

```text
PACKAGE_VALID
  only when ARTIFACT_PACKAGE_RECONCILED is ACCEPTED

PACKAGE_INCOMPLETE
  required/selected declared artifacts are missing

PACKAGE_LAYOUT_INVALID
  undeclared/wrong-root/role-mismatched persistent topology exists

PACKAGE_LIFECYCLE_INVALID
  required selected projections lack accepted publication lifecycle evidence
```

Do not return `PACKAGE_VALID` in the same result that reports
`ARTIFACT_PACKAGE_RECONCILED: NOT_ACCEPTED`.

A review whose semantic analysis is otherwise complete but whose artifact
package is missing, invented, misnumbered, misplaced, lifecycle-incomplete, or
unreconciled returns:

```text
REVIEW_PARTIALLY_COMPLETE
```

with the exact layout/package/lifecycle blockers.

The following never prove package completeness:

```text
all intended topics were discussed
all Markdown files rendered
all workers reported done
artifact count looks plausible
INDEX says COMPLETE
final prose looks coherent
files have hashes computed after generation
```

## 12. Canonical regression cases

### Layout regression

Invalid:

```text
FORENSIC + REVIEW_PLUS_TARGET_AND_ROADMAP
→ write package under docs/reviews/
→ omit 02-authoritative-findings-ledger.md
→ number Target as 02 and Roadmap as 03
→ invent 05-test-engineering.md and 06-code-quality.md
→ invent working/technical-model/components/, interfaces/, auth/, ...
→ mark REVIEW_COMPLETE
```

Required result:

```text
ARTIFACT_LAYOUT_DRIFT
REQUIRED_ARTIFACT_MISSING
ARTIFACT_PACKAGE_RECONCILIATION_REQUIRED
REVIEW_PARTIALLY_COMPLETE
```

### Lifecycle regression

Invalid:

```text
selected Technical Documentation projection exists as Markdown
→ PRJ revision absent
→ V1-V4 absent
→ canonical fingerprint absent
→ freshness absent
→ compute MD5 after the fact
→ call package valid
```

Required result:

```text
PACKAGE_LIFECYCLE_INVALID
ARTIFACT_PACKAGE_RECONCILIATION_REQUIRED
REVIEW_PARTIALLY_COMPLETE
```

Valid:

```text
resolve/freeze ARTIFACT_LAYOUT_MANIFEST
→ use established local convention OR canonical default
→ resolve mode/endpoint/capability members
→ create directories lazily
→ write artifacts only at declared paths
→ complete owner/projection publication gates
→ reconcile actual tree + INDEX + lifecycle records
→ ARTIFACT_PACKAGE_RECONCILED
→ final editorial acceptance
→ FINAL_WORKFLOW_AUTHORITY_RECONCILED
→ REVIEW_COMPLETE
```
