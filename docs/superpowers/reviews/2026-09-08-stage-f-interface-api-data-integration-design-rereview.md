# Stage F — Interface, API & Data Integration Catalog
## Targeted Design Re-Review

### Review metadata

- Repository: `/home/tod/skills/architecture-code-review`
- Branch: `main`
- Baseline: `9d5c09b6e1dc2686d640e66b1760dcd47640ef42`
- Remediated Design: `docs/superpowers/specs/2026-09-08-stage-f-interface-api-data-integration-design.md`
- Original review: `docs/superpowers/reviews/2026-09-08-stage-f-interface-api-data-integration-design-review.md`
- Review type: targeted independent re-review

Repository verification passed. `origin/main` is an ancestor of the approved
local baseline, tracked files are clean, and the known historical untracked
files were preserved.

### Scope

This re-review covers only DRF-001 through DRF-005, the originally ambiguous
pressure/adversarial scenarios, and bounded regressions adjacent to those
remediations. It does not reopen the approved architecture or perform another
broad Design review.

### Original findings

| Finding | Severity | Original defect | Required closure |
|---|---:|---|---|
| DRF-001 | MEDIUM | Stage F compatibility values had no closed mapping to `CC-*`; Contract Verification was incorrectly described as used “when selected.” | Automatic applicability, exact CC status/classification/adjudication mapping, and candidate-only non-authoritative display. |
| DRF-002 | MEDIUM | `contract_role` and `observed_view` had no validity matrix or tested-role rule. | Closed role/view matrix, invalid-combination handling, orthogonal `TESTED`, and historical fallback. |
| DRF-003 | MEDIUM | INT and `READS_FROM`/`WRITES_TO` source-of-truth, derivation, conflict, and legacy rules were incomplete. | INT authority for new precise access, explicit derivation, `READ_WRITE` expansion, legacy handling, and bounded revalidation. |
| DRF-004 | MEDIUM | `STORE_ONLY` was usable as an IF precision despite being a data-resource concept. | Family-specific precision applicability and safe selector behavior. |
| DRF-005 | MEDIUM | DS procedure/function identity and optional callable IF identity were not explicitly separated. | DS schema-object identity, optional IF callable contract, INT execute edge, explicit cross-reference, and DS-only rule. |

All five original findings were reproducible before remediation and are
re-evaluated below against the current Design text.

### DRF-001 validation

**Result: RESOLVED.**

Section 20 now states that Contract Verification runs automatically when the
existing materially-relevant-contract applicability rule is met. It preserves
`CC-*` as the Test Engineering authority and explicitly maps the normalized
Stage F result vocabulary to existing CC state:

- `COMPATIBLE` requires resolved CC adjudication accepting compatibility;
- `INCOMPATIBLE` requires resolved CC adjudication accepting a material
  mismatch with a material mismatch classification;
- `INDETERMINATE` covers missing/unresolved comparison data and non-final or
  unresolved CC state;
- `NOT_COMPARABLE` means no valid comparison pair and no CC comparison.

The Design also states that non-applicable comparisons have no Stage F result;
catalogs may show only candidate/not-evaluated information, which cannot become
CC, STM, or RF authority. This closes the competing-truth path without adding a
compatibility family or redefining CC ownership.

### DRF-002 validation

**Result: RESOLVED.**

Section 6 contains a closed matrix for all four roles and the valid primary
views. `TESTED` is explicitly valid for every role as an evidence view, not as
a lifecycle or authority replacement. Invalid combinations such as
`CONSUMER_EXPECTATION + IMPLEMENTED` and
`PROVIDER_IMPLEMENTATION + CONSUMED` are rejected or retained only as
unresolved evidence. Historical IF facts without `contract_role` retain their
existing view and receive no inferred role. The dimensions are therefore
orthogonal without being unconstrained or duplicate lifecycles.

### DRF-003 validation

**Result: RESOLVED.**

Sections 12, 14, 35, and the Q4 decision row establish that new precise data
access is authored in INT. A materialized `READS_FROM`/`WRITES_TO` relation
for the same qualified edge is a derived STM navigation relation with an
explicit INT derivation link; a projection may compute it without materializing
it. `READ` derives `READS_FROM`, `WRITE` derives `WRITES_TO`, and `READ_WRITE`
derives both. `EXECUTE`, `DDL`, and `MIGRATION` do not derive either relation
without separate evidence. Relation-only historical facts remain broad and do
not receive inferred access modes. A contradiction makes the precise INT
authoritative, preserves the legacy relation with stale/revalidation
limitation, and routes the conflict to bounded revalidation. Dependency
metadata is explicitly excluded from access authority.

### DRF-004 validation

**Result: RESOLVED.**

Section 17 defines precision as independent from confidence, coverage,
freshness, and observed view, then gives family applicability rules. `STORE_ONLY`
is valid only for DS store facts and DATA_ACCESS INT facts whose parent store is
known; it is invalid for IF, EVENT, FLOW, and non-data INT. IF facts use
`EXACT`, `RESOURCE_BOUNDED`, or `UNRESOLVED`. Section 8 also prohibits
`STORE_ONLY` for unsupported interface properties. The decision table and
selector rule preserve absent historical qualifiers without inferring unsafe
values.

### DRF-005 validation

**Result: RESOLVED.**

Section 11 explicitly defines `PROCEDURE` and `FUNCTION` as DS database-owned
schema-object identities. An IF is added only when an independently evidenced
callable contract or comparison surface is materially present. DS and IF have
distinct stable identities and explicit cross-references; neither aliases or
replaces the other. INT targets the DS object with `EXECUTE` and may reference
the callable IF. DS-only is sufficient when execution is evidenced without an
independent callable contract. This preserves DS, IF, and INT authority
boundaries and avoids duplicate callable identity.

### Affected review dimensions

| Dimension | Result |
|---|---|
| contract_role_observed_view_assessment | PASS |
| data_relation_authority_assessment | PASS |
| db_callable_boundary_assessment | PASS |
| precision_model_assessment | PASS |
| compatibility_authority_assessment | PASS |
| compatibility_result_assessment | PASS |
| test_engineering_boundary | PASS |
| migration_assessment | PASS |
| foundational_completeness | PASS |

### Pressure scenarios PS-F01..PS-F26

| Scenario | Result | Verification |
|---|---|---|
| PS-F01 | GREEN | Provider declaration maps to provided IF with declaration evidence. |
| PS-F02 | GREEN | Consumed IF and INT can link to the exact provider revision. |
| PS-F03 | GREEN | Different paths do not alias; resolved mismatch is incompatible, otherwise indeterminate/not comparable. |
| PS-F04 | GREEN | Dynamic operation remains unresolved at interface precision. |
| PS-F05 | GREEN | Base configuration without call evidence remains a weak hint. |
| PS-F06 | GREEN | Unused generated client does not establish integration use. |
| PS-F07 | GREEN | DS table plus INT READ is authoritative; `READS_FROM` is derived. |
| PS-F08 | GREEN | Cross-owned write remains an STM fact, not automatic RF. |
| PS-F09 | GREEN | Separate INT WRITE facts derive separate `WRITES_TO` relations. |
| PS-F10 | GREEN | Migration authority and runtime writer coexist independently. |
| PS-F11 | GREEN | Dynamic SQL uses bounded/unresolved precision without fabricated target. |
| PS-F12 | GREEN | ORM ambiguity remains an evidence/precision limitation. |
| PS-F13 | GREEN | Unknown Redis key pattern is DS/data INT `STORE_ONLY`, not interface precision. |
| PS-F14 | GREEN | S3 bucket/prefix is recorded only when evidenced. |
| PS-F15 | GREEN | Semantic event does not require duplicate IF. |
| PS-F16 | GREEN | Webhook uses EVENT + IF + INT only when all meanings are material. |
| PS-F17 | GREEN | Secret-bearing connection strings are referenced without secret output. |
| PS-F18 | GREEN | Private hostnames use safe logical identifiers or redaction. |
| PS-F19 | GREEN | Historical broad IF remains valid without inferred qualifiers. |
| PS-F20 | GREEN | Historical store-level DS remains valid without enrichment. |
| PS-F21 | GREEN | Service catalog works without Product mode. |
| PS-F22 | GREEN | Product aggregation retains exact Project revisions. |
| PS-F23 | GREEN | Unavailable Project produces partial availability. |
| PS-F24 | GREEN | Provider change targets dependent consumers/projections only. |
| PS-F25 | GREEN | Weak configuration hint does not become an accepted API call. |
| PS-F26 | GREEN | Missing schema produces CC-backed `INDETERMINATE`, never `COMPATIBLE`. |

**Totals:** 26 total; 26 GREEN; 0 AMBIGUOUS; 0 FAIL.

### Adversarial scenarios AR-F01..AR-F15

| Scenario | Result | Verification |
|---|---|---|
| AR-F01 | GREEN | Declaration and implementation remain distinct views for the same role model. |
| AR-F02 | GREEN | Differing declaration/implementation views are compared through CC, not silently merged. |
| AR-F03 | GREEN | Exact provider Project revision and Product baseline qualification remain inputs. |
| AR-F04 | GREEN | Identical operation/address text does not equate providers without qualification. |
| AR-F05 | GREEN | Dynamic provider selection remains bounded and unresolved where necessary. |
| AR-F06 | GREEN | DS identity includes schema/address context, not table name alone. |
| AR-F07 | GREEN | Continuity requires explicit migration evidence or `supersedes`; no silent merge. |
| AR-F08 | GREEN | Stored callable has distinct DS object, optional IF contract, and INT execute edge. |
| AR-F09 | GREEN | Legacy relation conflict is resolved by precise INT authority plus revalidation. |
| AR-F10 | GREEN | Migration authority does not imply runtime migration execution. |
| AR-F11 | GREEN | Runtime migration access does not imply migration authority ownership. |
| AR-F12 | GREEN | Weak config and unused client remain non-accepted concrete use. |
| AR-F13 | GREEN | Safe path may remain while credential material is excluded. |
| AR-F14 | GREEN | Product projection can separately report unavailable and stale Projects. |
| AR-F15 | GREEN | Indeterminate candidate match yields no compatibility result. |

**Totals:** 15 total; 15 GREEN; 0 AMBIGUOUS; 0 FAIL.

### Migration assessment

**Result: PASS.**

The classification remains `COMPATIBLE_EXTENSION`. Old IF, DS, INT, relation,
EVENT, and CC records retain their identities and meanings. New precision,
role, access, derivation, and callable qualifiers are optional and are not
inferred for historical records. Legacy relation-only facts remain broad and
are revalidated rather than rewritten. Existing CC status/classification/
adjudication remains Test Engineering-owned; Stage F only normalizes it for
catalog display. No Product conversion or destructive migration is required.

### Foundational completeness

**Result: PASS.**

Foundational open questions: **0**. Implementation may choose serialization,
filenames, selector IDs, storage layout, fingerprints, and validation tooling,
but may not choose authority ownership, relation source of truth, callable
boundaries, precision applicability, compatibility meaning, or migration
semantics.

### Regression scan

Bounded regression checks found no new regressions in authority ownership,
IF/INT/DS boundaries, provider/consumer independence, EVENT treatment, access
modes, migration authority, evidence acceptance, matching, compatibility,
Test Engineering ownership, historical compatibility, single-project mode,
Stage E Product semantics, projection/package lifecycle, or redaction.

```text
recommended_direction: B
new_identity_family_required: NO
single_project_compatibility: PASS
stage_e_compatibility: PASS
historical_compatibility: PASS
projection_lifecycle_reuse: PASS
package_authority_reuse: PASS
authority_conflicts: 0
secret_leakage_paths: 0
new_regressions: NONE
```

### New findings

None. No DRR findings were identified.

### Findings summary

| Severity | Count |
|---|---:|
| HIGH | 0 |
| MEDIUM | 0 |
| LOW | 0 |

finding_ids: `NONE`

### Promotion to Design checkpoint readiness

The five original findings are resolved, all originally ambiguous scenarios are
now deterministic, and no new HIGH or MEDIUM finding was introduced. The
remediated Design is ready for the Stage F Design checkpoint.

### Final verdict

```text
DRF-001: RESOLVED
DRF-002: RESOLVED
DRF-003: RESOLVED
DRF-004: RESOLVED
DRF-005: RESOLVED
pressure_scenarios: 26 GREEN / 0 AMBIGUOUS / 0 FAIL
adversarial_scenarios: 15 GREEN / 0 AMBIGUOUS / 0 FAIL
migration: COMPATIBLE_EXTENSION
foundational_open_questions: 0
new_findings: NONE
verdict: STAGE_F_DESIGN_APPROVED
```
