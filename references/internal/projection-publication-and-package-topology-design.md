# Projection Publication and Package Topology Hardening — Design

## Problem

Recent pressure runs exposed three coupled defects in the review skill:

1. Code Quality user-facing projections are registered under `working/projections/code-quality/`, which incorrectly places final capability deliverables inside internal working state.
2. Selected generated outputs can exist as Markdown without accepted Stage B first-generation lifecycle evidence (`PRJ-*` revision, V1–V4, canonical fingerprint, freshness).
3. Undeclared persistent paths can be described as "non-blocking" even though the frozen artifact manifest contract forbids undeclared review-package topology.

## Design

### Capability topology

User-facing capability deliverables live under capability-owned package directories. Code Quality projections move to:

```text
capabilities/code-quality-review/
├── 00-code-quality-findings.md
├── 01-code-quality-summary.md
├── 02-maintainability-hotspots.md
└── 03-roadmap-contribution.md
```

The stable `PRJ-CQ-*` identities remain unchanged. This is a declared path migration, not new semantic identity.

`working/projections/` remains reserved for operational Stage B views such as registry, impact, and regeneration-session state, not capability delivery outputs.

### First-generation publication gate

Every selected generated projection must complete the same lifecycle required by the existing projection contracts before it can satisfy package membership:

```text
registered PRJ identity
→ projection contract revision
→ accepted dependency/selector snapshot
→ generate candidate
→ V1 PASS
→ V2 PASS
→ V3 PASS
→ V4 PASS
→ canonical fingerprint
→ accepted PRJ-*@revN (or NO_CHANGE for an existing revision)
→ CURRENT
```

A file existing on disk, being untracked or committed in Git, carrying YAML metadata, or having an ad-hoc MD5/SHA computed after the fact does not satisfy this gate.

### Undeclared-path policy

Within a frozen review package, any persistent generated path absent from the manifest and absent from an owning contract is blocking structural drift until one of these happens:

- the owning contract is explicitly changed and the manifest is reconciled; or
- the undeclared artifact is removed/migrated without changing semantic ownership.

There is no generic "non-blocking undeclared path" category.

The artifact manifest itself receives an explicit canonical coordinator path so its own persistence is not recursive drift. Project Profile persistence must likewise use a declared coordinator path if materialized as a file; otherwise it remains INDEX/ref state only.

## Completion rule

`PACKAGE_VALID` is legal only when `ARTIFACT_PACKAGE_RECONCILED: ACCEPTED` and every selected generated projection required by package policy has accepted lifecycle evidence. A package with missing lifecycle evidence is `PACKAGE_LIFECYCLE_INVALID` / `REVIEW_PARTIALLY_COMPLETE`, even if every Markdown file exists.
