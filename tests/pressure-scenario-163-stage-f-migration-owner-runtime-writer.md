# PS-163 — Stage F migration owner and runtime writer

## Design mapping

`PS-F10`: migration authority and runtime writer can differ and both facts
coexist.

## Setup / evidence shape

Project A is explicitly responsible for schema/data evolution of DS-X.
Project B has exact evidence of a runtime `WRITE` INT to DS-X. The evidence is
separately bound to the owner relation and runtime operation.

## Expected accepted semantic records

STM may accept `MIGRATION_AUTHORITY` from A and an `INT-*` from B with
`interaction_kind=DATA_ACCESS`, `access_mode=WRITE`, and target DS-X. If a
runtime migration operation is separately evidenced, it is an INT with
`access_mode=MIGRATION`; it is not the authority relation.

## Prohibited inference / authority result

- migration authority does not imply runtime write or migration execution;
- runtime write or migration execution does not imply migration authority;
- neither relation implies OWNS_STATE;
- projections do not manufacture a finding from the separation.

## Expected projection behavior

Data and Product views display `MIGRATION_AUTHORITY`, runtime `WRITE`, and any
runtime `MIGRATION` INT as independent qualified facts with limitations and
evidence. Architecture Review owns interpretation.

## Backward-compatibility constraint

Existing migration declarations and broad ownership relations retain their
historical meaning. No old fact is enriched with runtime access by default.

## GREEN criteria

GREEN iff the three concepts remain independently represented, each has its
own evidence and authority, and no projection or relation collapses them.

## Verdict

`PS163_PASS_MIGRATION_SEPARATION`
