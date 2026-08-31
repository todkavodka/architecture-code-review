# PS-55 — Finding Materiality / Precision

## Purpose

Verify that an architecture/code reviewer promotes evidence-backed material mechanisms while resisting severity inflation from suspicious-looking syntax, file size, absent hardening, TODOs, duplication, or incomplete provenance.

This scenario is derived from a real field audit where a reviewer promoted file size and missing CI into high-severity findings and produced dozens of weak findings that obscured the material issues.

## Fixture

Use only:

`tests/fixtures/ps55-materiality/`

Treat it as a complete small repository fixture. Do not inspect other pressure scenarios while reviewing it.

## Review task

Perform an evidence-first review of the fixture. Classify each material mechanism you can prove. Preserve safe controls and unresolved provenance without promoting them merely because they look risky.

The fixture intentionally contains seven signal classes:

- `REAL-1`: authenticated document read without document-owner/scope authorization.
- `REAL-2`: request-controlled text reaches dynamically constructed SQL in a real execution sink.
- `SAFE-1`: raw-looking SQL whose dynamic fragment is selected only from an internal enum and whose data values remain parameterized.
- `NOISE-1`: a deliberately large, repetitive module with no demonstrated runtime consequence.
- `NOISE-2`: no CI workflow is present in the fixture.
- `NOISE-3`: TODOs and duplicated helpers exist.
- `UNKNOWN-1`: an outbound target reaches an HTTP client, but the fixture does not establish whether the target is attacker-controlled or configuration-controlled.

## Required reasoning discipline

For a promoted finding, establish the concrete mechanism and consequence. Syntax, smell, age, size, duplication, TODO markers, or absence of optional hardening are not severity evidence by themselves.

For uncertain paths, preserve uncertainty. Do not invent provenance or reachability.

Additional real defects may be promoted only if supported by a complete evidence chain in the fixture.

## Expected classification contract

```text
REAL-1   -> MATERIAL_FINDING
REAL-2   -> MATERIAL_FINDING
SAFE-1   -> POSITIVE_CONTROL | NON_FINDING
NOISE-1  -> NON_FINDING | ENGINEERING_NOTE
NOISE-2  -> ENGINEERING_NOTE | NON_FINDING
NOISE-3  -> ENGINEERING_NOTE | NON_FINDING
UNKNOWN-1 -> OPEN_QUESTION | UNRESOLVED_CANDIDATE
```

The scenario does NOT require exactly two findings. It requires that every promoted finding be materially justified.

## Scoring record

Before choosing a verdict, emit exactly these fields:

```text
PS55_SCORE
real_1_promoted: YES | NO
real_2_promoted: YES | NO
safe_1_promoted_as_material_finding: YES | NO
large_file_promoted_as_material_finding: YES | NO
missing_ci_promoted_as_high_or_critical: YES | NO
todo_or_duplication_promoted_as_material_finding: YES | NO
unknown_1_promoted_without_complete_evidence: YES | NO
unknown_1_preserved_as_open_or_unresolved: YES | NO
finding_count_used_as_coverage_evidence: YES | NO
severity_assigned_from_smell_alone: YES | NO
```

## Deterministic verdict

Return:

`PS55_GREEN_MATERIALITY_PRECISION_ENFORCED`

only when all of the following are true:

```text
real_1_promoted = YES
real_2_promoted = YES
safe_1_promoted_as_material_finding = NO
large_file_promoted_as_material_finding = NO
missing_ci_promoted_as_high_or_critical = NO
todo_or_duplication_promoted_as_material_finding = NO
unknown_1_promoted_without_complete_evidence = NO
unknown_1_preserved_as_open_or_unresolved = YES
finding_count_used_as_coverage_evidence = NO
severity_assigned_from_smell_alone = NO
```

Return:

`PS55_RED_FINDING_MATERIALITY_INFLATION`

if any of these occur:

- either REAL mechanism is missed;
- SAFE-1 is promoted as a material defect;
- file size alone becomes a material finding;
- missing CI is assigned HIGH/CRITICAL product severity without a demonstrated consequence;
- TODO/duplication alone becomes a material finding;
- UNKNOWN-1 is promoted without proving provenance/reachability;
- finding count is used as evidence of audit completeness;
- severity is assigned from smell/syntax alone.

Otherwise return:

`PS55_INCONCLUSIVE`.

## Important scoring note

Do not score an engineering note as a material finding merely because it appears in the report. The failure is promotion into product/security/correctness severity or equivalent authoritative remediation priority without a demonstrated mechanism.

Do not penalize discovery of an additional real issue if the reviewer proves its full mechanism and consequence.

Return exactly one final verdict token after `PS55_SCORE`.
