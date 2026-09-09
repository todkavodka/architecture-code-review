# PS-161 — Stage F cross-owned table write

## Design mapping

`PS-F08`: a write into another service’s owned table remains a fact, not an
automatic architecture finding.

## Setup / evidence shape

Service A owns state in a qualified table DS. Service B has exact evidence of a
write operation to that table at its own Project revision. The evidence is
bound to the operation and target; ownership and access are independently
accepted facts.

## Expected accepted semantic records

STM may contain `OWNS_STATE` for A and a qualified `INT-*` for B with
`interaction_kind=DATA_ACCESS`, `access_mode=WRITE`, and the target DS. The INT
may derive `WRITES_TO`. These facts remain separately qualified.

## Prohibited inference / authority result

- the cross-owned write does not automatically create an RF-*;
- ownership does not imply write access, and write access does not imply
  ownership;
- Product or documentation projections cannot adjudicate architectural impact;
- no new write/ownership identity family is introduced.

## Expected projection behavior

Data and Product views may show owner, consumer/source, target DS, `WRITE`, and
derived `WRITES_TO` as distinct facts with evidence. Architecture Review
interprets any boundary concern separately.

## Backward-compatibility constraint

Existing OWNS_STATE and relation-only WRITES_TO facts remain valid and are not
silently converted into precise INT access.

## GREEN criteria

GREEN iff ownership and precise write access coexist without inference between
them, the INT is the access authority, and no projection manufactures a finding.

## Verdict

`PS161_PASS_CROSS_OWNED_WRITE`
