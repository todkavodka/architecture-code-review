# PS-160 — Stage F PostgreSQL table read

## Design mapping

`PS-F07`: one PostgreSQL table read becomes a DS table plus INT READ at
evidence-supported precision and may derive `READS_FROM`.

## Setup / evidence shape

An exact repository call reads `orders` in a known PostgreSQL schema and is
bound to a Project revision. Evidence identifies the source operation and
target table with `STRONG_INFERENCE` or `DIRECT_DECLARATION`; no secret DSN is
stored.

## Expected accepted semantic records

The Technical Model Gate may accept a qualified `DS-*` with
`resource_kind=TABLE` and an `INT-*` with `interaction_kind=DATA_ACCESS`,
`access_mode=READ`, target reference to that DS, and evidence/provenance. A
`READS_FROM` relation may be derived from the INT; it is not a second access
authority and need not be materialized.

## Prohibited inference / authority result

- database connection does not imply table access;
- DS containment does not imply access;
- relation-only navigation cannot replace the authoritative INT;
- no ownership, migration authority, or architecture finding is inferred.

## Expected projection behavior

The data/persistence projection selects the DS and precise INT directly,
renders `READ`, and may show derived `READS_FROM` with its INT source. It does
not require relation materialization before selecting the INT.

## Backward-compatibility constraint

Legacy relation-only `READS_FROM` remains broad and retains its historical
meaning. Existing DS facts are not rewritten when a precise INT is added.

## GREEN criteria

GREEN iff the accepted access authority is the qualified INT READ, the DS is a
separate resource identity, derived navigation is optional, and no access or
ownership is inferred from a connection or containment alone.

## Verdict

`PS160_PASS_INT_READ_AUTHORITY`
