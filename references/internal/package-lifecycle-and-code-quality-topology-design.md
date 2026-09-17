# Package Lifecycle and Code Quality Topology Hardening — Design

## Problem

The latest pressure run reached a structurally improved package but still exposed three contract gaps:

1. selected Stage B projections existed as Markdown without accepted `PRJ-*` revision, V1-V4 verification, canonical fingerprint, or persisted `CURRENT` freshness;
2. undeclared files were classified as non-blocking despite the package contract forbidding undeclared generated paths;
3. Code Quality user-facing outputs were registered under `working/projections/code-quality/`, making a capability delivery surface look like internal working state.

## Design

### 1. Code Quality delivery topology

Keep existing stable projection identities. Change only their declared artifact paths to capability-owned delivery paths:

```text
capabilities/code-quality-review/00-findings-view.md
capabilities/code-quality-review/01-summary.md
capabilities/code-quality-review/02-maintainability-hotspots.md
capabilities/code-quality-review/03-roadmap-contribution.md
```

`working/projections/` remains reserved for shared Stage B operational views such as registry, impact, and `RG-*` session records.

A path migration does not create new `PRJ-*` identities. Existing packages using legacy Code Quality paths remain historical input and require explicit projection path migration/reconciliation before being considered current under the new contract.

### 2. First-generation lifecycle is part of package validity

Filesystem existence is not enough for a selected projection. `ARTIFACT_PACKAGE_RECONCILIATION` must verify, for every selected Stage B projection:

```text
active registered PRJ-* identity
projection contract revision
accepted dependency/selector snapshot
V1 PASS
V2 PASS
V3 PASS
V4 PASS
canonical fingerprint
accepted PRJ-*@revN or verified NO_CHANGE
freshness: CURRENT
```

Missing lifecycle evidence returns `PROJECTION_LIFECYCLE_INCOMPLETE` and prevents `ARTIFACT_PACKAGE_RECONCILED` and `PACKAGE_VALID`.

A checksum computed ad hoc during reconciliation is not a canonical lifecycle fingerprint.

### 3. Strict undeclared-path policy

There is no `non-blocking undeclared path` category. Every actual generated review-package file or directory must be declared by the frozen manifest or an owning operational contract.

Canonical coordinator/meta paths are declared explicitly:

```text
working/ARTIFACT_LAYOUT_MANIFEST.md
working/project-profile.md   # when Project Profile is materialized as a file
```

An old root-level `ARTIFACT_LAYOUT_MANIFEST.md` is legacy drift and must be migrated or removed before package reconciliation can pass.

### 4. Package verdict vocabulary

Use mutually exclusive structural verdicts:

```text
PACKAGE_VALID
PACKAGE_INCOMPLETE
PACKAGE_LAYOUT_INVALID
PACKAGE_LIFECYCLE_INVALID
```

`PACKAGE_VALID` is permitted only when `ARTIFACT_PACKAGE_RECONCILED: ACCEPTED`.

### 5. INDEX repair boundary

`working/INDEX.md` is reconciled from owning accepted gates and projection lifecycle state. An execution-plan checkbox or prose `COMPLETE` cannot by itself justify changing an INDEX capability, coverage, discovery, or projection state.

## Regression target

The following must be rejected:

```text
selected tech-doc Markdown exists
+ no PRJ revision/V1-V4/fingerprint/CURRENT
+ two undeclared files
+ stale INDEX
→ PACKAGE_VALID
```

Required result before remediation:

```text
PACKAGE_LIFECYCLE_INVALID or PACKAGE_LAYOUT_INVALID
ARTIFACT_PACKAGE_RECONCILED: NOT_ACCEPTED
FINAL_WORKFLOW_AUTHORITY_RECONCILED: NOT_ACCEPTED
REVIEW_PARTIALLY_COMPLETE
```
