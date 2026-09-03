# Session Orchestration v0.3

This reference is the sole authority for startup/session orchestration.

## Ownership

Owns:

- repository identity and previous-audit discovery/usability;
- lineage-aware source-audit selection;
- Session Intent recommendation and selection;
- Review Suite startup configuration;
- Project Profile lifecycle, migration, and backfill;
- dirty-working-tree baseline choice.

Does not own:

- execution-stage lifecycle or capability registry mechanics (`review-modes-and-orchestration.md`);
- substantive freshness or project-change decision evidence (`revalidation-and-freshness.md`);
- specialist Test Review methodology (`capabilities/test-review/SKILL.md`).

Startup is routing and metadata work, not a blanket repository read:

```text
START
→ repository identity
→ discover previous audit packages
→ validate usability/lineage
→ establish committed baseline + dirty state
→ reuse/refresh/backfill Project Profile
→ recommend/select Session Intent
→ context-sensitive Review Suite Configuration
→ persist/reconcile INDEX
→ substantive workflow
```

Do not inspect every project file in the model context merely to route a session.

## Repository identity and previous audits

Record a stable repository identity from the repository root and canonical remote identity where available. Discover candidate audit packages without selecting by file timestamp alone. For each candidate validate:

- repository identity;
- readable `INDEX.md` and persisted handoffs;
- known previous baseline and current source-audit revision;
- coherent authority/status/revision bindings;
- lineage suitability, including ancestor/descendant relation to the selected baseline.

An unsafe or ambiguous package yields `PREVIOUS_AUDIT_RECONCILIATION_REQUIRED`; stale compact state is not downstream authority. When multiple valid packages compete, rank identity, authority state, and lineage before recency and show the competing choices when user intent remains ambiguous.

## Session Intent

Persist exactly these five intents:

```text
USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND
```

The recommendation matrix is:

| State | Recommendation |
|---|---|
| no previous audit | `NEW` |
| `IN_PROGRESS` + same baseline | `RESUME` |
| `IN_PROGRESS` + changed baseline | `RESUME` with reconciliation |
| `COMPLETE` + same committed baseline | `USE_EXISTING` |
| `COMPLETE` + changed committed baseline | `REVALIDATE` |
| new assurance scope/capability/endpoint | `EXTEND` |

`RESUME_WITH_RECONCILIATION` is a flow/recommendation under `RESUME`, never a sixth persisted intent. Explicit `NEW` remains available in every reusable case.

`USE_EXISTING` performs no technical stage transition solely for startup. It may run metadata-only actions. `REVALIDATE` delegates impact and fresh-evidence semantics to `revalidation-and-freshness.md`; it does not imply a full audit. `EXTEND` adds only the requested assurance scope and does not reopen unrelated accepted stages.

## Review Suite Configuration

For `NEW`, always show this complete startup shape before substantive work:

```text
Architecture Review
  depth: STANDARD_FULL | FORENSIC
  endpoint: REVIEW_ONLY | REVIEW_PLUS_TARGET_ARCHITECTURE | REVIEW_PLUS_TARGET_AND_ROADMAP

Capabilities
  Test Review: OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN

Stack Addenda
  detected automatically; confirmed before substantive use
```

Test Review is a visible capability choice. Lightweight reconnaissance may recommend it when a material automated-test surface exists, but it must never be silently enabled. Stack addenda are lenses, not capabilities. `RESUME` reuses reconciled persisted configuration by default; `REVALIDATE` shows the previous suite as default; `EXTEND` shows only additions.

## Project Profile

Project Profile is cheap local routing/estimation metadata, not architecture evidence. For v0.3 it uses `schema_version: 1` and `collector_version: 1` and contains:

```text
schema_version
collector_version
collected_for_revision
collected_at
baseline_type
substantive:
  files
  lines
  characters
languages:
  <language>:
    files
    lines
    characters
excluded:
  generated
  vendor_or_dependencies
  build_artifacts
  binaries
```

The local collector uses substantive tracked files as its primary inventory. It processes bytes locally and does not require putting each file into model context. Classification is deterministic and ordered:

```text
binary → generated → vendor/dependency → build artifact → substantive text
```

Known binary content is excluded from text line/character totals. Known generated, vendor/dependency, and build paths or markers are excluded from primary totals and counted separately. Recognized source, document, and config extensions map to deterministic language labels; unknown text types map to `Other Text`, never silently disappear.

Profile lifecycle is:

```text
MISSING → COLLECTED
OUTDATED → REFRESHED
OLD_SCHEMA → MIGRATED | BACKFILLED
CURRENT → REUSED
```

When a historical baseline commit is accessible, collect its profile locally. When it is unavailable, record `HISTORICAL_PROFILE_UNAVAILABLE` and do not invent statistics. The current profile remains usable and accepted technical evidence is not invalidated solely for this metadata gap. For `REVALIDATE`, compare both profiles over files, lines, characters, and language footprint when available. Profile totals and deltas never establish architecture materiality.

For a legacy v0.2 `COMPLETE` audit at the same HEAD with no profile, select `USE_EXISTING` and perform `METADATA_BACKFILL`. The audit remains `COMPLETE` and accepted technical gates remain closed. Schema migration is additive and does not reopen technical gates unless it exposes an authority or freshness inconsistency.

## Dirty working tree and baseline

The reproducible default is the exact committed `HEAD`. If the working tree is dirty, show this explicit choice:

```text
1. Audit committed HEAD only — recommended
2. Include working-tree changes as EPHEMERAL snapshot
3. Stop
```

Committed-HEAD-only records dirty state but excludes uncommitted paths from the evidence scope. An `EPHEMERAL` selection records:

```text
git_revision: <commit>
working_tree_snapshot: <deterministic fingerprint>
baseline_type: EPHEMERAL
```

The fingerprint is a digest over sorted bytewise repository-relative changed or untracked paths, their content digests, and tracked-file status. Timestamps are not inputs. EPHEMERAL is never equivalent to a reproducible commit baseline. If the snapshot cannot later be reconstructed, resume/revalidation reports that limitation rather than claiming full recoverability.

## INDEX projection and reconciliation

Persist this compact workflow projection, without treating it as substantive technical authority:

```text
orchestrator_version: 0.3
session_intent
repository_identity
source_audit
source_audit_revision
previous_baseline
current_baseline
baseline_type
working_tree_snapshot
review_suite
stack_addenda
project_profile:
  schema_version
  collector_version
  collected_for_revision
  status
  artifact_or_projection_ref
revalidation:
  change_range
  impact_status
  impact_classification
  affected_domains
  affected_findings
  affected_capabilities
  preserved_domains
  context_expansions
```

Legacy packages missing these fields are legacy state requiring additive reconciliation/backfill, not automatically corrupt state. Before downstream use validate owning-artifact freshness and authority as required by `revalidation-and-freshness.md`.
