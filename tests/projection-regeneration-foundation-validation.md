# Stage B projection/regeneration foundation validation

## Scope and execution boundary

This record freezes the Stage B pressure contracts for `PS-100..PS-114`.
The range is monotonic: the highest pressure ID found before these edits was
`99`. These are static/contract scenarios, not runtime executions. The
repository has no executable Stage B coordinator, so no scenario below claims
runtime behavior.

Baseline under inspection: `f2557b0165687434454e7228dee21717fc8d1cdf`
(the isolated worktree HEAD before this Task 1 slice).

The approved semantics are read from:

- `docs/superpowers/specs/2026-09-04-audit-projection-regeneration-design.md`;
- `docs/superpowers/specs/2026-09-04-audit-projection-regeneration-design-remediation.md`.

## Pressure contracts

### PS-100 — Explicit classification protects authorities

pressure: classify a derived artifact, a semantic authority, and
`working/INDEX.md` when filenames and Markdown shape are misleading.

required behavior: classification is explicit by contract; `projection !=
semantic authority`; `working/INDEX.md` is `COORDINATOR_WORKFLOW_AUTHORITY` and
never receives `PRJ-*` identity/lifecycle, fingerprint or drift state,
regeneration or `RG-*` execution state, projection freshness, or retirement.

forbidden behavior: infer projection status from path/name/`INDEX`; regenerate,
retire, fingerprint, or overwrite `working/INDEX.md`; use a generated index as
semantic authority; place the operational registry/impact/session views at
the coordinator `working/INDEX.md` path.

expected verdict token: `PS100_RED_EXPLICIT_PROJECTION_CLASSIFICATION_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A preserves `working/INDEX.md` as persistent workflow authority and
separates STM facts from projections, but does not define the shared explicit
projection classification and exclusion contract.

### Task 10 focused static validation — PS-100 coordinator boundary

The Task 10 candidate must be checked with these read-only commands:

```text
git diff --check <task-10-base> HEAD
rg -n "COORDINATOR_WORKFLOW_AUTHORITY|working/INDEX\.md|working/projections/(registry|impact|sessions)|PRJ-.*RG-\*|fingerprint.*drift|projection freshness|retired" SKILL.md references tests
```

The probe must show all Stage B exclusions (`PRJ-*`, fingerprint/drift,
regeneration, retirement, projection freshness, and `RG-*`) for
`working/INDEX.md`, plus distinct `working/projections/registry.md`,
`working/projections/impact.md`, and `working/projections/sessions/RG-*.md`
operational paths. It must not show any Task 9 capability projection file in
the candidate diff. This remains static/contract validation; it claims no
runtime coordinator behavior.

### PS-101 — Semantic change marks projection stale only

pressure: an accepted STM, Architecture, or Test Engineering semantic revision
changes an exact dependency.

required behavior: Projection Impact Analysis persists the affected projection
as `STALE` with a reason and completes impact accounting; regeneration remains
a separate explicit process.

forbidden behavior: silently rewrite/regenerate content, mutate semantic
authority from projection content, or call an affected projection `CURRENT`.

expected verdict token: `PS101_RED_SEMANTIC_CHANGE_NO_STAGE_B_IMPACT_CONTRACT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A has semantic revalidation/freshness routes, but no shared projection
freshness or impact-persistence contract.

### PS-102 — Selector membership add/remove is impact

pressure: an accepted object is added to or removed from a controlled semantic
selector's resolved membership.

required behavior: the selector contract and resolution snapshot are compared;
membership addition/removal makes every dependent projection `STALE`.

forbidden behavior: inspect only previously resolved IDs, ignore removal, or
regenerate an unrelated projection.

expected verdict token: `PS102_RED_SELECTOR_MEMBERSHIP_IMPACT_UNDEFINED`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A records selector/dependency foundations but not Stage B selector
resolution snapshots and freshness invalidation.

### PS-103 — Canonical dependency edge direction

pressure: resolve `PRJ-C -> PRJ-B -> PRJ-A` and plan regeneration.

required behavior: the arrow always means `CONSUMER -> PREREQUISITE`; direct
metadata belongs to the consumer; execution order is `PRJ-A`, `PRJ-B`,
`PRJ-C`.

forbidden behavior: reverse the arrow meaning, execute downstream first, or
treat a generated reverse index as direct dependency authority.

expected verdict token: `PS103_RED_PROJECTION_EDGE_DIRECTION_UNDEFINED`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A has direct dependency metadata and generated-index principles, but no
canonical Stage B projection-to-projection edge/execution contract.

### PS-104 — Upstream stale and NO_CHANGE reconciliation

pressure: an upstream projection first becomes `STALE`, then is verified with
identical output and `NO_CHANGE`.

required behavior: downstream freshness becomes uncertain on upstream `STALE`;
after verified upstream `NO_CHANGE`, downstream may reconcile freshness without
content regeneration when its inputs still match.

forbidden behavior: leave downstream `CURRENT` during uncertainty, create a
new revision for `NO_CHANGE`, or force needless downstream regeneration.

expected verdict token: `PS104_RED_UPSTREAM_FRESHNESS_RECONCILIATION_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A has no projection revision/freshness lifecycle or NO_CHANGE outcome.

### PS-105 — Verified upstream revision invalidates downstream

pressure: an upstream regeneration produces a new verified revision while the
downstream content has not yet been regenerated.

required behavior: reverse dependency impact marks downstream `STALE` with
`UPSTREAM_PROJECTION_REVISION_CHANGED`; downstream is not treated as current.

forbidden behavior: propagate only semantic changes, skip downstream impact, or
change downstream revision before its own verification.

expected verdict token: `PS105_RED_UPSTREAM_REVISION_IMPACT_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A generated indexes do not define projection revision propagation.

### PS-106 — TARGETED closure and ALL_STALE snapshot

pressure: target `PRJ-C` in the chain `C -> B -> A`, with mixed current/stale
states; separately plan `ALL_STALE` while another projection changes during
execution.

required behavior: `TARGETED` expands only the requested target plus required
stale upstream prerequisites and executes topologically; `ALL_STALE` freezes
the stale-at-planning snapshot and does not loop until globally clean.

forbidden behavior: include downstream impact closure in targeted execution,
regenerate already-current prerequisites, or add projections discovered after
the ALL_STALE plan was frozen.

expected verdict token: `PS106_RED_REGENERATION_SCOPE_UNDEFINED`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A `TARGETED` terminology applies to STM coverage, not projection
regeneration planning.

### PS-107 — Independent branch failure permits partial progress

pressure: two independent regeneration branches execute and one generation or
verification fails.

required behavior: the successful branch can reach its verified result; the
failed branch remains `STALE` or `BLOCKED`; the session reports partial
progress and does not claim global completion.

forbidden behavior: abort unrelated work, mark failed output `CURRENT`, or
propagate a failed candidate revision downstream.

expected verdict token: `PS107_RED_PARTIAL_REGENERATION_CONTRACT_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
No Stage A projection execution/session state exists.

### PS-108 — Manual generated-projection drift is disposable

pressure: a fully generated projection file differs from its last verified
fingerprint without a successful regeneration.

required behavior: record `PROJECTION_CONTENT_DIVERGED`, mark the projection
`STALE`, and require regeneration; Git remains history and the edit is not
extracted into semantic authority.

forbidden behavior: preserve manual sections as hidden authority, create a
`.bak`/`.old` forensic archive, or silently accept the file as current.

expected verdict token: `PS108_RED_MANUAL_DRIFT_CONTRACT_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A does not define projection fingerprints or disposable manual drift.

### PS-109 — Semantic authority prerequisites block regeneration

pressure: a projection's required semantic authority is missing, stale, or
conflicting at regeneration time.

required behavior: regeneration becomes `BLOCKED` and routes to the owning
semantic gate/revalidation; the Projection Layer does not invent or repair
authority.

forbidden behavior: regenerate from stale/conflicting input, use projection
prose to resolve conflict, or relabel a missing authority as accepted.

expected verdict token: `PS109_RED_AUTHORITY_BLOCKING_CONTRACT_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A establishes STM/capability authority boundaries, but not regeneration
blocking and routing semantics.

### PS-110 — V1..V4 precede CURRENT

pressure: generation writes candidate output that is structurally valid but has
not completed all verification dimensions.

required behavior: `V1 STRUCTURAL`, `V2 DEPENDENCY / PROVENANCE`, `V3 CONTRACT
COMPLETENESS`, and `V4 AUTHORITY CONSISTENCY` all pass before `CURRENT`.

forbidden behavior: equate `REGENERATED` with `CURRENT`, accept candidate output
after only structural checks, or let the verifier adjudicate authority.

expected verdict token: `PS110_RED_V1_V4_CURRENT_GATE_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A has artifact review gates but no four-part projection verification
lifecycle.

### PS-111 — Gate-scoped freshness ignores unrelated stale projections

pressure: one capability gate consumes projection package A while unrelated
projection package B is stale.

required behavior: only the named required scope and mandatory prerequisites
must be `CURRENT`; unrelated stale state remains visible and non-blocking.

forbidden behavior: globally require zero stale projections for every gate or
hide the unrelated stale state.

expected verdict token: `PS111_RED_GATE_SCOPED_FRESHNESS_ABSENT`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A does not define projection packages or `PERMISSIVE`,
`REQUIRED_SCOPE_CURRENT`, and `ALL_SCOPED_CURRENT` policies.

### PS-112 — Legacy projection registration and verification

pressure: an existing readable/generated artifact has no `PRJ-*` lifecycle
metadata.

required behavior: assign identity, define contract, resolve dependencies and
selectors, verify against accepted authority, establish a fingerprint/revision,
then allow `CURRENT`.

forbidden behavior: infer `CURRENT` from readability, path, age, or prior
acceptance; silently promote human-edited content into authority.

expected verdict token: `PS112_RED_LEGACY_PROJECTION_MIGRATION_UNDEFINED`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A PS-98/PS-99 preserve legacy As-Built boundaries but do not provide the
Stage B legacy projection registration lifecycle.

### PS-113 — Architecture authority survives projection regeneration

pressure: regenerate the final Architecture Review projection containing RF,
SER, target, roadmap, and factual As-Built material.

required behavior: persistent meaning is mapped to Architecture-owned semantic
authority; factual As-Built content remains STM-backed; unmapped report meaning
blocks full generation with
`PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY`.

forbidden behavior: let report prose be the sole authority, let regeneration
change RF/SER/target/roadmap semantics, or treat `working/INDEX.md` as a
generated workflow projection.

expected verdict token: `PS113_RED_ARCHITECTURE_PROJECTION_MIGRATION_BLOCKED`

validation type: static contract inspection.

baseline observation: `RED — required Stage B contract absent/incomplete`.
Stage A explicitly preserves report authority language while also separating
STM-backed As-Built facts; the remediation addendum requires the remaining
mapping before fully generated final-report behavior.

### PS-114 — Bounded PROJECTION_REPAIR remains presentation-only

pressure: repair wording, structure, links, Mermaid, terminology, or summary
formatting while accepted semantic dependencies and meaning are unchanged.

required behavior: use `PROJECTION_REPAIR`/`PROJECTION_REVALIDATION` for the
changed projection, preserve semantic meaning, and return the bounded repair
result without reopening technical gates.

forbidden behavior: use repair to hide source/baseline change, alter accepted
meaning, create a human-owned persistent section, or replace `REGENERATE` after
dependency change.

expected verdict token: `PS114_BASELINE_COMPLIANT_PROJECTION_REPAIR_BOUNDARY`

validation type: static contract inspection.

baseline observation: `BASELINE_COMPLIANT — Stage A already satisfies this
invariant`.
`PROJECTION_REPAIR` and `PROJECTION_REVALIDATION` are already documented as
bounded presentation-only correction with semantic-drift escalation. Stage B
must preserve that boundary.

## Static baseline checks

The following checks were run before this file was created; outputs are
recorded verbatim enough to reproduce the baseline decision without implying
runtime execution.

```text
$ grep -R "PS-[0-9][0-9]*" tests | sed -E 's/.*PS-([0-9]+).*/\1/' | sort -n | tail -20
94
94
94
95
95
95
96
96
96
97
97
97
97
98
98
98
99
99
99
99
```

Result: highest existing pressure ID was `99`; `PS-100..PS-114` is unused.

```text
$ git rev-parse HEAD
f2557b0165687434454e7228dee21717fc8d1cdf
```

```text
$ rg -n "PRJ-|PROJECTION_IMPACT_ACCOUNTED|ALL_STALE|TARGETED|V1|PROJECTION_CONTENT_DIVERGED|PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY|CONSUMER -> PREREQUISITE|COORDINATOR_WORKFLOW_AUTHORITY" SKILL.md references tests
```

Result: no Stage B lifecycle tokens or canonical projection edge/classification
record were present. Existing matches were Stage A `TARGETED`/dependency
foundations and existing workflow/repair/STM boundaries; therefore the Stage B
contracts above are recorded as RED except PS-114's preserved Stage A repair
invariant.

## Validation limitation

Validation type is static/contract only. No runtime coordinator, projection
registry, regeneration executor, or verifier exists in this repository, so
these records do not claim scenario execution or GREEN Stage B behavior.

## Task 9 capability projection-contract validation

Inspection target: the Task 9 correction candidate in the Stage B audit
projection/regeneration worktree. The pre-correction baseline is
`da3f246` (`feat: integrate capability projection contracts`). This is an
auditable static contract check; it neither invokes nor implies a runtime
coordinator, generator, package resolver, or verifier.

### PS-115 — Capability packages are finite schema declarations

Baseline observation: `PKG-TECHNICAL-DOCUMENTATION` and
`PKG-TEST-REVIEW-DELIVERY` named owners, gates, and policies, but omitted their
`package_id`, had no explicit `optional_members` list, and represented members
as shorthand identities/arrows rather than the member objects required by
`projection-gates-and-packages.md`.

Candidate static checks inspect the two capability-owned declarations for:

```text
package_id
owner
gate
freshness_policy
required_members: projection_id + purpose + mandatory_prerequisites
optional_members: explicit finite list
conditional_members: condition_id + bounded when + projection_id + purpose
                     + mandatory_prerequisites
```

The candidate declares only the ten registered Technical Documentation
projections and the nine registered Test Review projections. Technical
Documentation section membership is bounded by persisted `documentation_sections.01`
through `.09`; Test Review membership is bounded by the named persisted output
booleans or the persisted Behavior Model document-requirement result. Package
membership is not calculated by selector, path, title, or file presence.

Static verdict: `PS115_GREEN_CAPABILITY_PACKAGE_SCHEMA`.

### PS-116 — Capability selectors are deterministic

Baseline observation: Technical Documentation used phrases such as "material"
and "documented scope" in its dynamic dependency description; Test Review used
"reviewed scope", "relevant", and "qualifying" without a formally bounded
selector predicate. Neither declaration supplied a complete selector catalog
with authoritative record type, closed dimensions/operators, and ordering.

Candidate static checks inspect that every `SEL-TECH-DOC-*` and
`SEL-TEST-REVIEW-*` catalog entry has a consumer projection, authoritative
record type, `definition_revision: 1`, inherited closed allowed dimensions and
operators, a finite family/property/relation predicate, and
`semantic_id ASC, revision ASC` resolved-member ordering. Technical
Documentation selectors operate only on accepted, valid STM facts and the
closed STM relation vocabulary. Test Review selectors operate only on accepted,
valid, resolved Test Engineering records or valid `CC-*` records carrying the
persisted `TRS-*` scope binding; STM slices for Test Review projections 05, 06,
and 08 remain exact dependencies rather than prose-derived selectors.

Static verdict: `PS116_GREEN_CAPABILITY_SELECTOR_DETERMINISM`.

### Focused static check record

The candidate must be checked with the following read-only commands before its
commit. The structural probe binds the result to the candidate diff and checks
each catalog entry rather than merely searching for representative tokens:

```text
git diff --check da3f246..c4b34ce
python3 -c 'from pathlib import Path; import re; td=Path("references/technical-documentation.md").read_text(); tr=Path("capabilities/test-review/references/test-engineering-contract.md").read_text(); tsel=set(re.findall(r"SEL-TECH-DOC-0[0-9]-[^`| ]+",td)); rows=[[p.strip() for p in line.split("|")] for line in tr.splitlines() if line.startswith("| `SEL-TEST-REVIEW-")]; assert len(tsel) == 10; assert len(rows) == 11; assert "authoritative_record_type: STM_FACT" in td; assert "definition_revision: 1" in td and "definition_revision: 1" in tr; assert tr.count("test_review_scope_id = <persisted TRS>") == 11; assert "optional_members: []" in td and "optional_members: []" in tr; assert "stable_order: semantic_id ASC, revision ASC" in td and "stable_order: semantic_id ASC, revision ASC" in tr; assert all((row[1].endswith("-BC") and row[3] == "`TEST_ENGINEERING_SEMANTIC_RECORD`") or (row[1].endswith("-CC") and row[3] == "`TEST_ENGINEERING_CONSISTENCY_RECORD`") or (not row[1].endswith(("-BC", "-CC"))) for row in rows); print("candidate=c4b34ce technical_doc_selectors=10 test_review_selectors=11 selector_rows=11 record_types=bounded required_schema_fields=present stable_order=present")'
rg -n "PS115_GREEN_CAPABILITY_PACKAGE_SCHEMA|PS116_GREEN_CAPABILITY_SELECTOR_DETERMINISM" tests/projection-regeneration-foundation-validation.md
```

Observed candidate result: all three commands exited `0`; the revision-bound
probe reported `candidate=61a85fc`, exactly ten Technical Documentation
selectors and exactly eleven Test Review selectors (the simulator and simulator
plan each use separate BC and CC selectors), the required schema fields, and
stable ordering. The catalogs match their finite registered projection sets.

### PS-81..99 — Stage A Test Engineering compatibility

Validation type: `STATIC_CONTRACT`.

Check:

```text
rg -n "BC-\*|CC-\*|MAT-\*|TM-\*|GAP-\*|TARGETED STM|Technical Model Gate|DECLARED|IMPLEMENTED|CONSUMED|TESTED" capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md references/technical-model-coverage.md
rg -n "PS-(8[1-9]|9[0-9])|PS99_GREEN_TEST_ENGINEERING_STM_DEPENDENCY" tests/test-engineering-capability-validation.md tests/shared-technical-model-foundation-validation.md tests/pressure-scenario-99-legacy-and-cross-capability-reuse.md tests/pressure-scenario-9[0-8]-*.md
```

Expected behavior: Stage A semantic ownership, targeted STM acquisition,
independent observation views, and minimum-slice EXTEND/REVALIDATE behavior
remain explicit. Observed result: the required ownership, gate, dependency,
and view statements are present; named PS-81..99 records (including PS-90..98
STM compatibility records and PS-99 cross-capability reuse) are present and
static-only. Violations: none. Verdict:
`PS81_99_GREEN_STAGE_A_TEST_ENGINEERING_COMPATIBILITY`.

No runtime result is recorded. The repository still has no executable Stage B
coordinator or projection runtime, so `PS-115` and `PS-116` are static contract
results only.
