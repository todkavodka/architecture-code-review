# PS-167 — Stage F S3 resource access

## Design mapping

`PS-F14`: S3 bucket/prefix access is represented only when the resource and
access are evidenced.

## Setup / evidence shape

An application has evidence of an S3 operation targeting a known bucket and,
when supported, a bounded prefix. The source operation, Project/revision, and
safe logical bucket identity are bound in WS/EV evidence. A bucket declaration
or generic SDK dependency without an operation is only a `WEAK_HINT`.

## Expected accepted semantic records

The Technical Model Gate may accept a `DS-*` with `resource_kind=BUCKET` or
`PREFIX` at evidence-supported precision and a qualified `INT-*` with
`interaction_kind=DATA_ACCESS` and an evidenced access mode. An unresolved key
or prefix remains `RESOURCE_BOUNDED` or `UNRESOLVED`.

## Prohibited inference / authority result

- S3 configuration or SDK presence does not prove bucket/prefix access;
- bucket presence does not imply access to every object or prefix;
- a parent bucket does not imply an exact child resource;
- no new S3 identity family or factual catalog authority is introduced.

## Expected projection behavior

The data projection renders accepted DS/INT records, safe logical identifiers,
access mode, precision, evidence, and any bounded limitation. Product views,
when selected, retain Project and baseline qualification.

## Backward-compatibility constraint

Historical store-level or broad DS observations remain valid without inferred
object access. Later exact evidence is additive and does not rewrite history.

## GREEN criteria

GREEN iff only evidenced S3 resources and access operations are accepted, the
target precision remains bounded when necessary, and projections do not infer
object access from configuration or containment.

## Verdict

`PS167_PASS_S3_EVIDENCE_BOUNDARY`
