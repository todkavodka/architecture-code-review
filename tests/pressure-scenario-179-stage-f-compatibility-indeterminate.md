# PS-179 — Stage F compatibility indeterminate

## Design mapping

`PS-F26`: missing schema in an applicable comparison creates or updates CC and
returns `INDETERMINATE`, never `COMPATIBLE`; a non-applicable comparison remains
candidate/not-evaluated only.

## Setup / evidence shape

Provider and consumer IFs have exact qualified revisions and a materially
relevant declared external contract makes Contract Verification applicable, but
the required schema reference is missing or unresolved. A candidate match may
exist. A separate case has no valid comparison pair and is not applicable.

## Expected accepted semantic records

Test Engineering Contract Verification remains the automatic gate for the
applicable pair and may create/update the existing `CC-*` state with the
missing-input limitation. The catalog-facing result is `INDETERMINATE` until
exact required inputs and a resolved valid CC adjudication exist. The
non-applicable case exposes only candidate/not-evaluated context and does not
manufacture a CC result or compatibility value.

## Prohibited inference / authority result

- missing schema or unresolved CC != `COMPATIBLE`;
- candidate match != compatibility;
- unresolved valid pair != `NOT_COMPARABLE`;
- no-match/non-applicable context != `INCOMPATIBLE`;
- Product and catalogs cannot adjudicate or create a compatibility family.

## Expected projection behavior

Service and Product projections retain exact provider/consumer revisions,
limitations, CC reference/status where present, and normalized
`INDETERMINATE` only from the existing CC boundary. Non-applicable context is
shown as non-authoritative candidate/not-evaluated information.

## Backward-compatibility constraint

Historical CC identity, revision, status, classification, adjudication, and
meaning remain unchanged. An old resolved CC for another provider revision does
not prove compatibility for this current pair; no automatic re-run occurs.

## GREEN criteria

GREEN iff the applicable missing-input case routes through CC and remains
`INDETERMINATE`, the non-applicable case remains candidate/not-evaluated only,
and neither case emits fabricated compatibility.

## Verdict

`PS179_PASS_COMPATIBILITY_INDETERMINATE`
