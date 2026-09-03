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

The local collector uses substantive tracked files as its primary inventory. For a
commit-bound baseline, inventory is the exact Git tree at
`collected_for_revision`; current working-tree content is never substituted. It
processes bytes locally and does not require putting each file into model
context. Every file belongs to exactly one primary classification bucket, using
repository-relative POSIX-style paths with path separators normalized to `/`.
Paths are not case-folded. Classification precedence is exactly:

```text
1. binary
2. generated
3. vendor/dependency
4. build artifact
5. substantive text
```

### Deterministic classification

A tracked or snapshot file is binary when Git identifies it as binary for diff
purposes while the relevant Git object is available, or when its first 8192 raw
bytes contain a NUL byte. Binary classification never comes from an extension
alone. A binary file is counted only in `excluded.binaries`; it contributes no
text lines or characters.

A non-binary file is generated when its normalized path has a component exactly
equal to `generated`, `gen`, or `dist-generated`; when `.gitattributes` in the
inspected tree gives it `linguist-generated=true`; or when one of its first five
logical text lines contains one of these exact case-insensitive markers:
`@generated`, `generated file`, `do not edit`, or `code generated`. The only
repository-declared metadata inputs for this contract are these exact
`.gitattributes` values: `true` marks generated and `false` marks
non-generated/source-owned. Metadata is evaluated before heuristic marker
matching and wins over it. Repetitive-looking content is not a rule.

A non-binary, non-generated file is vendor/dependency material when a normalized
path component exactly equals one of `node_modules`, `vendor`, `vendors`,
`third_party`, `third-party`, `deps`, `dependencies`, `packages-cache`,
`.venv`, or `venv`, or when it is Git submodule content in the inspected tree.
The project-owned source directory `packages/` is not dependency material by
name alone.

A remaining file is a build artifact when a normalized path component exactly
equals one of `build`, `dist`, `out`, `target`, `coverage`, `.next`, `.nuxt`, or
`.cache`. `.gitattributes linguist-generated=false` explicitly marking material
under such a path as source-owned overrides this path rule; without that exact
metadata the path rule wins.

Everything else that decodes as text is substantive text. If UTF-8 decoding
fails, a non-binary file is classified as binary for Project Profile purposes.

### Deterministic language mapping and text counts

Language mapping is filename-first, case-sensitive, and never uses model
inference. Suffix rules match the final suffix of the basename exactly;
directory names do not participate.

| Filename suffix | Language |
|---|---|
| `.py` | Python |
| `.js`, `.mjs`, `.cjs` | JavaScript |
| `.ts`, `.tsx` | TypeScript |
| `.jsx` | JavaScript JSX |
| `.rs` | Rust |
| `.go` | Go |
| `.java` | Java |
| `.kt`, `.kts` | Kotlin |
| `.c` | C |
| `.h` | C Header |
| `.cpp`, `.cc`, `.cxx` | C++ |
| `.hpp`, `.hh`, `.hxx` | C++ Header |
| `.cs` | C# |
| `.rb` | Ruby |
| `.php` | PHP |
| `.swift` | Swift |
| `.sh`, `.bash` | Shell |
| `.ps1` | PowerShell |
| `.sql` | SQL |
| `.html`, `.htm` | HTML |
| `.css` | CSS |
| `.scss` | SCSS |
| `.less` | Less |
| `.vue` | Vue |
| `.svelte` | Svelte |
| `.md`, `.markdown` | Markdown |
| `.rst` | reStructuredText |
| `.json` | JSON |
| `.yaml`, `.yml` | YAML |
| `.toml` | TOML |
| `.xml` | XML |

Exact filenames map as follows: `Dockerfile` → Dockerfile, `Makefile` → Make,
`CMakeLists.txt` → CMake, `requirements.txt` → Requirements,
`pyproject.toml` → TOML, and `package.json` → JSON. For text files not matched
by these exact filename or suffix rules, language is `Other Text`; unknown text
extensions are never discarded.

Decode text as UTF-8. Remove a UTF-8 BOM before counting, then normalize CRLF
and lone CR to LF. Character count is Unicode scalar value/code point count
after those transformations, not byte count. Empty text has zero lines;
otherwise line count is the number of LF characters plus one when normalized
text does not end in LF. Thus `""` → 0, `"a"` → 1, `"a\\n"` → 1,
`"a\\nb"` → 2, and `"a\\nb\\n"` → 2.

Each substantive text file contributes exactly one to `substantive.files` and
one to exactly one `languages.<language>.files` bucket. Excluded files
contribute only their exclusion-category file count; the approved schema does
not invent excluded line/character totals.

For historical backfill, collect from the historical Git tree/object content.
If required Git objects are unavailable, record
`HISTORICAL_PROFILE_UNAVAILABLE`; do not substitute current filesystem content
or partially reconstruct historical statistics.

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
working_tree_snapshot_algorithm: sha256-v1
baseline_type: EPHEMERAL
```

### Canonical EPHEMERAL snapshot

The snapshot record set contains modified, added, deleted, renamed, and
type-changed tracked files, plus untracked files not ignored by Git. Ignored
files are excluded. Use repository-relative POSIX-style paths, with separators
normalized to `/`, and do not case-fold them. Normalize Git status letters to
these canonical states: modified `M`, tracked addition `A`, deletion `D`,
rename `R`, type change `T`, and untracked `U`. A rename is one record with the
old and new path and the new-content digest. A deletion has
`content_digest = -`; no digest is computed for it. If Git exposes composite
status letters, map them to the applicable canonical semantic state before
serialization.

For status inventory, use Git's porcelain status with rename detection fixed at
50% similarity. A reported rename is normalized to `R`; a copy is represented
as a tracked addition `A`. Otherwise apply
the first matching state in this order when composite status letters occur:
`D`, `T`, `A`, `M`. Untracked entries are `U`. This makes the status mapping
independent of index/worktree column placement; a rename record always carries
the old path, new path, and new-content digest.

Content digests are SHA-256 over raw working-tree bytes exactly as present;
there is no newline normalization. Render digests as lowercase hexadecimal,
exactly 64 characters. The snapshot fingerprint does not include timestamps,
inode numbers, filesystem ordering, absolute paths, or other filesystem
metadata.

Serialize ordinary records as the UTF-8 bytes of:

```text
STATUS<TAB>PATH<TAB>CONTENT_SHA256<LF>
```

Serialize a rename as:

```text
R<TAB>OLD_PATH<TAB>NEW_PATH<TAB>CONTENT_SHA256<LF>
```

`<TAB>` is ASCII 0x09 and `<LF>` is ASCII 0x0A. Do not escape ordinary spaces
or non-ASCII UTF-8 path bytes. If a path contains TAB or LF, encode that path
field using a JSON string with `ensure_ascii=false`, including surrounding
quotes; apply the rule independently to old and new rename paths. Sort records
by their complete serialized UTF-8 byte sequence in ascending byte order and
concatenate them without a header or footer. The final
`working_tree_snapshot` is the lowercase hexadecimal SHA-256 of those
concatenated bytes.

If there are no included dirty records, the baseline is not EPHEMERAL and no
snapshot fingerprint is created. `working_tree_snapshot_algorithm: sha256-v1`
is stable under `collector_version: 1`; incompatible future hashing changes
require a new fingerprint algorithm version. EPHEMERAL is never equivalent to
a reproducible commit baseline. If the snapshot cannot later be reconstructed,
resume/revalidation reports that limitation rather than claiming full
recoverability.

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
working_tree_snapshot_algorithm
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
